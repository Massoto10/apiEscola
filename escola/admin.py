from django.contrib import admin
from escola.models import Estudante,Curso, Matricula


class Estudantes(admin.ModelAdmin):
    """Classe Estudantes.  
        
        Intenção:
            Cria classe "Estudantes" que ocupará um dos campos da página de admin do site. Sendo necessária para realizar 
            o fornecimento de dados para a mesma, além de realizar o CRUD e organização dos dados. Estruturalmente, faz seu trabalho
            através dos comandos melhor explicados nos Atributos.

        Args:  
            param : "ModelAdmin" representa um modelo na interface de administração, para acessa-lo basta busca no arquivo "adimin".    
    
        Atributos: 
            list_display : nomeação padrão que especifica os campos que estarão amostra na interface do meu Admin
            list_display_links : nomeação padrão que especifica os campos que vão conter links responsáveis por carregar o link de acesso ao objeto
            list_per_page : " " " " o número de objetos por página dentro do Admin
            search_fields : " " " " os campos pesquisáveis, ou seja, aqueles que poderão ser encontrados a partir de uma busca no Admin
            ordering  : " " " " os campos que eu poderei ordenar, seja de forma crescente ou descrescente.
    """  
    
    list_display = ('id','nome','email','cpf','data_nascimento','celular')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome','cpf',)
    ordering = ('nome',)

admin.site.register(Estudante,Estudantes)
# Função de registrar os dados recebidos pelo models na respectiva lista do admin.


class Cursos(admin.ModelAdmin):
    # Cria a lista "Cursos" dentro de admin, organiza os campos através dos atributos mais um vez e registra através do "register".
    list_display = ('id','codigo','descricao')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)


class Matriculas(admin.ModelAdmin):
    # Cria a lista "matrícula" no admin, organiza seus campos e os registra.
    list_display = ('id','estudante','curso','periodo')
    list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)