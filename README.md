# Tableau de Bord de la Population de Guinée

Ce projet est un tableau de bord de visualisation de données complet pour les statistiques de la population de la Guinée. Construit en utilisant PostgreSQL, Streamlit et déployé sur Heroku, ce tableau de bord offre des visualisations perspicaces et des éléments interactifs pour explorer les tendances démographiques et la répartition de la population dans les différentes régions de la Guinée.

## Fonctionnalités

- **Carte Interactive** : Visualisez la répartition de la population à travers la Guinée avec une carte interactive.
- **Statistiques de Population** : Consultez des statistiques détaillées de la population pour chaque région.
- **Tendances Migratoires** : Analysez les tendances migratoires et les changements de population au fil des ans.
- **Design Réactif** : Accessible sur différents appareils avec une interface conviviale.

## Technologies Utilisées

- **PostgreSQL** : Système de gestion de base de données pour stocker et gérer les données de population.
- **Streamlit** : Cadre pour créer des applications web interactives de visualisation de données.
- **Heroku** : Plateforme cloud pour déployer et héberger l'application.

## Installation et Déploiement

1. **Clonez le dépôt :**

    ```bash
    git clone hhttps://github.com/Santoudllo/guinea-population-dashboard.git
    ```

2. **Installez les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configurez la base de données PostgreSQL :**

    ```bash
    # Créez la base de données et les tables nécessaires
    # Insérez les données de population
    ```

4. **Lancez l'application Streamlit :**

    ```bash
    streamlit run app.py
    ```

5. **Déployez sur Heroku :**

    ```bash
    heroku create guinea-population-dashboard
    heroku addons:create heroku-postgresql:hobby-dev
    git push heroku main
    ```
