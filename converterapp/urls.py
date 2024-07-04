from django.urls import path
from . import views


app_name = 'conv'
urlpatterns = [
    path('', views.convert_view),
]