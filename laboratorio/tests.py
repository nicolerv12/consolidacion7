from django.test import TestCase
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       
        Laboratorio.objects.create(nombre='Laboratorio A', ciudad='Ciudad A', pais='País A')

    def test_laboratorio_creation(self):
        
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio A')

        self.assertEqual(laboratorio.nombre, 'Laboratorio A')
        self.assertEqual(laboratorio.ciudad, 'Ciudad A')
        self.assertEqual(laboratorio.pais, 'País A')

    def test_laboratorio_str(self):
        
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio A')
        self.assertEqual(str(laboratorio), 'Laboratorio A')
