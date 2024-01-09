import requests
import streamlit as st
import pandas as pd


def main():
    st.title("Application Streamlit pour Recherche de Prix Immobilier par Ville et Quartier")
    # Liste unique des villes pour la sélection
    villes_uniques = requests.get('http://127.0.0.1:5000/villes').json()

    # Sélection de la ville à partir de l'interface utilisateur
    ville_choisie = st.selectbox("Choisissez une ville", villes_uniques)

    st.write(f"### Contenu du fichier CSV pour la ville {ville_choisie}")

    # Filtrer les données en fonction de la ville choisie
    df_ville = pd.DataFrame(requests.get('http://127.0.0.1:5000/ville/'+ville_choisie).json())

    # Liste unique des quartiers pour la sélection
    quartiers_uniques = df_ville['Quartier'].unique()

    # Sélection du quartier à partir de l'interface utilisateur
    quartier_choisi = st.selectbox("Choisissez un quartier", quartiers_uniques)

    st.write(f"### Vous avez choisi le quartier : {quartier_choisi}")

    # Filtrer les données en fonction du quartier choisi
    df_quartier = pd.DataFrame(requests.get('http://127.0.0.1:5000/quartierParVille/'+ville_choisie+'/'+quartier_choisi).json())

    # Afficher les données pour le quartier choisi
    st.write(df_quartier)


if __name__ == '__main__':
    main()
