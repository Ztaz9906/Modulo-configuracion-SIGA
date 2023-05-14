# from django.db import models
# from base.models import TbDpersona
# from adminschema.models import TbUser
# from cajero.models import TbDtarjetaAlimentacion
# from abastecimientoapp.models import TbDalmacen

# class TbNclasificacionEvento(models.Model):
#     id_clasificacion_evento = models.AutoField(primary_key=True)
#     nombre_clasificacion_evento = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_clasificacion_evento = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_nclasificacion_evento'
        
# class TbNhorario(models.Model):
#     id_horario = models.AutoField(primary_key=True)
#     nombre_horario = models.TextField()
#     hora_inicio = models.TimeField()
#     hora_fin = models.TimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tb_nhorario'

# class TbCategory(models.Model):
#     name = models.TextField()
#     description = models.TextField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     version = models.IntegerField()
#     color = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'tb_category'

# class TbStructure(models.Model):
#     category = models.ForeignKey(TbCategory, models.DO_NOTHING)
#     estructura_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
#     name = models.TextField()
#     initials = models.TextField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     version = models.IntegerField()
#     branch = models.TextField(blank=True, null=True)  # This field type is a guess.
#     description = models.TextField(blank=True, null=True)
#     capacidad = models.IntegerField(blank=True, null=True)
#     id_sub_director = models.ForeignKey(TbDpersona,models.DO_NOTHING, db_column='id_sub_director', blank=True, null=True)
#     id_tecnico_general = models.ForeignKey(TbDpersona,models.DO_NOTHING, db_column='id_tecnico_general', blank=True, null=True)
#     centro_costo = models.TextField(blank=True, null=True)
#     id_almacen_pertenece = models.ForeignKey(TbDpersona,models.DO_NOTHING, db_column='id_almacen_pertenece', blank=True, null=True)
#     id_tecnico_atm = models.TextField(blank=True, null=True)#ojo mirar por que esta sin ralacion
#     id_especialista_complejo = models.ForeignKey(TbDpersona,models.DO_NOTHING, db_column='id_especialista_complejo', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_structure'

# class TbNclasificacionDistribucion(models.Model):
#     id_clasificacion_distribucion = models.AutoField(primary_key=True)
#     nombre = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_nclasificacion_distribucion'

# class TbNevento(models.Model):
#     id_evento = models.AutoField(primary_key=True)
#     nombre_evento = models.TextField(blank=True, null=True)
#     activo = models.BooleanField()
#     descripcion_evento = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     id_clasificacion_evento = models.ForeignKey(TbNclasificacionEvento, models.DO_NOTHING, db_column='id_clasificacion_evento', blank=True, null=True)
#     accesos = models.IntegerField(blank=True, null=True)
#     orden = models.IntegerField(blank=True, null=True)
#     evento_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='evento_padre', blank=True, null=True)
#     id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
#     icono = models.TextField(blank=True, null=True)
#     color = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_nevento'

       
# class TbDdistribucion(models.Model):
#     id_distribucion = models.AutoField(primary_key=True)
#     nombre = models.TextField(blank=True, null=True)
#     descripcion = models.TextField(blank=True, null=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     id_clasificacion_distribucion = models.ForeignKey(TbNclasificacionDistribucion, models.DO_NOTHING, db_column='id_clasificacion_distribucion', blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     fecha_distribucion = models.DateField(blank=True, null=True)
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
#     activo = models.BooleanField()
#     es_principal = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_ddistribucion'

# class TbDpersonaDistribucion(models.Model):
#     id_persona_distribucion = models.AutoField(primary_key=True)
#     id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     fecha_modificacion = models.DateField(blank=True, null=True)
#     id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion', blank=True, null=True,related_name='id_usuario_modificacion_distribucion')
#     id_distribucion = models.ForeignKey(TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion', blank=True, null=True,related_name='id_distribucion_persona')
#     id_complejo_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo_comedor', blank=True, null=True,related_name='id_complejo_comedor_persona')
#     id_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_comedor', blank=True, null=True,related_name='id_comedor_persona')
#     id_puerta = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta', blank=True, null=True,related_name='id_puerta_persona')
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True,related_name='id_evento_persona')

#     class Meta:
#         managed = False
#         db_table = 'tb_dpersona_distribucion'

# class TbDtarjetaDistribucion(models.Model):
#     id_tarjeta_distribucion = models.AutoField(primary_key=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     fecha_modificacion = models.DateField(blank=True, null=True)
#     id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion', blank=True, null=True,related_name='id_usuario_modificacion_distribucion')
#     id_distribucion = models.ForeignKey(TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion', blank=True, null=True,related_name='id_distribucion_tarjeta')
#     id_complejo_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo_comedor', blank=True, null=True,related_name='id_complejo_comedor_tarjeta')
#     id_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_comedor', blank=True, null=True,related_name='id_comedor_tarjeta')
#     id_puerta = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta', blank=True, null=True,related_name='id_puerta_tarjeta')
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True,related_name='id_evento_tarjeta')
#     id_tarjeta = models.ForeignKey(TbDtarjetaAlimentacion, models.DO_NOTHING, db_column='id_tarjeta', blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_dtarjeta_distribucion'

# class TbNregla(models.Model):
#     id_regla = models.AutoField(primary_key=True)
#     nombre_regla = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_regla = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_nregla'
        
# class TbDvaloresRegla(models.Model):
#     id_valores_regla = models.AutoField(primary_key=True)
#     nombre_valores_regla = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     id_regla = models.ForeignKey(TbNregla, models.DO_NOTHING, db_column='id_regla', blank=True, null=True)
#     id_valor_regla = models.IntegerField(blank=True, null=True)# hay q  ver para q es este id y por que esta ahi sin relacion alguna

#     class Meta:
#         managed = False
#         db_table = 'tb_dvalores_regla'

# # Revisar por q este modelo en la base de datos no tiene ninguna relacion con las tablas 
# class TbLastDistribucion(models.Model):
#     id_temp = models.AutoField(primary_key=True)
#     id_persona = models.CharField(max_length=255, blank=True, null=True)
#     id_usuario_registro = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     fecha_modificacion = models.DateField(blank=True, null=True)
#     id_usuario_modificacion = models.IntegerField(blank=True, null=True)
#     id_distribucion = models.IntegerField(blank=True, null=True)
#     id_complejo_comedor = models.IntegerField(blank=True, null=True)
#     id_comedor = models.IntegerField(blank=True, null=True)
#     id_puerta = models.IntegerField(blank=True, null=True)
#     id_evento = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_last_distribucion'

# class TbNdiaSemana(models.Model):
#     id_dia_semana = models.AutoField(primary_key=True)
#     nombre_dia_semana = models.CharField(max_length=10)
#     abreviatura_dia_semana = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'tb_ndia_semana'

# class TbNrangoEvento(models.Model):
#     id_rango_evento = models.AutoField(primary_key=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_rango_evento = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     hora_inicio = models.TimeField(blank=True, null=True)
#     hora_fin = models.TimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_nrango_evento'

# class TbRdistribucionRegla(models.Model):
#     id_distribucion_regla = models.AutoField(primary_key=True)
#     id_distribucion = models.ForeignKey(TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion', blank=True, null=True)
#     nombre_regla = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     nombre_valor_regla = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_rdistribucion_regla'

# class TbRestructuraRegla(models.Model):
#     id_estructura_regla = models.AutoField(primary_key=True)
#     id_estructura = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
#     id_regla = models.ForeignKey(TbNregla, models.DO_NOTHING, db_column='id_regla', blank=True, null=True)
#     id_valor_regla = models.IntegerField(blank=True, null=True) # por que esta este id asi sin relacion aqui ojo
#     nombre_valor_regla = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_restructura_regla'

# class TbReventoHorario(models.Model):
#     id_evento_horario = models.AutoField(primary_key=True)
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento')
#     id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario')

#     class Meta:
#         managed = False
#         db_table = 'tb_revento_horario'

# class TbReventoRangoEvento(models.Model):
#     id_evento_rango_evento = models.AutoField(primary_key=True)
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
#     id_rango_evento = models.ForeignKey(TbNrangoEvento, models.DO_NOTHING, db_column='id_rango_evento', blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_revento_rango_evento'

# class TbRhorarioDiaSemana(models.Model):
#     id_horario_dia_semana = models.AutoField(primary_key=True)
#     id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
#     id_dia_semana = models.ForeignKey(TbNdiaSemana, models.DO_NOTHING, db_column='id_dia_semana', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_rhorario_dia_semana'

# #revisar por que esta sin ralacion alguna ninnguno de estos id
# class TbTempDistribucionTarjeta(models.Model):
#     id_temp = models.AutoField(primary_key=True)
#     id_persona = models.CharField(max_length=255, blank=True, null=True)
#     id_usuario_registro = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     fecha_modificacion = models.DateField(blank=True, null=True)
#     id_usuario_modificacion = models.IntegerField(blank=True, null=True)
#     id_distribucion = models.IntegerField(blank=True, null=True)
#     id_complejo_comedor = models.IntegerField(blank=True, null=True)
#     id_comedor = models.IntegerField(blank=True, null=True)
#     id_puerta = models.IntegerField(blank=True, null=True)
#     id_evento = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_temp_distribucion_tarjeta'

