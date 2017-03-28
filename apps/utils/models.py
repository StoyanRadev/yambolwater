# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models


@python_2_unicode_compatible
class CreationModifiedMixin(models.Model):

    """ CreationModifiedMixin
    """

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(_('Created By'),
                                   settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.OneToOneField(_('Modified By'),
                                       settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class InfoNetMixin(models.Model):

    """ InfoNetMixin
    """

    slug = models.SlugField(null=True, blank=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    is_InfoNet = models.BooleanField(default=True)

    class Meta:
        abstract = True
