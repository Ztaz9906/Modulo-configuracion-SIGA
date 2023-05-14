# from django.db import models
# from abastecimientoapp.models import TbNunidadMedida

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
#     id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida') #revisar abastecimiento tambien 

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



    




    
