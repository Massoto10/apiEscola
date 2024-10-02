from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    """Classe Estudante 

        Definição:
            A classe models "Estudante" é onde irei armazenar e definir um  modelo para os dados
            a serem recebidos. Cada nome de classe se trata de uma tabela que será criada dentro do
            ORM.

        Argumentos:
            parametro: Model é um modelo de ORM fundamental para a organização, capticação e armazenamento dos dados
            sendo necessário busca-lo no arquivo importado "models".

        Atributos:
            nome (str) :  Nome do Estudante e de até 100 caracteres
            email (str) : Email do Estudante, no modelo de e-mail, preenchimento obrigatório e de até 30 caracteres
            cpf (str) : Cpf do Estudante, de até 11 caracteres e único na Tabela 
            data_nascimento (date): Data de nascimento do Estudante
            celular (str) : Número de celular do Estudante e de até 14 caracteres

        Return: Retorno o "nome" do meu "Estudante" quando instanciado à minha class
    """

    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    """Classe Curso 

        Definição:
            Aplicavél a descrição da classe anterior

        Argumentos:
           Aplicavél a descrição da classe anterior

        Atributos:
            codigo (str): Abreviação do curso, de até 10 caracteres, valor único na tabela e  mínimo de 3 caracteres. 
            descição (str) : Resumo do curso, de até 100 caracteres e preenchimento obrigatório 
            nível : Nível do curso, de apenas 1 caracter, escolhas na tupla "NIVEL", preenchimento obrigatório e por padrão "B" ("Básico")

        Return: Retorno o "codigo" do meu "Curso" quando instanciada à minha classe
    """
    
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
     
    codigo = models.CharField(max_length = 10, unique = True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    """Classe Matrícula

        Definição:
            Aplicavél a descrição da classe anterior

        Argumentos:
           Aplicavél a descrição da classe anterior

        Atributos:
            estudante : Chave estrangeira de "Estudante" .
            curso : Chave estrangeira de "Curso".
            observação: Se curso ou estudante instanciado deixe de existir, será apagado também a matricula.
            periodo : Horário que o estudante escolheu, de apenas 1 caracter, escolhas na tupla "PERIODO", preenchimento obrigatório e por padrão "M" (matutino)

        Return: Retorno o "codigo" do meu "Curso" quando instanciada à minha classe
    """    
    

    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )

    estudante = models.ForeignKey(Estudante,on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')