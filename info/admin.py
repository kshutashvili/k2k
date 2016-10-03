# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from info.models import Flatpage, LandingTab


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


@admin.register(Flatpage)
class FlatpageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'is_draft')
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(LandingTab)
class LandingTabAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'content_url', 'is_draft')

    content_url = ChangeUrl('content', descr='Страница')

    def is_draft(self, obj):
        return obj.content and obj.content.is_draft
    is_draft.boolean = True
    is_draft.short_description = 'Черновик'
