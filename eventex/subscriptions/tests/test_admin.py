from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkPaidTest(TestCase):
    def setUp(self):
        # instancia o model admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        # Popula o banco
        Subscription.objects.create(name='AdeilsonT', cpf='123456789022', email='test@test.com')

    def test_has_action(self):
        'Action is installed'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Mark all as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())