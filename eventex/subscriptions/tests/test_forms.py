from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
     def test_has_field(self):
        'Form must has 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

     def test_cpf_is_digit(self):
         'CPF must only accept digits.'
         form = self.make_validated_form(cpf='ABCD1234567')
         self.assertItemsEqual(['cpf'], form.errors)

     def test_cpf_has_11_digits(self):
         'CPF must have 11 digits.'
         form = self.make_validated_form(cpf='1234')
         self.assertItemsEqual(['cpf'], form.errors)

     def test_email_is_optional(self):
         'Email is optional'
         form = self.make_validated_form(email='')
         self.assertFalse(form.errors)

     def make_validated_form(self, **kwargs):
         data = dict(name='teste', email='teste@teste.com', cpf='12345678900', phone='86-99887766')
         data.update(kwargs)
         form = SubscriptionForm(data)
         form.is_valid()
         return form