import streamlit as st
from leerResultados import leerResultadosFaseGrupos, leerTablaClasificacion, leerResultadosSemifinales, leerResultadosFinales
from datosTorneo import aliasEquipos
from creaHTML import crearHTMLPartido, crear_html_clasificacion, crearHTMLTitulosPartidos

def tabFaseGrupos(spreadsheet, nombreTab):
    partidos = leerResultadosFaseGrupos(spreadsheet, nombreTab)
    clasificacion = leerTablaClasificacion(spreadsheet, nombreTab)
    alias = aliasEquipos() # Cargar los alias de equipos

    if clasificacion:
        # Opciones para la tabla de clasificación:
        usar_logos_en_tabla = True # Cambia a False si prefieres solo texto
        
        # Descomenta la siguiente línea si no quieres usar alias
        # mapeo_alias_equipos = None 

        html_tabla_clasif = crear_html_clasificacion(
            clasificacion,
            usar_logos=usar_logos_en_tabla,
            alias_equipos=alias
        )
        st.markdown(html_tabla_clasif, unsafe_allow_html=True)
    else:
        st.warning("No se pudieron cargar los datos de clasificación para el Grupo A.")

    # st.markdown("---") # Separador visual

    # --- Mostrar cada partido ---
    if not partidos:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        # Generar todo el HTML junto para evitar múltiples llamadas a st.markdown si es posible
        # html_completo = "".join([crear_html_partido(p) for p in partidos])
        # st.markdown(html_completo, unsafe_allow_html=True)
        # Nota: Streamlit puede manejar mejor llamadas separadas para re-renderizados parciales
        for index, partido_data in enumerate(partidos):
            es_sombreado = index % 2 == 1 # Para sombrear el 2º, 4º, etc. (filas impares del índice)
                                        # Usa `index % 2 == 0` para sombrear el 1º, 3º, etc.
            # Llamar a la función con el argumento 'shaded'
            html_partido = crearHTMLPartido(partido_data, shaded=es_sombreado) 
            st.markdown(html_partido, unsafe_allow_html=True)

def tabFasesFinales(spreadsheet, nombreFase, titulos):
    partidosSemifinalesOro = leerResultadosSemifinales(spreadsheet, nombreFase)
    # --- Mostrar cada partido ---
    if not partidosSemifinalesOro:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        st.markdown(crearHTMLTitulosPartidos(titulos[0]), unsafe_allow_html=True)
        for index, partido_data in enumerate(partidosSemifinalesOro):
            html_partido = crearHTMLPartido(partido_data, shaded=False) 
            st.markdown(html_partido, unsafe_allow_html=True)


    partidosFinalesOro = leerResultadosFinales(spreadsheet, nombreFase)

    # --- Mostrar cada partido ---
    if not partidosFinalesOro:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        htmlTitulos = [crearHTMLTitulosPartidos(titulos[1]), crearHTMLTitulosPartidos(titulos[2])]
        
        for index, partido_data in enumerate(partidosFinalesOro):
            st.markdown(htmlTitulos[index], unsafe_allow_html=True)
            html_partido = crearHTMLPartido(partido_data, shaded=False) 
            st.markdown(html_partido, unsafe_allow_html=True)