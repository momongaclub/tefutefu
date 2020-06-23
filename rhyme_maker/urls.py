from django.urls import path
from . import views

app_name = 'rhyme_maker'
urlpatterns = [
    path(r'', views.index, name='index'),
    path('ajax/', views.get_data, name='get_data'),
    path('make_rhyme', views.exercise, name='make_rhymea'),
    path('rhyme', views.search_rhyme, name='make_rhymeb'),
]
