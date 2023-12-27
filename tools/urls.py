from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdfUploadView, name = 'UploadPdf'),
    path('emails/', views.emailview, name = 'emails'),
    path('links/', views.linkview, name = 'link'),
    path('text/', views.textview, name = 'text'),

]