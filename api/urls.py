from .views import *
from django.urls import path

urlpatterns = [
    path('', ListView.as_view(), name='apilist'),
    path('update/<int:pk>/', UpdateView.as_view(), name='post'),
    path('create/', CreateView.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]