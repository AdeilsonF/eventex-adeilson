# coding: utf-8
from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription
# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribe_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'created_at', 'email')
    list_filter = ['created_at']
    def subscribe_today(self, obj):
        return obj.created_at.date() == now().date()
    subscribe_today.short_description = _(u'inscrito hoje?')
    subscribe_today.boolean = True


admin.site.register(Subscription, SubscriptionAdmin)