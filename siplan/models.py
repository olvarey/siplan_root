from tabnanny import verbose
from django.db import models
from django.forms import Widget

# Create your models here.


class Accion(models.Model):
    id_accion = models.BigAutoField(primary_key=True)
    descripcion_accion = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion_accion = models.DateField(blank=True, null=True)
    nombre_accion = models.CharField(max_length=300)
    nombre_responsable_accion = models.CharField(max_length=500, blank=True, null=True)
    numero_acciones_anuales_accion = models.IntegerField()
    observacion = models.CharField(max_length=500, blank=True, null=True)
    presupuesto_asignado_accion = models.FloatField(blank=True, null=True)
    usuario_creacion_accion = models.CharField(max_length=300)
    id_anio_resultado = models.ForeignKey(
        "AnioResultado", models.RESTRICT, db_column="id_anio_resultado"
    )
    id_financiamiento = models.ForeignKey(
        "Financiamiento", models.RESTRICT, db_column="id_financiamiento"
    )
    id_linea_trabajo = models.ForeignKey(
        "LineaTrabajo", models.RESTRICT, db_column="id_linea_trabajo"
    )

    class Meta:
        managed = True
        db_table = "accion"


class Anio(models.Model):
    id_anio = models.BigAutoField(primary_key=True)
    valor_anio = models.BigIntegerField()
    id_periodo = models.ForeignKey("Periodo", models.RESTRICT, db_column="id_periodo")

    class Meta:
        managed = True
        db_table = "anio"
        unique_together = (("id_anio", "id_periodo"),)


class AnioResultado(models.Model):
    id_anio_resultado = models.BigAutoField(primary_key=True)
    id_anio = models.ForeignKey("Anio", models.RESTRICT, db_column="id_anio")
    id_resultado = models.ForeignKey(
        "Resultado", models.RESTRICT, db_column="id_resultado"
    )
    activo = models.BooleanField()

    class Meta:
        managed = True
        db_table = "anio_resultado"
        unique_together = (("id_anio", "id_resultado"),)


class Eje(models.Model):
    id_eje = models.BigAutoField(primary_key=True)
    descripcion_eje = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion_eje = models.DateField()
    nombre_eje = models.CharField(max_length=300)
    usuario_creacion_eje = models.CharField(max_length=300)
    id_objetivo = models.ForeignKey(
        "Objetivo", models.RESTRICT, db_column="id_objetivo"
    )

    class Meta:
        managed = True
        db_table = "eje"


class Financiamiento(models.Model):
    id_financiamiento = models.BigAutoField(primary_key=True)
    nombre_financiamiento = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "financiamiento"


class Indicador(models.Model):
    id_indicador = models.BigAutoField(primary_key=True)
    nombre_indicador = models.CharField(max_length=300)
    id_tipo_indicador = models.ForeignKey(
        "TipoIndicador", models.RESTRICT, db_column="id_tipo_indicador"
    )
    id_unidad_medida = models.ForeignKey(
        "UnidadMedida", models.RESTRICT, db_column="id_unidad_medida"
    )

    class Meta:
        managed = True
        db_table = "indicador"


class LineaTrabajo(models.Model):
    id_linea_trabajo = models.BigAutoField(primary_key=True)
    nombre_linea_trabajo = models.CharField(max_length=300)
    id_unidad_presupuestaria = models.ForeignKey(
        "UnidadPresupuestaria", models.RESTRICT, db_column="id_unidad_presupuestaria"
    )

    class Meta:
        managed = True
        db_table = "linea_trabajo"
        unique_together = (("id_linea_trabajo", "id_unidad_presupuestaria"),)


class Mes(models.Model):
    id_mes = models.BigIntegerField(primary_key=True)
    nombre_mes = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "mes"


class Objetivo(models.Model):
    id_objetivo = models.BigAutoField(primary_key=True)
    descripcion_objetivo = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion_objetivo = models.DateField()
    nombre_objetivo = models.CharField(max_length=300)
    usuario_creacion_objetivo = models.CharField(max_length=300)
    id_organizacion = models.ForeignKey(
        "Organizacion", models.RESTRICT, db_column="id_organizacion"
    )
    id_tipo_objetivo = models.ForeignKey(
        "TipoObjetivo", models.RESTRICT, db_column="id_tipo_objetivo"
    )

    class Meta:
        managed = True
        db_table = "objetivo"


class Organizacion(models.Model):
    id_organizacion = models.BigAutoField(primary_key=True)
    nombre_organizacion = models.CharField(max_length=500, verbose_name="Nombre")
    descripcion_organizacion = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Descripción"
    )
    mision_organizacion = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Misión"
    )
    vision_organizacion = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Visión"
    )

    class Meta:
        managed = True
        db_table = "organizacion"
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"
        ordering = ["descripcion_organizacion"]

    def __str__(self):
        return self.nombre_organizacion


class Periodo(models.Model):
    id_periodo = models.BigAutoField(primary_key=True)
    anio_fin = models.BigIntegerField()
    anio_inicio = models.BigIntegerField()
    nombre_periodo = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "periodo"


class Plan(models.Model):
    id_plan = models.BigAutoField(primary_key=True)
    descripcion_plan = models.CharField(max_length=500)
    fecha_creacion_plan = models.DateField()
    nombre_plan = models.CharField(max_length=300)
    usuario_creacion_plan = models.CharField(max_length=300)
    id_tipo_plan = models.ForeignKey(
        "TipoPlan", models.RESTRICT, db_column="id_tipo_plan"
    )

    class Meta:
        managed = True
        db_table = "plan"


class Resultado(models.Model):
    id_resultado = models.BigAutoField(primary_key=True)
    descripcion_resultado = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion_resultado = models.DateField(blank=True, null=True)
    nombre_responsable_resultado = models.CharField(
        max_length=500, blank=True, null=True
    )
    nombre_resultado = models.CharField(max_length=500)
    usuario_creacion_resultado = models.CharField(max_length=300)
    id_eje = models.ForeignKey(Eje, models.RESTRICT, db_column="id_eje")
    id_indicador = models.ForeignKey(
        Indicador, models.RESTRICT, db_column="id_indicador"
    )

    class Meta:
        managed = True
        db_table = "resultado"


class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    id_accion = models.ForeignKey("Accion", models.RESTRICT, db_column="id_accion")
    id_mes = models.ForeignKey("Mes", models.RESTRICT, db_column="id_mes")
    detalle_seguimiento = models.CharField(max_length=500)
    ejecutado = models.BooleanField(blank=True, null=True)
    fecha_creacion_seguimiento = models.DateField()
    fecha_edicion_seguimiento = models.DateField(blank=True, null=True)
    fecha_ejecucion_seguimiento = models.DateField(blank=True, null=True)
    numero_acciones_mensuales = models.BigIntegerField()
    presupuesto_ejecutado = models.FloatField()
    usuario_creacion_seguimiento = models.CharField(max_length=300)
    usuario_edicion_seguimiento = models.CharField(
        max_length=300, blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "seguimiento"
        unique_together = (("id_accion", "id_mes"),)


class TipoIndicador(models.Model):
    id_tipo_indicador = models.BigAutoField(primary_key=True)
    nombre_tipo_indicador = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "tipo_indicador"


class TipoObjetivo(models.Model):
    id_tipo_objetivo = models.BigAutoField(primary_key=True)
    nombre_tipo_objetivo = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "tipo_objetivo"


class TipoPlan(models.Model):
    id_tipo_plan = models.BigAutoField(primary_key=True)
    nombre_tipo_plan = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "tipo_plan"


class UnidadMedida(models.Model):
    id_unidad_medida = models.BigAutoField(primary_key=True)
    nombre_unidad_medida = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "unidad_medida"


class UnidadOrganizativa(models.Model):
    id_unidad_organizativa = models.BigAutoField(
        primary_key=True, verbose_name="Unidad organizativa"
    )
    nombre_unidad_organizativa = models.CharField(
        max_length=500, verbose_name="Nombre unidad organizativa"
    )
    organizacion = models.ForeignKey(
        Organizacion,
        models.RESTRICT,
        db_column="id_organizacion",
        verbose_name="Organización",
        # @olvarey This is related with OrganizacionSerializer
        # related_name="unidades_organizativas",
    )
    unidad_superior = models.ForeignKey(
        "self",
        models.RESTRICT,
        db_column="id_unidad_superior",
        blank=True,
        null=True,
        verbose_name="Unidad superior",
    )

    class Meta:
        managed = True
        db_table = "unidad_organizativa"
        verbose_name = "Unidad organizativa"
        verbose_name_plural = "Unidades organizativas"
        ordering = ["nombre_unidad_organizativa"]

    def __str__(self):
        return self.nombre_unidad_organizativa


class UnidadPresupuestaria(models.Model):
    id_unidad_presupuestaria = models.BigAutoField(primary_key=True)
    nombre_unidad_presupuestaria = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = "unidad_presupuestaria"
