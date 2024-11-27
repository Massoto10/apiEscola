from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    """classe ModelEstudanteTestCase

    Intenção : 
    Se trata de um teste unitário referente ao modelo de Estudante previamente definido no Models. Criação de contexto feito pelo "setUp"
    e um teste simples a respeito das exigências básicas do models.
    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-los

    Atributos : 
    "setUp" : Usado para definir o contexto de testes nesse casa o contexto criado é de um estudante com os dados fornecidos no corpo do código
    "test_verifica_atributos_de_estudante" : Realiza os testes em si, ultilizando os padrões definidos dentro do Models e a solidez dos dados. 
    """

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "Teste de Modelo",
            email = "testemodelo@gmail.com",
            cpf = "68195899056",
            data_nascimento = "2023-02-02",
            celular = "21998107410"
        )

    def test_verifica_atributos_de_estudante(self):
        self.assertEqual(self.estudante.nome,"Teste de Modelo")
        self.assertEqual(self.estudante.email,"testemodelo@gmail.com")
        self.assertEqual(self.estudante.cpf,"68195899056")
        self.assertEqual(self.estudante.data_nascimento,"2023-02-02")
        self.assertEqual(self.estudante.celular,"21998107410")


class ModelCursoTestCase(TestCase):
    """classe ModelCursoTestCase

    Intenção : 
    Se trata de um teste unitário referente ao modelo de Cursos previamente definido no Models. Com a criação de contexto e testes das exigênicas 
    básicas feitas no models.

    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-los

    Atributos : 
    "setUp" : Usado para definir o contexto de testes nesse caso o contexto criado é de um estudante com os dados fornecidos no corpo do código
    "test_verifica_atributos_de_estudante" : Realiza os testes em si, ultilizando os padrões definidos dentro do Models e a solidez dos dados. 
    """
        
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "CPP",
            descricao = "curso de programação python",
            nivel = "I"
    )
        
    def test_verifica_atributos_de_curso(self):
        self.assertEqual(self.curso.codigo, "CPP")
        self.assertEqual(self.curso.descricao, "curso de programação python")
        self.assertEqual(self.curso.nivel, "I")

class ModelMatriculaTestCase(TestCase):
    """classe ModelMatriculaTestCase

    Intenção : 
    Se trata de um teste unitário referente ao modelo de Matricula previamente definido no Models. Com a criação de contexto um pouco distinta,
    por conta das chaves estrangeiras heradadas de estudante e curso.

    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-ços

    Atributos : 
    "setUp" : Usado para definir o contexto de testes nesse caso o contexto criado é de um estudante com os dados fornecidos no corpo do código. tendo que criar
    também um estudante e uma matrícula para que seja possível herdar os dados de ambos e formar assim a matricula desejada.
    "test_verifica_atributos_de_estudante" : Realiza os testes em si, ultilizando os padrões definidos dentro do Models e a solidez dos dados. 
    """
        
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86999999999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')


