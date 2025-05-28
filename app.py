import streamlit as st
from tabs import tabFaseGrupos, tabFasesFinales
from creaHTML import crearHTMLCabecera, crearHTMLLogosFinales
from estilosCSS import inyectaEstilos
from autenticacion import autentica
import time
from datetime import datetime, timedelta

from datosTorneo import denominacionesFase

from streamlit_server_state import server_state, server_state_lock

def ejecutaTabs(spreadsheet):
    tab1, tab2, tab3, tab4 = st.tabs(denominacionesFase())

    with tab1:
        tabFaseGrupos(spreadsheet, "Grupo A")
    with tab2:
        tabFaseGrupos(spreadsheet, "Grupo B")
    with tab3:
        tabFasesFinales(spreadsheet, "Fase Oro", ["Semifinales", "Final", "Tercer y Cuarto Puesto"])
    with tab4:
        tabFasesFinales(spreadsheet, "Fase Plata", ["Semifinales Fase Plata", "Final Fase Plata", "Tercer y Cuarto Puesto Fase Plata"])

def main():
    spreadsheet = autentica()
    with server_state_lock["reload"]:
        if "reload" not in server_state:
            server_state.reload = 0

    if st.query_params.get("reset") == "true":  
        st.cache_data.clear()
        time.sleep(2) 
        ejecutaTabs(spreadsheet)
        time.sleep(2) 
        server_state.reload = (server_state.reload + 1) % 2

    
    # Inyección de estilos CSS
    inyectaEstilos()
    st.markdown(crearHTMLCabecera(), unsafe_allow_html=True)
    ahora = datetime.now() + timedelta(hours=2)
    fecha_hora_minutos_str = ahora.strftime("%Y-%m-%d %H:%M")
    
    col1, col2 = st.columns([1, 2]) # El botón ocupará 1/3 y el texto 2/3 del espacio

    with col1:
        if st.button("🔄 Última actualización: **{fecha_hora_minutos_str}**", use_container_width=True):
            st.rerun()
    with col2:
        st.markdown(
            f"""
            <div style="margin-top: 0.5em;"> 
                Última actualización: <b>{fecha_hora_minutos_str}</b>
            </div>
            """, unsafe_allow_html=True)
    ejecutaTabs(spreadsheet)
    st.markdown(crearHTMLLogosFinales(), unsafe_allow_html=True)


if __name__ == "__main__":
    main()