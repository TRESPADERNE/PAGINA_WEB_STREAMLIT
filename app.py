import streamlit as st
from tabs import tabFaseGrupos, tabFasesFinales
from creaHTML import crearHTMLCabecera, crearHTMLLogosFinales
from estilosCSS import inyectaEstilos
from autenticacion import autentica

from datosTorneo import denominacionesFase

from streamlit_server_state import server_state, server_state_lock


def main():

    with server_state_lock["reload"]:
        if "reload" not in server_state:
            server_state.reload = 0

    if st.query_params.get("reset") == "true":  
        st.query_params.reset = "false"
        st.cache_data.clear()
        server_state.reload = (server_state.reload + 1) % 2

        

    # if st.session_state.contador == 1:
    #     st.write("¡Bienvenido.")

    spreadsheet = autentica()

    # Inyección de estilos CSS
    inyectaEstilos()

    # Cabecera
    st.markdown(crearHTMLCabecera(), unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(denominacionesFase())

    with tab1:
        tabFaseGrupos(spreadsheet, "Grupo A")
    with tab2:
        tabFaseGrupos(spreadsheet, "Grupo B")
    with tab3:
        tabFasesFinales(spreadsheet, "Fase Oro", ["Semifinales", "Final", "Tercer y Cuarto Puesto"])
    with tab4:
        tabFasesFinales(spreadsheet, "Fase Plata", ["Semifinales Fase Plata", "Final Fase Plata", "Tercer y Cuarto Puesto Fase Plata"])
 
    
    st.markdown(crearHTMLLogosFinales(), unsafe_allow_html=True)


if __name__ == "__main__":
    main()