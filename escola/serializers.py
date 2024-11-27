from rest_framework import serializers
from escola.models import Estudante,Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    """classe EstudanteSerializer

    Intenção : 
    Sendo um serializer se trata da conversão de dados complexos em dados mais fáceis de serem manipulados como
    Json por exemplo. além disso se escolhe os campos que serão herdados do models e o model em si. Conta também
    com os validadores de cpf, nome e celular.

    Argumentos : 
    "serializers.ModelSerializer" : traz o modelo padrão de serializar, trazendo as características necessárias e padrões.

    Atributos : 
    "Classe Meta" : Recebe nome "Meta" por padrão de uso. E o model base ("Estudante") e os campos(Fields) que serão recebidos
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

    Intenção : 
    Se trata de um serializador, que nesse caso, apenas trabalha com o model("Curso") e os campos que serão herdado desse model.

    Argumentos : 
    Ultiliza novamente o padrão "serializers.ModelSerializer"

    Atributos : 
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Curso" e os campos(Fields) que serão recebidos,
    nesse caso todos (__all__)
    """

    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    """classe MatriculaSerializer

    Intenção : 
    Assim como o anterior, trabalha apenas com o model, nesse caso o filtro de campos é representado pelo "exclude".

    Argumentos : 
    Adota o padrão "serializer.ModelSerializer".

    Atributos : 
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Matricula" e os campos(Fields) que serão recebidos,
    nesse caso todos, ou não exluiu nenhum ("exclude = []")
    """

    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    """classe ListaMatriculasEstudanteSerializer

    Intenção : 
    Aplicavél a descrição da classe anterior, porém além de mudar os dados ele também puxa dados de outras tabelas, juntando à uma só

    Argumentos : 
    Como padrão "serializers.ModelSerializer"

    Atributos : 
    "estudante_nome = serializers.ReadOnlyField"  função de leitura apenas, que tem como fonte "curso.descricao"
    
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Matricula" e o campo(Fields) que será recebido nesse caso referente ao estudante
    "get_periodo" : Onde é definido o dado a ser incluso no "SerializerMethodField", o retorno traz o "obj" para referenciar o produto e 
    o "_display" para dizer que se deve trazer a informação completado do campo, não somente a sigla (matrículas.período)

    """
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']
    
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    """classe ListaMatriculasCuesoSerializer

    Intenção : 
    Trata-se de um serializer, e possui como um dos 

    Argumentos : 
    Aplicavél a descrição da classe anterior

    Atributos : 
    "curso = serializers.ReadOnlyField" função de leitura apenas, que tem como fonte "estudante.nome"
    "periodo = serializers.SerializerMethodField()" função de espeficiar a fonte posteriormente através do get
    "Classe Meta" : Recebe "Meta" por padrão de uso e recebe esse nome e o model base "Matricula" e os campos(Fields) que serão recebidos
    nesse caso referente ao curso.
    """

    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    
    def get_periodo(self,obj):
        
        return obj.get_periodo_display()

class EstudanteSerializerV2(serializers.ModelSerializer):
    """classe EstudanteSerializerV2

    Intenção :
    Sendo um serializer se trata da conversão de dados complexos em dados mais fáceis de serem manipulados como
    Json por exemplo. Mas nesse caso temos que se trata de uma segunda versão de "EstudanteSerializer"
    

    Argumentos : 
    segue o padrão "serializers,ModelSerializer"

    Atributos :
    "Classe Meta" : Recebe Meta por padrão de uso e recebe esse nome e o model base "Estudante" e os campos(Fields) que serão recebidos
    perceptivelmente menor que a versão 1 do "EstudanteSerializer"
    """
    
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']