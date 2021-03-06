# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms.utils import ErrorList
from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from info.models import (
    Flatpage,
    LandingTab,
    LandingTabTransfer,
    Question,
    Contact,
    MainBlock,
    FooterMenuBlock1Credit,
    FooterMenuBlock2Credit,
    FooterMenuBlock3Credit,
    FooterMenuBlock1Transfer,
    FooterMenuBlock2Transfer,
    FooterMenuBlock3Transfer,
    LandingTabExtra,
    Privileges
)


class ChangeUrl(object):
    def __init__(self, field, descr=None):
        self.field = field
        self.short_description = descr

    def __call__(self, obj):
        obj = getattr(obj, self.field)
        if obj is None:
            return '-'
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                              obj._meta.model_name),
                      args=(obj.pk,))
        return format_html('<a href="{}">{}</a>', url, unicode(obj))


def set_draft(model_admin, request, queryset, value=True):
    queryset.update(is_draft=value)


set_draft.short_description = 'Отметить как черновик'


def publish(model_admin, request, queryset):
    set_draft(model_admin, request, queryset, value=False)


publish.short_description = 'Опубликовать'


@admin.register(Flatpage)
class FlatpageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'is_draft')
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = [set_draft, publish]


@admin.register(LandingTab)
class LandingTabAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'content_url', 'order', 'is_draft')

    content_url = ChangeUrl('content', descr='Страница')

    def is_draft(self, obj):
        return obj.content and obj.content.is_draft

    is_draft.boolean = True
    is_draft.short_description = 'Черновик'


@admin.register(LandingTabTransfer)
class LandingTabTransferAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'content_url', 'order', 'is_draft')

    content_url = ChangeUrl('content', descr='Страница')

    def is_draft(self, obj):
        return obj.content and obj.content.is_draft

    is_draft.boolean = True
    is_draft.short_description = 'Черновик'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_preview', 'theme', 'is_draft', 'order')
    list_filter = ('is_draft', 'theme')
    actions = [set_draft, publish]

    def answer_preview(self, obj):
        if obj.answer and len(obj.answer) > 200:
                return obj.answer[:200] + '...'
        return obj.answer

    answer_preview.short_description = 'Ответ'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'type', 'comment', 'is_actual')
    list_filter = ('is_actual', 'type')
    actions = ['set_actual', 'set_not_actual']

    def set_actual(self, request, queryset, value=True):
        queryset.update(is_actual=value)

    set_actual.short_description = 'Отметить как актуальные'

    def set_not_actual(self, request, queryset):
        self.set_actual(request, queryset, value=False)

    set_not_actual.short_description = 'Отметить как неактуальные'


class MainBlockAdminForm(forms.ModelForm):
    model = MainBlock
    fields = '__all__'

    def clean(self):
        if MainBlock.objects.count() > 2:
            self._errors.setdefault('__all__', ErrorList()).append(
                'Вы можете добавить только два основных блока.'
            )
        return self.cleaned_data


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    form = MainBlockAdminForm
    list_display = ('title', 'page')
    list_filter = ('page',)


@admin.register(Privileges)
class PrivilegesAdmin(admin.ModelAdmin):
    list_display = ('content', 'draft')
    list_filter = ('draft',)


admin.site.register(LandingTabExtra)
admin.site.register(FooterMenuBlock1Credit)
admin.site.register(FooterMenuBlock2Credit)
admin.site.register(FooterMenuBlock3Credit)
admin.site.register(FooterMenuBlock1Transfer)
admin.site.register(FooterMenuBlock2Transfer)
admin.site.register(FooterMenuBlock3Transfer)
