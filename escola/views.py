from escola.models import Estudante,Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    """Classe EstudanteViewSet

    Definição : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "queryset" : seleciona do models a informação que vou trazer, se serão todas e o campo de ordenação.
    "filter_backends" : traz os filtros através do "DjangoFilterBackend", dentre eles o filtro de ordenação(OrderingFilter)
    e o filtro de pesquisa(SearchFilter)
    "ordering_fields, search_field" : recebem os campos que serão responsáveis por cada filtro, por isso o "_fields"
    
    get_serializer_class : Vai ser responsável ´pelo controle de versão a escolha do usuário na qual será estraído da URL
    
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

    Definição : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "queryset" : seleciona do models a informação que vou trazer, se serão todas e o campo de ordenação.
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "CursoSerializer"
    "permission_classes" : alteramos essa permissão para quando usarmos junto com um front, seja posível a leitura dos dados
    """

    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculaViewSet(viewsets.ModelViewSet):
    """Classe MatriculaViewSet

    Definição : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "queryset" : seleciona do models a informação que vou trazer, se serão todas e o campo de ordenação.
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "MatriculaSerializer"
    "throttle_classes" : resposável pela limitação nas requisições feitas. Limites impostos no "throttles.py" e no "settings.py"
    "http_method_names" : define os métodos permitido dentro das views referente as matrículas, nesse caso "get" "post"
    """

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle ]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    """Classe ListaMatriculaEstudante

    Definição : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "get_queryset" : permite que eu defina posteriormente o meu queryset de forma mais detalhada e fazendo com que se torne um método
    de leitura apenas. e retorna o próipio queryset

    "queryset" :  nesse caso ele está usando os dados do model "Matricula" e aplicando um filtro de id do estudante que será referenciada pela primary key
    trazida dentro da url.
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "ListaMatriculasEstudanteSerializer"
    """

    def get_queryset(self):

        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """Classe ListaMatriculaCurso

    Definição : 
    Cuida da parte de visualização e utilização da api onde decide os campos pesquisáveis, decide os filtros, entre outras funções

    Argumentos : 
    "viewsets.ModelViewSet" modelo padrão para as views sets, trazendo os padrões de nomeação para os
    atributos, e outro detalhes que fica por parte do framework cuidar
     
    Atributos : 
    "get_queryset" : permite que eu defina posteriormente o meu queryset de forma mais detalhada e fazendo com que se torne um método
    de leitura apenas. e retorna o próipio queryset

    "queryset" :  nesse caso ele está usando os dados do model "Matricula" e aplicando um filtro de id do curso que será referenciada pela primary key
    trazida dentro da url.
    "serializer_class" : colocamos o setrializer que iremo ultilizar nesse caso o "ListaMatriculasCursoSerializer"
    """
        
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer