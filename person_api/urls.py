from django.urls import path

from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
]
