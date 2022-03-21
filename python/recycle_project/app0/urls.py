from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('agendamentos/', views.getAgendamentos),
    path('agendamentos/create/', views.createAgendamento),
    path('agendamentos/<str:pk>/', views.getAgendamento),
    path('agendamentos/<str:pk>/update/', views.updateAgendamento),
    path('agendamentos/<str:pk>/delete/', views.deleteAgendamento),
]
