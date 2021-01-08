from . import views
from  django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.add_widget, name='add_widget'),
    path('index/<int:widget_id>', views.delete_widget, name='delete_widget')
]