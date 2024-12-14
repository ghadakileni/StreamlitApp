import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mon premier projet")
fichier = st.file_uploader("Sélectionnez un fichier au format CSV", type="CSV")

if fichier is not None:
    st.success("Fichier chargé avec succès !")
    df = pd.read_csv(fichier)
    
    st.subheader("Prévisualisation des données")
    st.dataframe(df.head())

    st.subheader("Résumé Statistique")
    st.write(df.describe())

    st.subheader("Filtrer les données")
    col1, col2 = st.columns(2)
    with col1:
        colonnes = df.columns.to_list()
        selected_column = st.selectbox("Sélectionnez une colonne à filtrer", colonnes)
    with col2:
        val_unique = df[selected_column].unique()
        selected_valeur = st.selectbox("Sélectionnez une valeur à filtrer", val_unique)
    df_filtre = df[df[selected_column] == selected_valeur]
    st.write(df_filtre)

    st.subheader("Graphique")
    # Utilisateur sélectionne X et Y
    col3, col4 = st.columns(2)
    with col3:
        X_col = st.selectbox("Sélectionnez votre axe des X", colonnes)
    with col4:
        Y_col = st.selectbox("Sélectionnez votre axe des Y", colonnes)  # Correction ici

    if st.button("Générer le graphique"):
        try:
            # Vérifiez si les colonnes sélectionnées sont valides pour un graphique
            if pd.api.types.is_numeric_dtype(df[X_col]) or pd.api.types.is_numeric_dtype(df[Y_col]):
                st.line_chart(df[[X_col, Y_col]].set_index(X_col))  # Correction ici
            else:
                st.error("Les colonnes sélectionnées doivent être numériques pour générer un graphique.")
        except Exception as e:
            st.error(f"Erreur lors de la génération du graphique : {e}")

else:
    st.warning("En attente de fichier.")