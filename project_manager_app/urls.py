from django.urls import path
from .views import (
    UserRegisterView,
    UserDetailView,
    ProjectListCreateView,
    ProjectDetailView
)

urlpatterns = [
    # USERS
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),

    # PROJECTS
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:id>/<str:username>/', ProjectDetailView.as_view(), name='project-detail'),
]
