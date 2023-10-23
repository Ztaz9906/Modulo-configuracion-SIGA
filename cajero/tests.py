from django.test import TestCase
from .models import TbNunidadMedida, TbNevento, TbNclasificacionEvento, TbRdistribucionRegla, TbRpersonaTarjeta, TbNhorario, TbNdiaSemana, TbCategory, TbDsolapinPerdido, TbDvaloresRegla, TbNregla, TbDaccesoEventoSecundario, TbDpersonaIPPuerta, TbCategory, TbNclasificacionPlato, TbNtipoProducto, TbDproducto,  TbStructure, TbNtipoTarjeta, TbDtarjetaAlimentacion, TbNestadoTarjeta, TbRpersonaTarjeta
from base.models import TbNtipoEstructura, TbNestructura, TbNsexo, TbNmunicipio, TbNprovincia, TbNpais, TbNcategoria
from datetime import date
from django.utils import timezone
from datetime import datetime
from datetime import time
from reservacion.models import TbDperiodoReservacion, TbDelementosMostrar, TbDresponsableAreaPersonas
from configuracion.models import TbDdatosContacto, TbDconfiguracionProceso
from cobro.models import TbNconfiguracionCobro, TbNtipoCobro, TbNvaloresConfiguracionCobro
from autenticacion.models.entities.institucion import Institucion
from autenticacion.models.entities.usuario import Usuario
from autenticacion.models.entities.persona import Persona
from autenticacion.models.entities.torpedo import TbDpersonaTorpedo
from autenticacion.models.entities.perfil import Perfil
from autenticacion.models.entities.groups import Group
from autenticacion.models.entities.configuracion_comensales import TbDconfiguracionPersona
from django.db.utils import IntegrityError


class TbNclasificacionPlatoTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para enlazarla
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        # Crea una instancia de TbNclasificacionPlato para pruebas
        self.clasificacion_plato = TbNclasificacionPlato.objects.create(
            id_institucion=self.institucion,
            nombre_clasificacion_plato="Clasificación de Plato de Prueba",
            activo=True,
            descripcion_clasificacion_plato="Descripción de Clasificación de Plato de Prueba",
            fecha_registro="2023-09-28",  # Ajusta la fecha según tus necesidades
        )

    def test_creacion_de_clasificacion_plato(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.clasificacion_plato.nombre_clasificacion_plato, "Clasificación de Plato de Prueba")
        self.assertTrue(self.clasificacion_plato.activo)
        self.assertEqual(self.clasificacion_plato.descripcion_clasificacion_plato,
                         "Descripción de Clasificación de Plato de Prueba")

    def test_actualizacion_de_clasificacion_plato(self):
        # Realiza una actualización en la instancia
        self.clasificacion_plato.nombre_clasificacion_plato = "Nueva Clasificación de Plato"
        self.clasificacion_plato.save()

        # Verifica si la actualización se realizó correctamente
        updated_clasificacion_plato = TbNclasificacionPlato.objects.get(pk=self.clasificacion_plato.pk)
        self.assertEqual(updated_clasificacion_plato.nombre_clasificacion_plato, "Nueva Clasificación de Plato")

    def test_eliminacion_de_clasificacion_plato(self):
        # Obtiene el ID de la clasificación de plato antes de eliminarla
        clasificacion_plato_id = self.clasificacion_plato.id_clasificacion_plato
        self.clasificacion_plato.delete()

        # Verifica si la clasificación de plato se ha eliminado correctamente
        with self.assertRaises(TbNclasificacionPlato.DoesNotExist):
            TbNclasificacionPlato.objects.get(id_clasificacion_plato=clasificacion_plato_id)


class TbNunidadMedidaTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para enlazarla
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        # Crea una instancia de TbNunidadMedida para pruebas
        self.unidad_medida = TbNunidadMedida.objects.create(
            id_institucion=self.institucion,
            nombre_unidad_medida="Unidad de Medida de Prueba",
            activo=True,
            descripcion_unidad_medida="Descripción de la Unidad de Medida de Prueba",
            fecha_registro="2023-09-28",
            siglas="UM",
            clasificacion="Clasificación UM",
        )

    def test_creacion_de_unidad_medida(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.unidad_medida.nombre_unidad_medida, "Unidad de Medida de Prueba")
        self.assertEqual(self.unidad_medida.siglas, "UM")
        self.assertEqual(self.unidad_medida.clasificacion, "Clasificación UM")

    def test_actualizacion_de_unidad_medida(self):
        # Realiza una actualización en la instancia
        self.unidad_medida.nombre_unidad_medida = "Nueva Unidad de Medida"
        self.unidad_medida.save()

        # Verifica si la actualización se realizó correctamente
        updated_unidad_medida = TbNunidadMedida.objects.get(pk=self.unidad_medida.pk)
        self.assertEqual(updated_unidad_medida.nombre_unidad_medida, "Nueva Unidad de Medida")

    def test_eliminacion_de_unidad_medida(self):
        # Obtiene el ID de la unidad de medida antes de eliminarla
        unidad_medida_id = self.unidad_medida.id_unidad_medida
        self.unidad_medida.delete()

        # Verifica si la unidad de medida se ha eliminado correctamente
        with self.assertRaises(TbNunidadMedida.DoesNotExist):
            TbNunidadMedida.objects.get(id_unidad_medida=unidad_medida_id)


class TbNtipoProductoTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para enlazarla
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        # Crea una instancia de TbNtipoProducto para pruebas
        self.tipo_producto = TbNtipoProducto.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_producto="Tipo de Producto de Prueba",
            activo=True,
            descripcion_tipo_producto="Descripción del Tipo de Producto de Prueba",
            fecha_registro="2023-09-28",  # Ajusta la fecha según tus necesidades
        )

    def test_creacion_de_tipo_producto(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.tipo_producto.nombre_tipo_producto, "Tipo de Producto de Prueba")
        self.assertTrue(self.tipo_producto.activo)
        self.assertEqual(self.tipo_producto.descripcion_tipo_producto, "Descripción del Tipo de Producto de Prueba")

    def test_actualizacion_de_tipo_producto(self):
        # Realiza una actualización en la instancia
        self.tipo_producto.nombre_tipo_producto = "Nuevo Tipo de Producto"
        self.tipo_producto.save()

        # Verifica si la actualización se realizó correctamente
        updated_tipo_producto = TbNtipoProducto.objects.get(pk=self.tipo_producto.pk)
        self.assertEqual(updated_tipo_producto.nombre_tipo_producto, "Nuevo Tipo de Producto")

    def test_eliminacion_de_tipo_producto(self):
        # Obtiene el ID del tipo de producto antes de eliminarlo
        tipo_producto_id = self.tipo_producto.id_tipo_producto
        self.tipo_producto.delete()

        # Verifica si el tipo de producto se ha eliminado correctamente
        with self.assertRaises(TbNtipoProducto.DoesNotExist):
            TbNtipoProducto.objects.get(id_tipo_producto=tipo_producto_id)


class TbDproductoTestCase(TestCase):
    def setUp(self):
        # Crea instancias de Institucion, TbNtipoProducto y TbNunidadMedida para enlazarlas
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        self.tipo_producto = TbNtipoProducto.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_producto="Tipo de Producto de Prueba",
            activo=True,
            descripcion_tipo_producto="Descripción del Tipo de Producto de Prueba",
            fecha_registro="2023-09-28",
        )

        self.unidad_medida = TbNunidadMedida.objects.create(
            id_institucion=self.institucion,
            nombre_unidad_medida="Unidad de Medida de Prueba",
            activo=True,
            descripcion_unidad_medida="Descripción de la Unidad de Medida de Prueba",
            fecha_registro="2023-09-28",
            siglas="UM",
            clasificacion="Clasificación UM",
        )

        # Crea una instancia de TbDproducto para pruebas
        self.producto = TbDproducto.objects.create(
            id_institucion=self.institucion,
            nombre_producto="Producto de Prueba",
            descripcion="Descripción del Producto de Prueba",
            precio_cup=10.99,
            id_tipo_producto=self.tipo_producto,
            id_unidad_medida=self.unidad_medida,
        )

    def test_creacion_de_producto(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.producto.nombre_producto, "Producto de Prueba")
        self.assertEqual(self.producto.precio_cup, 10.99)
        self.assertEqual(self.producto.id_tipo_producto, self.tipo_producto)
        self.assertEqual(self.producto.id_unidad_medida, self.unidad_medida)

    def test_actualizacion_de_producto(self):
        # Realiza una actualización en la instancia
        self.producto.nombre_producto = "Nuevo Producto"
        self.producto.save()

        # Verifica si la actualización se realizó correctamente
        updated_producto = TbDproducto.objects.get(pk=self.producto.pk)
        self.assertEqual(updated_producto.nombre_producto, "Nuevo Producto")

    def test_eliminacion_de_producto(self):
        # Obtiene el ID del producto antes de eliminarlo
        producto_id = self.producto.id_producto
        self.producto.delete()

        # Verifica si el producto se ha eliminado correctamente
        with self.assertRaises(TbDproducto.DoesNotExist):
            TbDproducto.objects.get(id_producto=producto_id)


class TbNtipoTarjetaTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para enlazarla
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        # Crea una instancia de TbNtipoTarjeta para pruebas
        self.tipo_tarjeta = TbNtipoTarjeta.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_tarjeta="Tipo de Tarjeta de Prueba",
            fecha_registro="2023-09-28",
            descripcion="Descripción del Tipo de Tarjeta de Prueba",
            activo=True,
            color="Azul",
        )

    def test_creacion_de_tipo_tarjeta(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.tipo_tarjeta.nombre_tipo_tarjeta, "Tipo de Tarjeta de Prueba")
        self.assertEqual(self.tipo_tarjeta.color, "Azul")

    def test_actualizacion_de_tipo_tarjeta(self):
        # Realiza una actualización en la instancia
        self.tipo_tarjeta.nombre_tipo_tarjeta = "Nuevo Tipo de Tarjeta"
        self.tipo_tarjeta.save()

        # Verifica si la actualización se realizó correctamente
        updated_tipo_tarjeta = TbNtipoTarjeta.objects.get(pk=self.tipo_tarjeta.pk)
        self.assertEqual(updated_tipo_tarjeta.nombre_tipo_tarjeta, "Nuevo Tipo de Tarjeta")

    def test_eliminacion_de_tipo_tarjeta(self):
        # Obtiene el ID del tipo de tarjeta antes de eliminarlo
        tipo_tarjeta_id = self.tipo_tarjeta.id_tipo_tarjeta
        self.tipo_tarjeta.delete()

        # Verifica si el tipo de tarjeta se ha eliminado correctamente
        with self.assertRaises(TbNtipoTarjeta.DoesNotExist):
            TbNtipoTarjeta.objects.get(id_tipo_tarjeta=tipo_tarjeta_id)

    def setUp(self):
        # Crea una instancia de Institucion para enlazarla
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        # Crea una instancia de TbNtipoTarjeta para pruebas
        self.tipo_tarjeta = TbNtipoTarjeta.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_tarjeta="Tipo de Tarjeta de Prueba",
            fecha_registro="2023-09-28",
            descripcion="Descripción del Tipo de Tarjeta de Prueba",
            activo=True,
            color="Azul",
        )

    def test_creacion_de_tipo_tarjeta(self):
        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(self.tipo_tarjeta.nombre_tipo_tarjeta, "Tipo de Tarjeta de Prueba")
        self.assertEqual(self.tipo_tarjeta.color, "Azul")

    def test_actualizacion_de_tipo_tarjeta(self):
        # Realiza una actualización en la instancia
        self.tipo_tarjeta.nombre_tipo_tarjeta = "Nuevo Tipo de Tarjeta"
        self.tipo_tarjeta.save()

        # Verifica si la actualización se realizó correctamente
        updated_tipo_tarjeta = TbNtipoTarjeta.objects.get(pk=self.tipo_tarjeta.pk)
        self.assertEqual(updated_tipo_tarjeta.nombre_tipo_tarjeta, "Nuevo Tipo de Tarjeta")

    def test_eliminacion_de_tipo_tarjeta(self):
        # Obtiene el ID del tipo de tarjeta antes de eliminarlo
        tipo_tarjeta_id = self.tipo_tarjeta.id_tipo_tarjeta
        self.tipo_tarjeta.delete()

        # Verifica si el tipo de tarjeta se ha eliminado correctamente
        with self.assertRaises(TbNtipoTarjeta.DoesNotExist):
            TbNtipoTarjeta.objects.get(id_tipo_tarjeta=tipo_tarjeta_id)


class TbDtarjetaAlimentacionTestCase(TestCase):
    def setUp(self):
        # Crea instancias de modelos relacionados
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        self.estado_tarjeta = TbNestadoTarjeta.objects.create(
            id_institucion=self.institucion,
            nombre_estado_tarjeta="Estado de Prueba",
            fecha_registro=date.today(),
            descripcion="Descripción del Estado de Prueba",
            activo=True,
        )

        self.usuario = Usuario.objects.create(
            email="usuario@ejemplo.com",
            institucion=self.institucion,
        )

        self.tipo_tarjeta = TbNtipoTarjeta.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_tarjeta="Tipo de Tarjeta de Prueba",
            fecha_registro=date.today(),
            descripcion="Descripción del Tipo de Tarjeta de Prueba",
            activo=True,
            color="Azul",
        )

    def test_creacion_de_tarjeta_alimentacion(self):
        tarjeta_alimentacion = TbDtarjetaAlimentacion(
            id_institucion=self.institucion,
            codigo="COD1",
            numero_serie="NS1",
            id_estado_tarjeta=self.estado_tarjeta,
            fecha_inicio=date.today(),
            id_usuario_registro=self.usuario,
            id_tipo_tarjeta=self.tipo_tarjeta,
            fecha_fin=date.today(),
            id_usuario_modificacion=self.usuario,
        )
        tarjeta_alimentacion.save()

        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(tarjeta_alimentacion.codigo, "COD1")
        self.assertEqual(tarjeta_alimentacion.numero_serie, "NS1")

    def test_actualizacion_de_tarjeta_alimentacion(self):
        tarjeta_alimentacion = TbDtarjetaAlimentacion(
            id_institucion=self.institucion,
            codigo="COD2",
            numero_serie="NS2",
            id_estado_tarjeta=self.estado_tarjeta,
            fecha_inicio=date.today(),
            id_usuario_registro=self.usuario,
            id_tipo_tarjeta=self.tipo_tarjeta,
            fecha_fin=date.today(),
            id_usuario_modificacion=self.usuario,
        )
        tarjeta_alimentacion.save()

        # Realiza una actualización en la instancia
        tarjeta_alimentacion.codigo = "COD3"
        tarjeta_alimentacion.save()

        # Verifica si la actualización se realizó correctamente
        updated_tarjeta_alimentacion = TbDtarjetaAlimentacion.objects.get(
            pk=tarjeta_alimentacion.pk)
        self.assertEqual(updated_tarjeta_alimentacion.codigo, "COD3")

    def test_eliminacion_de_tarjeta_alimentacion(self):
        tarjeta_alimentacion = TbDtarjetaAlimentacion(
            id_institucion=self.institucion,
            codigo="COD4",
            numero_serie="NS4",
            id_estado_tarjeta=self.estado_tarjeta,
            fecha_inicio=date.today(),
            id_usuario_registro=self.usuario,
            id_tipo_tarjeta=self.tipo_tarjeta,
            fecha_fin=date.today(),
            id_usuario_modificacion=self.usuario,
        )
        tarjeta_alimentacion.save()

        # Obtiene el ID de la tarjeta antes de eliminarla
        tarjeta_id = tarjeta_alimentacion.id_tarjeta_alimentacion
        tarjeta_alimentacion.delete()

        # Verifica si la tarjeta se ha eliminado correctamente
        with self.assertRaises(TbDtarjetaAlimentacion.DoesNotExist):
            TbDtarjetaAlimentacion.objects.get(id_tarjeta_alimentacion=tarjeta_id)


class TbRpersonaTarjetaTestCase(TestCase):
    def setUp(self):
        # Crea instancias de modelos relacionados
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

        self.persona = Persona.objects.create(
            nombre_completo="Nombre de Persona",
            ci="12345",
            institucion=self.institucion,
            # otros campos relacionados aquí
        )

        self.tarjeta = TbDtarjetaAlimentacion(
            id_institucion=self.institucion,
            codigo="COD1",
            numero_serie="NS1",
            # otros campos relacionados aquí
        )
        self.tarjeta.save()

    def test_creacion_de_r_persona_tarjeta(self):
        r_persona_tarjeta = TbRpersonaTarjeta(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_tarjeta=self.tarjeta,
            fecha_registro=date.today(),
            activo=True,
        )
        r_persona_tarjeta.save()

        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(r_persona_tarjeta.id_persona, self.persona)
        self.assertEqual(r_persona_tarjeta.id_tarjeta, self.tarjeta)

    def test_edicion_de_r_persona_tarjeta(self):
        r_persona_tarjeta = TbRpersonaTarjeta(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_tarjeta=self.tarjeta,
            fecha_registro=date.today(),
            activo=True,
        )
        r_persona_tarjeta.save()

        # Realiza la edición
        nuevo_tarjeta = TbDtarjetaAlimentacion(
            id_institucion=self.institucion,
            codigo="COD2",
            numero_serie="NS2",
            # otros campos relacionados aquí
        )
        nuevo_tarjeta.save()

        r_persona_tarjeta.id_tarjeta = nuevo_tarjeta
        r_persona_tarjeta.save()

        # Verifica si la instancia se ha editado correctamente
        self.assertEqual(r_persona_tarjeta.id_tarjeta, nuevo_tarjeta)

    def test_eliminar_r_persona_tarjeta(self):
        r_persona_tarjeta = TbRpersonaTarjeta(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_tarjeta=self.tarjeta,
            fecha_registro=date.today(),
            activo=True,
        )
        r_persona_tarjeta.save()

        # Realiza la eliminación
        r_persona_tarjeta.delete()

        # Verifica si la instancia se ha eliminado correctamente
        with self.assertRaises(TbRpersonaTarjeta.DoesNotExist):
            TbRpersonaTarjeta.objects.get(id_persona_tarjeta=r_persona_tarjeta.id_persona_tarjeta)


class TbDpersonaIPPuertaTestCase(TestCase):

    def setUp(self):
        # Crear instancias de modelos relacionados
        self.institucion = Institucion.objects.create(
            name='Instituto', description='Descripcion', active=True)
        self.tb_structure = TbStructure.objects.create(
            id_institucion=self.institucion,
            name='Estructura 1',
            category=TbCategory.objects.create(
                id_institucion=self.institucion,
                name='Categoria 1',
                color='Azul',
                base=True
            )
        )
        self.usuario = Usuario.objects.create(
            username='usuario1',
            email='usuario1@ejemplo.com',
            institucion=self.institucion
        )

    def test_adicion(self):
        # Prueba de adición
        persona_puerta = TbDpersonaIPPuerta.objects.create(
            id_institucion=self.institucion,
            id_puerta=self.tb_structure,
            ip_puerta='192.168.0.1',
            id_usuario_registro=self.usuario
        )
        self.assertEqual(persona_puerta.ip_puerta, '192.168.0.1')

    def test_edicion(self):
        # Prueba de edición
        persona_puerta = TbDpersonaIPPuerta.objects.create(
            id_institucion=self.institucion,
            id_puerta=self.tb_structure,
            ip_puerta='192.168.0.1',
            id_usuario_registro=self.usuario
        )
        persona_puerta.ip_puerta = '192.168.0.2'
        persona_puerta.save()
        self.assertEqual(persona_puerta.ip_puerta, '192.168.0.2')

    def test_eliminacion(self):
        # Prueba de eliminación
        persona_puerta = TbDpersonaIPPuerta.objects.create(
            id_institucion=self.institucion,
            id_puerta=self.tb_structure,
            ip_puerta='192.168.0.1',
            id_usuario_registro=self.usuario
        )
        persona_puerta_id = persona_puerta.id_ip_puerta
        persona_puerta.delete()
        with self.assertRaises(TbDpersonaIPPuerta.DoesNotExist):
            TbDpersonaIPPuerta.objects.get(id_ip_puerta=persona_puerta_id)


class TbDaccesoEventoSecundarioTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion
        self.institucion = Institucion.objects.create(
            name="Institución de Prueba",
            description="Descripción de la Institución de Prueba",
            active=True,
            active_modules=["Módulo1", "Módulo2"],
        )

    def test_agregar_dacceso_evento_secundario(self):
        cantidad_acceso = 10  # Cantidad de acceso que deseas probar
        fecha_registro = date.today()  # Fecha de registro actual
        acceso_evento_secundario = TbDaccesoEventoSecundario(
            id_institucion=self.institucion,
            cantidad_acceso=cantidad_acceso,
            fecha_registro=fecha_registro,
        )
        acceso_evento_secundario.save()

        # Verifica si la instancia se ha creado correctamente
        self.assertEqual(acceso_evento_secundario.cantidad_acceso, cantidad_acceso)
        self.assertEqual(acceso_evento_secundario.fecha_registro, fecha_registro)

    def test_editar_dacceso_evento_secundario(self):
        # Crea una instancia de acceso evento secundario
        cantidad_acceso_original = 5
        fecha_registro = date.today()
        acceso_evento_secundario = TbDaccesoEventoSecundario(
            id_institucion=self.institucion,
            cantidad_acceso=cantidad_acceso_original,
            fecha_registro=fecha_registro,
        )
        acceso_evento_secundario.save()

        # Realiza la edición
        cantidad_acceso_nuevo = 15
        acceso_evento_secundario.cantidad_acceso = cantidad_acceso_nuevo
        acceso_evento_secundario.save()

        # Verifica si la instancia se ha editado correctamente
        self.assertEqual(acceso_evento_secundario.cantidad_acceso, cantidad_acceso_nuevo)

    def test_eliminar_dacceso_evento_secundario(self):
        cantidad_acceso = 8
        fecha_registro = date.today()
        acceso_evento_secundario = TbDaccesoEventoSecundario(
            id_institucion=self.institucion,
            cantidad_acceso=cantidad_acceso,
            fecha_registro=fecha_registro,
        )
        acceso_evento_secundario.save()

        # Realiza la eliminación
        acceso_evento_secundario.delete()

        # Verifica si la instancia se ha eliminado correctamente
        with self.assertRaises(TbDaccesoEventoSecundario.DoesNotExist):
            TbDaccesoEventoSecundario.objects.get(
                id_acceso_evento_secundario=acceso_evento_secundario.id_acceso_evento_secundario)


class TbDpersonaTorpedoTestCase(TestCase):

    def setUp(self):
        # Crear instancias de modelos relacionados
        self.institucion = Institucion.objects.create(
            name='Instituto',
            description='Descripcion',
            active=True
        )

        self.sexo = TbNsexo.objects.create(
            nombre_sexo='Masculino',
            fecha_registro_sexo=datetime.now(),
            activo=True
        )

        self.pais = TbNpais.objects.create(
            nombre_pais='Pais 1',
            fecha_registro_pais=datetime.now(),
            activo=True
        )

        self.provincia = TbNprovincia.objects.create(
            nombre_provincia='Provincia 1',
            fecha_registro_provincia=datetime.now(),
            descripcion_provincia='Descripcion',
            codigo_oficial_provincia='001',
            activo=True,
            abreviatura='PV',
            id_pais=self.pais
        )

        self.municipio = TbNmunicipio.objects.create(
            id_provincia=self.provincia,
            nombre_municipio='Municipio 1',
            fecha_registro_municipio=datetime.now(),
            descripcion_municipio='Descripción del municipio',
            activo=True,
            codigo_oficial_municipio=123
        )

    def test_registro(self):
        # Prueba de registro
        persona = TbDpersonaTorpedo.objects.create(
            id_institucion=self.institucion,
            nombre_completo='Juan Perez',
            ci='123456',
            id_sexo=self.sexo,
            id_municipio=self.municipio,
            id_provincia=self.provincia,
            id_pais=self.pais
        )
        self.assertEqual(persona.nombre_completo, 'Juan Perez')

    def test_edicion(self):
        # Prueba de edición
        persona = TbDpersonaTorpedo.objects.create(
            nombre_completo='Juan Perez',
            ci='123456',
            id_institucion=self.institucion,
            id_sexo=self.sexo,
            id_municipio=self.municipio,
            id_provincia=self.provincia,
            id_pais=self.pais
        )
        persona.nombre_completo = 'Pedro Gomez'
        persona.save()
        self.assertEqual(persona.nombre_completo, 'Pedro Gomez')

    def test_eliminacion(self):
        # Prueba de eliminación
        persona = TbDpersonaTorpedo.objects.create(
            nombre_completo='Juan Perez',
            ci='123456',
            id_institucion=self.institucion,
            id_sexo=self.sexo,
            id_municipio=self.municipio,
            id_provincia=self.provincia,
            id_pais=self.pais
        )
        persona_id = persona.id_persona_torpedo
        persona.delete()
        with self.assertRaises(TbDpersonaTorpedo.DoesNotExist):
            TbDpersonaTorpedo.objects.get(id_persona_torpedo=persona_id)


class TbDsolapinPerdidoTestCaseeditareliminar(TestCase):
    def setUp(self):
        # Crear una instancia de Institucion para usarla en las pruebas
        self.institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True,
        )

        # Crear una instancia de Usuario para usarla en las pruebas
        self.usuario = Usuario.objects.create(
            email="usuario@ejemplo.com",
            institucion=self.institucion,
        )

        # Crear una instancia de Persona para usarla en las pruebas
        self.persona = Persona.objects.create(
            nombre_completo="Nombre de la Persona",
            ci="123456789",
            solapin="SOL123",
            institucion=self.institucion,
        )

    def test_creacion_dsolapin_perdido(self):
        # Crear una instancia de TbDsolapinPerdido y asociarla con Usuario y Persona
        dsolapin_perdido = TbDsolapinPerdido.objects.create(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_usuario_registro=self.usuario,
            activo=True,
        )

        # Comprobar que la instancia se creó correctamente
        self.assertEqual(dsolapin_perdido.id_institucion, self.institucion)
        self.assertEqual(dsolapin_perdido.id_persona, self.persona)
        self.assertEqual(dsolapin_perdido.id_usuario_registro, self.usuario)
        self.assertTrue(dsolapin_perdido.activo)

    # Puedes agregar más pruebas según sea necesario


class TbDsolapinPerdidoTestCase(TestCase):
    def setUp(self):
        # Crear una instancia de Institucion para usarla en las pruebas
        self.institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True,
        )

        # Crear una instancia de Usuario para usarla en las pruebas
        self.usuario = Usuario.objects.create(
            email="usuario@ejemplo.com",
            institucion=self.institucion,
        )

        # Crear una instancia de Persona para usarla en las pruebas
        self.persona = Persona.objects.create(
            nombre_completo="Nombre de la Persona",
            ci="123456789",
            solapin="SOL123",
            institucion=self.institucion,
        )

        # Crear una instancia de TbDsolapinPerdido para editar y eliminar
        self.dsolapin_perdido = TbDsolapinPerdido.objects.create(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_usuario_registro=self.usuario,
            activo=True,
        )

    def test_editar_dsolapin_perdido(self):
        # Modificar los campos de la instancia de TbDsolapinPerdido
        self.dsolapin_perdido.id_institucion = Institucion.objects.create(
            name="Nueva Institución",
            description="Nueva Descripción",
            active=False,
        )
        self.dsolapin_perdido.id_persona = Persona.objects.create(
            nombre_completo="Nuevo Nombre",
            ci="987654321",
            solapin="SOL456",
            institucion=self.institucion,
        )
        self.dsolapin_perdido.activo = False
        self.dsolapin_perdido.save()

        # Recuperar la instancia actualizada de la base de datos
        dsolapin_perdido_actualizado = TbDsolapinPerdido.objects.get(pk=self.dsolapin_perdido.id_solapin_perdido)

        # Comprobar que los campos se actualizaron correctamente
        self.assertEqual(dsolapin_perdido_actualizado.id_institucion.name, "Nueva Institución")
        self.assertEqual(dsolapin_perdido_actualizado.id_persona.nombre_completo, "Nuevo Nombre")
        self.assertFalse(dsolapin_perdido_actualizado.activo)

    def test_eliminar_dsolapin_perdido(self):
        # Eliminar la instancia de TbDsolapinPerdido
        self.dsolapin_perdido.delete()

        # Intentar recuperar la instancia eliminada de la base de datos
        with self.assertRaises(TbDsolapinPerdido.DoesNotExist):
            TbDsolapinPerdido.objects.get(pk=self.dsolapin_perdido.id_solapin_perdido)

    # Puedes agregar más pruebas según sea necesario


class TbNestructuraTestCase(TestCase):
    def setUp(self):
        # Crear una instancia de Institucion para usarla en las pruebas
        self.institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True,
        )

        # Crear una instancia de TbNtipoEstructura para usarla en las pruebas
        self.tipo_estructura = TbNtipoEstructura.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_estructura="Tipo de Estructura 1",
            activo=True,
        )

    def test_creacion_estructura(self):
        # Crear una instancia de TbNestructura
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura 1",
            codigo_externo="COD1",
            codigo_area="AREA1",
            estructura_consejo=True,
            estructura_credencial=True,
            activo=True,
        )

        # Comprobar que la instancia se creó correctamente
        self.assertEqual(estructura.id_tipo_estructura, self.tipo_estructura)
        self.assertEqual(estructura.id_institucion, self.institucion)
        self.assertEqual(estructura.nombre_estructura, "Estructura 1")
        self.assertTrue(estructura.activo)

    def test_edicion_estructura(self):
        # Crear una instancia de TbNestructura para editar
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura a Editar",
            codigo_externo="COD2",
            codigo_area="AREA2",
            estructura_consejo=False,
            estructura_credencial=False,
            activo=True,
        )

        # Modificar los campos de la instancia de TbNestructura
        estructura.nombre_estructura = "Estructura Editada"
        estructura.codigo_externo = "COD3"
        estructura.codigo_area = "AREA3"
        estructura.estructura_consejo = True
        estructura.estructura_credencial = True
        estructura.save()

        # Recuperar la instancia actualizada de la base de datos
        estructura_actualizada = TbNestructura.objects.get(pk=estructura.id_estructura)

        # Comprobar que los campos se actualizaron correctamente
        self.assertEqual(estructura_actualizada.nombre_estructura, "Estructura Editada")
        self.assertEqual(estructura_actualizada.codigo_externo, "COD3")
        self.assertEqual(estructura_actualizada.codigo_area, "AREA3")
        self.assertTrue(estructura_actualizada.estructura_consejo)
        self.assertTrue(estructura_actualizada.estructura_credencial)

    def test_eliminacion_estructura(self):
        # Crear una instancia de TbNestructura para eliminar
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura a Eliminar",
            codigo_externo="COD4",
            codigo_area="AREA4",
            estructura_consejo=False,
            estructura_credencial=False,
            activo=True,
        )

        # Eliminar la instancia de TbNestructura
        estructura.delete()

        # Intentar recuperar la instancia eliminada de la base de datos
        with self.assertRaises(TbNestructura.DoesNotExist):
            TbNestructura.objects.get(pk=estructura.id_estructura)

    # Puedes agregar más pruebas según sea necesario


class TbNcategoriaTestCase(TestCase):
    def test_creacion_categoria(self):
        # Crear una instancia de TbNcategoria
        categoria = TbNcategoria.objects.create(
            nombre_categoria="Nueva Categoría",
            fecha_registro_categoria="2023-10-20 12:00:00",
            descripcion_categoria="Descripción de la Categoría",
            activo=True,
        )

        # Comprobar que la instancia se creó correctamente
        self.assertEqual(categoria.nombre_categoria, "Nueva Categoría")
        self.assertEqual(categoria.descripcion_categoria, "Descripción de la Categoría")
        self.assertTrue(categoria.activo)

    def test_edicion_categoria(self):
        # Crear una instancia de TbNcategoria para editar
        categoria = TbNcategoria.objects.create(
            nombre_categoria="Categoría a Editar",
            fecha_registro_categoria="2023-10-20 12:00:00",
            descripcion_categoria="Descripción Original",
            activo=True,
        )

        # Modificar los campos de la instancia de TbNcategoria
        categoria.nombre_categoria = "Categoría Editada"
        categoria.descripcion_categoria = "Nueva Descripción"
        categoria.save()

        # Recuperar la instancia actualizada de la base de datos
        categoria_actualizada = TbNcategoria.objects.get(pk=categoria.id_categoria)

        # Comprobar que los campos se actualizaron correctamente
        self.assertEqual(categoria_actualizada.nombre_categoria, "Categoría Editada")
        self.assertEqual(categoria_actualizada.descripcion_categoria, "Nueva Descripción")

    def test_eliminacion_categoria(self):
        # Crear una instancia de TbNcategoria para eliminar
        categoria = TbNcategoria.objects.create(
            nombre_categoria="Categoría a Eliminar",
            fecha_registro_categoria="2023-10-20 12:00:00",
            descripcion_categoria="Descripción Original",
            activo=True,
        )

        # Eliminar la instancia de TbNcategoria
        categoria.delete()

        # Intentar recuperar la instancia eliminada de la base de datos
        with self.assertRaises(TbNcategoria.DoesNotExist):
            TbNcategoria.objects.get(pk=categoria.id_categoria)

    def setUp(self):
        # Crear una instancia de Institucion para usarla en las pruebas
        self.institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True,
        )

        # Crear una instancia de TbNtipoEstructura para usarla en las pruebas
        self.tipo_estructura = TbNtipoEstructura.objects.create(
            id_institucion=self.institucion,
            nombre_tipo_estructura="Tipo de Estructura 1",
            fecha_registro_tipo_estructura="2023-10-20 12:00:00",
            descripcion_tipo_estructura="Descripción del Tipo de Estructura",
            activo=True,
        )

    def test_creacion_estructura(self):
        # Crear una instancia de TbNestructura
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura 1",
            codigo_externo="COD1",
            codigo_area="AREA1",
            estructura_consejo=True,
            estructura_credencial=True,
            activo=True,
        )

        # Comprobar que la instancia se creó correctamente
        self.assertEqual(estructura.id_tipo_estructura, self.tipo_estructura)
        self.assertEqual(estructura.id_institucion, self.institucion)
        self.assertEqual(estructura.nombre_estructura, "Estructura 1")
        self.assertTrue(estructura.activo)

    def test_edicion_estructura(self):
        # Crear una instancia de TbNestructura para editar
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura a Editar",
            codigo_externo="COD2",
            codigo_area="AREA2",
            estructura_consejo=False,
            estructura_credencial=False,
            activo=True,
        )

        # Modificar los campos de la instancia de TbNestructura
        estructura.nombre_estructura = "Estructura Editada"
        estructura.codigo_externo = "COD3"
        estructura.codigo_area = "AREA3"
        estructura.estructura_consejo = True
        estructura.estructura_credencial = True
        estructura.save()

        # Recuperar la instancia actualizada de la base de datos
        estructura_actualizada = TbNestructura.objects.get(pk=estructura.id_estructura)

        # Comprobar que los campos se actualizaron correctamente
        self.assertEqual(estructura_actualizada.nombre_estructura, "Estructura Editada")
        self.assertEqual(estructura_actualizada.codigo_externo, "COD3")
        self.assertEqual(estructura_actualizada.codigo_area, "AREA3")
        self.assertTrue(estructura_actualizada.estructura_consejo)
        self.assertTrue(estructura_actualizada.estructura_credencial)

    def test_eliminacion_estructura(self):
        # Crear una instancia de TbNestructura para eliminar
        estructura = TbNestructura.objects.create(
            id_tipo_estructura=self.tipo_estructura,
            id_institucion=self.institucion,
            nombre_estructura="Estructura a Eliminar",
            codigo_externo="COD4",
            codigo_area="AREA4",
            estructura_consejo=False,
            estructura_credencial=False,
            activo=True,
        )

        # Eliminar la instancia de TbNestructura
        estructura.delete()

        # Intentar recuperar la instancia eliminada de la base de datos
        with self.assertRaises(TbNestructura.DoesNotExist):
            TbNestructura.objects.get(pk=estructura.id_estructura)

    # Puedes agregar más pruebas según sea necesario


class TbStructureTestCase(TestCase):

    def setUp(self):
        # Crea una instancia de Institucion (si no existe una en la base de datos)
        institucion, created = Institucion.objects.get_or_create(name='Mi Institucion')

        # Crea una instancia de TbCategory
        category = TbCategory.objects.create(
            id_institucion=institucion,
            name='Nombre de la Categoría',
            description='Descripción de la Categoría',
            active=True,
            color='Color de la Categoría',
            base=True
        )

        # Crea una instancia de Usuario
        usuario = Persona.objects.create(
            nombre_completo='test',
        )

        # Crea una instancia de TbStructure
        self.structure = TbStructure.objects.create(
            id_institucion=institucion,
            category=category,
            name='Nombre de la Estructura',
            active=True,
            id_sub_director=usuario,
        )

    def test_estructura_se_crea_correctamente(self):
        structure = TbStructure.objects.get(id=self.structure.id)
        self.assertEqual(structure.name, 'Nombre de la Estructura')
        self.assertTrue(structure.active)
        self.assertEqual(structure.id_sub_director.nombre_completo, 'test')

    def test_estructura_se_actualiza_correctamente(self):
        structure = TbStructure.objects.get(id=self.structure.id)
        structure.name = 'Nuevo Nombre de Estructura'
        structure.save()

        updated_structure = TbStructure.objects.get(id=self.structure.id)
        self.assertEqual(updated_structure.name, 'Nuevo Nombre de Estructura')

    def test_estructura_se_elimina_correctamente(self):
        structure = TbStructure.objects.get(id=self.structure.id)
        structure.delete()

        with self.assertRaises(TbStructure.DoesNotExist):
            TbStructure.objects.get(id=self.structure.id)


class TbNeventoTestCase(TestCase):
    def setUp(self):
        institucion = Institucion.objects.create(name="Mi Institución")

        # Crear un objeto relacionado para TbNclasificacionEvento y TbNhorario (si es necesario)
        clasificacion_evento = TbNclasificacionEvento.objects.create(
            id_institucion=institucion,
            nombre_clasificacion_evento="Clasificación de Evento",
            activo=True,
        )
        horario = TbNhorario.objects.create(
            id_institucion=institucion,
            nombre_horario="Horario de Prueba",
            hora_inicio="08:00:00",
            hora_fin="17:00:00",
            activo=True,
        )

        # Crear un nuevo evento para las pruebas
        self.evento_nombre = "Evento de Prueba"
        self.evento = TbNevento.objects.create(
            id_institucion=institucion,
            nombre_evento=self.evento_nombre,
            activo=True,
            id_clasificacion_evento=clasificacion_evento,
            fecha_registro="2023-10-20",
            accesos=10,
            orden=1,
            id_horario=horario,
            icono="icono.png",
            color="#00FF00",
        )

    def test_evento_se_crea_correctamente(self):
        evento = TbNevento.objects.get(nombre_evento=self.evento_nombre)
        self.assertEqual(evento.nombre_evento, self.evento_nombre)

    def test_evento_se_actualiza_correctamente(self):
        evento_actualizado = "Evento Actualizado"
        self.evento.nombre_evento = evento_actualizado
        self.evento.save()
        evento = TbNevento.objects.get(pk=self.evento.pk)
        self.assertEqual(evento.nombre_evento, evento_actualizado)


class TbNhorarioTestCase(TestCase):
    def setUp(self):
        # Crear un objeto Institución
        institucion = Institucion.objects.create(
            name="Mi Institución",
            active=True
        )

        # Crear objetos TbNdiaSemana
        lunes = TbNdiaSemana.objects.create(
            dia_semana="Lunes"
        )
        martes = TbNdiaSemana.objects.create(
            dia_semana="Martes"
        )

        # Crear un nuevo horario para las pruebas
        self.horario_nombre = "Horario de Prueba"
        self.horario = TbNhorario.objects.create(
            id_institucion=institucion,
            nombre_horario=self.horario_nombre,
            hora_inicio="08:00:00",
            hora_fin="17:00:00",
            activo=True
        )
        self.horario.dias_semana.add(lunes, martes)

    def test_horario_se_crea_correctamente(self):
        horario = TbNhorario.objects.get(nombre_horario=self.horario_nombre)
        self.assertEqual(horario.nombre_horario, self.horario_nombre)
        self.assertTrue(horario.dias_semana.count() > 0)

    def test_horario_se_actualiza_correctamente(self):
        horario_actualizado = "Horario Actualizado"
        self.horario.nombre_horario = horario_actualizado
        self.horario.save()
        horario = TbNhorario.objects.get(pk=self.horario.pk)
        self.assertEqual(horario.nombre_horario, horario_actualizado)

    def test_horario_se_elimina_correctamente(self):
        horario_id = self.horario.id_horario  # Cambiar .id a .id_horario
        self.horario.delete()
        with self.assertRaises(TbNhorario.DoesNotExist):
            TbNhorario.objects.get(pk=horario_id)


class TbNtipoEstructuraTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para utilizarla en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")

    def test_agregar_tipo_estructura(self):
        # Crea una instancia de TbNtipoEstructura y la guarda en la base de datos
        nuevo_tipo_estructura = TbNtipoEstructura.objects.create(
            nombre_tipo_estructura="Tipo de Estructura",
            descripcion_tipo_estructura="Descripción de la estructura",
            activo=True,
            id_institucion=self.institucion
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbNtipoEstructura.objects.count(), 1)

    def test_editar_tipo_estructura(self):
        # Crea una instancia de TbNtipoEstructura
        tipo_estructura = TbNtipoEstructura.objects.create(
            nombre_tipo_estructura="Tipo de Estructura",
            descripcion_tipo_estructura="Descripción de la estructura",
            activo=True,
            id_institucion=self.institucion
        )

        # Edita los atributos de la instancia
        tipo_estructura.nombre_tipo_estructura = "Nuevo Nombre"
        tipo_estructura.descripcion_tipo_estructura = "Nueva Descripción"
        tipo_estructura.activo = False
        tipo_estructura.save()

        # Recupera la instancia actualizada desde la base de datos
        tipo_estructura_actualizado = TbNtipoEstructura.objects.get(pk=tipo_estructura.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(tipo_estructura_actualizado.nombre_tipo_estructura, "Nuevo Nombre")
        self.assertEqual(tipo_estructura_actualizado.descripcion_tipo_estructura, "Nueva Descripción")
        self.assertFalse(tipo_estructura_actualizado.activo)

    def test_eliminar_tipo_estructura(self):
        # Crea una instancia de TbNtipoEstructura
        tipo_estructura = TbNtipoEstructura.objects.create(
            nombre_tipo_estructura="Tipo de Estructura",
            descripcion_tipo_estructura="Descripción de la estructura",
            activo=True,
            id_institucion=self.institucion
        )

        # Elimina la instancia
        tipo_estructura.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbNtipoEstructura.objects.count(), 0)


class TbDperiodoReservacionTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para utilizarla en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")

    def test_registrar_periodo_reservacion(self):
        # Crea una instancia de TbDperiodoReservacion y la guarda en la base de datos
        nuevo_periodo_reservacion = TbDperiodoReservacion.objects.create(
            id_institucion=self.institucion,
            periodo_reservacion=10,
            activo=True,
            fecha_registro="2023-10-20"
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDperiodoReservacion.objects.count(), 1)

    def test_editar_periodo_reservacion(self):
        # Crea una instancia de TbDperiodoReservacion
        periodo_reservacion = TbDperiodoReservacion.objects.create(
            id_institucion=self.institucion,
            periodo_reservacion=10,
            activo=True,
            fecha_registro="2023-10-20"
        )

        # Edita los atributos de la instancia
        periodo_reservacion.periodo_reservacion = 20
        periodo_reservacion.activo = False
        periodo_reservacion.save()

        # Recupera la instancia actualizada desde la base de datos
        periodo_reservacion_actualizado = TbDperiodoReservacion.objects.get(pk=periodo_reservacion.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(periodo_reservacion_actualizado.periodo_reservacion, 20)
        self.assertFalse(periodo_reservacion_actualizado.activo)

    def test_eliminar_periodo_reservacion(self):
        # Crea una instancia de TbDperiodoReservacion
        periodo_reservacion = TbDperiodoReservacion.objects.create(
            id_institucion=self.institucion,
            periodo_reservacion=10,
            activo=True,
            fecha_registro="2023-10-20"
        )

        # Elimina la instancia
        periodo_reservacion.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDperiodoReservacion.objects.count(), 0)


class TbDelementosMostrarTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para utilizarla en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")

    def test_registrar_elementos_mostrar(self):
        # Crea una instancia de TbDelementosMostrar y la guarda en la base de datos
        nuevo_elementos_mostrar = TbDelementosMostrar.objects.create(
            id_institucion=self.institucion,
            elementos_mostrar_menu=1,
            elementos_mostrar_reservacion=2,
            activo=True,
            fecha_registro="2023-10-20",
            elementos_mostrar_calendario=3
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDelementosMostrar.objects.count(), 1)

    def test_editar_elementos_mostrar(self):
        # Crea una instancia de TbDelementosMostrar
        elementos_mostrar = TbDelementosMostrar.objects.create(
            id_institucion=self.institucion,
            elementos_mostrar_menu=1,
            elementos_mostrar_reservacion=2,
            activo=True,
            fecha_registro="2023-10-20",
            elementos_mostrar_calendario=3
        )

        # Edita los atributos de la instancia
        elementos_mostrar.elementos_mostrar_menu = 10
        elementos_mostrar.activo = False
        elementos_mostrar.save()

        # Recupera la instancia actualizada desde la base de datos
        elementos_mostrar_actualizado = TbDelementosMostrar.objects.get(pk=elementos_mostrar.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(elementos_mostrar_actualizado.elementos_mostrar_menu, 10)
        self.assertFalse(elementos_mostrar_actualizado.activo)

    def test_eliminar_elementos_mostrar(self):
        # Crea una instancia de TbDelementosMostrar
        elementos_mostrar = TbDelementosMostrar.objects.create(
            id_institucion=self.institucion,
            elementos_mostrar_menu=1,
            elementos_mostrar_reservacion=2,
            activo=True,
            fecha_registro="2023-10-20",
            elementos_mostrar_calendario=3
        )

        # Elimina la instancia
        elementos_mostrar.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDelementosMostrar.objects.count(), 0)


class TbDdatosContactoTestCase(TestCase):
    def setUp(self):
        # Crea instancias de Institucion y Usuario para utilizar en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")
        self.usuario = Usuario.objects.create(email="usuario@test.com", institucion=self.institucion)

    def test_registrar_datos_contacto(self):
        # Crea una instancia de TbDdatosContacto y la guarda en la base de datos
        nuevo_datos_contacto = TbDdatosContacto.objects.create(
            id_institucion=self.institucion,
            direccion="Dirección de prueba",
            telefono="123456789",
            correo="correo@test.com",
            id_usuario_registro=self.usuario,
            fecha_registro="2023-10-20"
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDdatosContacto.objects.count(), 1)

    def test_editar_datos_contacto(self):
        # Crea una instancia de TbDdatosContacto
        datos_contacto = TbDdatosContacto.objects.create(
            id_institucion=self.institucion,
            direccion="Dirección de prueba",
            telefono="123456789",
            correo="correo@test.com",
            id_usuario_registro=self.usuario,
            fecha_registro="2023-10-20"
        )

        # Edita los atributos de la instancia
        datos_contacto.direccion = "Nueva dirección"
        datos_contacto.telefono = "987654321"
        datos_contacto.correo = "nuevo_correo@test.com"
        datos_contacto.save()

        # Recupera la instancia actualizada desde la base de datos
        datos_contacto_actualizado = TbDdatosContacto.objects.get(pk=datos_contacto.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(datos_contacto_actualizado.direccion, "Nueva dirección")
        self.assertEqual(datos_contacto_actualizado.telefono, "987654321")
        self.assertEqual(datos_contacto_actualizado.correo, "nuevo_correo@test.com")

    def test_eliminar_datos_contacto(self):
        # Crea una instancia de TbDdatosContacto
        datos_contacto = TbDdatosContacto.objects.create(
            id_institucion=self.institucion,
            direccion="Dirección de prueba",
            telefono="123456789",
            correo="correo@test.com",
            id_usuario_registro=self.usuario,
            fecha_registro="2023-10-20"
        )

        # Elimina la instancia
        datos_contacto.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDdatosContacto.objects.count(), 0)


class TbDresponsableAreaPersonasTestCase(TestCase):
    def setUp(self):
        # Crea instancias de Institucion, Persona, TbNestructura y Usuario para utilizar en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")
        self.persona = Persona.objects.create(nombre_completo="Nombre de Persona")
        self.estructura = TbNestructura.objects.create(
            id_tipo_estructura=None,
            id_institucion=self.institucion,
            nombre_estructura="Nombre Estructura",
            codigo_externo="Codigo Externo",
            codigo_area="Codigo Area",
            estructura_consejo=True,
            estructura_credencial=False,
            activo=True
        )
        self.usuario = Usuario.objects.create(email="usuario@test.com", institucion=self.institucion,
                                              persona=self.persona)

    def test_registrar_responsable_area_personas(self):
        # Crea una instancia de TbDresponsableAreaPersonas y la guarda en la base de datos
        nuevo_responsable_area_personas = TbDresponsableAreaPersonas.objects.create(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_estructura=self.estructura,
            fecha_registro="2023-10-20",
            id_persona_registro=self.usuario
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDresponsableAreaPersonas.objects.count(), 1)

    def test_editar_responsable_area_personas(self):
        # Crea una instancia de TbDresponsableAreaPersonas
        responsable_area_personas = TbDresponsableAreaPersonas.objects.create(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_estructura=self.estructura,
            fecha_registro="2023-10-20",
            id_persona_registro=self.usuario
        )

        # Edita los atributos de la instancia
        responsable_area_personas.fecha_registro = "2023-11-15"
        responsable_area_personas.save()

        # Recupera la instancia actualizada desde la base de datos
        responsable_area_personas_actualizado = TbDresponsableAreaPersonas.objects.get(pk=responsable_area_personas.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(str(responsable_area_personas_actualizado.fecha_registro), "2023-11-15")

    def test_eliminar_responsable_area_personas(self):
        # Crea una instancia de TbDresponsableAreaPersonas
        responsable_area_personas = TbDresponsableAreaPersonas.objects.create(
            id_institucion=self.institucion,
            id_persona=self.persona,
            id_estructura=self.estructura,
            fecha_registro="2023-10-20",
            id_persona_registro=self.usuario
        )

        # Elimina la instancia
        responsable_area_personas.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDresponsableAreaPersonas.objects.count(), 0)


class InstitucionTestCase(TestCase):
    def test_crear_institucion(self):
        # Crea una instancia de Institucion y la guarda en la base de datos
        nueva_institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(Institucion.objects.count(), 1)

    def test_editar_institucion(self):
        # Crea una instancia de Institucion
        institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True
        )

        # Edita los atributos de la instancia
        institucion.name = "Nuevo Nombre de la Institución"
        institucion.active = False
        institucion.save()

        # Recupera la instancia actualizada desde la base de datos
        institucion_actualizado = Institucion.objects.get(pk=institucion.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(institucion_actualizado.name, "Nuevo Nombre de la Institución")
        self.assertFalse(institucion_actualizado.active)

    def test_eliminar_institucion(self):
        # Crea una instancia de Institucion
        institucion = Institucion.objects.create(
            name="Nombre de la Institución",
            description="Descripción de la Institución",
            active=True
        )

        # Elimina la instancia
        institucion.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(Institucion.objects.count(), 0)


class TbDconfiguracionProcesoTestCase(TestCase):
    def setUp(self):
        # Crea instancias de Institucion y Usuario para utilizar en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")
        self.usuario = Usuario.objects.create(email="usuario@test.com", institucion=self.institucion)

    def test_registrar_configuracion_proceso(self):
        # Crea una instancia de TbDconfiguracionProceso y la guarda en la base de datos
        nueva_configuracion_proceso = TbDconfiguracionProceso.objects.create(
            id_institucion=self.institucion,
            flujo=True,
            descripcion_configuracion_proceso="Descripción de la configuración",
            fecha_registro="2023-10-20",
            id_usuario_registro=self.usuario
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDconfiguracionProceso.objects.count(), 1)

    def test_editar_configuracion_proceso(self):
        # Crea una instancia de TbDconfiguracionProceso
        configuracion_proceso = TbDconfiguracionProceso.objects.create(
            id_institucion=self.institucion,
            flujo=True,
            descripcion_configuracion_proceso="Descripción de la configuración",
            fecha_registro="2023-10-20",
            id_usuario_registro=self.usuario
        )

        # Edita los atributos de la instancia
        configuracion_proceso.flujo = False
        configuracion_proceso.fecha_registro = "2023-11-15"
        configuracion_proceso.save()

        # Recupera la instancia actualizada desde la base de datos
        configuracion_proceso_actualizado = TbDconfiguracionProceso.objects.get(pk=configuracion_proceso.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertFalse(configuracion_proceso_actualizado.flujo)
        self.assertEqual(str(configuracion_proceso_actualizado.fecha_registro), "2023-11-15")

    def test_eliminar_configuracion_proceso(self):
        # Crea una instancia de TbDconfiguracionProceso
        configuracion_proceso = TbDconfiguracionProceso.objects.create(
            id_institucion=self.institucion,
            flujo=True,
            descripcion_configuracion_proceso="Descripción de la configuración",
            fecha_registro="2023-10-20",
            id_usuario_registro=self.usuario
        )

        # Elimina la instancia
        configuracion_proceso.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDconfiguracionProceso.objects.count(), 0)


class TbDconfiguracionPersonaTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para utilizar en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")

    def test_registrar_configuracion_persona(self):
        # Crea una instancia de TbDconfiguracionPersona y la guarda en la base de datos
        nueva_configuracion_persona = TbDconfiguracionPersona.objects.create(
            id_institucion=self.institucion,
            activo=True,
            descripcion="Descripción de la configuración",
            fecha_registro="2023-10-20"
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbDconfiguracionPersona.objects.count(), 1)

    def test_editar_configuracion_persona(self):
        # Crea una instancia de TbDconfiguracionPersona
        configuracion_persona = TbDconfiguracionPersona.objects.create(
            id_institucion=self.institucion,
            activo=True,
            descripcion="Descripción de la configuración",
            fecha_registro="2023-10-20"
        )

        # Edita los atributos de la instancia
        configuracion_persona.activo = False
        configuracion_persona.fecha_registro = "2023-11-15"
        configuracion_persona.save()

        # Recupera la instancia actualizada desde la base de datos
        configuracion_persona_actualizado = TbDconfiguracionPersona.objects.get(pk=configuracion_persona.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertFalse(configuracion_persona_actualizado.activo)
        self.assertEqual(str(configuracion_persona_actualizado.fecha_registro), "2023-11-15")

    def test_eliminar_configuracion_persona(self):
        # Crea una instancia de TbDconfiguracionPersona
        configuracion_persona = TbDconfiguracionPersona.objects.create(
            id_institucion=self.institucion,
            activo=True,
            descripcion="Descripción de la configuración",
            fecha_registro="2023-10-20"
        )

        # Elimina la instancia
        configuracion_persona.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbDconfiguracionPersona.objects.count(), 0)


class TbNconfiguracionCobroTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Institucion para utilizar en las pruebas
        self.institucion = Institucion.objects.create(name="Nombre Institucion")

    def test_registrar_configuracion_cobro(self):
        # Crea una instancia de TbNconfiguracionCobro y la guarda en la base de datos
        nueva_configuracion_cobro = TbNconfiguracionCobro.objects.create(
            nombre_configuracion_cobro="Configuración de Cobro 1",
            descripcion="Descripción de la configuración",
            activo=True,
            id_institucion=self.institucion
        )

        # Comprueba que la instancia se haya guardado correctamente
        self.assertEqual(TbNconfiguracionCobro.objects.count(), 1)

    def test_editar_configuracion_cobro(self):
        # Crea una instancia de TbNconfiguracionCobro
        configuracion_cobro = TbNconfiguracionCobro.objects.create(
            nombre_configuracion_cobro="Configuración de Cobro 1",
            descripcion="Descripción de la configuración",
            activo=True,
            id_institucion=self.institucion
        )

        # Edita los atributos de la instancia
        configuracion_cobro.nombre_configuracion_cobro = "Configuración de Cobro 2"
        configuracion_cobro.activo = False
        configuracion_cobro.save()

        # Recupera la instancia actualizada desde la base de datos
        configuracion_cobro_actualizado = TbNconfiguracionCobro.objects.get(pk=configuracion_cobro.pk)

        # Comprueba que los cambios se hayan guardado correctamente
        self.assertEqual(configuracion_cobro_actualizado.nombre_configuracion_cobro, "Configuración de Cobro 2")
        self.assertFalse(configuracion_cobro_actualizado.activo)

    def test_eliminar_configuracion_cobro(self):
        # Crea una instancia de TbNconfiguracionCobro
        configuracion_cobro = TbNconfiguracionCobro.objects.create(
            nombre_configuracion_cobro="Configuración de Cobro 1",
            descripcion="Descripción de la configuración",
            activo=True,
            id_institucion=self.institucion
        )

        # Elimina la instancia
        configuracion_cobro.delete()

        # Comprueba que la instancia se haya eliminado
        self.assertEqual(TbNconfiguracionCobro.objects.count(), 0)


class UsuarioModelTest(TestCase):
    def test_creacion_usuario(self):
        # Prueba la creación de un usuario
        usuario = Usuario.objects.create(
            username="testuser",
            email="testuser@example.com",
        )
        self.assertEqual(usuario.username, "testuser")
        self.assertEqual(usuario.email, "testuser@example.com")

    def test_edicion_usuario(self):
        # Prueba la edición de un usuario
        usuario = Usuario.objects.create(
            username="testuser",
            email="testuser@example.com",
        )
        usuario.username = "newuser"
        usuario.save()
        updated_usuario = Usuario.objects.get(id=usuario.id)
        self.assertEqual(updated_usuario.username, "newuser")

    def test_eliminacion_usuario(self):
        # Prueba la eliminación de un usuario
        usuario = Usuario.objects.create(
            username="testuser",
            email="testuser@example.com",
        )
        usuario_id = usuario.id
        usuario.delete()
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(id=usuario_id)
