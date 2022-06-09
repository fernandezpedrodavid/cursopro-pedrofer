from atexit import register
from shutil import register_archive_format
from django.contrib import admin
from pkg_resources import register_finder
from .models import Prueba
# Register your models here.

admin.site.register(Prueba)