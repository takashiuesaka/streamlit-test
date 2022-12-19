import streamlit as st
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
from streamlit.server.server import Server

st.title('Hello! test session and headers')

# Get headers
session_id = get_script_run_ctx().session_id
server = Server.get_current()
session_info = server._get_session_info(session_id)
if session_info.ws is None:
    # At first page load, this is None (at least until #4099 is fixed)
    st.markdown("Unable to get session websocket. Please refresh the page.")
    st.stop()
headers = session_info.ws.request.headers

st.text('headers')
st.text(headers)