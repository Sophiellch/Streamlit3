def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

# Vérifier si l'utilisateur est authentifié
if auth_status:
    # Si l'utilisateur est authentifié
    st.session_state["authentication_status"] = True
    accueil()
    
    # Bouton de déconnexion
    if st.sidebar.button("Déconnexion"):
        authenticator.logout("Déconnexion")
        st.experimental_rerun()  # Recharger la page après la déconnexion
elif auth_status is False:
    # Si l'utilisateur n'est pas authentifié
    st.session_state["authentication_status"] = False
    st.error("L'username ou le mot de passe est/sont incorrect(s)")
elif auth_status is None:
    # Si l'utilisateur n'a pas encore rempli les champs de connexion
    st.session_state["authentication_status"] = None
    st.warning('Les champs username et mot de passe doivent être remplis')

# Si l'utilisateur est authentifié, lui permettre de voir le contenu
if st.session_state["authentication_status"]:
    with st.sidebar:
        selection = option_menu(
            menu_title=None,  # Titre du menu, None signifie pas de titre
            options=["Accueil 😍", "Les photos de potamochère 🐗"],  # Options du menu
            orientation="vertical",  # Menu vertical dans la barre latérale
            default_index=0,  # Option sélectionnée par défaut
            key="sidebar",  # Clé unique pour éviter les conflits avec d'autres widgets
            menu_icon="cast",  # Icône pour le menu (facultatif)
        )

    # Afficher le contenu en fonction de la sélection
    if selection == "Accueil 😍":
        st.title("Bienvenue sur ma page !")
        st.image('https://img.freepik.com/photos-gratuite/mot-bienvenue-disponible-lancement-ouvert_53876-124476.jpg?semt=ais_hybrid', use_container_width=True)
    elif selection == "Les photos de potamochère 🐗":
        st.title("Bienvenue dans l'album des potamochères")

        col1, col2, col3 = st.columns(3)

        # Placer des images dans les colonnes
        with col1:
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Potamochoerus_porcus_-_Disney%27s_Animal_Kingdom_Lodge%2C_Orlando%2C_Florida%2C_USA_-_20100119_-_02.jpg/1200px-Potamochoerus_porcus_-_Disney%27s_Animal_Kingdom_Lodge%2C_Orlando%2C_Florida%2C_USA_-_20100119_-_02.jpg', use_container_width=True)
        with col2:
            st.image('https://www.cerza.com/wp-content/uploads/2023/04/bebe-potamochere.jpg', use_container_width=True)
        with col3:
            st.image('https://www.reserveafricainesigean.fr/content/uploads/2023/10/potamochere.jpg', use_container_width=True)
else:
    # Si l'utilisateur n'est pas authentifié, ne pas afficher le contenu
    st.warning("Veuillez vous connecter pour accéder au contenu.")
    
    ###JB
    def accueil():
    st.title('Bienvenue sur le contenu réservé aux utilisateurs connectés')
    st.write('Vous avez maintenant accès à ce contenu protégé.')
    st.write('Explorez les fonctionnalités via le menu à gauche.')
# Fonction pour afficher l’album photo
def photos():
    st.title('Mon album photo')
    st.write("Les photos de potamochère 🐗")
# Interface de connexion
def login():
    st.title('Authentification')
    with st.form('login_form'):
        username = st.text_input("Nom d’utilisateur")
        password = st.text_input("Mot de passe", type="password")
        submit = st.form_submit_button("Se connecter")
    if submit:
        if username in users and check_password(username, password):
            st.success(f"Bienvenue, {username} !")
            st.session_state["authentication_status"] = True
            st.session_state["username"] = username
        else:
            st.session_state["authentication_status"] = False
# Initialisation de l’état de session
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None
# Logique de gestion de l’accès
if st.session_state["authentication_status"]:
    # Barre latérale avec le bouton de déconnexion
    with st.sidebar:
        st.sidebar.success(f"Connecté en tant que : {st.session_state['username']}")
        if st.sidebar.button("Déconnexion"):
            st.session_state["authentication_status"] = None
            st.experimental_rerun()
    # Menu principal
    selection = option_menu(
        menu_title="Menu principal",
        options=["Accueil", "Photos"],
        icons=["house", "image"],  # Optionnel : icônes
        menu_icon="cast",  # Icône du menu
        default_index=0,  # Page par défaut
        orientation="horizontal",
    )
    # Afficher les pages selon la sélection
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        photos()
elif st.session_state["authentication_status"] is False:
    st.error("Le nom d’utilisateur ou le mot de passe est incorrect.")
    login()
elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez remplir les champs de connexion.")
    login()