from . import views
from  django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.add_widget, name='add_widget')
]