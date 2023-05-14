from django.db import models
from base.models import TbDpersona
class TbAvatar(models.Model):
    photo = models.BinaryField(blank=True, null=True)
    photo_dir = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_avatar'

class TbCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()
    color = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'tb_category_admin'

class TbCompanyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        
        db_table = 'tb_company_type'
        
class TbCompany(models.Model):
    company_type = models.ForeignKey(TbCompanyType, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    initials = models.CharField(max_length=10, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        
        db_table = 'tb_company'


class TbFunctionalGrouping(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    functional_grouping_code = models.CharField(primary_key=True, max_length=1)
    active = models.BooleanField()
    register_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_functional_grouping'
        
class TbSystem(models.Model):
    name = models.TextField(blank=True, null=True)
    system_code = models.CharField(primary_key=True, max_length=1)
    active = models.BooleanField()
    register_date = models.DateTimeField(blank=True, null=True)
    acronym = models.TextField(unique=True, blank=True, null=True)
    routing = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_system'

class TbModule(models.Model):
    name = models.TextField(blank=True, null=True)
    module_code = models.CharField(primary_key=True, max_length=1)
    active = models.BooleanField()
    register_date = models.DateTimeField(blank=True, null=True)
    system_code = models.ForeignKey(TbSystem, models.DO_NOTHING, db_column='system_code', blank=True, null=True)
    acronym = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_module'
        
class TbFunctionalGroupingModule(models.Model):
    functional_grouping_code = models.ForeignKey(TbFunctionalGrouping, models.DO_NOTHING, db_column='functional_grouping_code', blank=True, null=True)
    module_code = models.ForeignKey(TbModule, models.DO_NOTHING, db_column='module_code', blank=True, null=True)
    functional_grouping_module_id = models.AutoField(primary_key=True)

    class Meta:
        
        db_table = 'tb_functional_grouping_module'


class TbFunctionality(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=6, blank=True, null=True)
    security_basic_role = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence_code = models.CharField(max_length=3, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    module_code = models.ForeignKey(TbModule, models.DO_NOTHING, db_column='module_code', blank=True, null=True)
    functional_grouping_code = models.ForeignKey(TbFunctionalGrouping, models.DO_NOTHING, db_column='functional_grouping_code', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_functionality'

class TbGroupRoles(models.Model):
    name = models.CharField(unique=True, max_length=255)
    roles = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_group_roles'

class TbResponsability(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        
        db_table = 'tb_responsability'

class TbRgrupoRolIp(models.Model):
    id_grupo_rol_ip = models.AutoField(primary_key=True)
    id_grupo_rol = models.ForeignKey(TbGroupRoles, models.DO_NOTHING, db_column='id_grupo_rol', blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_rgrupo_rol_ip'

class TbRole(models.Model):
    name = models.CharField(unique=True, max_length=255)
    roles = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_role'
        
class TbRolGroupRoles(models.Model):
    group_roles = models.OneToOneField(TbGroupRoles, models.DO_NOTHING, primary_key=True)
    rol = models.ForeignKey(TbRole, models.DO_NOTHING)
    class Meta:
        
        db_table = 'tb_rol_group_roles'
        unique_together = (('group_roles', 'rol'),)

class TbStructure(models.Model):
    category = models.ForeignKey(TbCategory, models.DO_NOTHING)
    company = models.ForeignKey(TbCompany, models.DO_NOTHING, blank=True, null=True)
    estructura_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    initials = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()
    address = models.CharField(max_length=500, blank=True, null=True)
    branch = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        
        db_table = 'tb_structure_admin'


class TbStructureResponsability(models.Model):
    id = models.BigAutoField(primary_key=True)
    structure = models.ForeignKey(TbStructure, models.DO_NOTHING)
    responsability = models.ForeignKey(TbResponsability, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        
        db_table = 'tb_structure_responsability'

class TbUser(models.Model):
    avatar = models.OneToOneField(TbAvatar, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=255)
    username_canonical = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_canonical = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.BooleanField()
    salt = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    locked = models.BooleanField()
    expired = models.BooleanField()
    expires_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()
    credentials_expired = models.BooleanField()
    credentials_expire_at = models.DateTimeField(blank=True, null=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_user'


class TbUserGroupRoles(models.Model):
    user = models.OneToOneField(TbUser, models.DO_NOTHING, primary_key=True)
    group_roles = models.ForeignKey(TbGroupRoles, models.DO_NOTHING)

    class Meta:
        
        db_table = 'tb_user_group_roles'
        unique_together = (('user', 'group_roles'),)


class TbrStructureContact(models.Model):
    structure_contact_id = models.AutoField(primary_key=True)
    structure = models.ForeignKey(TbStructure, models.DO_NOTHING)
    contact_item_id = models.IntegerField(blank=True, null=True)
    structure_contact_value = models.CharField(max_length=50)
    structure_contact_description = models.CharField(max_length=1, blank=True, null=True)
    structure_contact_register_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'tbr_structure_contact'
