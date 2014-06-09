# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')