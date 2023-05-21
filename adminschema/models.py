from django.db import models
from base.models import TbDpersona
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group,Permission

################ Nuevo modelo #################################
class TbInstitucion(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = 'tb_institucion_admin'
        
################   final     #################################



class TbAvatar(models.Model):
    photo = models.BinaryField(blank=True, null=True)
    photo_dir = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_avatar'
        
 
class TbUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
        
class TbUser(AbstractBaseUser, PermissionsMixin):
    avatar = models.OneToOneField(TbAvatar, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    username_canonical = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_canonical = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
    salt = models.CharField(max_length=255)
    locked = models.BooleanField(blank=True, null=True)
    expired = models.BooleanField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    credentials_expired = models.BooleanField(blank=True, null=True)
    credentials_expire_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='tb_user_roles', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='tb_user_permissions', blank=True)
    # id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_institucion = models.ForeignKey(TbInstitucion, models.DO_NOTHING, db_column='id_institucion', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TbUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id_persona', 'id_institucion']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'tb_user'

    def __str__(self):
        return self.username