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
# forncedido pela documentação para uso do swagger

router = routers.DefaultRouter()
# fazemos uso do DeafultRouter por ja possuir uma interface

router.register('estudantes',EstudanteViewSet,basename='Estudantes')
router.register('cursos',CursoViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')
# registramos (register) as rotas, passamos o prefixo, o viewset e o basename apenas para identificação

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    # colocamos o routers para funcionar aqui no path e o incluimos (include)
    # obs: não passamos argumento no prefixo ('') pois já está definido no "router"

    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
    # aqui puxamos as informações da url para auxiliar nas no "views" vale salientar que
    # é somente para consulta "as_view()"
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #direcionam para a documentação em swagger e redoc
]   
