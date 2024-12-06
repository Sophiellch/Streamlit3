import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

lesDonneesDesComptes = {'usernames': {'sophie': {'name': 'utilisateur',
   'password': 'xxx',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'utilisateur': {'name': 'root',
   'password': 'utilisateurMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}
authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire
)
authenticator.login()
if st.session_state["authentication_status"]:
      with st.sidebar:
            authenticator.logout("Déconnexion")
            selected = option_menu("Menu principal", ["Accueil 😍", 'Les photos de potamochères 🐗'])
      if selected == "Accueil 😍" :
            st.title("Bienvenue sur ma page")
            st.image('https://img.freepik.com/photos-gratuite/mot-bienvenue-disponible-lancement-ouvert_53876-124476.jpg?semt=ais_hybrid')
      elif selected == "Les photos de potamochères 🐗" :
            st.title("Bienvenue dans l'album des potamochères")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Potamochoerus_porcus_-_Disney%27s_Animal_Kingdom_Lodge%2C_Orlando%2C_Florida%2C_USA_-_20100119_-_02.jpg/1200px-Potamochoerus_porcus_-_Disney%27s_Animal_Kingdom_Lodge%2C_Orlando%2C_Florida%2C_USA_-_20100119_-_02.jpg', use_container_width=True)
            with col2:
                st.image('https://www.cerza.com/wp-content/uploads/2023/04/bebe-potamochere.jpg', use_container_width=True)
            with col3:
                st.image('https://www.reserveafricainesigean.fr/content/uploads/2023/10/potamochere.jpg', use_container_width=True)

  # Le bouton de déconnexion
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')

   
