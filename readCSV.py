import pandas as pd

# IMPORTANT: changer le chemin du fichier avec celui de votre local pour que ça fonctionne
df = pd.read_csv('../../prix_immobilier_fictif.csv', sep=',')

def loadAllCitiesAvailable():
    return df['Ville'].unique().tolist()


def getCity(city):
    return df[df['Ville'] == city]


def quartier(quartier):
    return df[df['Quartier'] == quartier]