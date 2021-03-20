from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BoardMember)
admin.site.register(Advisor)
admin.site.register(Duty)
admin.site.register(Year)