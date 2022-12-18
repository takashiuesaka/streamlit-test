import streamlit as st
import requests

st.title('Easy Auth Test2')

api_url = ".auth/me"
response = requests.get(api_url)

st.text(response.json())
