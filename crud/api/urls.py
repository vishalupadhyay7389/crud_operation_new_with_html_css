from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name='home'),
    path('show/', views.show , name='show'),
    path('send' , views.send),
    path('delete',views.delete),
    path('edit/',views.edit),
    path('RecordEdited' , views.RecordEdited),
]