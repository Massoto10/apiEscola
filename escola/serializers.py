from rest_framework import serializers
from escola.models import Estudante,Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    """classe EstudanteSerializer

    Definição : 
    Sendo um serializer se trata da conversão de dados complexos em dados mais fáceis de serem manipulados como
    Json por exemplo.

    Argumentos : 
    "serializers.ModelSerializer"  traz o modelo padrão de serializar, trazendo as características necessárias

    Atributos : 
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Estudante" e os campos(Fields) que serão recebidos
    "Função validate" : valida os os dados recebidos através de funções criada no "escola.validators". traz também o raise com o 
    "validationError" que permite personalizar o retorno do erro. E depois volta com os dados
    """
    
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']  

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular inválido. ex:11901234567'})
        return dados
    
class CursoSerializer(serializers.ModelSerializer):
    """classe CursoSerializer

    Definição : 
    Aplicavél a descrição da classe anterior

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos : 
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Curso" e os campos(Fields) que serão recebidos,
    nesse caso todos (__all__)
    """

    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    """classe MatriculaSerializer

    Definição : 
    Aplicavél a descrição da classe anterior

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos : 
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Matricula" e os campos(Fields) que serão recebidos,
    nesse caso todos, ou não exluiu nenhum ("exclude = []")
    """

    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    """classe ListaMatriculasEstudanteSerializer

    Definição : 
    Aplicavél a descrição da classe anterior, porém além de mudar os dados ele também puxa dados de outras tabelas, juntando à uma só

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos : 
    "curso = serializers.ReadOnlyField" Trazemos aqui a função de leitura apenas, que tem como fonte "curso.descricao"
    "periodo = serializers.SerializerMethodField()" Trazemos a possibilidade de espeficiar a fonte posteriormente através do get
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Matricula" e os campos(Fields) que serão recebidos
    "get_periodo" : Onde é definido o dado a ser incluso no "SerializerMethodField", o retorno traz o "obj" para referenciar o produto e 
    o "_display" para dizer que se deve trazer a informação completado do campo, não somente a sigla (matrículas.período)

    """
    
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    
    def get_periodo(self,obj):
        
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    """classe ListaMatriculasCuesoSerializer

    Definição : 
    Aplicavél a descrição da classe anterior

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos : 
    "estudante_nome = serializers.ReadOnlyField" Trazemos aqui a função de leitura apenas, que tem como fonte "estudante.nome"
    "Classe Meta" : Recebe "M"eta" por padrão de uso e recebe esse nome e o model base "Matricula" e os campos(Fields) que serão recebidos
    """

    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    """classe EstudanteSerializerV2

    Definição :
    Sendo um serializer se trata da conversão de dados complexos em dados mais fáceis de serem manipulados como
    Json por exemplo. Mas nesse caso temos que se trata de uma segunda versão de "EstudanteSerializer"
    

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos :
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Estudante" e os campos(Fields) que serão recebidos
    perceptivelmente menor que a versão 1 do "EstudanteSerializer"
    """
    
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']