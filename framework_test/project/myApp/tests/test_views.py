from django.test import TestCase, Client
from django.urls import reverse
from myApp.models import User, Homework, Teacher, Teacher_grade, Teacher_homework, Homework1,Student
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
import json, os



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.launch_url = reverse('launch', args='1')
        # self.submit_url = reverse('submit', args='1')
        # self.correct1_url = reverse('correct1', args='1')

        self.teacher1=Teacher.objects.create(
            sname='3',
            sage=30,
            semail='3@qq.com'
        )
        self.user1=User.objects.create(
            username='3',
            password='3',
            email='3@qq.com',
            age=30,
            isTeacher='12345678'
        )
        self.tgrade=Teacher_grade.objects.create(
            teacher_id=1,
            grade='1',
            teacher_name='3'
        )
        self.student1=Student.objects.create(
            sname='1',
            sage=1,
            sgrade='1',
            semail='1@qq.com'
        )
        self.student2 = Student.objects.create(
            sname='2',
            sage=1,
            sgrade='1',
            semail='2@qq.com'
        )


    #测试def launch_homework(request, num)
    #传了一个参，老师的pk
    def test_launch_POST(self):

        #检查初始化是否正确
        assert Student.objects.count() == 2
        assert Teacher.objects.count() == 1
        assert Homework.objects.count() == 0

        #在对应url上提交homework_content和deadline_days两项内容
        response1 = self.client.post(self.launch_url, {
            'homework_content': '123',
            'deadline_days': 4
        })

        #检验Teacher_homework
        homeworkList1 = Teacher_homework.objects.filter(teacher_id=1)
        for homework in homeworkList1:
            self.assertEquals(homework.homework_content, '123')
            self.assertEquals(response1.status_code, 200)

        #检验Homework
        homeworkList2 = Homework.objects.filter(teacher_id=1)
        assert homeworkList2.count() == 2
        for homework in homeworkList2:
            self.assertEquals(homework.homework_content, '123')
            print(homework.pk)

        #检验Homework1
        homeworkList3 = Homework1.objects.filter(teacher_id=1)
        assert homeworkList3.count() == 2
        for homework in homeworkList3:
            self.assertEquals(homework.homework_content, '123')
            print(homework.pk)


    # #检验def submit_student_homework(request, num)
    # #传一个参，作业的pk
    # def test_submit_POST(self):

    #     # 检查当前状态
    #     assert Student.objects.count() == 2
    #     assert Teacher.objects.count() == 1
    #     assert Homework.objects.count() == 0

    #     #初始化
    #     self.homework_1 = Homework.objects.create(
    #         student_id=1,
    #         teacher_id=1,
    #         homework_id=1,
    #         homework_content='123',
    #         homework_create_time='2020-02-03',
    #         homework_deadline='2020-02-04'
    #     )

    #     self.homework1_1 = Homework1.objects.create(
    #         student_id=1,
    #         teacher_id=1,
    #         homework_id=1,
    #         homework_content='123'
    #     )

    #     # print(Homework.objects.first())
    #     # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     # file_path = os.path.join(base_dir, 'static', 'media')

    #     with open('file1.txt', 'wb+') as fp:
    #          response = self.client.post('/static/media', 1, {
    #           'handIn_homework': fp
    #          })


    #     #检验handIn_homework的内容
    #     homework = Homework.objects.first()
    #     # for homework in homeworkList:
    #     self.assertEquals(homework.handIn_homework, 'file1')
    #     self.assertEquals(response.status_code, 200)

    #     homework1 = Homework1.objects.first()
    #     # for homework in homeworkList1:
    #     self.assertEquals(homework1.handIn_homework, 'file1')
    #     self.assertEquals(response.status_code, 200)



    # # # 检验def correct_homework(request, num)
    # # def test_correct_1_POST(self):
    # #
    # #    self.homework_1 = Homework.objects.create(
    # #                 student_id=1,
    # #                 teacher_id=1,
    # #                 homework_id=1,
    # #                 homework_content='123',
    # #                 homework_create_time='2020-02-03',
    # #                 homework_deadline='2020-02-04',
    # #                 handIn_homework='file1'
    # #             )
    # #
    # #    self.homework1_1 = Homework1.objects.create(
    # #                 student_id=1,
    # #                 teacher_id=1,
    # #                 homework_id=1,
    # #                 homework_content='123',
    # #                 isComplete=True
    # #             )
    # #
    # #    response=self.client.post(self.correct1_url, {
    # #         'isCorrect': 'dui',
    # #         'teacher_comment': 'good',
    # #     })
    # #
    # #     # homework = Homework1.objects.get(pk=1)
    # #     # for homework in homeworkList:
    # #    assert response.status_code == 200
    # #     # assert homework.isComplete == True
    # #     # assert homework.tcomment == 'good'
    # #     # assert homework.isCorrect == False
    # #





