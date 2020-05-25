# 视图配置页

from django.shortcuts import render, render_to_response
from django import forms
from .models import User, Teacher, Student, Teacher_grade
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class UserForm_regist(forms.Form):  # 注册表单
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')
    gender = forms.CharField(label='性别')
    age = forms.IntegerField(label='年龄')
    grade = forms.CharField(required=False, label='班级号（老师不填)', max_length=20)
    isTeacher = forms.CharField(required=False, label='老师密钥（学生不填)')


class UserForm_login(forms.Form):  # 登录表单
    email = forms.EmailField(label='邮箱')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    isTeacher = forms.CharField(required=False, label='老师密钥（学生不填)')


class UserForm_teacher(forms.Form):  # 教师修改信息表单
    sname = forms.CharField(label='姓名', max_length=50)
    sgender = forms.CharField(label='性别')
    sage = forms.IntegerField(label='年龄')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


class UserForm_student(forms.Form):  # 学生修改信息表单
    sname = forms.CharField(label='姓名', max_length=50)
    sgender = forms.CharField(label='性别')
    sage = forms.IntegerField(label='年龄')
    sgrade = forms.CharField(label='班级号', max_length=20)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


class UserForm_teacher_add_grade(forms.Form):  # 添加老师所教班级表单
    grade1 = forms.CharField(required=False, label='所教班级号1(非必填)', max_length=20)
    grade2 = forms.CharField(required=False, label='所教班级号2(非必填)', max_length=20)
    grade3 = forms.CharField(required=False, label='所教班级号3(非必填)', max_length=20)


TeacherPassword = "12345678"  # 老师身份验证的密码

def index(request):  # 主页
    return render_to_response('myApp/preparation/index.html')

@csrf_exempt
def regist(request):  # 注册函数
    if request.method == 'POST':
        userform = UserForm_regist(request.POST)
        if userform.is_valid():

            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            confirm_password = userform.cleaned_data['confirm_password']
            email = userform.cleaned_data['email']
            gender = userform.cleaned_data['gender']
            age = userform.cleaned_data['age']
            grade = userform.cleaned_data['grade']
            isTeacher = userform.cleaned_data['isTeacher']

            if "男" in gender:
                gender = True
            elif "公" in gender:
                gender = True
            elif "雄" in gender:
                gender = True
            elif "male" in gender:
                gender = True
            else:
                gender = False

            age = int(age)

            userList0 = User.objects.all()
            for user0 in userList0:
                if user0.email == email:
                    return render_to_response('myApp/webpage/regist_0.html')

            if isTeacher == "":
                user = User.objects.create(username=username, password=password, email=email, gender=gender, age=age,
                                           grade=grade, isTeacher=-1)
                user.save()
                student = Student.objects.create(sname=username, sgender=gender, sage=age, sgrade=grade, semail=email,
                                                 isDelete=False)
                student.save()
                return render_to_response('myApp/webpage/regist_1.html')

            if isTeacher != TeacherPassword:
                user = User.objects.create(username=username, password=password, email=email, gender=gender, age=age,
                                           grade=grade, isTeacher=-1)
                user.save()
                student = Student.objects.create(sname=username, sgender=gender, sage=age, sgrade=grade, semail=email,
                                                 isDelete=False)
                student.save()
                return render_to_response('myApp/webpage/regist_2.html')

            if isTeacher == TeacherPassword:
                user = User.objects.create(username=username, password=password, email=email, gender=gender, age=age,
                                           grade=-1, isTeacher=isTeacher)
                user.save()
                teacher = Teacher.objects.create(sname=username, sgender=gender, sage=age, semail=email, isDelete=False)
                teacher.save()
                return render_to_response('myApp/webpage/regist_3.html')
    else:
        userform = UserForm_regist()
    return render_to_response('myApp/preparation/regist.html', {'userform': userform})  # error


@csrf_exempt
def login(request):  # 登录函数
    if request.method == 'POST':
        userform = UserForm_login(request.POST)
        if userform.is_valid():
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            isTeacher = userform.cleaned_data['isTeacher']

            user = User.objects.filter(email__exact=email, password__exact=password)
            if user and isTeacher == TeacherPassword:
                teacher = Teacher.objects.get(semail=email)
                teacher_id = teacher.id
                pindex = 1
                return render_to_response('myApp/preparation/info_teacher.html', {'teacher': teacher, 'pindex': pindex ,"teacher_id": teacher_id})

            if user and isTeacher == "":
                student = Student.objects.get(semail=email)
                student_id = student.id
                return render_to_response('myApp/preparation/info_student.html', {'student': student, "student_id": student_id})

            if user and isTeacher != TeacherPassword:
                student = Student.objects.get(semail=email)
                student_id = student.id
                return render_to_response('myApp/preparation/info_student.html', {'student': student, "student_id": student_id})

            if not user:
                return render_to_response('myApp/webpage/login_wrong.html')
    else:
        userform = UserForm_login()
    return render_to_response('myApp/preparation/login.html', {'userform': userform})


def check_teacher_info(request, num):  # 查看老师个人信息
    teacher = Teacher.objects.get(pk=num)
    user = User.objects.get(username=teacher.sname)
    teacher_grade_List = Teacher_grade.objects.filter(teacher_id=teacher.pk)
    return render_to_response('myApp/preparation/check_teacher_info.html',
                              {'teacher': teacher, 'user': user, 'teacher_grade_List': teacher_grade_List, 'teacher_id':num})


def check_student_info(request, num):  # 查看学生个人信息
    student = Student.objects.get(pk=num)
    user = User.objects.get(username=student.sname)
    return render_to_response('myApp/preparation/check_student_info.html', {'student': student, 'user': user})


@csrf_exempt
def alter_teacher_info(request, num):  # 修改老师个人信息
    if request.method == 'POST':
        userform = UserForm_teacher(request.POST)
        if userform.is_valid():
            sname = userform.cleaned_data['sname']
            sgender = userform.cleaned_data['sgender']
            sage = userform.cleaned_data['sage']
            password = userform.cleaned_data['password']
            confirm_password = userform.cleaned_data['confirm_password']
            email = userform.cleaned_data['email']

            if "男" in sgender:
                sgender = True
            elif "公" in sgender:
                sgender = True
            elif "雄" in sgender:
                sgender = True
            elif "male" in sgender:
                sgender = True
            else:
                sgender = False

            sage = int(sage)

            teacher = Teacher.objects.get(pk=num)
            User.objects.filter(username=teacher.sname).update(password=password, email=email)
            Teacher.objects.filter(pk=num).update(sname=sname, sgender=sgender, sage=sage)

            return render_to_response('myApp/webpage/alter_teacher_info_0.html')
    else:
        userform = UserForm_teacher()
    return render_to_response('myApp/preparation/alter_teacher_info.html', {'userform': userform, 'teacher_id': num})


@csrf_exempt
def alter_student_info(request, num):  # 修改学生个人信息
    if request.method == 'POST':
        userform = UserForm_student(request.POST)
        if userform.is_valid():
            sname = userform.cleaned_data['sname']
            sgender = userform.cleaned_data['sgender']
            sage = userform.cleaned_data['sage']
            sgrade = userform.cleaned_data['sgrade']
            password = userform.cleaned_data['password']
            confirm_password = userform.cleaned_data['confirm_password']
            email = userform.cleaned_data['email']

            if "男" in sgender:
                sgender = True
            elif "公" in sgender:
                sgender = True
            elif "雄" in sgender:
                sgender = True
            elif "male" in sgender:
                sgender = True
            else:
                sgender = False

            sage = int(sage)

            student = Student.objects.get(pk=num)
            User.objects.filter(username=student.sname).update(password=password, email=email)
            Student.objects.filter(pk=num).update(sname=sname, sgender=sgender, sage=sage, sgrade=sgrade)

            return render_to_response('myApp/webpage/alter_student_info_0.html')
    else:
        userform = UserForm_student()
    return render_to_response('myApp/preparation/alter_student_info.html', {'userform': userform, 'studentId': num})


@csrf_exempt
def add_teacher_grade(request, num):  # 添加老师所教班级
    if request.method == 'POST':
        userform = UserForm_teacher_add_grade(request.POST)
        if userform.is_valid():
            grade1 = userform.cleaned_data['grade1']
            grade2 = userform.cleaned_data['grade2']
            grade3 = userform.cleaned_data['grade3']

            teacher = Teacher.objects.get(pk=num)

            flag = False

            if grade1 != "":
                teacher_grade1 = Teacher_grade.objects.create(teacher_id=teacher.pk, teacher_name=teacher.sname,
                                                              grade=grade1)
                teacher_grade1.save()
                flag = True

            if grade2 != "":
                teacher_grade2 = Teacher_grade.objects.create(teacher_id=teacher.pk, teacher_name=teacher.sname,
                                                              grade=grade2)
                teacher_grade2.save()
                flag = True

            if grade3 != "":
                teacher_grade3 = Teacher_grade.objects.create(teacher_id=teacher.pk, teacher_name=teacher.sname,
                                                              grade=grade3)
                teacher_grade3.save()
                flag = True

            if flag:
                return render_to_response('myApp/webpage/add_teacher_grade_0.html')
    else:
        userform = UserForm_teacher_add_grade()
    return render_to_response('myApp/preparation/add_teacher_grade.html', {'userform': userform})


def delete_teacher_grade(request, num):  # 删除老师所教班级
    teacher_gradeList = Teacher_grade.objects.filter(pk=num)
    if teacher_gradeList:
        Teacher_grade.objects.filter(pk=num).delete()
        return render_to_response('myApp/webpage/delete_teacher_grade_0.html')
    else:
        return render_to_response('myApp/webpage/delete_teacher_grade_1.html')


def check_gradelist(request, num):  # 老师查看所属班级
    gradelist = Teacher_grade.objects.filter(teacher_id=num)

    return render_to_response('myApp/preparation/check_gradelist.html', {'gradelist': gradelist, 'teacher_id': num})


def check_studentlist(request, char):  # 老师查看所属班级学生信息
    studentlist = Student.objects.filter(sgrade=char)
    return render_to_response('myApp/preparation/check_studentlist.html', {'studentlist': studentlist})
