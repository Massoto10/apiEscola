from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    """Classe SerializerEstudanteTestCase

    Intenção : 
    Se trata de um teste de serializer referente ao serializer de Estudante previamente definido no serializer.py. Onde será definida
    o contexto através do setUp. Além de realizar os devidos testes tanto referentes as chaves quanto referentes ao valor.

    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-los

    Atributos : 
    "setUp" : Usado para definir o contexto de testes nesse caso o contexto criado é de um estudante com os dados fornecidos no corpo do código e
    instanciados no "self.serializer_estudante" onde é feito a inclusão dos dados criados ao serializador já definido em "escola.serializers"
    "test_verifica_campos_serializados_de_estudante" : Verifica se todos os campos estão preenchidos e presentes nos dados criados
    "test_verifica_conteudo_dos_campos_serializados_de_estudante" : verifica agora o conteudo presente nos campos, se estão de acordo com o é exigido pelo serializer.
    """
    def setUp(self):
         self.estudante = Estudante(
            nome = "Teste de Modelo",
            email = "testemodelo@gmail.com",
            cpf = "68195899056",
            data_nascimento = "2023-02-02",
            celular = "21998107410"
        )
         self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
         dados = self.serializer_estudante.data
         self.assertEqual(set(dados.keys()), set(['id','nome','email','cpf','data_nascimento','celular'] ))
         # Ultiliza-se o set para poder fazer a comparação dos campos em si, sem se importar com o tipo ou ordem de verificação

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
         dados = self.serializer_estudante.data
         self.assertEqual(dados['id'], self.estudante.id)
         self.assertEqual(dados['nome'], self.estudante.nome)
         self.assertEqual(dados['email'], self.estudante.email)
         self.assertEqual(dados['cpf'], self.estudante.cpf)
         self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
         self.assertEqual(dados['celular'], self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    """Classe SerializerCursoTestCase

    Intenção : 
    Se trata de um teste de serializer referente ao serializer de Curso previamente definido no serializer.py. Gerado novamente um cenário 
    no código e com os testes de chave e de valor. 

    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-los

    Atributos : 
    "setUp" : Usado para definir o contexto de testes nesse caso o contexto criado é de um curso com os dados fornecidos no corpo do código
    instanciados no "self.serializer_curso" onde é feito a inclusão dos dados criados ao serializador já definido em "escola.serializers"
    "test_verifica_campos_serializados_de_curso" : Verifica se todos os campos estão preenchidos e presentes no teste
    "test_verifica_conteudo_dos_campos_serializados_de_curso" : verifica agora o conteudo presente nos campos, se estão de acordo
    """    

    def setUp(self):
          self.curso = Curso(
            codigo = "POO",
            descricao = "Programação Orientada Objeto",
            nivel = "B"
            )
          self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_do_curso(self):
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id','codigo', 'descricao', 'nivel']))

    def test_verifica_conteudo_dos_campos_serializados_do_curso(self):
         dados = self.serializer_curso.data
         self.assertEqual(dados['id'], self.curso.id)
         self.assertEqual(dados['codigo'], self.curso.codigo)
         self.assertEqual(dados['descricao'], self.curso.descricao)
         self.assertEqual(dados['nivel'], self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
    """Classe SerializerMatriculaTestCase

    Intenção : 
    Se trata de um teste de serializer referente ao serializer de matricula previamente definido no serializer.py. Dessa vez um pouco diferente a criação de cenário por trabalhar
    com chaves estrangeiras, mas com os mesmos teste de chave e de valor.
 
    Argumentos : 
    "TestCase" é a biblioteca responsável pelos testes dentro do Django Rest, que ulitliza o Unnitest do Python para realiza-los

    Atributos : 
    "setUp" : Usado para definir o contexto de testesm nesse casa o contexto criado é de uma matricula com os dados fornecidos no corpo do código
    Dentro do setup definimos "estudante_matricula" e "curso_matricula". pois para esse serializer existe a questão de herança de outros objetos, por isso
    se torna necessário a criação desses dois objetos para poder herdar suas caracteríticas.

    "test_verifica_campos_serializados_de_matricula" : Verifica se todos os campos estão preenchidos e presentes no teste
    "test_verifica_conteudo_dos_campos_serializados_de_matricula" : verifica agora o conteudo presente nos campos, se estão de acordo
    """    
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = "Teste de Modelo",
            email = "testemodelo@gmail.com",
            cpf = "68195899056",
            data_nascimento = "2023-02-02",
            celular = "21998107410"
        )

        self.curso_matricula = Curso.objects.create(
            codigo = "POO",
            descricao = "Programação Orientada Objeto",
            nivel = "B"
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante_matricula,  
            curso = self.curso_matricula,
            periodo = "N"
        )  
        
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
    
    def test_verifica_campos_serializados_da_matricula(self):
         dados = self.serializer_matricula.data
         self.assertEqual(set(dados.keys()), set(['id','estudante', 'curso', 'periodo']))

    def test_verifica_conteudo_dos_campos_serializados_da_matricula(self):
        dados = self.serializer_matricula.data
        self.assertEqual(dados["id"], self.matricula.id)
        self.assertEqual(dados["estudante"], self.estudante_matricula.id)
        self.assertEqual(dados["curso"], self.curso_matricula.id)
        self.assertEqual(dados["periodo"], self.matricula.periodo)


