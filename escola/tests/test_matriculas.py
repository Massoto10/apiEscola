from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso, Estudante, Matricula

class MatriculasTestCase(APITestCase):
    """classe MatriculasTestCase

    Intenção : 
    Se trata do teste de rotas dentro do serializer de matriculas onde faremos as requisições e e instanciar "matriculas para os testes". 
    Além do contexto, serão feitos também: testes de requição get, post, delete e put. Fazendo uso das fixtures do banco de dados anteriormente criado.

    Argumentos : 
    "APITestCase": é a biblioteca responsável pelos testes dentro do Django Rest, dedicado exclusicamente aos testes de funcionalidade da API.

    Atributos : 
    "setUp" : Usado para criação do contexto, nesse caso puxará informações do banco de dados para testes com 1 cursos, 1 estudante e 1 superusuário e uma url, além da criação inline de uma matrícula. 

    "test_requisicao_get_para_listar_matriculas" : Realiza o teste de requisição "get" para os cursos em geral e finaliza através do assertequal.
    "test_requisicao_post_para_criar_uma_matricula" : Realiza o teste de requisição "post" para criar uma matricula onde os dados são fornceidos inline, com estudante e curso sendo herdados do banco de dados
    e finalizado com o assertequal
    "test_requisicao_delete_matricula" : Realiza o teste de requisição "delete" para excluir matricula onde é fornecido a url e finaliza com o asserteaqual (405, pois nesse caso n tem permissão para deletar usuário e curso)
    "test_requisicao_put_para_atualizar_uma_matricula" : Realiza teste de requisição "put" para atualizar uma matricula, fornecendo os novos dados, a url com a primary key e finalizando com o assertequal (405, também pois não tem permissão
    para atualizar os usuário e curso)
    """    
    
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='massoto')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)

        self.estudante = Estudante.objects.get(pk=12)
        
        self.curso = Curso.objects.get(pk=3)

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'V'
        )

    def test_requisicao_get_para_listar_matriculas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_uma_matricula(self):
        dados =  {
            'estudante' : self.estudante.pk,
            'curso' : self.curso.pk,
            'periodo' : 'M',
            
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_requisicao_delete_matricula(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        # nesse caso não é permitido deletar uma vez que existe a herança de outros dados

    def test_requisicao_put_para_atualizar_um_matricula(self):
        dados = {
            'estudante' : self.estudante.pk,
            'curso' : self.estudante.pk,
            'periodo' : 'N'
        }
        response = self.client.put(f"{self.url}1/", dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)