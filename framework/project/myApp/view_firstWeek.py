from datetime import datetime
from datetime import timedelta
from django.shortcuts import render, render_to_response
from django import forms
from .models import User, Teacher, Student, Teacher_grade, Homework, Notice_student, Teacher_homework, Homework1
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


class UserForm_launch_homework(forms.Form):  # 发布作业信息表单
    homework_content = forms.CharField(label='作业内容', max_length=50)
    deadline_days = forms.IntegerField(label='截止日期为多少天后')

class UserForm_submit_homework(forms.Form):  # 提交作业信息表单
    handIn_homework = forms.FileField(label='提交作业内容')

class UserForm_correct_homework(forms.Form):  #批改作业表单
    teacher_comment = forms.CharField(required=False, label='批改作业', max_length=200)
    isCorrect = forms.BooleanField(required=False, label='作业是否正确')

@csrf_exempt
def launch_homework(request, num):  # 发布作业
    if request.method == 'POST':
        userform = UserForm_launch_homework(request.POST)
        if userform.is_valid():
            homework_content = userform.cleaned_data['homework_content']
            deadline_days = userform.cleaned_data['deadline_days']

            teacher = Teacher.objects.get(pk=num)
            user = User.objects.get(email=teacher.semail)
            teacher_gradeList = Teacher_grade.objects.filter(teacher_id=teacher.pk)

            ht = Teacher_homework.objects.create(teacher_id=num,homework_content=homework_content)
            ht.save()

            for teacher_grade in teacher_gradeList:
                studentList = Student.objects.filter(sgrade=teacher_grade.grade)
                create_time = timezone.now()
                create_time = datetime.strptime(create_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                homework_deadline = create_time + timedelta(days=deadline_days)
                homework_deadline = datetime.strptime(homework_deadline.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

                for student in studentList:
                    homework = Homework.objects.create(homework_create_time=create_time,
                                                       teacher_name=teacher.sname,
                                                       student_name=student.sname,
                                                       student_id=student.pk,
                                                       homework_content=homework_content,
                                                       homework_deadline=homework_deadline,
                                                       teacher_id=teacher.pk,
                                                       homework_id=ht.pk)
                    homework.save()
                    homework1 = Homework1.objects.create()

                    homework1.save()

                    notice_content = "作业显示" + homework_content
                    notice_student = Notice_student.objects.create(notice_create_time=create_time,
                                                                   teacher_email=user.email,
                                                                   student_id=student.pk,
                                                                   notice_content=notice_content)
                    notice_student.save()

            return HttpResponse('成功发布作业！')
    else:
        userform = UserForm_launch_homework()
    return render_to_response('myApp/firstWeek/launch_homework.html', {'userform': userform})


def check_student_homework(request,num):  # 学生查看作业

    uncompleted_homeworkList = Homework.objects.filter(student_id=num,isComplete=False)
    completed_homeworkList = Homework.objects.filter(student_id=num,isComplete=True)

    return render_to_response('myApp/firstWeek/check_student_homework.html',{'uncompleted_homeworkList':uncompleted_homeworkList,'completed_homeworkList':completed_homeworkList})


def review_homework(request,num): #学生查看已完成作业
    homework = Homework.objects.get(pk=num)
    homework_correct = Homework1.objects.get(pk=num)

    return render_to_response('myApp/firstWeek/review_homework.html',{'homework_url':homework.handIn_homework.url,'homework_correct':homework_correct})



@csrf_exempt
def submit_student_homework (request,num):  #学生提交作业
    if request.method == 'POST':
        userform = UserForm_submit_homework(request.POST or None,request.FILES or None)
        if userform.is_valid():
            handIn_homework = request.FILES.get("handIn_homework")

            homework = Homework.objects.get(pk=num)

            handIn_time = timezone.now()
            handIn_time = datetime.strptime(handIn_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

            deadline = homework.homework_deadline
            deadline = datetime.strptime(deadline.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            isLate = handIn_time > deadline

            Homework.objects.filter(pk=num).update(isLate=isLate,handIn_time=handIn_time,handIn_homework=handIn_homework,isComplete=True)

            return HttpResponse('成功提交作业！')
    else:
        userform = UserForm_submit_homework()
    return render_to_response('myApp/firstWeek/submit_student_homework.html', {'userform': userform})

def check_teacher_homework(request,num):  # 老师查看作业

    homeworkList = Teacher_homework.objects.filter(teacher_id=num)

    return render_to_response('myApp/firstWeek/check_teacher_homework.html',{'homeworkList':homeworkList})

def check_submission_homework(request,num):       #老师查看作业提交情况

    studentnamelist = Homework.objects.filter(homework_id=num)

    return render_to_response('myApp/firstWeek/check_submission_homework.html',{'studentnamelist':studentnamelist})

@csrf_exempt
def correct_homework(request,num):  #老师批改作业
    s_homework = Homework.objects.get(pk=num)
    if s_homework.isComplete == False :
        return HttpResponse('这位学生还未完成作业哟！')

    else:
        if request.method == 'POST':
            userform = UserForm_correct_homework(request.POST)
            if userform.is_valid():
                teacher_comment = userform.cleaned_data['teacher_comment']
                isCorrect = userform.cleaned_data['isCorrect']

                if teacher_comment == "":
                    # homework = Homework1.objects.create(tcomment=teacher_comment, iscorrect=isCorrect, iscommented=False)
                    # homework.save()
                    return HttpResponse('您未添加评论！')

                else:
                    Homework1.objects.filter(pk=num).update(tcomment=teacher_comment, iscorrect=isCorrect,iscommented=True)
                    # homework.save()
                    return HttpResponse('成功添加评论！')

        else:
            userform = UserForm_correct_homework()
        return render_to_response('myApp/firstWeek/correct_homework.html',{'file_url': s_homework.handIn_homework.url, 'userform': userform})



