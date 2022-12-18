import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers

headers = _get_websocket_headers()
access_token = headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

st.title('Easy Auth Test2')

st.text('X-MS-CLIENT-PRINCIPAL-NAME')

if access_token is not None:
    st.text(access_token)
else:
    st.text('X-MS-CLIENT-PRINCIPAL-NAME is not in header.')