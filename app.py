import streamlit as st
from creaHTML import estilosCSS, crear_html_partido
from autenticacion import autentica
from leerResultados import leerResultados


if st.session_state.get("contador") is None:
    st.session_state.contador = 0

if st.query_params.get("reset") == "true":  
    # clear_leeCelda()
    st.query_params.reset = "false"

spreadsheet = autentica()

st.markdown(estilosCSS, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Grupo A", "Grupo B", "Fase Oro", "Fase Plata"])

with tab1:
    worksheet = spreadsheet.worksheet("Grupo A") 
    partidos = leerResultados(worksheet)


    # --- Mostrar cada partido ---
    if not partidos:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        # Generar todo el HTML junto para evitar múltiples llamadas a st.markdown si es posible
        # html_completo = "".join([crear_html_partido(p) for p in partidos])
        # st.markdown(html_completo, unsafe_allow_html=True)
        # Nota: Streamlit puede manejar mejor llamadas separadas para re-renderizados parciales
        for partido_data in partidos:
            html_partido = crear_html_partido(partido_data)
            st.markdown(html_partido, unsafe_allow_html=True)


with tab2:
    worksheet = spreadsheet.worksheet("Grupo B") 
    partidos = leerResultados(worksheet)


    # --- Mostrar cada partido ---
    if not partidos:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        # Generar todo el HTML junto para evitar múltiples llamadas a st.markdown si es posible
        # html_completo = "".join([crear_html_partido(p) for p in partidos])
        # st.markdown(html_completo, unsafe_allow_html=True)
        # Nota: Streamlit puede manejar mejor llamadas separadas para re-renderizados parciales
        for partido_data in partidos:
            html_partido = crear_html_partido(partido_data)
            st.markdown(html_partido, unsafe_allow_html=True)