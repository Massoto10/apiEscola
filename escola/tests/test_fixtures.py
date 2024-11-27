from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestes (TestCase):
    # teste com as fixtures para confirmar seu funcionamento onde está sendo puxado de um banco de dados, e se faz necessário testar 
    # a precisão e compatibilidade dos dados adquiridos e os dados verdadeiros.
    fixtures = ['prototipo_banco.json']

    def test_carregamento_das_fixtures(self):
        estudante =Estudante.objects.get(cpf='49465543357')
        curso = Curso.objects.get(pk=11)
        self.assertEqual(estudante.celular, "82941659863")
        self.assertEqual(curso.codigo, "CDJRF03")
