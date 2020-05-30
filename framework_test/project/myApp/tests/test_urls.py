
from django.test import TestCase
from django.urls import reverse, resolve
from myApp.views import regist, login, index, check_teacher_info, alter_teacher_info, check_student_info
from myApp.view_firstWeek import check_teacher_homework, teacher_alter_homework, delete_teacher_homework, \
    check_submission_homework, check_common_student_the_homework, check_feedback_homework, check_redo_homework, \
    check_not_submitted_homework, check_student_finished_homework_html3_handInTime, \
    check_student_finished_homework_html3_createtime, feedback_homework, download
from myApp.view_secondWeek import check_unfinished_objective_item_html3_sorted_by_deadline, \
    check_unfinished_objective_item_html3_sorted_by_createtime
# Create your tests here.
class TestUrls(TestCase):
    def test_regist_url_resolved(self):
        url = reverse('1')
        self.assertEquals(resolve(url).func, regist)

    def test_login_url_resolved(self):
        url = reverse('2')
        self.assertEquals(resolve(url).func, login)

    def test_index_url_resolved(self):
        url = reverse('3')
        self.assertEquals(resolve(url).func, index)

    def test_check_teacher_info_resolved(self):
        url = reverse('4', args=[1])
        self.assertEquals(resolve(url).func, check_teacher_info)

    def test_alter_teacher_info_resolved(self):
        url = reverse('5', args=[0])
        self.assertEquals(resolve(url).func, alter_teacher_info)

    def test_check_student_info_resolved(self):
        url = reverse('6', args=[1])
        self.assertEquals(resolve(url).func, check_student_info)

    def test_check_teacher_homework_resolved(self):
        url = reverse('7', args=[8, 1])
        self.assertEquals(resolve(url).func, check_teacher_homework)

    def test_teacher_alter_homework_resolved(self):
        url = reverse('8', args=[8])
        self.assertEquals(resolve(url).func, teacher_alter_homework)

    def test_delete_teacher_homework_resolved(self):
        url = reverse('9', args=[8])
        self.assertEquals(resolve(url).func, delete_teacher_homework)

    def test_check_submission_homework_resolved(self):
        url = reverse('10', args=[9, 2])
        self.assertEquals(resolve(url).func, check_submission_homework)

    def test_check_common_student_the_homework_resolved(self):
        url = reverse('11', args=[9, 2])
        self.assertEquals(resolve(url).func, check_common_student_the_homework)

    def test_check_feedback_homework_resolved(self):
        url = reverse('12', args=[9, 1])
        self.assertEquals(resolve(url).func, check_feedback_homework)

    def test_check_redo_homework_resolved(self):
        url = reverse('13', args=[9, 1])
        self.assertEquals(resolve(url).func, check_redo_homework)

    def test_check_not_submitted_homework_resolved(self):
        url = reverse('14', args=[9, 1])
        self.assertEquals(resolve(url).func, check_not_submitted_homework)

    def test_check_student_finished_homework_resolved(self):
        url = reverse('15', args=[14, 1, 1])
        self.assertEquals(resolve(url).func, check_student_finished_homework_html3_handInTime)

    def test_check_student_finished_homework1_resolved(self):
        url = reverse('16', args=[14, 1, 1])
        self.assertEquals(resolve(url).func, check_student_finished_homework_html3_createtime)

    def test_feedback_homework_resolved(self):
        url = reverse('17', args=[14, 1, 1])
        self.assertEquals(resolve(url).func, feedback_homework)

    def test_check_unfinished_objective_item_html3_sorted_by_deadline_resolved(self):
        url = reverse('18', args=[22, 1, 1])
        self.assertEquals(resolve(url).func, check_unfinished_objective_item_html3_sorted_by_deadline)

    def test_check_unfinished_objective_item_html3_sorted_by_createtime_resolved(self):
        url = reverse('19', args=[22, 1, 1])
        self.assertEquals(resolve(url).func, check_unfinished_objective_item_html3_sorted_by_createtime)

    def test_download_resolved(self):
        url = reverse('20', args={download})
        self.assertEquals(resolve(url).func, download)



