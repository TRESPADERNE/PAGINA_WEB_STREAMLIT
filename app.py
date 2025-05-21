import streamlit as st
import html
from creaHTML import crear_html_partido, crear_html_clasificacion
from estilosCSS import estilosCSS, estilos_cabecera_css, estilos_logos_finales
from autenticacion import autentica
from leerResultados import leerResultadosFaseGrupos, leerTablaClasificacion


st.markdown(estilos_cabecera_css, unsafe_allow_html=True) # Inyecta todos los estilos


# --- Cabecera ---
ruta_logo_patrocinador = "app/static/logoFundacionCajaBurgos.png"
titulo_linea_1 = "I Torneo BCF CUP Alevín Femenin" # Ajustado para que coincida con tu imagen
titulo_linea_2 = "Fundación Caja de Burgos"      # Ajustado

html_cabecera = f"""
<div class="cabecera-torneo-wrapper"> 
    <div class="logo-patrocinador-container">
        <img src="{ruta_logo_patrocinador}" alt="Logo Patrocinador" class="logo-patrocinador">
    </div>
    <div class="titulo-texto-container">
        <span class="titulo-linea1">{html.escape(titulo_linea_1)}</span>
        <span class="titulo-linea2">{html.escape(titulo_linea_2)}</span>
    </div>
</div>
"""
st.markdown(html_cabecera, unsafe_allow_html=True)


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

    # st.markdown("---") # Separador visual

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

st.markdown(estilos_logos_finales, unsafe_allow_html=True)


# --- SECCIÓN DE LOGOS AL FINAL DE LA PÁGINA ---

# Separador opcional (ahora con menos margen si el CSS de arriba funciona)
st.markdown("---") # Puedes quitarlo si no lo quieres o si el CSS lo hace muy pequeño

# Subheader con clase para control de margen
st.markdown("<div class='subheader-compacto'><h3>Con la colaboración de:</h3></div>", unsafe_allow_html=True)
# Alternativa si st.subheader es más simple, pero el control de margen es por CSS a su wrapper
# st.subheader("Con la colaboración de:") # Y luego intentar apuntar al div de st.subheader


ruta_logo_final_1 = "app/static/molinotejada.png" # Reemplaza con tus nombres de archivo
ruta_logo_final_2 = "app/static/ezsa.png"   # Reemplaza con tus nombres de archivo
alt_logo_1 = "Molino Tejada"
alt_logo_2 = "Ezsa Sanidad Ambiental"


st.markdown(estilos_logos_finales, unsafe_allow_html=True)

# HTML para los logos
html_logos_finales = f"""
<div class="logos-finales-container">
    <img src="{ruta_logo_final_1}" alt="{html.escape(alt_logo_1)}">
    <img src="{ruta_logo_final_2}" alt="{html.escape(alt_logo_2)}">
</div>
"""
st.markdown(html_logos_finales, unsafe_allow_html=True)

st.markdown("---")