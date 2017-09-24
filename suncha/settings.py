# -*- coding: utf-8 -*-

"""
Django settings for suncha project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

# Application definition
INSTALLED_APPS = [
    'suncha',
    #'cms_shop',
] + INSTALLED_APPS

CMS_TEMPLATES = [
    ('full-width.html', _('Full width')),
    ('left-sidebar.html', _('Left sidebar')),
    ('right-sidebar.html', _('Right sidebar')),
    ('double-sidebar.html', _('Double sidebar')),
]

CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES = [
    ('gallery', _('Gallery')),
]
