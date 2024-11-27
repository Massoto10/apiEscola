from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso

class CursosTestCase(APITestCase):
    """classe CursosTestCase

    Intenção : 
    Se trata do teste de rotas dentro do serializer de cursos onde faremos as requisições e e instanciar "cursos para os testes". Além do contexto, 
    serão feitos também: testes de requição get, post, delete e put. Fazendo uso das Fixtures do banco de dados anteriormente criado.

    Argumentos : 
    "APITestCase" é a biblioteca responsável pelos testes dentro do Django Rest, dedicado exclusicamente aos testes de funcionalidade da API.

    Atributos : 
    "setUp" : Usado para criação do contexto, nesse caso puxará informações do banco de dados para testes com 2 cursos e 1 superusuário e uma url. 

    "test_requisicao_get_para_listar_cursos" : Realiza o teste de requisição "get" para os cursos em geral e finaliza através do assertequal.
    "test_requisicao_post_para_criar_um_curso" : Realiza o teste de requisição "post" para criar um curso onde os dados são fornceidos inline e finalizado com o assertequal
    "test_requisicao_delete_um_curso" : Realiza o teste de requisição "delete" para excluir um curso onde é fornecido a url + a primary key e finaliza com o asserteaqual
    "test_requisicao_put_para_atualizar_um_curso" : Realiza teste de requisição "put" para atualizar um curso, fornecendo os novos dados, a url com a primary key e finalizando com o assertequal
    """
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='massoto')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)

        self.curso_01 = Curso.objects.get(pk=4)

        self.curso_02 = Curso.objects.get(pk=5)
    def test_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_curso(self):
        dados =  {
            'codigo' : 'TST',
            'descricao' : 'teste',
            'nivel' : 'B'
        }

        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_requisicao_delete_um_curso(self):
        response = self.client.delete(f"{self.url}2/") # deletando curso 2
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        dados = {
            'codigo' : "OTT",
            'descricao' : "Outro teste",
            'nivel' : 'A'
        }
        response = self.client.put(f"{self.url}1/", dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
