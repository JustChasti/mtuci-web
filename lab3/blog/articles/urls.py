from django.urls import include, path
from articles import views


urlpatterns = [
    path('test/', views.archive, name='archive'),
]
