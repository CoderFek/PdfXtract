from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdfUploadView, name = 'upload'),
    path('emails/', views.emailview, name = 'emails'),
    path('links/', views.linkview, name = 'link'),
    path('text/', views.textview, name = 'text'),
    path('download_csv/<str:data_type>/', views.download_csv, name='download_csv'),

]