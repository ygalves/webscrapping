import streamlit as st
import requests
import json

# 0 ***********************************************************************************************
 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

# 1 ***********************************************************************************************

def call_api(website_url):  
    api_url = "http://backendapi-dns.gccggafwdea6gvbw.koreacentral.azurecontainer.io:8040/model/predict?model_name=web"
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

if __name__ == '__main__':
    st.header("LinkScribe: Link processor")
    urlLink = st.text_input("Enter the url of the link to process: ")
    processingClicked = st.button ("Start Processing", key="processing")
    if processingClicked:
        call_api(urlLink)

# 2 *************************************************************************************************



# 4 *************************************************************************************************


    
