# Project Manager API – Backend Django REST

## Présentation

Cette API REST fournit un système complet de gestion d’utilisateurs et de projets. Elle s’appuie sur Django et Django REST Framework pour offrir une architecture fiable, sécurisée et extensible. L’ensemble des endpoints a été testé via Postman (Basic Auth) et via l’interface DRF (sessionid).

L’objectif du backend est de proposer :
- une authentification robuste,
- une gestion propre des utilisateurs,
- un CRUD complet sur les projets,
- des permissions strictes basées sur le propriétaire,
- une documentation claire et un code commenté pour faciliter la maintenance.

---

## Modèles

### Utilisateur (User)
- `username` — unique, max 150 caractères  
- `email` — unique et obligatoire  
- `password` — stocké de manière sécurisée (hash Django)

### Projet (Project)
- `title` — unique, max 100 caractères  
- `description` — optionnelle  
- `created_at` — généré automatiquement  
- `owner` — utilisateur propriétaire du projet  

---

## Documentation des API

# Utilisateurs

### 1. POST `/api/users/register/`
Créer un compte utilisateur.  
**Public**

**Body :**
```json
{
  "username": "john",
  "email": "john@test.com",

Réponses :

201 : utilisateur créé
400 : username ou email déjà utilisé

2. GET /api/users/<username>/
Afficher les informations du compte connecté.
Basic Auth obligatoire

Réponse :

{
  "username": "john",
  "email": "john@test.com"
}

3. PUT /api/users/<username>/
Modifier les informations du compte connecté.
Basic Auth obligatoire

Body :

{
  "email": "nouveau@mail.com"
}

4. DELETE /api/users/<username>/
Supprimer le compte connecté.
Basic Auth obligatoire

Réponse :

204 No Content

Projets

1. GET /api/projects/
Retourne une liste paginée de tous les projets.

Public

Options :

?page=2
?ordering=title
?ordering=-created_at
?owner=<user_id>

Exemple :

/api/projects/?ordering=-created_at&page=2

2. POST /api/projects/
Créer un nouveau projet.
Basic Auth obligatoire

Body :

{
  "title": "Mon projet",
  "description": "Texte facultatif"
}

L’API attribue automatiquement :
owner = utilisateur connecté

3. GET /api/projects/<id_project>/<username>/
Récupérer un projet spécifique.

Public
Réponse :

{
  "id": 1,
  "title": "Projet X",
  "description": "Texte",
  "created_at": "2026-02-22T20:15:00Z",
  "owner": "melodie"
}

4. PUT /api/projects/<id_project>/<username>/
Modifier un projet.
Réservé au propriétaire

Si non propriétaire :

{
  "detail": "Vous n'êtes pas le propriétaire de ce projet."
}

5. DELETE /api/projects/<id_project>/<username>/
Supprimer un projet.
Réservé au propriétaire

Réponses :

204 : projet supprimé
403 : utilisateur non propriétaire

Permissions & sécurité

Un utilisateur peut modifier ou supprimer uniquement ses propres projets.
Toute tentative non autorisée renvoie un 403 Forbidden.

Authentification :

Basic Auth (Postman)
sessionid (interface DRF)

Tests réalisés

Postman

Création d’utilisateurs
Authentification
CRUD complet sur les projets
Tests d’erreurs (400, 403, 404)
Vérification des permissions
Suppression (204 No Content)

Interface DRF

Tests GET/POST/PUT/DELETE
Authentification via cookie
Vérification des règles de permissions

Installation

git clone https://github.com/simohamedmnari/project-manager-backend
cd project-manager-backend
python -m venv env
env\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Conclusion

Ce backend fournit une base solide pour une application de gestion de projets. Il est conçu pour être :

extensible,
sécurisé,
facile à maintenir,
conforme aux bonnes pratiques Django/DRF.




