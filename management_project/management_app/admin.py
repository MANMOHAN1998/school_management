from django.contrib import admin
from .models import *

admin.site.register([StudentUser,Class,StudentProfile])
