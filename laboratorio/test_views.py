from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        Laboratorio.objects.create(nombre='Laboratorio A', ciudad='Ciudad A', pais='País A')

    def test_laboratorio_list_view(self):
    
        url = reverse('laboratorio_list')  
       
        response = self.client.get(url)

        
        self.assertEqual(response.status_code, 200)

       
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')

        
        self.assertContains(response, 'Laboratorio A') 
        self.assertContains(response, 'Ciudad A')      
        self.assertContains(response, 'País A')        