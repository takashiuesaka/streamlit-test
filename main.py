import streamlit as st
import requests
import socket

st.title('Easy Auth Test3')

host = socket.gethostname()
st.text('hostname: ' + host)


api_url = "https://msue-python-streamlit.azurewebsites.net/.auth/me"
response = requests.get(api_url)

st.text(response)
