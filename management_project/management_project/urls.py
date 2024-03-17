from django.contrib import admin
from django.urls import path
from management_app.views import *
from management_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-class/', add_class),
    path('register-student/', register_student),
    path('student-login/', student_login),
    path('update-profile/',update_student_profile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
