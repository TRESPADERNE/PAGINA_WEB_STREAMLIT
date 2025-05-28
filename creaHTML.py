import html # Para html.escape
import streamlit as st

@st.cache_resource
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
        return "app/static/logo_I_BCF_CUP.png"
    
    
@st.cache_resource
def crearHTMLCabecera():
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
    return html_cabecera

@st.cache_data # Ahora la caché considerará 'partido' y 'shaded'
def crearHTMLPartido(partido, shaded=False): # <--- AÑADIDO parámetro 'shaded'
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

@st.cache_resource
def crearHTMLTitulosPartidos(titulo):
    htmlTitulo = f"""
    <div class="resultadosFases-wrapper"> 
        <div class="titulo-texto-container">
            <span class="titulo-linea">{titulo}</span>
        </div>
    </div>
    """
    return htmlTitulo

#@st.cache_resource
def crearHTMLLogosFinales():
    ruta_logo_final_1 = "app/static/molinotejada.png"
    ruta_logo_final_2 = "app/static/ezsa.png"
    ruta_logo_final_3 = "app/static/nb.jpg"
    ruta_logo_final_4 = "app/static/diputacion.jpg"
    alt_logo_1 = "Molino Tejada"
    alt_logo_2 = "Ezsa Sanidad Ambiental"
    alt_logo_3 = "Grupo NB"
    alt_logo_4 = "Diputación de Burgos"

    # HTML para los logos, incluyendo un <hr> personalizado
    html_logos_finales = f"""
    <hr class="custom-hr-dentro-html"> 
    <div class='subheader-compacto'><h3>Con la colaboración de:</h3></div>
    <div class="logos-finales-container">
        <img src="{ruta_logo_final_1}" alt="{html.escape(alt_logo_1)}">
        <img src="{ruta_logo_final_2}" alt="{html.escape(alt_logo_2)}">
    </div>
    <div class="logos-finales-container">
        <img src="{ruta_logo_final_3}" alt="{html.escape(alt_logo_1)}">
        <img src="{ruta_logo_final_4}" alt="{html.escape(alt_logo_2)}">
    </div>
    """
    return html_logos_finales

