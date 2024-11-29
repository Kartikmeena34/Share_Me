from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('upload/', views.upload_file, name='upload_file'),
    path('send/',views.send,name='send'),
    path('receive/',views.receive, name='receive'),
]
