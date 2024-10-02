from django.contrib import admin
from escola.models import Estudante,Curso, Matricula


class Estudantes(admin.ModelAdmin):
    """Classe Estudantes.  
        
        Descrição:
            Vou criar a classe "Estudantes" que ocupará um dos campos da página de admin do site. Sendo necessária para realizar 
            o fornecimento de dados para a mesma, além de realizar o CRUD e organização dos dados.

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
"""admin.site.register()

    Descrição:
        Para fazer o resgistro das informações de forma funcional e tornar útil o admin criado e registrar as informações
        obtidas pelo models.

    Args: 
        param1 : "Estudante" se trata de um dos models, onde consigo obter as informações fornecidas pelo meu usuário, 
        no momento que o mesmo preenche os campos.

        param2 : "Estudantes" se trata do próprio admin onde será armazenadas as informações do "param1" sendo logo processada
        para uma futura organização.
"""


class Cursos(admin.ModelAdmin):
    """Aplicavél a DocString da Classe anterior!"""
    list_display = ('id','codigo','descricao')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)


class Matriculas(admin.ModelAdmin):
    """Aplicavél a DocString da Classe anterior!"""
    list_display = ('id','estudante','curso','periodo')
    list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)