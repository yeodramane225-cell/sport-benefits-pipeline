Pipeline Sport Benefits — Documentation du Projet
Ce projet met en place un pipeline complet permettant de collecter, générer, transformer, orchestrer et analyser les données RH et sportives des employés.
Il respecte l’ensemble des exigences du Projet 12, depuis la modélisation jusqu’à la scalabilité, avec des tests réalisés après chaque étape du pipeline.

1. Modélisation et diagrammes
Le projet inclut :

un diagramme de flux complet du pipeline

un diagramme d’architecture détaillé

une représentation claire des couches de données

une documentation visuelle du fonctionnement de Kestra, MinIO, Python et PostgreSQL

Tests réalisés après cette étape :  
Vérification de la cohérence du flux, validation des dépendances entre composants, conformité avec les exigences du projet.

2. Source de données
Le pipeline utilise :

les fichiers fournis : Données_RH.xlsx et Données_Sportives.xlsx

un script Python qui génère des activités sportives simulées sur 12 mois via Faker

une logique de réplication (REPPENDA) pour enrichir les cas d’usage si nécessaire

Tests réalisés après cette étape :  
Contrôle de la structure des fichiers, validation des colonnes, vérification de la qualité des données générées (dates, distances, cohérence).

3. Stockage dans MinIO (S3)
Les données sont organisées en trois couches :

raw/ : données brutes

processed/ : données transformées

curated/ : données finales prêtes pour l’analyse

Tests réalisés après cette étape :  
Vérification de l’upload dans MinIO, contrôle des chemins, validation de la présence des fichiers dans les bons buckets.

4. Centralisation de la configuration
Le fichier settings.py regroupe toutes les configurations :

accès MinIO

accès PostgreSQL

API Google Maps

Webhook Slack

chemins des fichiers et paramètres globaux

Tests réalisés après cette étape :  
Test de connexion MinIO, test de connexion PostgreSQL, test de validité des clés API.

5. Application des règles métier
Le module rules.py applique l’ensemble des règles définies dans la note de cadrage :

calcul de la prime sportive

calcul des jours de bien‑être

cohérence domicile ↔ lieu d’activité

distances calculées via Google Maps API

Tests réalisés après cette étape :  
Vérification des distances, cohérence des dates, validation des règles métier, tests unitaires sur les calculs.

6. Transformation des données (Python)
Le script transform.py :

fusionne les données RH et sport

nettoie et normalise les colonnes

applique les règles métier

calcule les avantages

réordonne les colonnes

génère un CSV propre pour PostgreSQL

Tests réalisés après cette étape :  
Contrôle du CSV généré, vérification des colonnes, tests de cohérence, validation du schéma final.

7. Chargement dans PostgreSQL
Le module postgres_utils.py :

crée la table finale

charge les données via COPY IN

garantit un schéma propre et aligné avec le CSV

Tests réalisés après cette étape :  
Vérification du schéma SQL, contrôle du nombre de lignes, validation des types, test de requêtes simples.

8. Publication dans Slack
Le module slack.py :

génère des messages motivants

envoie des notifications inspirées de Strava

informe sur les performances sportives

Tests réalisés après cette étape :  
Test d’envoi Slack, validation du format des messages, contrôle du webhook.

9. Orchestration et monitoring avec Kestra
Le pipeline est orchestré par Kestra via plusieurs flows :

flow de transformation Python

flow de création de table

flow de chargement dans PostgreSQL

Kestra fournit également :

le monitoring des exécutions

les logs détaillés

les dashboards internes

la gestion des alertes et erreurs

Tests réalisés après cette étape :  
Exécution complète du pipeline, validation des logs, tests d’erreur, contrôle du monitoring.

10. Tests de qualité
Les tests automatisés incluent :

pytest pour les règles métier, distances, dates, cohérence des transformations

possibilité d’intégrer Great Expectations ou SODA pour des tests de qualité avancés

tests exécutés après chaque étape du pipeline

Ces tests garantissent la fiabilité et la cohérence des données.

11. Utilisation de GitHub
Le projet a été versionné dès le début :

branches main et develop

commits réguliers

synchronisation et rebase propre

documentation versionnée

diagrammes intégrés au dépôt

GitHub assure la traçabilité et la reproductibilité du projet.

12. Scalabilité de la plateforme
Architecture scalable
MinIO peut être distribué sur plusieurs nœuds

Kestra supporte un mode cluster

PostgreSQL peut être migré vers un service managé (RDS, Cloud SQL)

Python peut être parallélisé via Spark, Dask ou Ray

Montée en charge
séparation des couches (raw → processed → curated)

stockage objet illimité

orchestration distribuée

base SQL optimisée pour l’analytique

Coût
En self‑hosted : coût minimal

En cloud :

S3 : coût au Go stocké

RDS/Postgres : coût par instance

Compute : coût par CPU/RAM

L’architecture est conçue pour évoluer d’un POC local vers une plateforme cloud scalable.
