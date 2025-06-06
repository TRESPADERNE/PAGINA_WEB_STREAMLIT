import streamlit as st

@st.cache_resource
def estiloOCultaCabecera():
    estilos = """
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
    return estilos

@st.cache_resource
def estilosCSSGrupos():
    estilos ="""
    <style>
    /* --- ESTILOS GENERALES Y RESET BÁSICO --- */
    html {
        font-size: 16px;
        box-sizing: border-box;
    }
    *, *:before, *:after {
        box-sizing: inherit;
    }
    body {
        font-family: Arial, sans-serif;
        color: #333;
        margin: 0;
    }

    /* --- CONTENEDOR DEL PARTIDO --- */
    .match-container {
        background-color: #ffffff;
        padding: 4px 4px; /* Fallback para navegadores antiguos */
        padding: clamp(0.25rem, 1vw, 0.5rem) clamp(0.25rem, 1vw, 0.5rem);
        margin-bottom: 0px;
        border-bottom: 1px solid #eee;
    }

    .match-container.shaded {
        background-color: #f0f0f0;
    }

    .match-container:last-child {
        border-bottom: none;
    }

    .datetime {
        text-align: center;
        color: #555;
        margin-bottom: 0.25rem; /* 4px */
        font-weight: bold;
        font-size: 0.85em; /* Fallback */
        font-size: clamp(0.8rem, 2.2vw, 0.9rem);
    }

    .details {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
    }

    .team {
        display: flex;
        align-items: center;
        flex-basis: 39%;
        min-width: 0;
    }

    .team-left {
        justify-content: flex-end;
        text-align: right;
    }

    .team-right {
        justify-content: flex-start;
        text-align: left;
    }

    .team-name {
        font-weight: bold;
        line-height: 1.2;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 150px;
        display: inline-block;
        vertical-align: middle;
        min-width: 0;
        font-size: 0.9em; /* Fallback */
        font-size: clamp(0.85rem, 2.5vw, 0.95rem);
        margin: 0 8px; /* Fallback */
        margin: 0 clamp(0.25rem, 1.5vw, 0.5rem);
    }

    .logo {
        object-fit: contain;
        flex-shrink: 0;
        vertical-align: middle;
        width: 28px; /* Fallback */
        height: 28px; /* Fallback */
        width: clamp(1.375rem, 5vw, 1.75rem);
        height: clamp(1.375rem, 5vw, 1.75rem);
    }

    /* Orden de los logos y nombres (sin cambios) */
    .team-left .team-name { order: 1; }
    .team-left .logo { order: 2; }
    .team-right .logo { order: 1; }
    .team-right .team-name { order: 2; }

    .score {
        font-weight: bold;
        color: #e63946;
        text-align: center;
        flex-basis: 18%;
        flex-shrink: 0;
        font-size: 1.6em; /* Fallback */
        font-size: clamp(1.4rem, 5vw, 1.8rem);
        padding: 0 3px; /* Fallback */
        padding: 0 clamp(0.125rem, 0.5vw, 0.25rem);
        min-width: 50px; /* Fallback */
        min-width: clamp(40px, 10vw, 60px);
    }

    .penalty-score {
        text-align: center;
        color: #4A90E2;
        font-weight: normal;
        clear: both;
        width: 100%;
        margin-top: 0.1875rem; /* 3px */
        font-size: 0.8em; /* Fallback */
        font-size: clamp(0.7rem, 2vw, 0.8rem);
    }

    /* --- TABLA DE CLASIFICACIÓN --- */
    .tabla-clasificacion {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 1.25rem; /* 20px */
        font-size: 0.85em; /* Fallback */
        font-size: clamp(0.75rem, 2.5vw, 0.9rem);
    }

    .tabla-clasificacion th, .tabla-clasificacion td {
        border: 1px solid #ddd;
        text-align: center;
        white-space: nowrap;
        padding: 6px 4px; /* Fallback */
        padding: clamp(0.25rem, 1vw, 0.375rem) clamp(0.125rem, 0.8vw, 0.25rem);
    }

    .tabla-clasificacion th {
        background-color: #004080;
        color: white;
        font-weight: bold;
        padding-top: 8px; /* Fallback */
        padding-bottom: 8px; /* Fallback */
        padding-top: clamp(0.375rem, 1.2vw, 0.5rem);
        padding-bottom: clamp(0.375rem, 1.2vw, 0.5rem);
    }

    .tabla-clasificacion td.col-equipo {
        text-align: left;
        white-space: normal;
    }

    .tabla-clasificacion td.col-equipo .logo-clasificacion {
        object-fit: contain;
        vertical-align: middle;
        display: inline-block;
        width: 20px; /* Fallback */
        height: 20px; /* Fallback */
        width: clamp(1rem, 3.5vw, 1.25rem);
        height: clamp(1rem, 3.5vw, 1.25rem);
        margin-right: 5px; /* Fallback */
        margin-right: clamp(0.1875rem, 1vw, 0.3125rem);
    }

    /* --- MEDIA QUERIES --- */
    /* No es estrictamente necesario añadir fallbacks dentro de las media queries si ya están fuera,
       pero para ser extra seguros y mantener la lógica, se han añadido también. */

    @media (max-width: 600px) {
        .datetime {
            font-size: 14px; /* Fallback para 600px */
            font-size: clamp(0.8125rem, 2.5vw, 0.9375rem);
        }

        .team-name {
            font-size: 15px; /* Fallback para 600px */
            font-size: clamp(0.875rem, 3.2vw, 1rem);
            margin: 0 5px; /* Fallback */
            margin: 0 clamp(0.25rem, 1.2vw, 0.375rem);
            white-space: normal;
            overflow: visible;
            text-overflow: clip;
            max-width: none;
            line-height: 1.2;
        }

        .logo {
            width: 26px; /* Fallback para 600px */
            height: 26px; /* Fallback */
            width: clamp(1.375rem, 5.5vw, 1.75rem);
            height: clamp(1.375rem, 5.5vw, 1.75rem);
        }

        .score {
            font-size: 26px; /* Fallback para 600px */
            font-size: clamp(1.5rem, 6vw, 1.875rem);
            min-width: 55px; /* Fallback */
            min-width: clamp(50px, 12vw, 60px);
            flex-basis: 20%;
        }

        .penalty-score {
            font-size: 13px; /* Fallback para 600px */
            font-size: clamp(0.8rem, 2.2vw, 0.9rem);
        }

        .tabla-clasificacion {
            font-size: 14px; /* Fallback para 600px */
            font-size: clamp(0.8125rem, 2.5vw, 0.9375rem);
        }
        .tabla-clasificacion th, .tabla-clasificacion td {
            padding: 6px 4px; /* Fallback para 600px */
            padding: clamp(0.3125rem, 1vw, 0.4375rem) clamp(0.1875rem, 0.8vw, 0.3125rem);
        }
        .tabla-clasificacion td.col-equipo .logo-clasificacion {
            width: 20px; /* Fallback para 600px */
            height: 20px; /* Fallback */
            width: clamp(1.125rem, 4vw, 1.375rem);
            height: clamp(1.125rem, 4vw, 1.375rem);
        }
    }

    @media (max-width: 380px) {
        .datetime {
            font-size: 12px; /* Fallback para <380px */
            font-size: clamp(0.75rem, 2.8vw, 0.85rem);
        }
        .team-name {
            font-size: 12px; /* Fallback para <380px */
            font-size: clamp(0.75rem, 3.2vw, 0.875rem);
        }
        .logo {
            width: 18px; /* Fallback para <380px */
            height: 18px; /* Fallback */
            width: clamp(1.125rem, 5vw, 1.375rem);
            height: clamp(1.125rem, 5vw, 1.375rem);
        }
        .score {
            font-size: 22px; /* Fallback para <380px */
            font-size: clamp(1.375rem, 5.5vw, 1.625rem);
            min-width: 45px; /* Fallback */
            min-width: clamp(45px, 11vw, 55px);
        }
        .penalty-score {
            font-size: 11.2px; /* Fallback para <380px */
            font-size: clamp(0.7rem, 2.2vw, 0.8rem);
        }

        .tabla-clasificacion {
            font-size: 11.2px; /* Fallback para <380px */
            font-size: clamp(0.7rem, 2.5vw, 0.8125rem);
        }
        .tabla-clasificacion th, .tabla-clasificacion td {
            padding: 4px 2px; /* Fallback para <380px */
            padding: clamp(0.25rem, 0.8vw, 0.3125rem) clamp(0.125rem, 0.5vw, 0.1875rem);
        }
        .tabla-clasificacion td.col-equipo .logo-clasificacion {
            width: 16px; /* Fallback para <380px */
            height: 16px; /* Fallback */
            width: clamp(1rem, 3.2vw, 1.125rem);
            height: clamp(1rem, 3.2vw, 1.125rem);
        }
    }

    </style>
    """
    return estilos

# En tu archivo donde defines estilosCSS.py o directamente en app.py

@st.cache_resource
def estilosCSSCabecera():
    estilos = """
    <style>
    /* === ESTILOS CABECERA === */
    .cabecera-torneo-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 0px;
        margin-top: 0px;
    }

    .cabecera-torneo-wrapper .logo-patrocinador-container {
        display: flex;
        justify-content: center;
        align-items: center; /* Alinea los logos verticalmente por su centro */
        gap: 25px; /* Espacio entre los logos, ajusta si es necesario */
        margin-bottom: 10px; /* Espacio entre logos y título */
    }

    /* ESTILO PRINCIPAL PARA LOS LOGOS DE LA CABECERA */
    .cabecera-torneo-wrapper img.logo-patrocinador {
        height: 90px;  /* ALTURA FIJA para ambos logos en escritorio */
        width: auto;   /* El ancho se ajustará para mantener la proporción */
        object-fit: contain; /* Asegura que la imagen quepa sin distorsión */
        vertical-align: middle; /* Ayuda a la alineación vertical dentro del flex item */
    }

    .cabecera-torneo-wrapper .titulo-texto-container {
        text-align: center;
        line-height: 1.3;
    }

    .cabecera-torneo-wrapper .titulo-linea1 {
        font-size: 1.3em; 
        font-weight: bold;
        color: #004080;
        display: block;
    }

    .cabecera-torneo-wrapper .titulo-linea2 {
        font-size: 1.3em; 
        font-weight: bold;
        color: #004080;
        display: block;
    }

    .cabecera-torneo-wrapper::after {
        content: "";
        display: block;
        width: 100%; 
        height: 8px;
        background-color: #004080;
        margin-top: 10px; 
    }

    /* === ESTILOS PARA EL SEPARADOR HR ANTES DE LOS TABS === */
    hr.st-hr { 
        margin-top: 10px !important;    
        margin-bottom: 0px !important; 
        border: none !important;
        border-top: 1px solid #dddddd !important; 
        height: 1px !important;
    }

    /* === MEDIA QUERY PARA MÓVILES === */
    @media (max-width: 600px) {
        .cabecera-torneo-wrapper img.logo-patrocinador {
            height: 75px; /* ALTURA FIJA REDUCIDA para móviles */
        }
        .cabecera-torneo-wrapper .logo-patrocinador-container {
            gap: 15px; /* Espacio reducido entre logos en móviles */
        }
        .cabecera-torneo-wrapper .titulo-linea1,
        .cabecera-torneo-wrapper .titulo-linea2 {
            font-size: 1.15em; /* Tamaño de fuente del título reducido para móviles */
        }
        .cabecera-torneo-wrapper::after {
            margin-top: 8px;
        }
        hr.st-hr {
            margin-top: 8px !important;
        }
    }


    </style>
    """
    return estilos

@st.cache_resource
def estilosCSSResultadosFases():
    estilos = """
    <style>
    /* === ESTILOS CABECERA === */
    .resultadosFases-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 10px;
    }


    .resultadosFases-wrapper .titulo-texto-container {
        text-align: center;
        line-height: 1.3;
    }

    .resultadosFases-wrapper .titulo-linea {
        font-size: 1.3em; 
        font-weight: bold;
        color: #004080;
        display: block;
    }

    .resultadosFases-wrapper::before {
        content: "";
        display: block;
        width: 100%; 
        height: 2px;
        background-color: #004080;
        margin-top: 5px; 
        margin-bottom: 5px; 
    }

    .resultadosFases-wrapper::after {
        content: "";
        display: block;
        width: 100%; 
        height: 2px;
        background-color: #004080;
        margin-top: 5px; 
        margin-bottom: 5px; 
    }


    /* === MEDIA QUERY PARA MÓVILES === */
    @media (max-width: 600px) 
        .resultadosFases-wrapper .titulo-linea {
            font-size: 1.15em; /* Tamaño de fuente del título reducido para móviles */
        }
        .resultadosFases-wrapper::after {
            margin-top: 2px;
            margin-bottom: 2px;
        }
        .resultadosFases-wrapper::before {
            margin-top: 2px;
            margin-bottom: 2px;
        }
        hr.st-hr {
            margin-top: 8px !important;
        }
    }


    </style>
    """
    return estilos


@st.cache_resource
def estilosCSSLogosFinales():
    estilos = """
    <style>
    /* Contenedor para el subheader "Con la colaboración de:" */
    .custom-hr-dentro-html {
    border: 0;
        height: 1px;
        background-color: #ccc; /* Color de la línea, ajusta según necesites */
        margin-top: 5px !important;    /* Espacio encima de la línea */
        margin-bottom: 10px !important; /* Espacio debajo de la línea */
    }
    .subheader-compacto {
        margin-top: -10px !important; /* Reduce el espacio inferior del subheader */
        margin-bottom: 5px !important; /* Reduce el espacio inferior del subheader */
        /* Puedes ajustar el margin-top también si es necesario */
        /* margin-top: 10px !important; */
    }
    .subheader-compacto h3 { /* Apunta al h3 dentro del subheader */
        margin-bottom: 0px !important; /* Quita el margen inferior del h3 mismo */
        padding-bottom: 0px !important;
        font-size: 1.2em; /* Opcional: ajustar tamaño si el subheader es muy grande */
    }

    /* Para el separador st.markdown("---") si lo usas */
    hr.st-emotion-cache-1sbq2qa.e1tzin5v0 { /* Esta clase puede cambiar, necesitas inspeccionar */
        margin-top: -30px !important;
        # margin-bottom: -10px !important;
    }

    /* Contenedor de logos finales si usas st.columns y quieres ajustar márgenes del div interno */
    .logo-column-content {
        /* padding-top: 0px !important; */ /* Ejemplo, si st.columns añade padding */
        /* padding-bottom: 0px !important; */
        margin-top: 0px !important;
        margin-bottom: 0px !important;
    }

    /* Si usaste la Opción 2 (HTML/CSS) para los logos finales: */
    .logos-finales-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        /* padding: 20px 0; */ /* Valor anterior */
        padding: 5px 0;   /* REDUCIDO: Padding vertical para el contenedor de logos */
        flex-wrap: wrap;
    }
    .logos-finales-container img {
        max-width: 160px;  /* Puedes ajustar esto */
        max-height: 90px; /* Puedes ajustar esto */
        object-fit: contain;
        /* margin: 10px 15px; */ /* Valor anterior */
        margin: 5px 10px;    /* REDUCIDO: Espacio alrededor de cada logo */
    }
    </style>
    """
    return estilos

@st.cache_resource
def estilosCSSTabs():
    estilos = '''
    <style>
        /* Estilo original para el texto de las pestañas */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 17px; /* Ajusta el tamaño de fuente de los títulos de las pestañas */
            font-weight: bold; /* Pone los títulos en negrita */
        }

        /* --- NUEVA REGLA PARA REDUCIR EL ESPACIO SUPERIOR --- */
        /* Apunta al contenedor principal del componente de pestañas de Streamlit */
        .stTabs {
            margin-top: -0px !important; /* Reduce el margen superior. Prueba con 0px primero. */
            /* Puedes ajustar este valor según sea necesario.
            Si 0px no es suficiente, prueba con un valor negativo pequeño, por ejemplo:
            margin-top: -10px !important;
            Ten cuidado con los valores negativos, ya que podrían causar solapamiento
            con el elemento de arriba si la línea gruesa no tiene suficiente espacio.
            Un valor positivo pequeño como 5px también podría ser una opción si 0px es demasiado ajustado:
            margin-top: 5px !important;
            */

            /* Alternativamente, si el espacio fuera un padding interno del contenedor de pestañas: */
            /* padding-top: 0px !important; */
            /* Pero margin-top es más probable para el espacio entre componentes. */
        }
    </style>
    '''
    return estilos


def inyectaEstilos():
    # Inyección de estilos CSS
    st.markdown(estiloOCultaCabecera(), unsafe_allow_html=True)
    st.markdown(estilosCSSCabecera(), unsafe_allow_html=True)  # Inyecta todos los estilos
    st.markdown(estilosCSSGrupos(), unsafe_allow_html=True)
    st.markdown(estilosCSSResultadosFases(), unsafe_allow_html=True)
    st.markdown(estilosCSSLogosFinales(), unsafe_allow_html=True)
    st.markdown(estilosCSSTabs(), unsafe_allow_html=True)