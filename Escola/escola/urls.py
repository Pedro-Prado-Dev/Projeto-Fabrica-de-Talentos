"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from aluno.api.viewsets import AlunoViewSet, AlunoViewSetOut
from disciplina.api.viewsets import DisciplinaViewSet, DisciplinaViewSetOut
from estagio.api.viewsets import EstagioViewSet
from matricula.api.viewsets import MatriculaViewSet, MatriculaViewSetOut
from professor.api.viewsets import ProfessorViewSet

router = routers.DefaultRouter()
router.register(r'listaAluno',AlunoViewSet, basename='ListaAluno')
router.register(r'listaDisciplina',DisciplinaViewSet, basename='ListaDisciplina')
router.register(r'listaEstagio',EstagioViewSet,basename='ListaEstagio')
router.register(r'listaMatricula',MatriculaViewSet,basename='ListaMatricula')
router.register(r'listaProfessor',ProfessorViewSet, basename='ListaProfessor')
router.register(r'viewMatricula',MatriculaViewSetOut,basename='ViewMatricula')
router.register(r'viewAluno',AlunoViewSetOut,basename='ViewAluno')
router.register(r'viewDisciplina',DisciplinaViewSetOut,basename='ViewDisciplina')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
