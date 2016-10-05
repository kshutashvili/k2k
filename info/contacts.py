# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


class ContactType(object):
    def __init__(self, name, verbose_name, link):
        self.name = name
        self.verbose_name = verbose_name
        self.link = link

    def __unicode__(self):
        return self.verbose_name

    def format_link(self, identifier):
        return self.link.format(id=identifier)


class Phone(ContactType):
    clean_re = re.compile(r'\+?\d+')

    def format_link(self, identifier):
        identifier = ''.join(self.clean_re.findall(identifier))
        return super(Phone, self).format_link(identifier)


phone = Phone('phone', 'Телефон', 'tel:{id}')
email = ContactType('email', 'Почта', 'mailto:{id}')

choices = []
by_name = {}

for c in (phone, email):
    choices.append((c.name, c.verbose_name))
    by_name[c.name] = c
del c
