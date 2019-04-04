# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Mucluc
class MuclucModelAdmin(admin.ModelAdmin):
    
    list_display = ('mucluc', 'noidung', 'date')

admin.site.register(Mucluc, MuclucModelAdmin)