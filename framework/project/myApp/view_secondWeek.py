from datetime import datetime
from datetime import timedelta

from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django import forms
from .models import User, Teacher, Student, Teacher_grade, Homework, Notice_student, Teacher_homework, Homework1, objective_item, objective_id
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from itertools import chain


class UserForm_launch_objective_item(forms.Form):  # 发布客观题表单
    item_content = forms.CharField(label='作业内容', max_length=200)
    item_num = forms.IntegerField(label='题目个数') #可用统计字符串长度代替
    answer = forms.CharField(label='标准答案',max_length=200)
    deadline_days = forms.IntegerField(label='截止日期为多少天后')


@csrf_exempt
def launch_objective_item(request, num):  # 发布作业
    if request.method == 'POST':
        userform = UserForm_launch_objective_item(request.POST)
        if userform.is_valid():
            item_content = userform.cleaned_data['item_content']
            item_num = userform.cleaned_data['item_num']
            answer = userform.cleaned_data['answer']
            deadline_days = userform.cleaned_data['deadline_days']

            teacher = Teacher.objects.get(pk=num)
            #user = User.objects.get(email=teacher.semail)
            teacher_gradeList = Teacher_grade.objects.filter(teacher_id=teacher.pk)

            create_time = timezone.now()
            create_time = datetime.strptime(create_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            homework_deadline = create_time + timedelta(days=deadline_days)
            homework_deadline = datetime.strptime(homework_deadline.strftime("%Y-%m-%d %H:%M:%S"),
                                                  "%Y-%m-%d %H:%M:%S")

            item_t = objective_id.objects.create(teacher_id=num, homework_create_time=create_time)
            item_t.save()

            for teacher_grade in teacher_gradeList:
                studentList = Student.objects.filter(sgrade=teacher_grade.grade)

                for student in studentList:
                    item = objective_item.objects.create(homework_create_time=create_time,
                                                       teacher_name=teacher.sname,
                                                       student_name=student.sname,
                                                       student_id=student.pk,
                                                       item_num=item_num,
                                                       item_content=item_content,
                                                       homework_deadline=homework_deadline,
                                                       teacher_id=teacher.pk,
                                                       item_id=item_t.pk,
                                                       )
                    item.save()


            return HttpResponse('成功发布客观题作业！')
    else:
        userform = UserForm_launch_objective_item()
    return render_to_response('myApp/secondWeek/launch_objective_item.html', {'userform': userform})



def teacher_check_objective_item(request, num):  # 老师查看作业

    homeworkList = objective_id.objects.filter(teacher_id=num)
    #paginator = Paginator(homeworkList, 5)  # 实例化Paginator, 每页显示5条数据
    #if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        #pindex = 1
    #else:  # 如果有返回在值，把返回值转为整数型
        #int(pindex)

    #pindex1 = 1

    #page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    return render_to_response('myApp/secondWeek/teacher_check_objective_item.html', {'homeworkList': homeworkList})


def teacher_check_student_submission(request, num): #老师查看学生提交情况
    studentList = objective_item.objects.filter(item_id=num)

    return render_to_response('myApp/secondWeek/teacher_check_student_submission.html', {'studentList':studentList})