from django.contrib import admin
from django.urls import path,include
from escola.views import EstudanteViewSet,CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante,ListaMatriculaCurso
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
     title="Documentação da API",
      default_version='v1',
      description="Documentação da API Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
# toda biblioteca drf_yasg se trata da documentação swagger, nesse caso preenchida com os dados necessários,
# como título, versão, descrição, termos, contato e licença. (https://swagger.io/specification/)

router = routers.DefaultRouter()
# "DefaultRouter": Ultilizado por já possuir uma interface própria

router.register('estudantes',EstudanteViewSet,basename='Estudantes')
router.register('cursos',CursoViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')
#"basename": serve como uma identificação da rota.

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    # "include": Inclui as urls a serem seguidas além do router.
    # obs: não passe argumento no prefixo ('') pois já está definido no "router"

    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
    # "as_view": Reforça o "leitura apenas" dessas rotas

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #"swagger/" e "redoc/": Direcionam até as documentações da API, de respectivos modelos.
    # cache_timeout=0, me garante que eu terei uma informação sempre atualizada, que se atualiza a cada 0 seg.
    #(https://drf-yasg.readthedocs.io/en/stable/readme.html)
]   
