# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _
from .utils import datetime_to_timestamp


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', _('Ezer ez')),
        ('event-warning', _('Partida')),
        ('event-info', _('Jokoa')),
        ('event-success', _('Hitzaldia')),
        ('event-inverse', _('Lehiaketa')),
        ('event-special', _('Txapelketa')),
        ('event-important', _('Berezia')),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    desc = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    css_class = models.CharField(max_length=20, verbose_name=_('Type'),
                                 choices=CSS_CLASS_CHOICES)
    start = models.DateTimeField(verbose_name=_('Start Date'))
    end = models.DateTimeField(verbose_name=_('End Date'), null=True,
                               blank=True)
    all_day = models.BooleanField(verbose_name=_('All Day'),help_text=_('Mark this when the time is irrelevant'))

    @property
    def start_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.start)

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.end)
        
    def getTwitText(self):
        return '[AGENDA] ' + truncatechars(self.title,110) + ' ' + settings.HOST + 'agenda' 

    def __unicode__(self):
        return self.title
