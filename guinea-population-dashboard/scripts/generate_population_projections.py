import pandas as pd

# Données de base pour les régions en 2011
data_2011 = {
    "Boké": 1037796,
    "Conakry": 1591498,
    "Faranah": 902213,
    "Kankan": 1880302,
    "Kindia": 1495176,
    "Labé": 951431,
    "Mamou": 700289,
    "Nzérékoré": 1100000
}

# Taux de croissance annuel

growth_rate = 2.26

# Années de calcul
years = list(range(2011, 2101))

# Initialiser le DataFrame
df = pd.DataFrame({"Année": years})

# Calcul des populations projetées

for region, pop_2011 in data_2011.items():
    df[region] = [int(pop_2011 * (1 + growth_rate / 100) ** (year - 2011)) for year in years]

# Sauvegarder le DataFrame dans un fichier CSV

df.to_csv("../data/population_regions_projections.csv", index=False)
