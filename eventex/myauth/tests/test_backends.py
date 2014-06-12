# coding: utf-8
from django.contrib.auth import get_user_model
from django.test.utils import override_settings
from django.test import TestCase
from eventex.myauth.backends import EmailBackend
from unittest import skip

@skip
class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='adeilson',
                                      email='adeilson@adeilson.com',
                                      password='12345')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='adeilson@adeilson.com',
                                         password='12345')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='adeilson@adeilson.com',
                                         password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@email.com',
                                         password='12345')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))
@skip
class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
                                      email='user1@user1.com', password='12345')
        UserModel.objects.create_user(username='user2',
                                      email='user1@user1.com', password='12345')
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(email='user1@user1.com',
                                        password='12345')
        self.assertIsNone(user)

@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FuncionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='adeilson',
                                      email='adeilson@adeilson.com',
                                      password='12345')

    def test_login_with_email(self):
        result = self.client.login(email='adeilson@adeilson.com',
                                   password='12345')
        self.assertTrue(result)

    def test_login_with_username(self):
        result =self.client.login(username='adeilson@adeilson.com',
                                  password='12345')
        self.assertTrue(result)