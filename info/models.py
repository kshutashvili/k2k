# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Flatpage(models.Model):
    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страницы'

    def __unicode__(self):
        return self.title

    slug = models.SlugField(primary_key=True)
    title = models.CharField('Заголовок', max_length=140)
    content = models.TextField('Содержание')
    is_draft = models.BooleanField('Черновик', default=False)

    def get_absolute_url(self):
        return reverse('flatpage', args=(self.slug,))


class LandingTabManager(models.Manager):
    def actual(self, *args, **kwargs):
        kwargs['content__is_draft'] = False
        return self.exclude(content=None).filter(**kwargs)

    def free_tab(self):
        curr = self.aggregate(models.Max('order'))['order__max']
        try:
            return curr + 1
        except TypeError:
            return 1


class LandingTab(models.Model):
    class Meta:
        verbose_name = 'Вкладка на лендинге'
        verbose_name_plural = 'Вкладки на лендинге'
        ordering = ('order',)

    def __unicode__(self):
        return 'Вкладка %i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=objects.free_tab,
                                unique=True)
    content = models.OneToOneField(Flatpage, verbose_name='Страница',
                                   limit_choices_to={'is_draft': False},
                                   blank=True, null=True)
