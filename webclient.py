import streamlit as st
import readCSV

df = readCSV.df


def main():
    st.title("Application Streamlit pour Recherche de Prix Immobilier par Ville et Quartier")

    if df is not None:
        # Liste unique des villes pour la sélection
        villes_uniques = df['Ville'].unique()

        # Sélection de la ville à partir de l'interface utilisateur
        ville_choisie = st.selectbox("Choisissez une ville", villes_uniques)

        st.write(f"### Contenu du fichier CSV pour la ville {ville_choisie}")

        # Filtrer les données en fonction de la ville choisie
        df_ville = df[df['Ville'] == ville_choisie]

        # Liste unique des quartiers pour la sélection
        quartiers_uniques = df_ville['Quartier'].unique()

        # Sélection du quartier à partir de l'interface utilisateur
        quartier_choisi = st.selectbox("Choisissez un quartier", quartiers_uniques)

        st.write(f"### Vous avez choisi le quartier : {quartier_choisi}")

        # Filtrer les données en fonction du quartier choisi
        df_quartier = readCSV.quartier(quartier_choisi)

        # Afficher les données pour le quartier choisi
        st.write(df_quartier)


if __name__ == '__main__':
    main()
