from django.urls import path
from . import views

app_name = 'conv'
urlpatterns = [
    path('', views.convert_view),
]

handler500 = views.server_error_500
