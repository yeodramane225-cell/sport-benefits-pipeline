---

## Installation du projet

### Prérequis

- Docker et Docker Compose  
- Python 3.10+  
- Git  
- Accès internet (API Google Maps, Slack)

### Clonage du dépôt

```bash
git clone https://github.com/yeodramane225-cell/sport-benefits-pipeline.git
cd sport-benefits-pipeline
---




##Installation des dépendances
pip install -r requirements.txt
##Lancement de l’infrastructure
docker-compose up -d
##Variables d’environnement

Créer un fichier .env à la racine du projet :

MINIO_ENDPOINT=http://localhost:9000
MINIO_ACCESS_KEY=minio
MINIO_SECRET_KEY=minio123

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=sportdb

GOOGLE_MAPS_API_KEY=xxxxxxxxxxxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxxx/xxxx/xxxx

Ces variables permettent de configurer l’accès aux services externes utilisés dans le pipeline.

##Génération et ingestion des données
##Données sources
Données_RH.xlsx
Données_Sportives.xlsx

##Génération de données (Faker)
python src/generate_fake_sport_data.py

Ce script génère des activités sportives simulées sur plusieurs mois afin d’enrichir le dataset.

##Upload dans MinIO
mc cp data/raw/* minio/raw/

L’upload peut également être automatisé via Kestra.

##Transformation des données
##Script principal
python transform.py
##Fonctionnalités
Fusion des données RH et sportives
Nettoyage et normalisation
Application des règles métier
Calcul des distances (API Google Maps)
Calcul des avantages employés
Réorganisation des colonnes
Export d’un fichier CSV final
##Lisibilité du code

Le projet respecte les bonnes pratiques de développement :

Docstrings dans les fonctions principales
Commentaires explicatifs pour les traitements complexes
Logs structurés (logging.info, logging.error)
Gestion des exceptions pour sécuriser le pipeline
##Chargement dans PostgreSQL
##Création de la table
python src/postgres_utils.py --create-table
##Chargement des données
python src/postgres_utils.py --load data/curated/final.csv

Le chargement est optimisé via des opérations de type COPY pour de meilleures performances.

##Orchestration avec Kestra
Flows disponibles
flow_transform.yaml
flow_create_table.yaml
flow_load_to_postgres.yaml
Fonctionnalités
Exécution automatisée des pipelines
Monitoring des workflows
Logs détaillés
Historique des exécutions
Alertes en cas d’échec
##Tests de qualité
##Tests unitaires
pytest tests/
##Tests avancés
SODA (optionnel)
Great Expectations (optionnel)
##Stratégie de test

Les tests sont exécutés après chaque étape du pipeline :

validation des données sources
vérification des transformations
contrôle des règles métier
validation du schéma final
Utilisation de GitHub

##Le projet suit de bonnes pratiques de versioning :

branche main : production
branche develop : développement
commits réguliers et explicites
historique propre (rebase)
documentation versionnée

GitHub garantit la traçabilité et la reproductibilité du projet.

##Scalabilité
##Architecture scalable
MinIO distribué
Kestra en cluster
PostgreSQL managé (RDS, Cloud SQL)
Python scalable (Spark, Dask, Ray)
##Montée en charge
séparation des couches de données
stockage objet extensible
orchestration distribuée
base optimisée pour l’analytique
##Coûts
environnement local (self-hosted) : coût minimal
environnement cloud : dépend du stockage, du compute et des services managés
##Migration cloud

L’architecture est conçue pour évoluer facilement :

passage de Docker local à Kubernetes
migration vers des services cloud managés
intégration dans une plateforme data moderne
##Conclusion

Ce projet démontre la mise en œuvre d’un pipeline data complet, modulaire et industrialisable.

Il constitue une base solide pour un déploiement en production dans un environnement scalable, avec un haut niveau de qualité, de test et de maintenabilité.
