# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

# Create your tests here.
class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'GET /inscricao/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Contex must have the subscription form.'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Adeilson', cpf='1223334',
                    email='adeilson@gmail.com', phone='332411211')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid post'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Adeilson', cpf='000000000012',
                    email='adeilson@gmail.com', phone='332411211')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalide post'
        self.assertEqual(200, self.resp.status_code)

    def test_form_erros(self):
        'Form must contain erros.'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Dont save data.'
        self.assertFalse(Subscription.objects.exists())