from django.urls import path
from . import views

app_name = 'rhyme_maker'
urlpatterns = [
    path(r'', views.index, name='index'),
    path('ajax/', views.get_data, name='get_data'),
    path('make_rhymes', views.exercise, name='make_rhymes'),
]
