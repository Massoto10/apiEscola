from escola.models import Estudante,Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    """Classe EstudanteViewSet

    Intenção : 
    Selecionar quais objetos serão herdados do model, sua ordem, seus filtros, seus campos ordenáveis e campos pesquisáveis,
    dentro da ViewSet de estudante, que nesse caso também possui um pequeno controle de versões.
    

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar. Viewsets nada mais são que views mais simples
    dentro do padrão rest e que já possuem ações http comuns.
     
    Atributos : 
    "queryset" : seleciona do models a informação que vou trazer, se serão todas e o campo de ordenação.
    "filter_backends" : traz os filtros através do "DjangoFilterBackend", dentre eles o filtro de ordenação(OrderingFilter)
    e o filtro de pesquisa(SearchFilter)
    "ordering_fields, search_field" : recebem os campos que serão responsáveis por cada filtro, por isso o "_fields"
    
    "get_serializer_class" : Vai ser responsável pelo controle de versão a escolha do usuário na qual será extraído da URL
    
    """
    
    queryset = Estudante.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """Classe CursoViewSet

    Intenção : 
    Assim como a anterior trata da herança do model, nesse caso, model de Curso. Nesse caso faz uso de um classe
    serializadora (serializer_class) e uma classe de permissividade (permission classes)

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "queryset" : seleciona do models a informação que irá trazer, se serão todos os objetos e o campo de ordenação.
    "serializer_class" : é colocado o serializer que será ultilizado, nesse caso o "CursoSerializer"
    "permission_classes" : alteramos as permissões da classe, nesse caso com o uso de "IsAuthenticatedOrReadOnly" que implica em
    somente pessoas autorizadas farão alterações, se não autorizada apenas a função de leitura.
    """

    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculaViewSet(viewsets.ModelViewSet):
    """Classe MatriculaViewSet

    Intenção :
    Vai tratar novamente da herança do models, trabalhar novamente com a classe serializadora. Trará como novidade
    a questão de segurança com limites que requisição através do throttle e os métodos http permitidos. 


    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "queryset" : seleciona do models a informação que vou trazer, se serão todas e o campo de ordenação.
    "serializer_class" : é colocado o serializer que será ultilizado, nesse caso o "MatriculaSerializer"
    "throttle_classes" : resposável pela limitação nas requisições feitas. Limites impostos no "throttles.py" e no "settings.py"
    "http_method_names" : define os métodos permitido dentro das views referente as matrículas, nesse caso "get" "post"
    """

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle ]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    """Classe ListaMatriculaEstudante

    Intenção : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "generics.ListAPIView" View genérica que faz retornar uma lista de objetos.
     
    Atributos : 
    "get_queryset" :  Permite personalizar, filtrar e ordenar os dados retornados pelo viewset.
    nesse caso ele está usando os dados do model "Matricula" e instanciando a primary key do estudante trazida dentro da url e ordenando pelo Id
    .
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "ListaMatriculasEstudanteSerializer" para transforma-lo em Json.
    """

    def get_queryset(self):

        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """Classe ListaMatriculaCurso

    Intenção : 
    Cuida da parte de visualização e utilização da api

    Argumentos : 
    "generics.ListAPIView" View genérica que faz retornar uma lista de objetos.
     
    Atributos : 
    "get_queryset" :  Permite personalizar, filtrar e ordenar os dados retornados pelo viewset.
    nesse caso ele está usando os dados do model "Matricula" e instanciando a primary key do curso trazida dentro da url e ordenando pelo Id
    .
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "ListaMatriculasCursoSerializer" para transforma-lo em Json.
    """
        
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer