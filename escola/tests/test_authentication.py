from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AutheticantionUserTestCase(APITestCase):
    """classe AuthenticationUserTestCase

    Intenção : 
    Se trata da criação de uma estrutura de teste para a autenticação na api, nesse caso que começa com a criação de um super usuário e termina com
    os testes de acerts e erros dos caracteres desse super usuário.

    Argumentos : 
    APITestCase" é a biblioteca responsável pelos testes dentro do Django Rest, dedicado exclusicamente aos testes de funcionalidade da API

    Atributos : 
    "setUp" : Usado para definir o contexto de testes. Nesse caso se trata de um teste de autenticação e nesse contexto é necessário a criação
    de um usuário prar forncer as credenciais, além da url que deverá ser criada e testada a Autenticação

    Os demais testes são tentativas de encontrar falha no sisitema de autenticação da API além da requisição get presente no último teste
    """
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        # Puxo a URL através do BaseName, sendo convertido na URL.
        self.url = reverse('Estudantes-list')
        

    def test_autenticacao_user_com_credenciais_corretas(self):
        usuario = authenticate(username='admin',password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_com_username_incorreto(self):
        usuario = authenticate(username='Python',password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_com_password_incorreta(self):
        usuario = authenticate(username='admin',password='Django')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """nesse caso em específico temos a requisição get feita. sendo necessária para o teste funcionar: Forçar uma autenticação de usuário
        (self.client.force_authenticate) e também verificar o status se é igual ao HTTP_200 através do assertEqual"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get (self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
