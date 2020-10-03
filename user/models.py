from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password):
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            phone=phone,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, phone, password):
        user = self.create_user(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=60, verbose_name='Nome completo')
    email = models.EmailField(max_length=120, unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=15, verbose_name='Telefone')

    is_subscribed = models.BooleanField(default=True, verbose_name='Newsletter')
    is_staff = models.BooleanField(default=False, verbose_name='Funcionário')
    is_admin = models.BooleanField(default=False, verbose_name='Administrador')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email', 'phone']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_module_perms(self, app_label):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin