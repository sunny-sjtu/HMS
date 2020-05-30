# myApp�����urls·������
from django.conf.urls import url, include
from django.contrib import admin
from . import view_firstWeek, view_secondWeek
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),  # ����ҳֱ��ת��views�е�index����
    

    url(r'^regist/$', views.regist, name='1'),  # regist����ת��views�е�regist����,��ͬ
    url(r'^login/$', views.login, name='2'),
    url(r'^index/$', views.index, name='3'),
    url(r'^login/(\d+)$', views.check_teacher_info, name='4'),
    url(r'^login/0/(\d+)$', views.alter_teacher_info, name='5'),
    url(r'^login/1/(\d+)$', views.check_student_info, name='6'),
    url(r'^login/2/(\d+)$', views.alter_student_info),
    url(r'^login/3/(\d+)$', views.add_teacher_grade),
    url(r'^login/4/(\d+)$', views.delete_teacher_grade),  # preparation��ģ�弰views����ͼ

    url(r'^login/5/(\d+)$', view_firstWeek.launch_homework, name='launch'),  # firstWeek��ģ�弰view_firstWeek����ͼ
    url(r'^login/6/(\d+)$', view_firstWeek.check_student_finished_homework_html2),  # ѧ���鿴���ύ��ҵhtml2
    url(r'^login/7/(\d+)$', view_firstWeek.submit_student_homework),  # �ύ��ҵ
    url(r'^login/8/(\d+)/(\d+)$', view_firstWeek.check_teacher_homework, name='7'),  # ��ʦ�鿴��ҵ������
    url(r'^login/8/1/1/(\d+)$', view_firstWeek.teacher_alter_homework, name='8'),  # ��ʦ�޸Ķ�Ӧ��ҵ
    url(r'^login/8/1/2/(\d+)$', view_firstWeek.delete_teacher_homework, name='9'),  # ��ʦɾ����Ӧ��ҵ
    url(r'^login/9/2/(\d+)/(\d+)$', view_firstWeek.check_submission_homework, name='10'),  # ��ʦ����ѧ���б�
    url(r'^login/9/2/2/(\d+)/(\d+)$', view_firstWeek.check_common_student_the_homework, name='11'),  # ��ʦ�鿴��ȷ������ȷ��δ�ٽ���ѧ������
    url(r'^login/9/(\d+)/(\d+)$', view_firstWeek.check_feedback_homework, name='12'),  # ��ʦ�鿴����ѧ���б�
    url(r'^login/9/1/1/(\d+)/(\d+)$', view_firstWeek.check_redo_homework, name='13'),  # ��ʦ�鿴δ����ѧ���б�
    url(r'^login/9/1/2/(\d+)/(\d+)$', view_firstWeek.check_not_submitted_homework, name='14'),  # ��ʦ�鿴δ�ύѧ���б�
    url(r'^login/10/(\d+)$', view_firstWeek.correct_homework),  # ��ʦ����ѧ����ҵ
    url(r'^login/10/1/(\d+)$', view_firstWeek.correct_feedback_homework),  # ��ʦ���ķ�������
    url(r'^login/11/(\d+)$', views.check_gradelist),  # ��ʦ�鿴�����༶
    url(r'^login/12/(\d+)$', views.check_studentlist),  # ��ʦ�鿴�����༶ѧ�����
    url(r'^login/14/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_finished_homework_html3_handInTime, name='15'),  # ѧ���鿴���ύ��ҵhtml3��Ĭ���ύ��������
    url(r'^login/14/1/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_finished_homework_html3_createtime, name='16'),  # ѧ���鿴���ύ��ҵhtml3����Ϊ������������
    url(r'^login/13/(\d+)$', view_firstWeek.check_student_unfinished_homework_html2),  # ѧ���鿴δ�ύ��ҵhtml2
    url(r'^login/15/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_unfinished_homework_html3_sorted_by_deadline),  # ѧ���鿴δ�ύ��ҵhtml3��Ĭ�Ͻ�ֹ��������
    url(r'^login/15/1/(\d+)/(\d+)/(\d+)$', view_firstWeek.check_student_unfinished_homework_html3_sorted_by_createtime),  # ѧ���鿴δ�ύ��ҵhtml3����Ϊ������������
    url(r'^login/14/1/1/(\d+)/(\d+)/(\d+)$', view_firstWeek.feedback_homework, name='17'),  # ѧ��������ҵ

    url(r'^login/16/(\d+)$', view_secondWeek.launch_objective_item),  # �����͹���
    url(r'^login/17/(\d+)/(\d+)$', view_secondWeek.teacher_check_objective_item),  # ��ʦ�鿴�͹���
    url(r'^login/18/(\d+)/(\d+)$', view_secondWeek.teacher_check_student_submission),  # ��ʦ�鿴ѧ���͹����ύ���
    url(r'^login/18/1/(\d+)/(\d+)$', view_secondWeek.teacher_check_not_submitted_objective),  # ��ʦ�鿴�͹���δ�ύ��ٽ�ѧ������
    url(r'^login/19/(\d+)$', view_secondWeek.check_unfinished_objective_item_html2),  # ѧ���鿴δ�ύ�͹���html2
    url(r'^login/20/(\d+)$', view_secondWeek.submit_objective_item),  # ѧ���ύ�͹�����ҵ
    url(r'^login/21/(\d+)$', view_secondWeek.check_finished_objective_item_html2),  # ѧ���鿴���ύ�͹���html2
    url(r'^login/22/(\d+)/(\d+)/(\d+)$', view_secondWeek.check_unfinished_objective_item_html3_sorted_by_deadline, name='18'),  # ѧ���鿴δ�ύ�͹���html3��Ĭ�Ͻ�ֹ��������
    url(r'^login/22/1/(\d+)/(\d+)/(\d+)$', view_secondWeek.check_unfinished_objective_item_html3_sorted_by_createtime, name='19'),  # ѧ���鿴δ�ύ�͹���html3����Ϊ������������
    url(r'^login/23/(\d+)/(\d+)/(\d+)$', view_secondWeek.check_finished_objective_item_html3_handInTime),  # ѧ���鿴���ύ�͹���html3��Ĭ���ύ��������
    url(r'^login/23/1/(\d+)/(\d+)/(\d+)$', view_secondWeek.check_finished_objective_item_html3_createtime),  # ѧ���鿴���ύ�͹���html3����Ϊ������������

    url(r'^login/download/(?P<file_name>.*)/$', view_firstWeek.download, name='20'),  # ������ҵ
]
