# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Teste1',
            cpf='12345689076',
            email='testetes@gmail.com',
            phone='2133334444'
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Teste1', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be False'
        self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
         Subscription.objects.create(name='Teste1', cpf='123456789076', email='testetes@gmail.com',
                                    phone='2133334444')

    def test_cpf_unique(self):
        'Cpf unique'
        s = Subscription(name='Teste21', cpf='123456789076', email='testetes2@gmail.com', phone='2133334444')
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        'Email unique'
        s = Subscription.objects.create(name='Teste241', cpf='12345670002', email='testetes2@gmail.com', phone='33344444')
        self.assertEqual(2, s.pk)