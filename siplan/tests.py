from django.test import TestCase
from .models import Organizacion

# Create your tests here.


class OrganizacionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Organizacion.objects.create(
            nombre_organizacion="Banco Central de Reserva de El Salvador",
            descripcion_organizacion="Descripción BCR",
            mision_organizacion="Misión BCR",
            vision_organizacion="Visión BCR",
        )

    def test_nombre_organizacion(self):
        organizacion = Organizacion.objects.get(id_organizacion=1)
        expected_object_name = f"{organizacion.nombre_organizacion}"
        self.assertEqual(expected_object_name, "Banco Central de Reserva de El Salvador")
