import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    """Função cpf_inválido

    Definição : 
    Usado para dizer se o cpf posto em nossa aplicação é um cpf válido. Essa função
    é usada no Serializer.

    Argumentos : 
    "numero_cpf" : Será recebido direto na execução no Serializer
     
    Atributos : 
    "cpf = CPF" : "cpf" recebe o tipo de dados da classe "CP"
    "cpf_valido" : receberá um boolean do "validate" que é uma funçãp do "cpf" que é referente ao
    "numero_cpf"
    
    Return :
    Retorna true caso o retorno Booleano seja falso, por conta do "not"
    """

    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    """Função nome_inválido

    Definição : 
    Usado para dizer se o nome posto em nossa aplicação é um nome válido. Essa função
    é usada no Serializer.

    Argumentos : 
    "nome" : Será recebido direto na execução no Serializer
    
    Return :
    Retorna true caso o retorno Booleano seja falso, por conta do "not"
    """

    return not nome.isalpha()

def celular_invalido(celular):
    """Função celular_inválido

    Definição : 
    Usado para dizer se o numero de celular posto em nossa aplicação é um número válido. Essa função
    é usada no Serializer.

    Argumentos : 
    "celular" : Será recebido direto na execução no Serializer
     
    Atributos : 
    "modelo" :  traz como o dado deve ser inserido, isso é uma forma de validação usada e manipulada
    ateravés do regex, importador como "re"
    "resposta" : findall traz a compração entre o "modelo" e o "celular", retornando um booleano 

    Return :
    Retorna true caso o retorno Booleano seja falso, por conta do "not"
    """   
    
    modelo = '[1-9]{2}[9]{1}[0-9]{8}'
    
    resposta = re.findall(modelo,celular)
    
    return not resposta