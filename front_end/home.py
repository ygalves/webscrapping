import streamlit as st
from user import login
import pandas as pd
import numpy as np
 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

import streamlit as st

def page_Link():
    #st.markdown("# Main page 🎈")
    #st.sidebar.markdown("# Main page 🎈")
    st.header("LinkScribe: Link processor")
    urlLink = st.text_input("Enter the url of the link to process: ")
    processingClicked = st.button ("Start Processing", key="processing")
    Respuesta = False
    if processingClicked:
        #Enviar solicitud al modelo por medio del backend, controlar respuesta.
        Respuesta = False
        if Respuesta:
            Mensaje = "We are making progress! 🏆"
        else:
            Mensaje = "Sorry, the link entered is not related to the different categories available ☹️"
        st.write(Mensaje)
        st.balloons()

    # ---- BARRA LATERAL ----
    st.sidebar.header("Add link to list:")
    addList = st.sidebar.selectbox(
        "Select the list: ",
        ("List1", "List2", "List3")
    )
    addlistClicked = st.sidebar.button ("Add link to list", key="adding")

def page_List():
    df = pd.DataFrame({
        "URL": np.random.randn(1000) / 50,
        "KEY": np.random.randn(1000) / 50,
        "OTHER": np.random.rand(1000, 4).tolist()
    })
    
    st.header("LinkScribe: My link lists")
    addList = st.selectbox(
        "Information to display: ",
        ("List name", "List details")
    )
    ciudad = st.multiselect(
        "Select the lists to view:",
        options=["All", "List1","List2"],
        default=["All"],
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        wordSearch = st.text_input("Enter word to search: ")

    with col2:
        tipeSearch = st.selectbox(
            "To look for: ",
            ("Categories", "Keywords")
        )
    with col3:
        st.write("")
        st.write("")
        searchClicked = st.button ("Search", key="searching")

    st.dataframe(df)
    
    # ---- BARRA LATERAL ----
    st.sidebar.header("Create new list:")
    nameList = st.sidebar.text_input("Enter the name of the list: ")
    categoryList = st.sidebar.text_input("Enter the list category: ")
    descripList = st.sidebar.text_input("Enter a description of the list: ")
    createlistClicked = st.sidebar.button ("Start Creating", key="creating")

#def page_Other():
#    st.header("Page_other 📜")
#    st.sidebar.header("Page_other 📜")

page_names_to_funcs = {
    "Process link 🛠️": page_Link,    
    "My link lists 🌐": page_List,
#    "Create a list 📜": page_Other,    
}

 
def show_main_page():
    with mainSection:
        #urlLink = st.text_input("Enter the url of the link to process: ")
        #processingClicked = st.button ("Start Processing", key="processing")
        selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
        page_names_to_funcs[selected_page]()
        #if processingClicked:
        #       st.balloons() 
 
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.sidebar.markdown("# Welcome LinkScribe Application :unlock:")
        st.sidebar.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            st.title("LinkScribe Application")
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))


with headerSection:
    #st.title("LinkScribe Application")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
        else:
            show_login_page()