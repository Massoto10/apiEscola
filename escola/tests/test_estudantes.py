from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer


class EstudantesTestCase(APITestCase):
    """classe EstudantesTestCase

    Intenção : 
    Se trata do teste de rotas dentro do serializer de estudante onde faremos as requisições e e instanciar "estudantes para os testes". Além do contexto, 
    serão feitos também: testes de requição get, post, delete e put. Fazendo uso das Fixtures do banco de dados anteriormente criado.

    Argumentos : 
    "APITestCase" é a biblioteca responsável pelos testes dentro do Django Rest, dedicado exclusicamente aos testes de funcionalidade da API.

    Atributos : 
    "setUp" : Usado para criação do contexto, nesse caso puxará informações do banco de dados para testes com 2 estudante e 1 superusuário 

    "test_requisicao_get_para_listar_estudantes" : Realiza o teste de requisição "get" para o estudantes em geral e finaliza através do assertequal.
    "test_requisicao_get_para_listar_um_estudante" : Realiza o teste de requisição "get" para apenas 1 estudante através da primary key (pk) e finaliza através do assertequal.
    "test_requisicao_post_para_criar_um_estudante" : Realiza o teste de requisição "post" para criar um estudante onde os dados são fornceidos inline e finalizado com o assertequal
    "test_requisicao_delete_um_estudante" : Realiza o teste de requisição "delete" para excluir um estudante onde é fornecido a url + a primary key e finaliza com o asserteaqual
    "test_requisicao_put_para_atualizar_um_estudante" : Realiza teste de requisição "put" para atualizar um estudante, fornecendo os novos dados, a url com a primary key e finalizando com o assertequal
    """

    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='massoto')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)

        self.estudante_01 = Estudante.objects.get(pk=2)

        self.estudante_02 = Estudante.objects.get(pk=3)
        
    def test_requisicao_get_para_listar_estudantes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_requisicao_get_para_listar_um_estudante(self):
        response = self.client.get(self.url+'01/')
        dados_estudante = Estudante.objects.get(pk=1)
        # O ".data" transforma os dados da instânca em dicionário de python facilmente convertido em Json
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        print(dados_estudante_serializados)
        self.assertEqual(response.data,dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        dados =  {
            'nome' : 'teste',
            'email' : 'testepost@gmail.com',
            'cpf' : '82449761012',
            'data_nascimento' : '1985-08-25',
            'celular' : '21970758285',
        }

        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        response = self.client.delete(f"{self.url}2/") # deletando estudante 2
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        dados = {
            'nome' : 'testeput',
            'email' : 'testeput@gmail.com',
            'cpf' : '52987802021',
            'data_nascimento' : '1985-08-25',
            'celular' : '21970758285',
        }
        response = self.client.put(f"{self.url}1/", dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)