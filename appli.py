import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components  # ouvrir les docs html

# --- Titre du dashboard ---

st.title ("Analyse de la situation sanitaire en           Afrique de l'Ouest")

# --- Chargement des données ---
df = ("appli_streamlit/Data/incidence-of-malaria.csv")
dt = ("appli_streamlit/Data/mat-mortality.csv")

# --- La Sidebar  ---

st.sidebar.title ("Sommaire")
pages = ["Contexte du Projet 3", "Objectifs", "Exploration des DTsets", "Analyse Univariée", "Analyse Bivariée", "Download CSV"]
page = st.sidebar.radio ("Aller à la pages :", pages)

if page == pages[0] :
    st.write ("#** Contexte du projet**")
    st.image("image.png", caption="Santé", use_container_width=True)

    st.write ("L'Afrique de l'Ouest est l'une des régions du monde les plus touchées par les maladies évitables, notamment le paludisme et les complications liées à la grossesse. Le Sénégal, comme de nombreux pays de la sous-région, doit faire face à des défis sanitaires importants malgré les progrès réalisés au cours des deux dernières décennies.")
    st.write ("Les décideurs publics, les ONG de santé et les agents de terrain disposent rarement d'outils visuels accessibles pour suivre l'évolution des indicateurs sanitaires clés (incidence du paludisme, taux de mortalité maternelle, couverture vaccinale) au fil du temps et selon les régions. L'absence de visualisation claire ralentit la prise de décision.")
    st.write ("Le paludisme représente encore une des premières causes de mortalité infantile en Afrique subsaharienne. La mortalité maternelle reste élevée dans les zones rurales faute de suivi et d'anticipation. Des données bien visualisées permettent d'orienter les ressources là où elles sont le plus nécessaires.")
    st.write ("La solution pourrait être utilisé par : le Ministères de la Santé, les ONG (MSF, Croix-Rouge sénégalaise), les chercheurs en santé publique, les journalistes de données, les étudiants en médecine ou en data.")
    

elif page == pages[1] :
    st.write ("#** Objectifs du projet**")
    st.image ("image\pile.png",
         caption="Santé",
         use_container_width = True)
    st.write ("**Objectif général**")
    st.write ("Il s'agit de concevoir et déployer un tableau de bord analytique interactif permettant de visualiser et d'interpréter l'évolution des principaux indicateurs de santé publique (paludisme, mortalité maternelle) au Sénégal et dans plusieurs pays d'Afrique de l'Ouest, à partir de données open source.")
    st.write ("**Objectifs spécifiques**")
    st.write ("Lister les tâches concrètes attendues :")
    st.write ("● Charger et explorer des jeux de données open source provenant de l'OMS, Our World in Data ou Africa CDC")
    st.write ("● Nettoyer et normaliser les données (valeurs manquantes, doublons, formats de dates, harmonisation des noms de pays)")
    st.write ("● Réaliser une analyse exploratoire des données (EDA) : tendances temporelles, comparaisons régionales, corrélations")
    st.write ("● Construire un tableau de bord interactif avec Power BI, Tableau Public ou Streamlit")
    st.write ("● Identifier les zones géographiques et les périodes les plus critiques")
    st.write ("● Documenter la méthodologie, les choix techniques et les limites de l'analyse")
    
elif page == pages[2] :
    st.write ("#**Exploration des Données**")

    st.write ("Data sur la Malaria ")
    df = pd.read_csv("Data\incidence-of-malaria.csv")
    st.dataframe(df)
    st.write ("Dimensions du tableau :", df.shape)
    
    st.write ("Data sur la Mortalité maternelle")
    dt = pd.read_csv("Data\mat-mortality.csv")
    st.dataframe(dt)
    st.write ("Dimensions du tableau :", dt.shape)
    
    if st.checkbox("Afficher les valeurs manquantes") : 
        print ("df", st.dataframe(df.isna().sum()))
        print ("dt", st.dataframe(dt.isna().sum()))     
        
    if st.checkbox("Afficher les doublons") : 
       print ("df", st.write("Pour df :", df.duplicated().sum()))
       print ("dt", st.write("Pour dt :", dt.duplicated().sum()))
    
    st.write ("Profile_Report")
    Report = st.radio("Choisir le rapport :", ["Paludisme", "Mortalité maternelle"])
    if Report == "Paludisme":
        with open ("Profile_report/output_projetDT_malaria.html", "r", encoding="utf-8") as f:
            report_html = f.read()
        components.html(report_html, height=800, scrolling=True)
    else :
        with open ("Profile_report/output_projetDt_mort.html", "r", encoding="utf-8") as f:
            P_report_html = f.read()
        components.html(P_report_html, height=800, scrolling=True)

    st.write ("*Résumé de l'exploration*") 
    st.write (" Notre dataset 'df' à rapport au paludisme. Il s'agit d'un dataset de 2851 lignes × 4 colonnes.")
    st.write ("Les variables sont : 'Entity', 'Code', 'Year' et 'INcidence of malaria (per 1,000population at risk)'.  La première variable comporte 116 différents pays du monde avec chacun une abréviation dans la deuxième vriable 'Code'. Ainsi, nous avons 116 abréviations distincts. L'incidence est donnée pour chaque pays de l'année 2000 à 2024. Nous avons donc 2 variables de types textuelles et 2 de types numériques.")            
    st.write ("Il n'y a pas de valeur nulls dans les lignes ni de valeurs dupliquées pour les données sur le Paludisme.")       
    st.write ("Le dataframe sur la mortalité maternelle 'dt', ayant 9264 lignes pour 5 colonnes, ne possède pas de valeurs manquantes mais possède assez de doublons dans sa dernière colonnes.")

elif page == pages[3] :
    st.subheader ("#**Analyses Univariées**")
    st.subheader ("Tendances Centrales")
    indics =  st.radio ("Choisir le fichier à afficher :", ["Malaria", "Mortality-Maternal"]) 
    if indics == "Malaria" :
        df = pd.read_csv("Data\incidence-of-malaria.csv")
        Median = df['Incidence of malaria (per 1,000 population at risk)'].median()
        Moynne = df['Incidence of malaria (per 1,000 population at risk)'].mean()
        print ('L incidence médiane est :', st.write ("L incidence médiane est :", Median))
        print ('L incidence moyenne est :', st.write ("L incidence moyenne est :", Moynne))
    else :
        dt = pd.read_csv("Data\mat-mortality.csv")
        Mediane = dt['Maternal mortality ratio'].median()
        Moyenne = dt['Maternal mortality ratio'].mean()
        print ( st.write ("Le ratio médiane est :", Mediane))
        print ( st.write ("La moyenne des ratio est :", Moyenne))
    
       # --- Top 10 ---
    st.subheader("Top 10 des pays les plus touchés ")
    Top = st.selectbox("Choisir le Top 10 pour :", ["Paludisme", "Mortalité maternelle"])

    if Top == "Paludisme":
        df = pd.read_csv("Data\incidence-of-malaria.csv")
        top_df = df.groupby("Entity")["Incidence of malaria (per 1,000 population at risk)"].mean().reset_index()
        top10 = top_df.sort_values(by="Incidence of malaria (per 1,000 population at risk)", ascending=False).head(10).reset_index(drop=True)
        st.table(top10[["Entity", "Incidence of malaria (per 1,000 population at risk)"]])
    else:
        dt = pd.read_csv("Data\mat-mortality.csv")
        top_dt = dt.groupby("Entity")["Maternal mortality ratio"].mean().reset_index()
        top_10 = top_dt.sort_values(by="Maternal mortality ratio", ascending=False).head(10).reset_index(drop=True)
        st.table(top_10[["Entity", "Maternal mortality ratio"]])

    
# --- Graph par pays et par maladie sur les années ---
    st.subheader ("Graph par pays et par maladie sur les années ")
    Affect = st.selectbox ("Choisir l'affection :", ["Malaria", "Mortalité maternelle"])
    
    if Affect == "Malaria":
        pays = st.selectbox ("Choisir un pays :", df['Entity'].unique())
        df_1 = df[df['Entity'] == pays]
        fig = px.line(df_1, x="Year", y="Incidence of malaria (per 1,000 population at risk)", 
                  title=f"Incidence du paludisme - {pays}")
    else:
        pays = st.selectbox("Choisir un pays :", dt['Entity'].unique())
        dt_1 = dt[dt['Entity'] == pays]
        fig = px.line(dt_1, x="Year", y="Maternal mortality ratio", 
                  title=f"Mortalité maternelle - {pays}")

    st.plotly_chart(fig)


    # Boxplot
    figs_1 = px.box(
        df,
        y="Incidence of malaria (per 1,000 population at risk)",
        title="Boxplot de : Incidence of malaria (per 1,000 population at risk)",
        labels={"Incidence of malaria (per 1,000 population at risk)": "Incidence du paludisme"}
    )
    st.plotly_chart (figs_1)

    # Histplot
    figs_2 = px.histogram (
        df,
        x="Incidence of malaria (per 1,000 population at risk)",
        title="Histplot de : Incidence of malaria (per 1,000 population at risk)",
        labels={"Incidence of malaria (per 1,000 population at risk)": "Incidence du paludisme"}
    )
    st.plotly_chart (figs_2)

    dt = pd.read_csv("Data\mat-mortality.csv")
    figs_3 = px.histogram (
        dt,
        x="World region according to OWID",
        title="Barplot de : World region according to OWID",
        labels={"World region according to OWID": "Région du monde (OWID)"}
    )
    st.plotly_chart (figs_3)

    # --- Carte choroplèthe (optionnel si données géographiques disponibles) ---
# --- Carte choroplèthe dynamique ---
    choix_carte = st.radio("Choisir la carte :", ["Paludisme 2020", "Mortalité maternelle 2020"])

    if choix_carte == "Paludisme 2020":
        df_map = df[df['Year'] == 2020]
        fig_map = px.choropleth(df_map, locations="Entity", locationmode="country names",
                            color="Incidence of malaria (per 1,000 population at risk)",
                            title="Carte du paludisme en Afrique de l'Ouest (2020)")
    else:
        dt_map = dt[dt['Year'] == 2020]
        fig_map = px.choropleth(dt_map, locations="Entity", locationmode="country names",
                            color="Maternal mortality ratio",
                            title="Carte de la mortalité maternelle en Afrique de l'Ouest (2020)")

    st.plotly_chart(fig_map)
    

elif page == pages[4] :
    st.subheader ("#**Analyses bivariées**")

    df = pd.read_csv("Data\incidence-of-malaria.csv")
    dt = pd.read_csv("Data\mat-mortality.csv")

    df1 = df.groupby("Year")["Incidence of malaria (per 1,000 population at risk)"].mean().reset_index()
    dt1 = dt.groupby("Year")["Maternal mortality ratio"].mean().reset_index()
    
    top_df = df.groupby("Entity")["Incidence of malaria (per 1,000 population at risk)"].mean().reset_index()
    top_dt = dt.groupby("Entity")["Maternal mortality ratio"].mean().reset_index()

    figbi_1 = px.line(
        df1,
        x="Year",
        y="Incidence of malaria (per 1,000 population at risk)",
        title="Évolution mondiale du paludisme de 2000 à 2024",
        labels={
            "Year": "Année",
            "Incidence of malaria (per 1,000 population at risk)": "Incidence moyenne"
        }
    )
    st.plotly_chart(figbi_1)

    ordre_df = top_df.sort_values (by="Incidence of malaria (per 1,000 population at risk)", ascending = False)
    st.write ("Top 10 par ordre décroissant sur la Malaria")
    st.dataframe (ordre_df)
    ordre_dt = top_dt.sort_values (by="Maternal mortality ratio", ascending = False)
    st.write ("Top 10 par ordre décroissant sur la mortalité maternelle")
    st.dataframe (ordre_dt)

    
    figbi_2 = px.line(
        dt1,
        x="Year",
        y="Maternal mortality ratio",
        title="Évolution Mondiale du Ratio de Mortalité Maternelle par An",
        labels={
            "Year": "Année",
            "Maternal mortality ratio": "Ratio de Mortalité Maternelle"
        }
    )
    # Ajout de la grille
    figbi_2.update_layout(
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
    )
    st.plotly_chart(figbi_2) 



elif page == pages[5] : 
    indics =  st.radio ("Choisir l'indicateur", ["Malaria", "Mortality-Maternal"]) 
    if indics == "Malaria" :
        df = pd.read_csv("Data\incidence-of-malaria.csv")
        st.download_button(
        label = "Télécharger Malaria.CSV",
        data = df.to_csv(index=False).encode("utf-8"),
        file_name = "incidence-paludisme.csv",
        mime="text/csv"
    )
    else :
        dt = pd.read_csv("Data\mat-mortality.csv")
        st.download_button(
        label = "Télécharger Mortalité maternelle.csv",
        data = dt.to_csv(index=False).encode("utf-8"),
        file_name = "mortalite-maternelle.csv",
        mime="text/csv"
    )
    st.image ("image\ChatGPT Image 30 juin 2026, 22_20_34.png",
         caption="Santé",
         use_container_width = True)
    