import streamlit as st
from tabs import tabFaseGrupos, tabFasesFinales
from creaHTML import crearHTMLCabecera, crearHTMLLogosFinales
from estilosCSS import estilosCSSGrupos, estilosCSSCabecera, estilosCSSResultadosFases, estilosCSSLogosFinales, estilosCSSTabs
from autenticacion import autentica

from datosTorneo import denominacionesFase


def main():
    # if "contador" not in st.session_state:
    #     st.session_state.contador = 0

    # if st.query_params.get("reset") == "true":  
    #     st.session_state.contador = 1
    #     st.query_params.reset = "false"

    # if st.session_state.contador == 1:
    #     st.write("¡Bienvenido.")

    spreadsheet = autentica()

    import streamlit as st

    hide_streamlit_style = """
            <style>
                /* Hide the Streamlit header and menu */
                header {
                    display: none !important; /* Cambio clave aquí */
                }
                /* Optionally, hide the footer */
                .streamlit-footer {
                    display: none !important;
                }
                /* Hide your specific div class, if it's still necessary */
                /* Si .st-emotion-cache-uf99v8 era el header o parte de él,
                   la regla de 'header' ya podría ser suficiente.
                   Si es otro elemento, mantenla. */
                .st-emotion-cache-uf99v8 {
                    display: none !important;
                }

                /* Reduce el padding superior del contenedor principal del contenido */
                /* Streamlit >1.12.0 usa esto */
                div.block-container {
                    padding-top: 1rem !important; /* Puedes probar con 0rem o 0.5rem si quieres menos espacio */
                    margin-top: 0rem !important; /* A veces también hay un margen */
                }
                /* Para versiones más antiguas de Streamlit, a veces el selector es más genérico */
                /*
                .main .block-container {
                    padding-top: 1rem !important;
                }
                */
                /* O incluso directamente sobre el main */
                /*
                .main {
                    padding-top: 1rem !important;
                }
                */
            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    # Inyección de estilos CSS
    st.markdown(estilosCSSCabecera(), unsafe_allow_html=True) # Inyecta todos los estilos
    st.markdown(estilosCSSGrupos(), unsafe_allow_html=True)
    st.markdown(estilosCSSResultadosFases(), unsafe_allow_html=True)
    st.markdown(estilosCSSLogosFinales(), unsafe_allow_html=True)
    st.markdown(estilosCSSTabs(), unsafe_allow_html=True)

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