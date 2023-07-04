from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.contrib.postgres.fields import ArrayField


def add_database(db_name):
    from django.conf import settings
    settings.DATABASES[db_name] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }

################ Nuevo modelo #################################


class TbInstitucion(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    db_name = models.TextField(blank=True, null=True)
    active_modules = ArrayField(models.CharField(
        max_length=200), blank=True, default=list)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        add_database(self.db_name)

    class Meta:
        db_table = 'tb_institucion_admin'

################   final     #################################


class TbAvatar(models.Model):
    photo = models.BinaryField(blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_avatar'


class TbUserManager(BaseUserManager):
    """Manager para usuarios"""

    def create_user(self, email, username, password=None, **extra_fields):
        """Crea un nuevo Usuario"""
        if not email:
            raise ValueError("El usuario debe tener un email")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, username,
                                password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class TbUser(AbstractBaseUser, PermissionsMixin):
    """Modelo BD para Users"""
    avatar = models.OneToOneField(
        TbAvatar, models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    rol = models.ForeignKey(Group, models.DO_NOTHING,
                            related_name='user_rol', blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_institucion = models.ForeignKey(
        TbInstitucion, models.DO_NOTHING, db_column='id_institucion', blank=True, null=True)

    objects = TbUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id_institucion', 'email']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'tb_user'

    def __str__(self):
        """Return String"""
        return self.email
