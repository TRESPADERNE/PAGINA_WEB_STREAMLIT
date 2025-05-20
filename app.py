import streamlit as st
from creaHTML import estilosCSS, crear_html_partido, crear_html_clasificacion
from autenticacion import autentica
from leerResultados import leerResultadosFaseGrupos, leerTablaClasificacion


if st.session_state.get("contador") is None:
    st.session_state.contador = 0

if st.query_params.get("reset") == "true":  
    # clear_leeCelda()
    st.query_params.reset = "false"

spreadsheet = autentica()

st.markdown(estilosCSS, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Grupo A", "Grupo B", "Fase Oro", "Fase Plata"])

with tab1:
    partidosGA = leerResultadosFaseGrupos(spreadsheet, "Grupo A")
    clasificacionGA = leerTablaClasificacion(spreadsheet, "Grupo A")

    if clasificacionGA:
        # Opciones para la tabla de clasificación:
        usar_logos_en_tabla = True # Cambia a False si prefieres solo texto
        mapeo_alias_equipos = {
            "Burgos CF": "BCF",
            "CD Parquesol": "PARQ",
            "Mullier FCN": "MUL",
            "CD Palencia FF": "PAL FF"
            # Añade más alias según necesites
        }
        # Descomenta la siguiente línea si no quieres usar alias
        # mapeo_alias_equipos = None 

        html_tabla_clasif = crear_html_clasificacion(
            clasificacionGA,
            usar_logos=usar_logos_en_tabla,
            alias_equipos=mapeo_alias_equipos
        )
        st.markdown(html_tabla_clasif, unsafe_allow_html=True)
    else:
        st.warning("No se pudieron cargar los datos de clasificación para el Grupo A.")

    st.markdown("---") # Separador visual

    # --- Mostrar cada partido ---
    if not partidosGA:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        # Generar todo el HTML junto para evitar múltiples llamadas a st.markdown si es posible
        # html_completo = "".join([crear_html_partido(p) for p in partidos])
        # st.markdown(html_completo, unsafe_allow_html=True)
        # Nota: Streamlit puede manejar mejor llamadas separadas para re-renderizados parciales
        for index, partido_data in enumerate(partidosGA):
            es_sombreado = index % 2 == 1 # Para sombrear el 2º, 4º, etc. (filas impares del índice)
                                        # Usa `index % 2 == 0` para sombrear el 1º, 3º, etc.
            # Llamar a la función con el argumento 'shaded'
            html_partido = crear_html_partido(partido_data, shaded=es_sombreado) 
            st.markdown(html_partido, unsafe_allow_html=True)


with tab2:
     
    partidos = leerResultadosFaseGrupos(spreadsheet, "Grupo B")


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