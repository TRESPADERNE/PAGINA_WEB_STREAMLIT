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
        /* Forzar la ocultación de la cabecera */
        header {
            display: none !important;
            visibility: hidden !important; /* Por si acaso display:none no es suficiente para algún sub-elemento */
            height: 0px !important;
            padding: 0px !important;
            margin: 0px !important;
        }

        /* Eliminar padding y margen del cuerpo y html, a veces ayuda */
        html, body {
            padding-top: 0px !important;
            margin-top: 0px !important;
        }

        /* Contenedor principal de la aplicación Streamlit */
        /* Este es el más importante después de 'header' */
        div[data-testid="stAppViewContainer"] {
            padding-top: -2rem !important; /* ¡Prueba con 0rem primero! */
            margin-top: -4rem !important;
        }

        /* Contenedor del contenido principal (donde van tus st.write, etc.) */
        div.block-container {
            padding-top: 0.5rem !important; /* Un poco de padding aquí puede ser bueno, o prueba 0rem */
            margin-top: 0rem !important;
        }

        /* A veces hay un elemento 'main' envolviendo */
        section.main {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }

        /* Ocultar el pie de página (opcional) */
        .streamlit-footer {
            display: none !important;
        }

        /* Tu clase específica, si sigue siendo relevante */
        .st-emotion-cache-uf99v8 { /* Reemplaza si identificas otra clase */
            display: none !important;
        }
        div[data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important; /* Por si acaso */
        }

        /* A veces, el texto "Made with Streamlit" está en un elemento separado
        o el footer general también necesita ser ocultado. */
        .streamlit-footer { /* Este ya lo tenías, pero asegúrate que está activo */
            display: none !important;
            visibility: hidden !important;
        }

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