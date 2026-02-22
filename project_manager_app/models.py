from django.db import models
from django.contrib.auth.models import AbstractUser

# -----------------------------
#   USER PERSONNALISÉ
# -----------------------------
class User(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']  # email obligatoire
    USERNAME_FIELD = 'username'  # identifiant principal

    def __str__(self):
        return self.username


# -----------------------------
#   PROJECT
# -----------------------------
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title
