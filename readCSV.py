import pandas as pd

# IMPORTANT: changer le chemin du fichier avec celui de votre local pour que ça fonctionne
df = pd.read_csv('../../prix_immobilier_fictif.csv', sep=',')

def loadAllCitiesAvailable():
    return df['Ville'].unique().tolist()


def getCity(ville):
    return df[df['Ville'] == ville].to_dict(orient='records')


def quartier(quartier):
    return df[df['Quartier'] == quartier].to_dict(orient='records')


def quartierParVille(ville, quartier):
    return (df[(df['Quartier'] == quartier) & (df['Ville'] == ville)]).to_dict(orient='records')