import streamlit as st
from user import login
import pandas as pd
import numpy as np
import requests
import json
import mariadb
import sys

# 0 ***********************************************************************************************
 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

# 1 ***********************************************************************************************

def call_api(website_url):  
    api_url = "http://localhost:8070/model/predict?model_name=web"
    payload = json.dumps({"website_url": website_url})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", api_url, headers=headers, data=payload)
    response_json = response.json()

    col1, col2 = st.columns(2)

    with col1:
        st.image(response_json['Icon'])
        st.image(response_json['Site_image'], width = 300)

    with col2:
        st.write(response_json['Título'])
        st.write(response_json['Descripción'])
        st.write(response_json['Url'])
        st.write(response_json['Categoría'])

# 2 *************************************************************************************************

def page_Link():
    st.header("LinkScribe: Link processor")
    urlLink = st.text_input("Enter the url of the link to process: ")
    processingClicked = st.button ("Start Processing", key="processing")
    if processingClicked:
        call_api(urlLink)
        #Enviar solicitud al modelo por medio del backend, controlar respuesta.
        #Respuesta = False
        #if Respuesta:
        #    Mensaje = "We are making progress! 🏆"
        #else:
        #    Mensaje = "Sorry, the link entered is not related to the different categories available ☹️"
        #st.write(Mensaje)
        st.balloons()

    # ---- BARRA LATERAL ----
    st.sidebar.header("Add link to list:")
    addList = st.sidebar.selectbox(
        "Select the list: ",
        ("List1", "List2", "List3")
    )
    addlistClicked = st.sidebar.button ("Add link to list", key="adding")
    return urlLink

# 3 ********************************************************************************************************

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

# 4 *************************************************************************************************
 
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
        st.sidebar.markdown(f'# Welcome LinkScribe Application {st.session_state.userN}')
        st.sidebar.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    logStatus, messageLog = dbuser_consultation(userName,password)
    if logStatus:
        st.session_state.userN = userName        
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error(messageLog)
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            st.title("LinkScribe Application")
            st.session_state.userN = ""
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))

def dbuser_consultation(user_app, password):
    try:
        conn = mariadb.connect(
            user = "user", # MARIADB_USER
            password = "user", # MARIADB_PASSWORD
            host = "127.0.0.1", # service name of the database container
            port = 7706, # MARIADB EXPOSED PORT
            database = "wsdb" # MARIADB_DATABASE
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    # Get Cursor
    cur = conn.cursor()
    cur1 = conn.cursor()
    cur2 = conn.cursor()

    #retrieving confirmation of exist user
    some_name = user_app
    some_pass = password
    cur.execute("Select count(row_id) as qty from user_name where user_id = ? or user_desc = ?", (some_name,some_name,))   

    for qty in cur: 
        # print(f"The user name: {some_name}, is active?: {qty}")
        if qty == (0,):
            #print(f"{some_name} user not exist, please log a new user!")
            messageLog = f"{some_name} user not exist, please log a new user!"
            logStatus = False
        else:
            cur1.execute("Select count(row_id) as qty from user_name where (user_id = ? or user_desc = ?) and encrypt_pw = PASSWORD(?)", (some_name,some_name,some_pass,))  
            for qty in cur1: 
                if qty == (0,):
                    #print(f"Wrong password for {some_name} user")
                    messageLog = f"Wrong password for {some_name} user"
                    logStatus = False
                else:
                    cur2.execute("Select user_desc from user_name where (user_id = ? or user_desc = ?) and encrypt_pw = PASSWORD(?)", (some_name,some_name,some_pass,)) 
                    for user_desc in cur2:
                        #print(f"WELCOME {user_desc}")
                        messageLog = f"WELCOME {user_desc}"
                        logStatus = True
    
    # close database connection
    conn.close()

    return logStatus, messageLog


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