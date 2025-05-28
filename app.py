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

def widgetUltimaActualizacion():
    ahora = datetime.now() + timedelta(hours=2)
    fecha_hora_minutos_str = ahora.strftime("%Y-%m-%d %H:%M")
    st.markdown(
            f"""
            <div style="margin-top: 0.5em;"> 
                Última consulta: <b>{fecha_hora_minutos_str}</b>
            </div>
            """, unsafe_allow_html=True)
      
    if st.button("🔄 **ACTUALIZA**", use_container_width=True):
        st.rerun()

def main():
    spreadsheet = autentica()
    with server_state_lock["reload"]:
        if "reload" not in server_state:
            server_state.reload = 0

    if st.query_params.get(st.secrets['query']['key']) == st.secrets['query']['value']:  
        st.cache_data.clear()
        time.sleep(2)
        # ejecutaTabs(spreadsheet)
        if st.button("🔄 **REINICIA**", use_container_width=True):
            server_state.reload = (server_state.reload + 1) % 2
         
        # server_state.reload = (server_state.reload + 1) % 2

    # _ = server_state.reload
    inyectaEstilos()
    st.markdown(crearHTMLCabecera(), unsafe_allow_html=True)
    
    widgetUltimaActualizacion()

    ejecutaTabs(spreadsheet)
    st.markdown(crearHTMLLogosFinales(), unsafe_allow_html=True)


if __name__ == "__main__":
    main()