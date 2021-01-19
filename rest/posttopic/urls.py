from django.urls import  path
from . import views

urlpatterns = [
    path('', views.send_commandRequestList,name="send-command-request-list"),
    path('commandList/', views.send_commandList,name="command-list"),
    path('commandDetail/<str:pk>/', views.send_commandDetail,name="command-detail"),
    path('commandCreate/', views.send_commandCreate,name="command-create"),
    path('commandUpdate/<str:pk>/', views.send_commandUpdate,name="command-update"),
    path('commandDelete/<str:pk>/', views.send_commandDelete,name="switch-delete"),
]