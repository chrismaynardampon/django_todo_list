from django.urls import path
from . import views

urlpatterns = [
    path('preview/', views.report_preview, name='report_preview'),
    path('download/', views.report_download, name='report_download'),
    ]
