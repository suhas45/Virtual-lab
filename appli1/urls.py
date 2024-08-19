from django.urls import path
from django.contrib import admin


from .views import mainview
from .views import erdiagramview
from .views import ersimulationview
from .views import exview
from .views import experimentsview
from .views import introductionview
from .views import aimview
from .views import objectivesview
from .views import quizview
from .views import aggview
from .views import aggaimview
from .views import aggggameview
from .views import aggquizview
from .views import aggrefview
from .views import aggsimview
from .views import aggtheoryview
from .views import ddlview
from .views import ddlaimview
from .views import ddlquizview
from .views import ddlrefview
from .views import ddltheoryview
from .views import dmlview
from .views import dmlquizview
from .views import dmlaimview
from .views import dmlrefview
from .views import dmlsimview
from .views import dmltheoryview
from .views import erefview
from .views import querysimview
from .views import fedview
from .views import feedbackview
from .views import gameview
from .views import gameeeview
from .views import queryview
from .views import queryaimview
from .views import queryquizview
from .views import querygameview
from .views import queryrefview
from .views import querytheoryview
from .views import theoryview


urlpatterns = [
    path('',mainview,name='main'),
    path('aim/', aimview,name='aim'),
    path('erdiagram/', erdiagramview,name='erdiagram'),
    path('ersimulation/', ersimulationview,name='ersimulation'),
    path('ex/', exview,name='ex'),
    path('main/',mainview,name='main'),
    path('experiments/',experimentsview,name='experiments'),
    path('introduction/', introductionview,name='introduction'),
    path('objectives/', objectivesview,name='objectives'),
    path('quiz/', quizview,name='quiz'),
    path('theory/', theoryview,name='theory'),
    path('agg/',aggview,name='agg'),
    path('aggaim/', aggaimview,name='aggaim'),
    path('aggggame/', aggggameview,name='aggggame'),
    path('aggquiz/', aggquizview,name='aggquiz'),
    path('aggref/', aggrefview,name='aggref'),
    path('aggsim/', aggsimview,name='aggsim'),
    path('aggtheory/', aggtheoryview,name='aggtheory'),
    path('ddl/', ddlview,name='ddl'),
    path('ddlaim/', ddlaimview,name='ddlaim'),
    path('ddlquiz/', ddlquizview,name='ddlquiz'),
    path('ddlref/', ddlrefview,name='ddlref'),
    path('ddltheory/', ddltheoryview,name='ddltheory'),
    path('dml/', dmlview,name='dml'),
    path('dmlaim/', dmlaimview,name='dmlaim'),
    path('dmlquiz/', dmlquizview,name='dmlquiz'),
    path('dmlref/', dmlrefview,name='dmlref'),
    path('dmlsim/', dmlsimview,name='dmlsim'),
    path('dmltheory/', dmltheoryview,name='dmltheory'),
    path('eref/', erefview,name='eref'),
    path('querysim/', querysimview,name='querysim'),
    path('fed/', fedview,name='fed'),
    path('feedback/', feedbackview,name='feedback'),
    path('game/', gameview,name='game'),
    path('gameee/', gameeeview,name='gameee'),
    path('query/', queryview,name='query'),
    path('queryaim/', queryaimview,name='queryaim'),
    path('queryquiz/',queryquizview,name='queryquiz'),
    path('querygame/', querygameview,name='querygame'),
    path('queryref/', queryrefview,name='queryref'),
    path('querytheory/',querytheoryview,name='querytheory')
]


