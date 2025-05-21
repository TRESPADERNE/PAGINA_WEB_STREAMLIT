import html # Para html.escape
import streamlit as st

# ------------- Estilos CSS -------------
estilosCSS ="""
<style>
.match-container {
    background-color: #ffffff; /* Fondo por defecto (para el que no está sombreado) */
    padding: 4px 4px;
    margin-bottom: 0px;
    font-family: Arial, sans-serif;
    color: #333;
    border-bottom: 1px solid #eee;
    box-sizing: border-box;
}

/* Clase para el sombreado sutil */
.match-container.shaded {
    background-color: #f0f0f0; /* Un gris muy, muy claro y sutil */
}
/* O si quieres que el que NO está sombreado tenga el fondo, y el otro sea blanco:
.match-container {
    background-color: #f7f7f7;
}
.match-container.unshaded { // Necesitarías añadir esta clase al otro
    background-color: #ffffff;
}
*/


.match-container:last-child {
    border-bottom: none;
}

.datetime {
    text-align: center;
    font-size: 0.85em;
    color: #555;
    /* margin-bottom: 12px; */ /* Reducimos el margen inferior */
    margin-bottom: 4px;     /* Nuevo margen inferior más compacto */
    font-weight: bold;
}

.details {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    box-sizing: border-box;
}

.team {
    display: flex;
    align-items: center;
    /* flex-basis: 38%; */ /* Mantenemos, pero el espacio se reducirá por el padding general */
    /* Podríamos ajustar a 39% o 40% si queremos dar un poco más a los equipos
       ahora que el padding general del match-container es menor */
    flex-basis: 39%;
    box-sizing: border-box;
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
    font-size: 0.9em;
    margin: 0 8px; /* Mantenemos este margen entre logo y nombre */
    line-height: 1.2;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 150px; /* Ajusta si es necesario con el nuevo padding */
    display: inline-block;
    vertical-align: middle;
}

.logo {
    width: 28px;
    height: 28px;
    object-fit: contain;
    flex-shrink: 0;
    vertical-align: middle;
}

.team-left .team-name { order: 1; }
.team-left .logo { order: 2; }
.team-right .logo { order: 1; }
.team-right .team-name { order: 2; }

.score {
    font-size: 1.6em;
    font-weight: bold;
    color: #e63946;
    text-align: center;
    /* min-width: 70px; */ /* El flex-basis debería controlar esto */
    padding: 0 3px;    /* Padding horizontal reducido para el marcador */
    flex-basis: 16%;   /* Reducimos un poco para compensar el padding reducido y dar más a los equipos */
    flex-shrink: 0;
    box-sizing: border-box;
}

.penalty-score {
    text-align: center;
    font-size: 0.8em;
    color: #4A90E2;
    font-weight: normal;
    margin-top: 3px; /* Reducido ligeramente */
    clear: both;
    width: 100%;
}

/* Media Query para móviles */
@media (max-width: 600px) {
    .match-container {
        /* padding: 10px 5px; */ /* Ya está bastante compacto arriba, pero podemos ajustar más si es necesario */
        padding: 8px 5px;
    }
    .datetime {
        margin-bottom: 6px; /* Aún más compacto en móviles */
        font-size: 0.8em;
    }
    .team {
        /* flex-basis: 37%; */ /* Ajustamos de nuevo */
        flex-basis: 38%;
    }
    .team-name {
        font-size: 0.8em; /* Mantenemos o reducimos un poco más si es necesario */
        margin: 0 4px;
        white-space: normal;
        overflow: visible;
        text-overflow: clip;
        max-width: none;
        line-height: 1.15;
    }
    .logo {
        width: 22px;
        height: 22px;
    }
    .score {
        font-size: 1.4em;
        /* min-width: 55px; */
        padding: 0 2px;
        flex-basis: 18%; /* Ajustamos para móviles */
    }
    .penalty-score {
        font-size: 0.7em; /* Un poco más pequeño */
        margin-top: 2px;
    }
}
/* Estilos para la tabla de clasificación */
.tabla-clasificacion {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px; /* Espacio debajo de la tabla */
    font-size: 0.85em; /* Tamaño de fuente base para la tabla */
}

.tabla-clasificacion th, .tabla-clasificacion td {
    border: 1px solid #ddd;
    padding: 6px 4px; /* Padding reducido para celdas */
    text-align: center; /* Centrar por defecto */
    white-space: nowrap; /* Evitar que el texto salte de línea por defecto */
}

.tabla-clasificacion th {
    background-color: #004080; /* Azul oscuro para cabeceras */
    color: white;
    font-weight: bold;
    padding-top: 8px;
    padding-bottom: 8px;
}

/* Alineación específica para la columna de Equipo */
.tabla-clasificacion td.col-equipo {
    text-align: left;
    white-space: normal; /* Permitir que el nombre del equipo salte de línea si es largo */
}
.tabla-clasificacion td.col-equipo .logo-clasificacion {
    width: 20px; /* Tamaño de logo más pequeño para la tabla */
    height: 20px;
    object-fit: contain;
    vertical-align: middle;
    margin-right: 5px;
    display: inline-block; /* Para que el margen funcione bien */
}

/* Estilos para hacerla responsive si es necesario */
@media (max-width: 600px) {
    .tabla-clasificacion {
        font-size: 0.75em; /* Fuente más pequeña en móviles */
    }
    .tabla-clasificacion th, .tabla-clasificacion td {
        padding: 4px 2px; /* Padding aún más reducido */
    }
    .tabla-clasificacion td.col-equipo .logo-clasificacion {
        width: 18px;
        height: 18px;
        margin-right: 3px;
    }
    /* Podrías ocultar columnas menos importantes en móviles si es necesario */
    /* .tabla-clasificacion .col-pj, .tabla-clasificacion .col-pe { display: none; } */
    /* .tabla-clasificacion th:nth-child(4), .tabla-clasificacion td:nth-child(4) { display: none; } */ /* PJ */
}

</style>
"""

estilos_cabecera_css = """
<style>
.cabecera-torneo {
    display: flex;
    align-items: center; /* Centrar verticalmente el logo y el bloque de texto */
    padding: 10px 0;    /* Espaciado vertical */
    border-bottom: 2px solid #004080; /* O el color que prefieras */
    margin-bottom: 20px; /* Espacio debajo de la cabecera */
    width: 100%;
}

.cabecera-torneo .logo-patrocinador-container {
    flex-shrink: 0; /* Para que el logo no se encoja */
    margin-right: 15px; /* Espacio entre el logo y el texto del título */
    /* Opcional: si quieres limitar el tamaño del contenedor del logo */
    /* max-width: 100px; */
}

.cabecera-torneo img.logo-patrocinador {
    display: block; /* Para evitar espacio extra debajo si es inline */
    max-height: 70px; /* Ajusta el tamaño máximo del logo */
    width: auto;      /* Para mantener la proporción */
}

.cabecera-torneo .titulo-texto-container {
    text-align: left; /* El texto dentro de este contenedor se alinea a la izquierda */
    line-height: 1.3; /* Espaciado entre las dos líneas del título */
    /* flex-grow: 1; */ /* Para que ocupe el espacio restante (opcional, puede no ser necesario) */
}

.cabecera-torneo .titulo-linea1 {
    font-size: 1.4em; /* Tamaño para la primera línea */
    font-weight: bold;
    color: #004080; /* Color para el título */
    display: block; /* Asegura que sea un bloque para ocupar su línea */
}

.cabecera-torneo .titulo-linea2 {
    font-size: 1.4em; /* Tamaño para la primera línea */
    font-weight: bold;
    color: #004080; /* Color para el título */
    display: block; /* Asegura que sea un bloque para ocupar su línea */
}

/* Ajustes para pantallas más pequeñas si son necesarios */
/* En este caso, como queremos mantener la disposición, los ajustes serían mínimos */
@media (max-width: 600px) {
    .cabecera-torneo img.logo-patrocinador {
        max-height: 55px; /* Logo un poco más pequeño en móviles */
        margin-right: 10px; /* Menos espacio */
    }
    .cabecera-torneo .titulo-linea1 {
        font-size: 1.2em;
    }
    .cabecera-torneo .titulo-linea2 {
        font-size: 1.0em;
    }
    .cabecera-torneo {
        padding: 8px 0;
    }
}
</style>
"""

@st.cache_data
def cargaLogo(nombre_equipo_original):
    if nombre_equipo_original == "CD Palencia FF":
        return "app/static/palencia.jpg"
    elif nombre_equipo_original == "Mullier FCN":
        return "app/static/mullier.png"
    elif nombre_equipo_original == "CD Parquesol":
        return "app/static/parquesol.png"
    elif nombre_equipo_original == "Burgos CF" or nombre_equipo_original == 'Burgos CF "B"':
        return "app/static/burgoscf.png"
    elif nombre_equipo_original == "Real Valladolid CF":
        return "app/static/valladolid.png"
    elif nombre_equipo_original == "CD San José":
        return "app/static/sanjose.png"
    elif nombre_equipo_original == "Gimnástica Segoviana":
        return "app/static/segoviana.png"
    else:
        raise ValueError(f"Logo no encontrado para el equipo: {nombre_equipo_original}")
    
    
@st.cache_data # Ahora la caché considerará 'partido' y 'shaded'
def crear_html_partido(partido, shaded=False): # <--- AÑADIDO parámetro 'shaded'
    """
    Genera el bloque HTML para un partido.
    Añade una clase 'shaded' al contenedor principal si shaded es True.
    """
    # --- DEBUG ---
    # print(f"--- CREAR_HTML_PARTIDO RECIBE: {partido}, shaded={shaded} ---")
    # --- FIN DEBUG ---

    html_generado_final = ""
    clase_sombreado_str = " shaded" if shaded else "" # Determinar la clase basada en el parámetro

    try:
        # Obtener valores del diccionario
        campo_raw = partido.get('campo', '')
        hora_raw = partido.get('hora', '')
        equipo_local_raw = partido.get('equipo_local', 'Local')
        logo_local = cargaLogo(equipo_local_raw) # cargaLogo ya está cacheada
        equipo_visitante_raw = partido.get('equipo_visitante', 'Visitante')
        logo_visitante = cargaLogo(equipo_visitante_raw) # cargaLogo ya está cacheada

        goles_local_str = partido.get('goles_local', '')
        goles_visitante_str = partido.get('goles_visitante', '')
        penaltis_local_str = partido.get('penaltis_local', '')
        penaltis_visitante_str = partido.get('penaltis_visitante', '')

        # Escapar strings
        campo_safe = html.escape(str(campo_raw))
        hora_safe = html.escape(str(hora_raw))
        equipo_local_safe = html.escape(str(equipo_local_raw))
        equipo_visitante_safe = html.escape(str(equipo_visitante_raw))

        # Display de goles (mostrar "" si está vacío, o "0" si prefieres)
        goles_local_display = goles_local_str if goles_local_str else "" 
        goles_visitante_display = goles_visitante_str if goles_visitante_str else ""
        
        # Mostrar bloque de penaltis
        mostrar_bloque_penaltis = bool(penaltis_local_str or penaltis_visitante_str)
        html_penaltis_render_str = ""
        if mostrar_bloque_penaltis:
            penaltis_local_display = penaltis_local_str if penaltis_local_str else "0"
            penaltis_visitante_display = penaltis_visitante_str if penaltis_visitante_str else "0"
            html_penaltis_render_str = f"""<div class="penalty-score">({penaltis_local_display} - {penaltis_visitante_display})</div>"""

        fecha_hora_render = f"Campo {campo_safe} - {hora_safe}"
        
        team_left_html = f"""<div class="team team-left"><span class="team-name">{equipo_local_safe}</span><img src="{logo_local}" alt="{equipo_local_safe}" class="logo"></div>"""
        score_html = f"""<div class="score"><span class="score-number">{goles_local_display}</span><span class="score-separator">-</span><span class="score-number">{goles_visitante_display}</span>{html_penaltis_render_str}</div>"""
        team_right_html = f"""<div class="team team-right"><img src="{logo_visitante}" alt="{equipo_visitante_safe}" class="logo"><span class="team-name">{equipo_visitante_safe}</span></div>"""

        # Se añade clase_sombreado_str al div principal
        html_generado_final = f"""
        <div class="match-container{clase_sombreado_str}"> 
            <div class="datetime">{fecha_hora_render}</div>
            <div class="details">
                {team_left_html}
                {score_html}
                {team_right_html}
            </div>
        </div>
        """
    except Exception as e:
        error_partido_str = str(partido)
        error_partido_str_safe = ""
        try:
            error_partido_str_safe = html.escape(error_partido_str)
        except:
            error_partido_str_safe = error_partido_str + " (Error al escapar datos del partido para mensaje)"

        print(f"ERROR GRAVE al crear HTML para el partido: {partido}, shaded={shaded}")
        print(f"Excepción: {e}")
        import traceback
        traceback.print_exc()
        # Añadir también la clase de sombreado al div de error para consistencia si se desea
        html_generado_final = f"<div class='match-container{clase_sombreado_str}' style='color:red; border:1px solid red; padding:10px;'>Error procesando datos del partido: {html.escape(str(e))}.<br>Datos: {error_partido_str_safe}</div>"
    
    return html_generado_final

@st.cache_data
def crear_html_clasificacion(clasificacion_data, usar_logos=False, alias_equipos=None):
    """
    Genera el HTML para una tabla de clasificación.

    Args:
        clasificacion_data (dict): Diccionario con "cabeceras" (list) y "datos" (list of lists).
        usar_logos (bool): Si es True, intenta mostrar logos junto al nombre del equipo.
        alias_equipos (dict): Un diccionario para mapear nombres completos de equipos a alias.
                              Ej: {"Burgos CF": "BCF", "CD Parquesol": "PAR"}

    Returns:
        str: La cadena HTML de la tabla.
    """
    if not clasificacion_data or not clasificacion_data.get("cabeceras") or not clasificacion_data.get("datos"):
        return "<p>No hay datos de clasificación para mostrar.</p>"

    cabeceras = clasificacion_data["cabeceras"]
    datos_filas = clasificacion_data["datos"]
    
    if alias_equipos is None:
        alias_equipos = {}

    html_tabla = "<div class='tabla-clasificacion-container' style='overflow-x: auto;'>" # Para scroll horizontal en móviles si es muy ancha
    html_tabla += "<table class='tabla-clasificacion'>"
    
    # Cabecera de la tabla
    html_tabla += "<thead><tr>"
    for i, cabecera in enumerate(cabeceras):
        # Asignar clases a las cabeceras para posible ocultación en CSS
        clase_col = f"col-{cabecera.lower().replace('ó', 'o').replace(' ', '_')}" # ej. col-posición, col-pj
        html_tabla += f"<th class='{clase_col}'>{html.escape(cabecera)}</th>"
    html_tabla += "</tr></thead>"
    
    # Cuerpo de la tabla
    html_tabla += "<tbody>"
    for fila_datos in datos_filas:
        html_tabla += "<tr>"
        for i, celda_valor_raw in enumerate(fila_datos):
            celda_valor_safe = html.escape(str(celda_valor_raw))
            clase_col_td = f"col-{cabeceras[i].lower().replace('ó', 'o').replace(' ', '_')}"

            if cabeceras[i].upper() == "EQUIPO": # Columna de Equipo
                nombre_equipo = str(celda_valor_raw).strip()
                nombre_a_mostrar = alias_equipos.get(nombre_equipo, nombre_equipo) # Usar alias si existe
                nombre_a_mostrar_safe = html.escape(nombre_a_mostrar)
                
                logo_html = ""
                if usar_logos:
                    try:
                        ruta_logo = cargaLogo(nombre_equipo) # cargaLogo ya está cacheada
                        if ruta_logo:
                            logo_html = f"<img src='{ruta_logo}' alt='{nombre_a_mostrar_safe}' class='logo-clasificacion'>"
                    except ValueError: # Si cargaLogo lanza error por logo no encontrado
                        logo_html = "" # No mostrar logo si no se encuentra

                html_tabla += f"<td class='col-equipo {clase_col_td}'>{logo_html}{nombre_a_mostrar_safe}</td>"
            else: # Otras columnas (Posición, Puntos, PJ, etc.)
                html_tabla += f"<td class='{clase_col_td}'>{celda_valor_safe}</td>"
        html_tabla += "</tr>"
    html_tabla += "</tbody></table>"
    html_tabla += "</div>" # Cierre de tabla-clasificacion-container
    
    return html_tabla