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


    hide_streamlit_style = """
            <style>
                /* Ocultar la cabecera de Streamlit */
                header {
                    display: none !important;
                }

                /* Ocultar el pie de página de Streamlit (opcional) */
                .streamlit-footer {
                    display: none !important;
                }

                /* Ocultar tu clase específica si aún es necesaria y correcta.
                   Si .st-emotion-cache-uf99v8 era parte de la cabecera,
                   la regla 'header' ya podría ser suficiente. */
                .st-emotion-cache-uf99v8 {
                    display: none !important;
                }

                /* Reducir el padding superior del contenedor principal de la vista de la aplicación.
                   Este es el cambio clave para versiones más recientes de Streamlit (>=1.33.0).
                   Ajusta el valor de padding-top según necesites (e.g., 0rem, 0.5rem, 1rem).
                */
                div[data-testid="stAppViewContainer"] {
                    padding-top: 0.5rem !important; /* Prueba con 0rem o un valor muy pequeño */
                }

                /*
                Ajuste adicional para el contenedor de bloques si el anterior no es suficiente.
                En muchos casos, ajustar stAppViewContainer es suficiente.
                Verifica con el inspector de elementos si aún hay un padding no deseado
                en este elemento (div.block-container).
                */
                /*
                div.block-container {
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