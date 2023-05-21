from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
######################################################################## Pertenece a distibucion ################################
router.register(r'Distribucion_TbCategory', TbCategoryViewSet)
router.register(r'Distribucion_TbNclasificacionEvento', TbNclasificacionEventoViewSet)
router.register(r'Distribucion_TbNhorario', TbNhorarioViewSet)
router.register(r'Distribucion_TbNevento', TbNeventoViewSet)
######################### tabla almacen de asset #############################
router.register(r'Asset_TbDalmacen', TbDalmacenViewSet)
######################### Final #############################
router.register(r'Distribucion_TbStructure', TbStructureViewSet)
######################################################################## Final ############################################
######################################################################## Abastecimiento con asset ###################################################
router.register(r'Abastecimiento_TbNcomposicionPlato', TbNcomposicionPlatoViewSet)
router.register(r'Abastecimiento_TbDmenu', TbDmenuViewSet)       
router.register(r'Abastecimiento_TbNclasificacionPlato', TbNclasificacionPlatoViewSet)
router.register(r'Abastecimiento_TbNtipoProducto', TbNtipoProductoViewSet)
router.register(r'Abastecimiento_TbNcategoriaTipoProducto', TbNcategoriaTipoProductoViewSet)
router.register(r'Abastecimiento_TbNunidadMedida', TbNunidadMedidaViewSet)       
####### Empieza esquema asset ##########
router.register(r'Asset_TbNclasificacionProducto', TbNclasificacionProductoViewSet)
router.register(r'Asset_TbDproducto', TbDproductoViewSet)
router.register(r'Asset_TbRproductoAlmacen', TbRproductoAlmacenViewSet)
router.register(r'Asset_TbFecha', TbFechaViewSet) 
######### Termina esquema assets #########
router.register(r'Abastecimiento_TbDconfiguracionProducto', TbDconfiguracionProductoViewSet)
router.register(r'Abastecimiento_TbDequivalenciaUnidadMedida', TbDequivalenciaUnidadMedidaViewSet)
router.register(r'Abastecimiento_TbNplato', TbNplatoViewSet)
router.register(r'Abastecimiento_TbRmenuPlato', TbRmenuPlatoViewSet)
router.register(r'Abastecimiento_TbRmenuPlatoProducto', TbRmenuPlatoProductoViewSet)
router.register(r'Abastecimiento_TbRplatoEvento', TbRplatoEventoViewSet)
router.register(r'Abastecimiento_TbRplatoProducto', TbRplatoProductoViewSet)  
######################################################################## Final #################################################
######################################################################## Cajero ################################################
router.register(r'Cajero_TbDaccesoEventoSecundario', TbDaccesoEventoSecundarioViewSet)
router.register(r'Cajero_TbDpersonaPuerta', TbDpersonaPuertaViewSet)
router.register(r'Cajero_TbDplanEvento', TbDplanEventoViewSet)
router.register(r'Cajero_TbDsolapinPerdido', TbDsolapinPerdidoViewSet)
router.register(r'Cajero_TbNestadoTarjeta', TbNestadoTarjetaViewSet)
router.register(r'Cajero_TbNtipoError', TbNtipoErrorViewSet)
router.register(r'Cajero_TbNtipoTarjetaViewSet', TbNtipoTarjetaViewSet)
router.register(r'Cajero_TbDtarjetaAlimentacion', TbDtarjetaAlimentacionViewSet)
################################################################ Final ########################################################################
################################################################ Distribucion #################################################################
router.register(r'Distribucion_TbNclasificacionDistribucion', TbNclasificacionDistribucionViewSet)
router.register(r'Distribucion_TbDdistribucion', TbDdistribucionViewSet)
router.register(r'Distribucion_TbDpersonaDistribucion', TbDpersonaDistribucionViewSet)
router.register(r'Distribucion_TbDtarjetaDistribucion', TbDtarjetaDistribucionViewSet)
router.register(r'Distribucion_TbNregla', TbNreglaViewSet)
router.register(r'Distribucion_TbDvaloresRegla', TbDvaloresReglaViewSet)
router.register(r'Distribucion_TbLastDistribucion', TbLastDistribucionViewSet)
router.register(r'Distribucion_TbNdiaSemana', TbNdiaSemanaViewSet)
router.register(r'Distribucion_TbNrangoEvento', TbNrangoEventoViewSet)
router.register(r'Distribucion_TbRdistribucionRegla', TbRdistribucionReglaViewSet)
router.register(r'Distribucion_TbRestructuraRegla', TbRestructuraReglaViewSet)
router.register(r'Distribucion_TbReventoHorario', TbReventoHorarioViewSet)
router.register(r'Distribucion_TbReventoRangoEvento', TbReventoRangoEventoViewSet)
router.register(r'Distribucion_TbRhorarioDiaSemana', TbRhorarioDiaSemanaViewSet)
router.register(r'Distribucion_TbTempDistribucionTarSemana', TbRhorarioDiaSemanaViewSet)
################################################################    Fin      #################################################################
############################################################### Esquema cajero ###############################################################
router.register(r'Cajero_TbDacceso', TbDaccesoViewSet)
router.register(r'Cajero_TbDconfiguracionTarjeta', TbDconfiguracionTarjetaViewSet)
router.register(r'Cajero_TbDerrorAcceso', TbDerrorAccesoViewSet)
router.register(r'Cajero_TbNestadoMovimientoAsignacion', TbNestadoMovimientoAsignacionViewSet)
router.register(r'Cajero_TbMovimientoAsignacion', TbMovimientoAsignacionViewSet)
router.register(r'Cajero_TbRmovimientoAsignacionPlato', TbRmovimientoAsignacionPlatoViewSet)
router.register(r'Cajero_TbRpersonaTarjeta', TbRpersonaTarjetaViewSet)
########################################################################## Fin ################################################################

urlpatterns = [
    path('', include(router.urls)),
]