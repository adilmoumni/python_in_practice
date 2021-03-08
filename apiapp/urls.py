from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_idea),
    path('<str:idea_name>', views.get_idea),
]
