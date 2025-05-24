import streamlit as st
import html
from creaHTML import crear_html_partido, crear_html_clasificacion
from estilosCSS import estilosCSS, estilos_cabecera_css, estilos_logos_finales, estilos_resultadosFases
from autenticacion import autentica
from leerResultados import leerResultadosFaseGrupos, leerTablaClasificacion, leerResultadosSemifinales, leerResultadosFinales

# st.logo("static/logo_I_bcfcup_fem.png") # Cambia la ruta según tu estructura de carpetas
st.markdown(estilos_cabecera_css, unsafe_allow_html=True) # Inyecta todos los estilos


# --- Cabecera ---
ruta_logo_torneo = "app/static/logo_I_BCF_CUP.png"
ruta_logo_patrocinador = "app/static/logoFundacionCajaBurgos.png"
titulo_linea_1 = "I Torneo BCF CUP Alevín Femenino" # Ajustado para que coincida con tu imagen
titulo_linea_2 = "Fundación Caja de Burgos"      # Ajustado


html_cabecera = f"""
<div class="cabecera-torneo-wrapper"> 
    <div class="logo-patrocinador-container">
        <img src="{ruta_logo_torneo}" alt="Logo Torneo BCF Cup" class="logo-patrocinador logo-torneo">  
        <img src="{ruta_logo_patrocinador}" alt="Logo Fundación Caja Burgos" class="logo-patrocinador logo-fundacion"> 
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


st.markdown(estilos_resultadosFases, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["**Grupo A**", "**Grupo B**", "**Fase Oro**", "**Fase Plata**"])
cssTabs = '''
<style>
    /* --- ESTILOS BASE DE TUS PESTAÑAS --- */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 17px;
        font-weight: bold;
        /* Añadimos transición para suavizar cambios de color en el texto */
        transition: color 0.2s ease-in-out, transform 0.1s ease-in-out;
    }

    /* --- REDUCIR ESPACIO SUPERIOR (como antes) --- */
    .stTabs {
        margin-top: 0px !important; /* O el valor que te funcionó mejor */
    }

    /* --- MEJORAS DE "AFFORDANCE" PARA LAS PESTAÑAS --- */

    /* 1. Estilo general para cada botón de pestaña */
    .stTabs [data-baseweb="tab"] {
        cursor: pointer; /* Asegura el cursor de mano */
        padding-top: 10px; /* Más espacio vertical dentro del botón de la pestaña */
        padding-bottom: 10px;
        padding-left: 15px; /* Más espacio horizontal */
        padding-right: 15px;
        border-radius: 6px 6px 0 0; /* Bordes superiores redondeados para un look más "tab" */
        transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
        /* Quitamos el borde inferior por defecto si lo tuviera para que solo se vea el de st.tabs */
        border-bottom-color: transparent !important;
    }

    /* 2. Efecto Hover para pestañas NO activas */
    /* Cuando el ratón pasa sobre una pestaña que NO está seleccionada */
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover {
        background-color: #f0f2f6; /* Un gris muy claro para indicar hover */
    }
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover p {
        /* Cambia el color del texto al color que usas para la pestaña activa,
           para indicar que se volverá así si se hace clic.
           Usa el mismo color rojo que tienes para 'Grupo B' y 'Fase Oro' en tu imagen.
           Asumo que es algo como #FF4B4B (el rojo de Streamlit) o similar.
           Si tu color rojo es diferente, ajústalo.
        */
        color: #FF4B4B; /* O el color exacto que usas para las pestañas activas rojas */
    }

    /* 3. Distinción para la pestaña ACTIVA */
    /* Streamlit ya pone el borde inferior de color.
       Si quieres, puedes añadir un fondo muy sutil a la pestaña activa. */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        /* background-color: #e6f2ff; /* Ejemplo: Un azul muy pálido si el color activo fuera azul */
        /* En tu caso, la pestaña activa tiene el texto rojo y una línea roja debajo.
           Podrías darle un fondo muy, muy claro, o dejarlo como está.
           Si tu "Fase Oro" activa tiene un fondo específico, ponlo aquí.
           Por ejemplo, si fuera un rojo muy pálido:
           background-color: #ffebee;
        */
    }
    /* El texto de la pestaña activa (ej. "Grupo B", "Fase Oro" en tu imagen)
       ya tiene un color distintivo (rojo). Ya está bien así. */

    /* 4. Hacer las pestañas NO activas un poco menos prominentes (opcional) */
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) p {
        /* color: #4F4F4F; /* Un gris oscuro en lugar de negro puro */
        opacity: 0.85; /* Ligeramente transparentes para dar más énfasis a la activa */
    }
    /* Al hacer hover sobre una no activa, recupera la opacidad total */
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover p {
        opacity: 1;
    }

    /* 5. (Opcional) Sutil efecto de "presionado" al hacer clic */
    .stTabs [data-baseweb="tab"]:active p { /* Mientras se está presionando el botón */
        transform: translateY(1px) scale(0.98); /* Se mueve ligeramente hacia abajo y se achica */
    }

</style>
'''


st.markdown(cssTabs, unsafe_allow_html=True)
with tab1:
    partidosGA = leerResultadosFaseGrupos(spreadsheet, "Grupo A")
    clasificacionGA = leerTablaClasificacion(spreadsheet, "Grupo A")

    if clasificacionGA:
        # Opciones para la tabla de clasificación:
        usar_logos_en_tabla = True # Cambia a False si prefieres solo texto
        mapeo_alias_equipos = {
            "Burgos CF": "BUR",
            "CD Parquesol": "PAR",
            "Mullier FCN": "MUL",
            "CD Palencia FF": "PAL"
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
    partidosGB = leerResultadosFaseGrupos(spreadsheet, "Grupo B")
    clasificacionGB = leerTablaClasificacion(spreadsheet, "Grupo B")

    if clasificacionGB:
        # Opciones para la tabla de clasificación:
        usar_logos_en_tabla = True # Cambia a False si prefieres solo texto
        mapeo_alias_equipos = {
            'Burgos CF "B"': "BURB",
            "Gimnástica Segoviana": "GSEG",
            "Real Valladolid CF": "RVAL",
            "CD San José": "SJOS"
            # Añade más alias según necesites
        }
        # Descomenta la siguiente línea si no quieres usar alias
        # mapeo_alias_equipos = None 

        html_tabla_clasif = crear_html_clasificacion(
            clasificacionGB,
            usar_logos=usar_logos_en_tabla,
            alias_equipos=mapeo_alias_equipos
        )
        st.markdown(html_tabla_clasif, unsafe_allow_html=True)
    else:
        st.warning("No se pudieron cargar los datos de clasificación para el Grupo B.")

    # st.markdown("---") # Separador visual

    # --- Mostrar cada partido ---
    if not partidosGB:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        # Generar todo el HTML junto para evitar múltiples llamadas a st.markdown si es posible
        # html_completo = "".join([crear_html_partido(p) for p in partidos])
        # st.markdown(html_completo, unsafe_allow_html=True)
        # Nota: Streamlit puede manejar mejor llamadas separadas para re-renderizados parciales
        for index, partido_data in enumerate(partidosGB):
            es_sombreado = index % 2 == 1 # Para sombrear el 2º, 4º, etc. (filas impares del índice)
                                        # Usa `index % 2 == 0` para sombrear el 1º, 3º, etc.
            # Llamar a la función con el argumento 'shaded'
            html_partido = crear_html_partido(partido_data, shaded=es_sombreado) 
            st.markdown(html_partido, unsafe_allow_html=True)

with tab3:
    htmlSemifinales = f"""
<div class="resultadosFases-wrapper"> 
    <div class="titulo-texto-container">
        <span class="titulo-linea">Semifinales</span>
    </div>
</div>
"""
    htmlFinal = f"""
<div class="resultadosFases-wrapper"> 
    <div class="titulo-texto-container">
        <span class="titulo-linea">Final</span>
    </div>
</div>
"""

    html3y4 = f"""
<div class="resultadosFases-wrapper"> 
    <div class="titulo-texto-container">
        <span class="titulo-linea">Tercer y Cuarto Puesto</span>
    </div>
</div>
"""
    partidosSemifinalesOro = leerResultadosSemifinales(spreadsheet, "Fase Oro")

    # --- Mostrar cada partido ---
    if not partidosSemifinalesOro:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        st.markdown(htmlSemifinales, unsafe_allow_html=True)
        for index, partido_data in enumerate(partidosSemifinalesOro):
            es_sombreado = index % 2 == 1 # Para sombrear el 2º, 4º, etc. (filas impares del índice)
                                        # Usa `index % 2 == 0` para sombrear el 1º, 3º, etc.
            # Llamar a la función con el argumento 'shaded'
            html_partido = crear_html_partido(partido_data, shaded=es_sombreado) 
            st.markdown(html_partido, unsafe_allow_html=True)


    partidosFinalesOro = leerResultadosFinales(spreadsheet, "Fase Oro")

    # --- Mostrar cada partido ---
    if not partidosFinalesOro:
        st.warning("No hay datos de partidos para mostrar.")
    else:
        titulo = [htmlFinal, html3y4]
        
        for index, partido_data in enumerate(partidosFinalesOro):
            st.markdown(titulo[index], unsafe_allow_html=True)
            es_sombreado = index % 2 == 1 # Para sombrear el 2º, 4º, etc. (filas impares del índice)
                                        # Usa `index % 2 == 0` para sombrear el 1º, 3º, etc.
            # Llamar a la función con el argumento 'shaded'
            html_partido = crear_html_partido(partido_data, shaded=False) 
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