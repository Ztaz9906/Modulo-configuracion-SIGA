from django.contrib import admin
# Register your models here.
from .models import (TbNpais, TbNprovincia, TbNtipoEstructura, TbNedificio, TbNestructura,
                     TbNcategoria, TbNapto, TbNsexo, TbNcarrera, TbNcategoriaResidente,
                     TbNgrupo, TbNtipoCurso, TbNcategoriaDocente, TbNorigen, TbNmunicipio,
                     TbNresponsabilidad, TbNcategoriaCientifica, TbNparentesco)

# Registra los modelos en el administrador de Django
admin.site.register(TbNpais)
admin.site.register(TbNprovincia)
admin.site.register(TbNtipoEstructura)
admin.site.register(TbNedificio)
admin.site.register(TbNestructura)
admin.site.register(TbNcategoria)
admin.site.register(TbNapto)
admin.site.register(TbNsexo)
admin.site.register(TbNcarrera)
admin.site.register(TbNcategoriaResidente)
admin.site.register(TbNgrupo)
admin.site.register(TbNtipoCurso)
admin.site.register(TbNcategoriaDocente)
admin.site.register(TbNorigen)
admin.site.register(TbNmunicipio)
admin.site.register(TbNresponsabilidad)
admin.site.register(TbNcategoriaCientifica)
admin.site.register(TbNparentesco)
