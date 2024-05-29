from django.test import TestCase
from requests import request
from views import (privacy_policy, current_date_view, home, feedback_view, feedback_add_view,
                   promocode_view, WorkView, NewsView, NewsReadView, faq_view,
                   service_list, service_detail, create_service, delete_card, update_card,
                   create_card, signup, card_detail, card_list, hall_list, hall_add, employee_list
                   , employees_info)
from models import feedback
from django.shortcuts import render, redirect
from django.utils import timezone


class privacyTestCase(TestCase):
    def testfunction(self):
        self.assertEquals(privacy_policy, render(request, 'privacy_policy.html'))


class currentdateTestCase(TestCase):
    def test(self):
        current_date = timezone.now().date()
        self.assertEquals(current_date_view, render(request, 'home.html', {'current_date': current_date}))


class homeTestCase(TestCase):
    def test(self):
        self.assertEquals(home, render(request, 'home.html'))


class feedbackTestCase(TestCase):
    def test(self):
        feedbacks = feedback.objects.all()
        render(request, 'feedback.html', {'feedback': feedbacks})
        self.assertEquals(feedback_view, render(request, 'feedback.html', {'feedback': feedbacks}))


class feedaddTestCase(TestCase):
    def test(self):
        self.assertEquals(feedback_add_view, render(request, 'feedback_add.html'))


class promocesTestCase(TestCase):
    def test(self):
        self.assertEquals(promocode_view, render(request, 'Promocodes.html'))


class NewsTestCase(TestCase):
    def test(self):
        self.assertEquals(NewsView, render(request, template_name = 'news.html'))


class WorkTestCase(TestCase):
    def test(self):
        self.assertEquals(WorkView, render(request, 'Work.html'))

class NewsReadTestCase(TestCase):
    def test(self):
        self.assertEquals(NewsReadView, render(request, template_name='news_read.html'))


class FaqTestCase(TestCase):
    def test(self):
        self.assertEquals(faq_view, render(request, template_name='FAQ.html'))


class ServiceDetTestCase(TestCase):
    def test(self):
        self.assertEquals(service_detail, render(request, 'service_detail.html'))


class ServiceListTestCase(TestCase):
    def test(self):
        self.assertEquals(service_list, render(request, 'service_list.html'))


class ServiceCrTestCase(TestCase):
    def test(self):
        self.assertEquals(create_service, render(request, 'create_service.html'))


class DeleteCardTestCase(TestCase):
    def test(self):
        self.assertEquals(delete_card, redirect('home'))


class UpdateCardTestCase(TestCase):
    def test(self):
        self.assertEquals(update_card, render(request, 'update_card.html'))


class signupTestCase(TestCase):
    def test(self):
        self.assertEquals(signup, redirect('home'))


class createcardTestCase(TestCase):
    def test(self):
        self.assertEquals(create_card, redirect('home'))


class carddetTestCase(TestCase):
    def test(self):
        self.assertEquals(card_detail, (request, 'card_detail.html'))


class cardlistTestCase(TestCase):
    def test(self):
        self.assertEquals(card_list, render(request, 'card_list.html'))


class halllistTestCase(TestCase):
    def test(self):
        self.assertEquals(hall_list, render(request, 'halls_list.html'))


class halladdTestCase(TestCase):
    def test(self):
        self.assertEquals(hall_add, redirect('home'))


class empllistTestCase(TestCase):
    def test(self):
        self.assertEquals(employee_list, render(request, 'employee_list.html'))


class emplinfoTestCase(TestCase):
    def test(self):
        self.assertEquals(employees_info, render(request, 'employees_info.html'))

