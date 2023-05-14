# from django.db import models
# from adminschema.models import TbUser
# from cajero.models import TbNevento


# class TbNcomposicionPlato(models.Model):
#     id_composicion_plato = models.AutoField(primary_key=True)
#     nombre_composicion_plato = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_composicion_plato = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     class Meta:
#         db_table = 'tb_ncomposicion_plato'
        
# class TbDmenu(models.Model):
#     id_menu = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     activo = models.BooleanField()
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     descontado = models.BooleanField()
#     class Meta:
#         db_table = 'tb_dmenu'

# class TbNclasificacionPlato(models.Model):
#     id_clasificacion_plato = models.AutoField(primary_key=True)
#     nombre_clasificacion_plato = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_clasificacion_plato = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     class Meta:
#         db_table = 'tb_nclasificacion_plato'
        
# class TbNtipoProducto(models.Model):
#     id_tipo_producto = models.AutoField(primary_key=True)
#     nombre_tipo_producto = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_tipo_producto = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     class Meta:   
#         db_table = 'tb_ntipo_producto'

# class TbNcategoriaTipoProducto(models.Model):
#     id_categoria_tipo_producto = models.AutoField(primary_key=True)
#     nombre_categoria_tipo_producto = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_categoria_tipo_producto = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     id_tipo_producto = models.ForeignKey(TbNtipoProducto, models.DO_NOTHING, db_column='id_tipo_producto', blank=True, null=True)
#     class Meta:  
#         db_table = 'tb_ncategoria_tipo_producto'

# class TbNunidadMedida(models.Model):
#     id_unidad_medida = models.AutoField(primary_key=True)
#     nombre_unidad_medida = models.TextField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     descripcion_unidad_medida = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     siglas = models.TextField(blank=True, null=True)
#     id_unidad_superior = models.IntegerField(blank=True, null=True)
#     convertible = models.BooleanField(blank=True, null=True)
#     id_unidad_inferior = models.IntegerField(blank=True, null=True)
#     orden = models.IntegerField(blank=True, null=True)
#     clasificacion = models.TextField(blank=False, null=False)
#     class Meta:    
#         db_table = 'tb_nunidad_medida'
 
# ####### Empieza esquema asset ##########
# class TbDalmacen(models.Model):
#     id_almacen = models.AutoField(primary_key=True)
#     nombre_almacen = models.CharField(unique=True, max_length=255)
#     descripcion = models.TextField(blank=True, null=True)
#     id_asset = models.CharField(max_length=1)
#     siglas_almacen = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_dalmacen'

# class TbNclasificacionProducto(models.Model):
#     id_clasificacion_producto = models.AutoField(primary_key=True)
#     nombre_clasificacion_producto = models.CharField(unique=True, max_length=255)
#     descripcion = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()
#     id_asset = models.CharField(max_length=1)
#     class Meta:
#         managed = False
#         db_table = 'tb_nclasificacion_producto'

# class TbDproducto(models.Model):
#     id_producto = models.AutoField(primary_key=True)
#     nombre_producto = models.CharField(max_length=255)
#     id_asset = models.CharField(max_length=1)
#     descripcion = models.TextField(blank=True, null=True)
#     precio_cuc = models.FloatField()
#     precio_cup = models.FloatField(blank=True, null=True)
#     id_clasificacion_producto = models.ForeignKey(TbNclasificacionProducto, models.DO_NOTHING, db_column='id_clasificacion_producto')
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida',blank=True, null=True,related_name='id_unidad_medida_producto') #revisar abastecimiento tambien 

#     class Meta:
#         managed = False
#         db_table = 'tb_dproducto'

# class TbRproductoAlmacen(models.Model):
#     id_producto = models.ForeignKey(TbDproducto, models.DO_NOTHING, db_column='id_producto')
#     id_almacen = models.ForeignKey(TbDalmacen, models.DO_NOTHING, db_column='id_almacen')
#     cantidad = models.DecimalField(max_digits=65535, decimal_places=65535)
#     id_producto_almacen = models.AutoField(primary_key=True)
#     cantidad_anterior = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     class Meta:
#         managed = False
#         db_table = 'tb_rproducto_almacen'
        
# class TbFecha(models.Model):
#     fecha_hora = models.DateTimeField(blank=True, null=True)
#     id_producto_almacen = models.OneToOneField(TbRproductoAlmacen, models.DO_NOTHING, db_column='id_producto_almacen', blank=True, null=True)
#     id_fecha = models.AutoField(primary_key=True)
#     analizado = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_fecha'
 
# ######### Termina esquema assets #########
# class TbDconfiguracionProducto(models.Model):
#     id_configuracion_producto = models.AutoField(primary_key=True)
#     id_categoria_tipo_producto = models.ForeignKey(TbNcategoriaTipoProducto, models.DO_NOTHING, db_column='id_categoria_tipo_producto', blank=True, null=True)
#     gramaje = models.FloatField(blank=True, null=True)
#     precio = models.FloatField(blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateField(blank=True, null=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     id_producto = models.ForeignKey(TbRproductoAlmacen, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida', blank=True, null=True,related_name='id_unidad_medida_configuracion')
#     valor_merma = models.FloatField(blank=True, null=True)
#     cantidad_disponible = models.FloatField(blank=True, null=True)
#     id_unidad_medida_merma = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida_merma', blank=True, null=True,related_name='id_unidad_medida_merma_configuracion')
#     valor_por_cada = models.FloatField(blank=True, null=True)
#     id_unidad_medida_por_cada = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida_por_cada', blank=True, null=True,related_name='id_unidad_medida_por_cada_configuracion')
#     fecha_actualizacion = models.DateField(blank=True, null=True)
#     entidad_actualiza = models.TextField(blank=True, null=True)
#     class Meta:   
#         db_table = 'tb_dconfiguracion_producto'

# class TbDequivalenciaUnidadMedida(models.Model):
#     id_equivalencia_unidad_medida = models.AutoField(primary_key=True)
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida', blank=True, null=True,related_name='id_unidad_medida_equivalencia')
#     cantidad = models.FloatField(blank=True, null=True)
#     id_unidad_medida_equivalente = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida_equivalente', blank=True, null=True,related_name='id_unidad_medida_equivalente_equivalencia')
#     cantidad_equivalente = models.FloatField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     class Meta:  
#         db_table = 'tb_dequivalencia_unidad_medida' 
              
# class TbNplato(models.Model):
#     id_plato = models.AutoField(primary_key=True)
#     nombre_plato = models.TextField(blank=True, null=True)
#     activo = models.BooleanField()
#     descripcion_plato = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateField(blank=True, null=True)
#     precio_plato = models.FloatField(blank=True, null=True)
#     gramaje = models.IntegerField(blank=True, null=True)
#     id_clasificacion_plato = models.ForeignKey(TbNclasificacionPlato, models.DO_NOTHING, db_column='id_clasificacion_plato', blank=True, null=True)
#     id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
#     id_composicion_plato = models.ForeignKey(TbNcomposicionPlato, models.DO_NOTHING, db_column='id_composicion_plato', blank=True, null=True)
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida', blank=True, null=True)
#     class Meta:  
#         db_table = 'tb_nplato'
        
# class TbRmenuPlato(models.Model):
#     id_menu_plato = models.AutoField(primary_key=True)
#     id_menu = models.ForeignKey(TbDmenu, models.DO_NOTHING, db_column='id_menu')
#     id_plato = models.ForeignKey(TbNplato, models.DO_NOTHING, db_column='id_plato')
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento')
#     es_visible = models.BooleanField(blank=True, null=True)
#     sujeto_cambio = models.BooleanField(blank=True, null=True)
#     class Meta:
#         db_table = 'tb_rmenu_plato'
        
# class TbRmenuPlatoProducto(models.Model):
#     id_menu_plato_producto = models.AutoField(primary_key=True)
#     id_menu = models.ForeignKey(TbDmenu, models.DO_NOTHING, db_column='id_menu', blank=True, null=True)
#     id_plato = models.ForeignKey(TbNplato, models.DO_NOTHING, db_column='id_plato', blank=True, null=True)
#     id_configuracion_producto = models.ForeignKey(TbDconfiguracionProducto, models.DO_NOTHING, db_column='id_configuracion_producto', blank=True, null=True)
#     cantidad_disponible = models.FloatField(blank=True, null=True)
#     cant_falta_sujeto_cambio = models.FloatField(blank=True, null=True)
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
#     class Meta:    
#         db_table = 'tb_rmenu_plato_producto'
        
# class TbRplatoEvento(models.Model):
#     id_plato_evento = models.AutoField(primary_key=True)
#     id_plato = models.ForeignKey(TbNplato, models.DO_NOTHING, db_column='id_plato', blank=True, null=True)
#     id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
#     class Meta:   
#         db_table = 'tb_rplato_evento'
        
# class TbRplatoProducto(models.Model):
#     id_plato_producto = models.AutoField(primary_key=True)
#     id_plato = models.ForeignKey(TbNplato, models.DO_NOTHING, db_column='id_plato', blank=True, null=True)
#     id_producto = models.ForeignKey(TbDproducto,on_delete = models.DO_NOTHING, db_column='id_producto', blank=True, null=True) # revisar si esta bien pensado esta relacion
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida', blank=True, null=True)
#     gramaje = models.FloatField(blank=True, null=True)
#     class Meta:   
#         db_table = 'tb_rplato_producto'
