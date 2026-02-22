from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Project
from .serializers import (
    UserRegisterSerializer,
    UserDetailSerializer,
    ProjectSerializer
)


# -----------------------------
#   USER REGISTER
# -----------------------------
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
#   USER DETAIL / UPDATE / DELETE
# -----------------------------
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_object(self):
        user = super().get_object()

        # L'utilisateur ne peut voir/modifier/supprimer QUE son propre compte
        if self.request.user != user:
            raise PermissionDenied("Vous ne pouvez accéder qu'à votre propre profil.")

        return user


# -----------------------------
#   PROJECT LIST + CREATE
# -----------------------------
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # Lecture publique OK, création réservée aux utilisateurs connectés
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Pagination, filtrage, tri
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['owner']  # ?owner=<user_id>
    ordering_fields = ['title', 'created_at']  # ?ordering=title / ?ordering=-created_at

    def perform_create(self, serializer):
        # Le propriétaire est l'utilisateur connecté
        serializer.save(owner=self.request.user)


# -----------------------------
#   PROJECT DETAIL / UPDATE / DELETE
# -----------------------------
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def get_object(self):
        project = super().get_object()

        # Lecture publique → OK
        # Modification / suppression → seulement le propriétaire
        username = self.kwargs.get('username')

        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if project.owner.username != username:
                raise PermissionDenied("Vous n'êtes pas le propriétaire de ce projet.")

        return project
