# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from info import contacts


credit = 'credit'
transfers = 'transfers'
CHOICES = (
    (credit, 'Кредит'),
    (transfers, 'Переводы')
)


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
        verbose_name = 'Вкладка на лендинге (Кредиты)'
        verbose_name_plural = 'Вкладки на лендинге (Кредиты)'
        ordering = ('order',)

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class LandingTabTransfer(models.Model):
    class Meta:
        verbose_name = 'Вкладка на лендинге (Переводы)'
        verbose_name_plural = 'Вкладки на лендинге (Переводы)'
        ordering = ('order',)

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class LandingTabExtra(models.Model):
    class Meta:
        verbose_name = 'Верхнее меню'
        verbose_name_plural = 'Верхнее меню'
        ordering = ('order',)

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
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

    theme = models.CharField(
        'Тема',
        max_length=20,
        choices=CHOICES,
        default=credit
    )
    email = models.EmailField()
    name = models.CharField('Имя', max_length=200)
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


class MainBlock(models.Model):
    class Meta:
        verbose_name = 'Основной блок'
        verbose_name_plural = 'Основной блок'

    def __unicode__(self):
        return '{}: {}'.format(self.page, self.title)

    page = models.CharField('Страница лендинга',
                            max_length=20,
                            choices=CHOICES,
                            default=credit)
    title = models.CharField('Заголовок', max_length=250)
    text = models.TextField('Текст')
    main_image = models.ImageField('Изображение', upload_to='images/')
    extra_image = models.ImageField(
        'Дополнительное изображения',
        upload_to='images/'
    )
    button1 = models.CharField('Название первой кнопки', max_length=50)
    button2 = models.CharField('Название второй кнопки', max_length=50)


class FooterMenuBlock1Credit(models.Model):
    class Meta:
        verbose_name = 'Меню подвала - Кредит(Блок 1)'
        verbose_name_plural = 'Меню подвала - Кредит (Блок 1)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class FooterMenuBlock2Credit(models.Model):
    class Meta:
        verbose_name = 'Меню подвала - Кредит (Блок 2)'
        verbose_name_plural = 'Меню подвала - Кредит (Блок 2)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class FooterMenuBlock3Credit(models.Model):
    class Meta:
        verbose_name = 'Меню подвала - Кредит (Блок 3)'
        verbose_name_plural = 'Меню подвала - Кредит (Блок 3)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class FooterMenuBlock1Transfer(models.Model):
    class Meta:
        verbose_name = 'Меню подвала - Переводы (Блок 1)'
        verbose_name_plural = 'Меню подвала - Переводы (Блок 1)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class FooterMenuBlock2Transfer(models.Model):
    class Meta:
        verbose_name = 'Меню подвала для - Переводы (Блок 2)'
        verbose_name_plural = 'Меню подвала - Переводы (Блок 2)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class FooterMenuBlock3Transfer(models.Model):
    class Meta:
        verbose_name = 'Меню подвала - Переводы (Блок 3)'
        verbose_name_plural = 'Меню подвала - Переводы (Блок 3)'

    def __unicode__(self):
        if self.content:
            return self.content.title
        return 'Свободная вкладка #%i' % self.order

    objects = LandingTabManager()

    order = models.IntegerField('Порядок', default=0)
    content = models.ForeignKey(Flatpage, verbose_name='Страница',
                                limit_choices_to={'is_draft': False},
                                blank=True, null=True)


class Privileges(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['order']

    def __unicode__(self):
        return self.content[:50]

    page = models.CharField(
        'Страница',
        max_length=20,
        choices=CHOICES,
        default=credit
    )
    icon = models.ImageField('Иконка', upload_to='images/')
    content = models.TextField('Текст')
    order = models.IntegerField('Порядок', default=0)
    draft = models.BooleanField('Черновик', default=False)
