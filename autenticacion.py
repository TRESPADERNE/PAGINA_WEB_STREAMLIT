import gspread
import streamlit as st

@st.cache_resource
def autentica():
    sheetID = st.secrets['gsheets']['spreadsheetID']
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file' # A veces necesario
    ]
    credenciales ={
        "type": st.secrets['gsheets']['type'],
        "project_id": st.secrets['gsheets']['project_id'],
        "private_key_id": st.secrets['gsheets']['private_key_id'],
        "private_key": st.secrets['gsheets']['private_key'],
        "client_email": st.secrets['gsheets']['client_email'],
        "client_id": st.secrets['gsheets']['client_id'],
        "auth_uri": st.secrets['gsheets']['auth_uri'],
        "token_uri": st.secrets['gsheets']['token_uri'],
        "auth_provider_x509_cert_url": st.secrets['gsheets']['auth_provider_x509_cert_url'],
        "client_x509_cert_url": st.secrets['gsheets']['client_x509_cert_url'],
        "universe_domain": st.secrets['gsheets']['universe_domain']
        }
    
    gc = gspread.service_account_from_dict(credenciales, scopes)
    spreadsheet = gc.open_by_key(sheetID)
    return spreadsheet