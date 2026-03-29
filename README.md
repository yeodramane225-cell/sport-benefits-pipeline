

## Installation du projet

### Prérequis

- Docker et Docker Compose  
- Python 3.10+  
- Git  
- Accès internet (API Google Maps, Slack)

### Clonage du dépôt


git clone https://github.com/yeodramane225-cell/sport-benefits-pipeline.git
cd sport-benefits-pipeline




## Installation des dépendances
pip install -r requirements.txt
## Lancement de l’infrastructure
docker-compose up -d
## Variables d’environnement

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

## Génération et ingestion des données
## Données sources
Données_RH.xlsx
Données_Sportives.xlsx

## Génération de données (Faker)
python src/generate_fake_sport_data.py

Ce script génère des activités sportives simulées sur plusieurs mois afin d’enrichir le dataset.

## Upload dans MinIO
mc cp data/raw/* minio/raw/

L’upload peut également être automatisé via Kestra.

## Transformation des données
## Script principal
python transform.py
## Fonctionnalités
Fusion des données RH et sportives
Nettoyage et normalisation
Application des règles métier
Calcul des distances (API Google Maps)
Calcul des avantages employés
Réorganisation des colonnes
Export d’un fichier CSV final
## Lisibilité du code

Le projet respecte les bonnes pratiques de développement :

Docstrings dans les fonctions principales
Commentaires explicatifs pour les traitements complexes
Logs structurés (logging.info, logging.error)
Gestion des exceptions pour sécuriser le pipeline
## Chargement dans PostgreSQL
## Création de la table
python src/postgres_utils.py --create-table
## Chargement des données
python src/postgres_utils.py --load data/curated/final.csv

Le chargement est optimisé via des opérations de type COPY pour de meilleures performances.

## Orchestration avec Kestra
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
## Tests de qualité
## Tests unitaires
pytest tests/
## Tests avancés
SODA (optionnel)
Great Expectations (optionnel)
## Stratégie de test

Les tests sont exécutés après chaque étape du pipeline :

validation des données sources
vérification des transformations
contrôle des règles métier
validation du schéma final
Utilisation de GitHub

## Le projet suit de bonnes pratiques de versioning :

branche main : production
branche develop : développement
commits réguliers et explicites
historique propre (rebase)
documentation versionnée

gitHub garantit la traçabilité et la reproductibilité du projet.

## Scalabilité de la plateforme
Introduction

Cette section décrit les mécanismes de scalabilité de la plateforme de données.
Bien que ces éléments ne soient pas implémentés dans le POC, ils permettent d’anticiper une mise en production pour gérer une montée en charge.

## Lecture de l’architecture
Kestra Server : interface, API et scheduler centralisés.
Executors : exécution parallèle des flows.
MinIO : cluster distribué pour éviter le point de panne unique.
PostgreSQL : séparation en primaire (écritures) et replicas (lectures BI).
Slack : alertes d’exécution et d’échec.
Prometheus + Grafana : supervision technique.

## Objectifs de scalabilité
Assurer la montée en charge : plus d’employés, activités et fichiers.
Garantir la disponibilité : éviter qu’un seul serveur Kestra/Postgres/MinIO soit un point de panne.
Maîtriser les coûts : dimensionner selon le volume réel.

## Architecture cible “scalable”
Kestra : 1 nœud server + N executors (Docker Swarm / Kubernetes).
MinIO : cluster distribué (4+ nœuds) avec erasure coding pour tolérance aux pannes.
PostgreSQL : 1 primaire + réplicas avec failover automatique.
Infrastructure : isolation des rôles (on-premise ou cloud), autoscaling possible.
Supervision : dashboards Kestra, Prometheus/Grafana, alertes Slack.

## Approche par étapes
Séparer les rôles : VM/conteneur dédié pour Kestra, MinIO et Postgres.
Haute disponibilité : réplication Postgres, cluster MinIO, Kestra server + executors.
Industrialiser le déploiement : Docker Compose (dev), Swarm/K8s (prod), limites CPU/RAM.
Suivi des indicateurs : stockage MinIO, temps d’exécution des flows, performances DB.

## Estimation des coûts


## Coût de la scalabilité

| Composant                | Besoin pour la scalabilité                         | Ressources nécessaires                              | Coût estimé (€/mois) | Commentaires                          |
|-------------------------|---------------------------------------------------|----------------------------------------------------|----------------------|--------------------------------------|
| Kestra – Server         | Nœud central (UI, API, scheduler)                 | 2 vCPU, 4 Go RAM                                   | 20–40 €              | Charge faible                        |
| Kestra – Executors      | Exécution parallèle des flows                     | 2–4 vCPU + 4–8 Go RAM par executor                 | 40–160 €             | Coût variable selon la charge        |
| MinIO – Cluster distribué | Stockage scalable + tolérance aux pannes        | 4 nœuds × (2 vCPU, 4 Go RAM, 200 Go disque)        | 80–200 €             | Poste principal du coût              |
| PostgreSQL – HA         | Haute disponibilité + réplication                 | 2 nœuds × (2 vCPU, 4 Go RAM, 100 Go disque)        | 60–120 €             | Réplica utilisé pour BI              |
| Stockage additionnel    | Historique + rétention 12 mois                    | +500 Go                                            | 20–50 €              | Dépend du volume                     |
| Réseau interne          | Communication Kestra ↔ MinIO ↔ Postgres           | 1–2 To/mois                                        | 10–30 €              | Dépend du trafic                     |
| Observabilité           | Prometheus + Grafana                              | 1 vCPU, 2 Go RAM                                   | 10–15 €              | Open source                          |
| Slack                   | Webhook + canal dédié                             | —                                                  | 0 €                  | Slack gratuit                        |
| Support / maintenance   | Optionnel                                         | —                                                  | 0–200 €              | Selon support entreprise             |

## Conclusion

Cette architecture scalable permet de garantir la performance, la disponibilité et la résilience du pipeline, facilitant la montée en charge et une transition vers une production robuste.
