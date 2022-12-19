import streamlit as st

from streamlit.web.server.websocket_headers import _get_websocket_headers


st.title('Hello! test session and headers')

headers = _get_websocket_headers()
access_token = headers.get("X-Access-Token")

st.text('headers count')
st.text(len(headers))

if headers is not None:
    for key, value in headers.items():
        text = 'key={}, value={}'
        st.text(text.format(key, value))