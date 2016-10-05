# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from info import contacts


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


class LandingTab(models.Model):
    class Meta:
        verbose_name = 'Вкладка на лендинге'
        verbose_name_plural = 'Вкладки на лендинге'
        ordering = ('order',)

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.OneToOneField(Flatpage, verbose_name='Страница',
                                   limit_choices_to={'is_draft': False},
                                   blank=True, null=True)


class QuestionManager(models.Manager):
    def answered(self, *args, **kwargs):
        kwargs['is_draft'] = False
        return self.filter(*args, **kwargs)


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('order', 'question')

    def __unicode__(self):
        return self.question

    objects = QuestionManager()

    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True, null=True)
    order = models.IntegerField('Порядок', default=0)
    is_draft = models.BooleanField('Черновик', default=True)


class ContactManager(models.Manager):
    def actual(self, *args, **kwargs):
        kwargs['is_actual'] = True
        return self.filter(*args, **kwargs)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __unicode__(self):
        return '{}: {}'.format(self.get_type().verbose_name, self.identifier)

    objects = ContactManager()

    type = models.CharField(verbose_name='Тип', choices=contacts.choices,
                            max_length=20)
    identifier = models.CharField(
        verbose_name='Идентификатор', max_length=255,
        help_text='Номер телефона, адрес электронной почты и т.д.'
    )
    comment = models.CharField('Комментарий', blank=True, null=True,
                               max_length=70)
    is_actual = models.BooleanField('Актуален', default=True)

    def get_type(self):
        return contacts.by_name.get(self.type)

    def get_link(self):
        return self.get_type().format_link(self.identifier)
