from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class StudentUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)

class StudentUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone'
    
    objects = StudentUserManager()

    def __str__(self):
        return self.phone

class Class(models.Model):
    class_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.class_name

class StudentProfile(models.Model):
    user = models.OneToOneField(StudentUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    status = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'