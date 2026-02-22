from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentification DRF (obligatoire pour afficher Login)
    path('api-auth/', include('rest_framework.urls')),

    # Inclusion des routes de ton app
    path('api/', include('project_manager_app.urls')),
]
