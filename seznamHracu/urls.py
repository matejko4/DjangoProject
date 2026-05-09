from django.urls import path
from . import views

urlpatterns = [
    path('tymy/', views.seznam_tymu, name='seznam_tymu'),
    path('tymy/<int:pk>/', views.detail_tymu, name='detail_tymu'),

    path('hraci/', views.seznam_hracu, name='seznam_hracu'),
    path('hraci/<int:pk>/', views.detail_hrace, name='detail_hrace'),

    path('zapasy/', views.seznam_zapasu, name='seznam_zapasu'),
    path('zapasy/<int:pk>/', views.detail_zapasu, name='detail_zapasu'),
]