import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
# define os requisitos para validação do cpf, já pré definidos pelo "validate_docbr"

    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
# define o requisito para a validação do nome, que seja alpha, ou seja, contenha apenas letras

    return not nome.isalpha()

def celular_invalido(celular):
# define os requisitos para a validação do celular, nesse caso temos um modelo base que ultiliza o "re.findall" para fazer a verificação
    
    modelo = '[1-9]{2}[9]{1}[0-9]{8}'
    
    resposta = re.findall(modelo,celular)
    
    return not resposta