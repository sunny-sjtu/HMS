# myApp里面的urls路由配置
from django.conf.urls import url, include
from django.contrib import admin
from . import views, view_firstWeek, view_secondWeek

from django.urls import path
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),  # 仅主页直接转到views中的index函数

    url(r'^regist/$', views.regist),  # regist需求转至views中的regist函数,下同
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^login/(\d+)$', views.check_teacher_info),
    url(r'^login/0/(\d+)$', views.alter_teacher_info),
    url(r'^login/1/(\d+)$', views.check_student_info),
    url(r'^login/2/(\d+)$', views.alter_student_info),
    url(r'^login/3/(\d+)$', views.add_teacher_grade),
    url(r'^login/4/(\d+)$', views.delete_teacher_grade),  # preparation的模板及views的视图


    url(r'^login/5/(\d+)$', view_firstWeek.launch_homework), # firstWeek的模板及view_firstWeek的视图
    url(r'^login/6/(\d+)$', view_firstWeek.check_student_finished_homework_html2),  # 学生查看已提交作业html2
    url(r'^login/7/(\d+)$', view_firstWeek.submit_student_homework),  # 提交作业
    url(r'^login/8/(\d+)/(\d+)$', view_firstWeek.check_teacher_homework),  # 老师查看作业完成情况
    url(r'^login/9/(\d+)/(\d+)$', view_firstWeek.check_submission_homework),  # 老师查看学生列表
    url(r'^login/9/(\d+)$',view_firstWeek.check_feedback_homework),  # 老师查看反馈学生列表
    url(r'^login/9/1/1/(\d+)$',view_firstWeek.check_redo_homework),  # 老师查看订正学生列表
    url(r'^login/10/(\d+)$', view_firstWeek.correct_homework),  # 老师批改学生作业
    url(r'^login/10/1/(\d+)$', view_firstWeek.correct_feedback_homework),  # 老师批改反馈内容
    url(r'^login/11/(\d+)$', views.check_gradelist),  # 老师查看所属班级
    url(r'^login/12/(\d+)$', views.check_studentlist),  # 老师查看所属班级学生情况
    url(r'^login/14/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_finished_homework_html3),  # 学生查看已提交作业html3
    url(r'^login/13/(\d+)$', view_firstWeek.check_student_unfinished_homework_html2),  # 学生查看未提交作业html2
    url(r'^login/15/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_unfinished_homework_html3),  # 学生查看未提交作业html3
    url(r'^login/14/1/(\d+)/(\d+)/(\d+)$', view_firstWeek.feedback_homework),  # 学生反馈作业


    url(r'^login/16/(\d+)$', view_secondWeek.launch_objective_item),
    url(r'^login/17/(\d+)$', view_secondWeek.teacher_check_objective_item),
    url(r'^login/18/(\d+)$', view_secondWeek.teacher_check_student_submission)


]