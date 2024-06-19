import psycopg2
import csv

# Connexion à PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="guinea_data",
    user="******************",
    password="************"
)

cur = conn.cursor()

# Créez la table pour les données de population par région
cur.execute('''
    CREATE TABLE population_regions (
        année INTEGER PRIMARY KEY,
        boké INTEGER,
        conakry INTEGER,
        faranah INTEGER,
        kankan INTEGER,
        kindia INTEGER,
        labé INTEGER,
        mamou INTEGER,
        nzérékoré INTEGER
    )
''')

# Insérez les données depuis le CSV
with open('../data/population_regions_projections.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute(
            "INSERT INTO population_regions VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

conn.commit()
cur.close()
conn.close()
