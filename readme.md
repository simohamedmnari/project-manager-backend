# API REST – Project Manager (Examen Django & DRF)

## Présentation du projet

Dans le cadre de l’examen Django/DRF, j’ai développé une API REST permettant de gérer des utilisateurs et des projets.  
L’objectif était de construire une API propre, sécurisée et cohérente, en respectant les bonnes pratiques du framework et en testant chaque fonctionnalité au fur et à mesure.

J’ai testé l’ensemble des endpoints :

- via **Postman** (Basic Auth)
- via **l’interface DRF**, qui utilise automatiquement un cookie `sessionid` pour authentifier l’utilisateur connecté

Ce document présente clairement les modèles, les endpoints, les permissions et le comportement attendu de l’API.

---

# Modèles
## Modèle Utilisateur (User)

- `username` : unique, max 150 caractères  
- `email` : unique et obligatoire  
- `password` : minimum 8 caractères, stocké de manière **hachée** (mécanisme Django)

## Modèle Projet (Project)

- `title` : unique, max 100 caractères  
- `description` : facultatif  
- `created_at` : généré automatiquement  
- `owner` : utilisateur propriétaire du projet  

---

# Commentaires dans le code

Pour faciliter la compréhension du projet, j’ai ajouté des commentaires dans les fichiers importants :

- explication du rôle de chaque vue  
- rappel des permissions appliquées  
- commentaires dans les serializers pour clarifier la logique  
- commentaires dans les modèles pour préciser les contraintes  
- explication du comportement des endpoints sensibles (PUT/DELETE protégés)

L’objectif était de rendre le code lisible et simple à maintenir.

---

# Documentation des API

## Utilisateurs

---

## 1 POST `/api/users/register/`
Créer un compte utilisateur.  
**Public — aucune authentification requise**

**Body :**
```json
{
  "username": "john",
  "email": "john@test.com",
  "password": "test12345"
}

Réponses :

201 : utilisateur créé
400 : username ou email déjà utilisé

2. GET /api/users/<username>/

Afficher les informations de l’utilisateur connecté.
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
Accessible à tout le monde

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

L’API attribue automatiquement owner = utilisateur connecté.

3. GET /api/projects/<id_project>/<username>/
Récupérer un projet spécifique.

Public

Réponse :

json
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

Réponses possibles :

204 : projet supprimé
403 : utilisateur non propriétaire

Permissions & sécurité
Un utilisateur peut modifier ou supprimer uniquement ses propres projets.

Toute tentative d’accès non autorisé renvoie un 403 Forbidden.

L’interface DRF utilise un cookie sessionid pour authentifier automatiquement l’utilisateur connecté.

Postman utilise Basic Auth pour tester les endpoints protégés.

Tests réalisés

Tests Postman

Création d’utilisateurs
Authentification Basic Auth
CRUD complet sur les projets
Tests d’erreurs (400, 403, 404)
Vérification des permissions
Suppression (204 No Content)

Tests via l’interface DRF

Tests GET/POST/PUT/DELETE
Authentification via cookie sessionid
Vérification des permissions côté serveur

Installation & lancement

git clone <repo>
cd ExamenDjango
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Conclusion

L’API respecte l’ensemble des exigences du sujet :

Modèles conformes
Endpoints complets
Permissions fonctionnelles
Tests Postman + DRF
Gestion des erreurs
Documentation claire et précise
Code commenté pour faciliter la compréhension
Le projet est finalisé et prêt à être évalué.
