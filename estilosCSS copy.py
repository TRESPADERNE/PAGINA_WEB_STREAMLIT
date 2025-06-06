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
        font-size: 16px; /* Base para unidades rem, ajusta si tu base es diferente */
        box-sizing: border-box;
    }
    *, *:before, *:after {
        box-sizing: inherit;
    }
    body {
        font-family: Arial, sans-serif;
        color: #333;
        margin: 0; /* Buena práctica */
    }

    /* --- CONTENEDOR DEL PARTIDO --- */
    .match-container {
        background-color: #ffffff;
        /* padding: 4px 4px; -> Se ajustará con clamp */
        padding: clamp(0.25rem, 1vw, 0.5rem) clamp(0.25rem, 1vw, 0.5rem); /* ej: 4px 4px */
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
        /* font-size: 0.85em; -> clamp(0.8rem, 2.2vw, 0.9rem) */
        font-size: clamp(0.8rem, 2.2vw, 0.9rem); /* ej: 13.6px, escala, max 14.4px */
        color: #555;
        /* margin-bottom: 4px; -> rem */
        margin-bottom: 0.25rem; /* 4px */
        font-weight: bold;
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
        flex-basis: 39%; /* Se mantendrá y ajustará con el espacio disponible */
        /* min-width: 0; Podría ser útil si los nombres de equipo causan problemas de desbordamiento */
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
        /* font-size: 0.9em; -> clamp(0.85rem, 2.5vw, 0.95rem) */
        font-size: clamp(0.85rem, 2.5vw, 0.95rem); /* ej: 13.6px, escala, max 15.2px */
        /* margin: 0 8px; -> rem */
        margin: 0 clamp(0.25rem, 1.5vw, 0.5rem); /* ej: 0 4px a 0 8px */
        line-height: 1.2;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 150px; /* Límite para que ellipsis funcione en desktop */
        display: inline-block; /* Para que max-width y ellipsis funcionen con nowrap */
        vertical-align: middle;
        min-width: 0; /* Ayuda a Flexbox a manejar texto largo */
    }

    .logo {
        /* width: 28px; height: 28px; -> clamp */
        width: clamp(1.375rem, 5vw, 1.75rem); /* ej: 22px, escala, max 28px */
        height: clamp(1.375rem, 5vw, 1.75rem);
        object-fit: contain;
        flex-shrink: 0;
        vertical-align: middle;
    }

    /* Orden de los logos y nombres (sin cambios) */
    .team-left .team-name { order: 1; }
    .team-left .logo { order: 2; }
    .team-right .logo { order: 1; }
    .team-right .team-name { order: 2; }

    .score {
        /* font-size: 1.6em; -> clamp(1.4rem, 5vw, 1.8rem) */
        font-size: clamp(1.4rem, 5vw, 1.8rem); /* ej: 22.4px, escala, max 28.8px */
        font-weight: bold;
        color: #e63946;
        text-align: center;
        /* padding: 0 3px; -> rem o clamp */
        padding: 0 clamp(0.125rem, 0.5vw, 0.25rem); /* ej: 0 2px a 0 4px */
        flex-basis: 18%; /* Aumentado un poco, antes 16% y luego 18% en móvil. Podríamos hacerlo dinámico con clamp(min-width) */
        min-width: clamp(40px, 10vw, 60px); /* Darle un ancho mínimo flexible */
        flex-shrink: 0;
    }

    .penalty-score {
        text-align: center;
        /* font-size: 0.8em; -> clamp(0.7rem, 2vw, 0.8rem) */
        font-size: clamp(0.7rem, 2vw, 0.8rem); /* ej: 11.2px, escala, max 12.8px */
        color: #4A90E2;
        font-weight: normal;
        /* margin-top: 3px; -> rem */
        margin-top: 0.1875rem; /* 3px */
        clear: both; /* Mantenido por si acaso, aunque con flex no debería ser necesario */
        width: 100%;
    }

    /* --- TABLA DE CLASIFICACIÓN --- */
    .tabla-clasificacion {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 1.25rem; /* 20px */
        /* font-size: 0.85em; -> clamp */
        font-size: clamp(0.75rem, 2.5vw, 0.9rem); /* ej: 12px, escala, max 14.4px */
    }

    .tabla-clasificacion th, .tabla-clasificacion td {
        border: 1px solid #ddd;
        /* padding: 6px 4px; -> clamp */
        padding: clamp(0.25rem, 1vw, 0.375rem) clamp(0.125rem, 0.8vw, 0.25rem); /* ej: 4px 2px a 6px 4px */
        text-align: center;
        white-space: nowrap;
    }

    .tabla-clasificacion th {
        background-color: #004080;
        color: white;
        font-weight: bold;
        /* padding-top: 8px; padding-bottom: 8px; -> se maneja con el padding general de th/td o se puede refinar */
        padding-top: clamp(0.375rem, 1.2vw, 0.5rem);    /* ej: 6px a 8px */
        padding-bottom: clamp(0.375rem, 1.2vw, 0.5rem);
    }

    .tabla-clasificacion td.col-equipo {
        text-align: left;
        white-space: normal; /* Permitir multilínea para nombres de equipo */
    }

    .tabla-clasificacion td.col-equipo .logo-clasificacion {
        /* width: 20px; height: 20px; -> clamp */
        width: clamp(1rem, 3.5vw, 1.25rem); /* ej: 16px, escala, max 20px */
        height: clamp(1rem, 3.5vw, 1.25rem);
        object-fit: contain;
        vertical-align: middle;
        /* margin-right: 5px; -> rem */
        margin-right: clamp(0.1875rem, 1vw, 0.3125rem); /* ej: 3px a 5px */
        display: inline-block;
    }


    /* --- MEDIA QUERIES --- */

    /* Tablets pequeñas y móviles grandes en landscape (ej. hasta 768px) */
    @media (max-width: 768px) {
        /* Los valores de clamp ya deberían estar haciendo un buen trabajo aquí.
        Puedes añadir overrides si algo específico necesita ser diferente
        fuera de los rangos de clamp para este breakpoint. */

        .team-name {
            /* Si los nombres aún son muy largos y el ellipsis no es suficiente,
            podrías forzar white-space: normal aquí antes que en móviles más pequeños.
            white-space: normal;
            overflow: visible;
            text-overflow: clip;
            max-width: none; */
        }
    }

    @media (max-width: 600px) {
        .match-container {
            /* Padding ya es fluido, pero si necesitas un mínimo mayor: */
            /* padding: clamp(0.4rem, 1.5vw, 0.5rem) clamp(0.3rem, 1vw, 0.375rem); */
        }

        .datetime {
            font-size: clamp(0.8125rem, 2.5vw, 0.9375rem); /* MIN: 13px, MAX: 15px */
            margin-bottom: 0.375rem; /* 6px */
        }

        .team {
            flex-basis: 39%; /* O ajusta según sea necesario */
        }

        .team-name {
            /* MIN: 13.6px (0.85rem) a 14px (0.875rem), PREFERRED puede ser 3vw o 3.2vw */
            font-size: clamp(0.875rem, 3.2vw, 1rem); /* MIN: 14px, MAX: 16px */
            /* 3.2vw de 393px = 12.57px -> se irá al MIN de 14px */
            margin: 0 clamp(0.25rem, 1.2vw, 0.375rem); /* ej: 0 4px a 0 6px */
            white-space: normal;
            overflow: visible;
            text-overflow: clip;
            max-width: none;
            line-height: 1.2; /* Un poco más de espacio entre líneas si se rompe */
        }

        .logo {
            /* MIN: 22px (1.375rem) a 24px (1.5rem) */
            width: clamp(1.375rem, 5.5vw, 1.75rem); /* MIN: 22px, MAX: 28px */
            height: clamp(1.375rem, 5.5vw, 1.75rem);
            /* 5.5vw de 393px = 21.6px -> se irá al MIN de 22px */
        }

        .score {
            /* MIN: 24px (1.5rem) a 26px (1.625rem) */
            font-size: clamp(1.5rem, 6vw, 1.875rem); /* MIN: 24px, MAX: 30px */
            /* 6vw de 393px = 23.58px -> se irá al MIN de 24px */
            min-width: clamp(50px, 12vw, 60px);
            padding: 0 clamp(0.125rem, 0.5vw, 0.25rem);
            flex-basis: 20%;
        }

        .penalty-score {
            font-size: clamp(0.8rem, 2.2vw, 0.9rem); /* MIN: 12.8px, MAX: 14.4px */
            margin-top: 0.1875rem; /* 3px */
        }

        /* Tabla de Clasificación en móviles medianos */
        .tabla-clasificacion {
            font-size: clamp(0.8125rem, 2.5vw, 0.9375rem); /* MIN: 13px, MAX: 15px */
        }
        .tabla-clasificacion th, .tabla-clasificacion td {
            padding: clamp(0.3125rem, 1vw, 0.4375rem) clamp(0.1875rem, 0.8vw, 0.3125rem); /* MIN: 5px 3px, MAX: 7px 5px */
        }
        .tabla-clasificacion td.col-equipo .logo-clasificacion {
            /* MIN: 18px (1.125rem) a 20px (1.25rem) */
            width: clamp(1.125rem, 4vw, 1.375rem); /* MIN: 18px, MAX: 22px */
            height: clamp(1.125rem, 4vw, 1.375rem);
            margin-right: clamp(0.25rem, 1vw, 0.3125rem);
        }
    }

    /* Móviles más pequeños (ej. para anchos POR DEBAJO de ~380px, AFECTARÁ A XIAOMI A1/A3) */
    /* ¡SI ESTO SE VE BIEN EN XIAOMI, NO LO TOQUES MUCHO! */
    @media (max-width: 380px) {
        .datetime {
            /* Original de la propuesta anterior: clamp(0.75rem, 2.5vw, 0.85rem) */
            /* Si 12px es bueno, mantenlo o ajusta mínimamente */
            font-size: clamp(0.75rem, 2.8vw, 0.85rem); /* MIN: 12px. 2.8vw de 360px = 10.08px -> 12px */
        }
        .team-name {
            /* Original: clamp(0.75rem, 3vw, 0.85rem); MIN: 12px */
            font-size: clamp(0.75rem, 3.2vw, 0.875rem); /* MIN: 12px. 3.2vw de 360px = 11.52px -> 12px. MAX: 14px */
        }
        .logo {
            /* Original: clamp(1.125rem, 4.5vw, 1.375rem); MIN: 18px */
            width: clamp(1.125rem, 5vw, 1.375rem); /* MIN: 18px. 5vw de 360px = 18px. MAX: 22px */
            height: clamp(1.125rem, 5vw, 1.375rem);
        }
        .score {
            /* Original: clamp(1.25rem, 5vw, 1.5rem); MIN: 20px */
            font-size: clamp(1.375rem, 5.5vw, 1.625rem); /* MIN: 22px. 5.5vw de 360px = 19.8px -> 22px. MAX: 26px */
            min-width: clamp(45px, 11vw, 55px); /* 11vw de 360 = 39.6px -> 45px */
        }
        .penalty-score {
            /* Original: clamp(0.7rem, 2vw, 0.8rem); MIN: 11.2px */
            font-size: clamp(0.7rem, 2.2vw, 0.8rem); /* MIN: 11.2px. 2.2vw de 360 = 7.92px -> 11.2px */
        }

        .tabla-clasificacion {
            /* Original: clamp(0.7rem, 2.2vw, 0.8rem); MIN: 11.2px */
            font-size: clamp(0.7rem, 2.5vw, 0.8125rem); /* MIN: 11.2px. 2.5vw de 360 = 9px -> 11.2px. MAX: 13px */
        }
        .tabla-clasificacion th, .tabla-clasificacion td {
            /* Original: padding: clamp(0.1875rem, 0.8vw, 0.25rem) clamp(0.1rem, 0.5vw, 0.125rem); */
            padding: clamp(0.25rem, 0.8vw, 0.3125rem) clamp(0.125rem, 0.5vw, 0.1875rem); /* MIN: 4px 2px */
        }
        .tabla-clasificacion td.col-equipo .logo-clasificacion {
            /* Original: clamp(1rem, 3vw, 1.125rem); MIN: 16px */
            width: clamp(1rem, 3.2vw, 1.125rem);   /* MIN: 16px. 3.2vw de 360 = 11.52px -> 16px. MAX: 18px */
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