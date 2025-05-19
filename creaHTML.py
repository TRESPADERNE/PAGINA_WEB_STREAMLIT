import html # Para html.escape

# ------------- Estilos CSS -------------
estilosCSS ="""
<style>
.match-container {
    background-color: #ffffff;
    padding: 15px 10px;
    margin-bottom: 0px;
    font-family: Arial, sans-serif;
    color: #333;
    border-bottom: 1px solid #eee;
    box-sizing: border-box;
}
.match-container:last-child {
    border-bottom: none;
    margin-bottom: 10px;
}
.datetime {
    text-align: center;
    font-size: 0.85em;
    color: #555;
    margin-bottom: 12px;
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
    flex-basis: 38%;
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
    margin: 0 8px;
    line-height: 1.2;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 150px;
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
    min-width: 70px;
    padding: 0 5px;
    flex-basis: 18%;
    flex-shrink: 0;
    box-sizing: border-box;
}
.penalty-score {
    text-align: center;
    font-size: 0.8em;
    color: #4A90E2;
    font-weight: normal;
    margin-top: 4px;
    clear: both;
    width: 100%;
}
/* .penalty-score span {} */ /* Sin estilos específicos por ahora */
.separator {
    text-align: center;
    color: #aaa;
    margin-top: 10px;
    font-weight: bold;
    display: none;
}
@media (max-width: 600px) {
    .match-container {
        padding: 10px 5px;
    }
    .details {
        flex-wrap: nowrap;
    }
    .team {
        flex-basis: 37%;
    }
    .team-name {
        font-size: 0.8em;
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
        min-width: 55px;
        padding: 0 3px;
        flex-basis: 20%;
    }
    .penalty-score {
        font-size: 0.75em;
        margin-top: 3px;
    }
    .datetime {
        font-size: 0.8em;
        margin-bottom: 10px;
    }
}
</style>
"""


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
        return ""
        raise ValueError(f"Logo no encontrado para el equipo: {nombre_equipo_original}")
    
    

def crear_html_partido(partido):
    """
    Genera el bloque HTML para un partido.
    Espera que todos los valores del diccionario 'partido' sean strings o None.
    Los goles/penaltis vacíos se mostrarán como "0".
    """
    # --- INICIO DE DEPURACIÓN ---
    # Descomenta para ver los datos crudos que llegan a esta función para cada partido
    # print(f"--- CREAR_HTML_PARTIDO RECIBE: {partido} ---")
    # --- FIN DE DEPURACIÓN ---

    html_generado_final = ""
    try:
        # Obtener valores del diccionario, usando string vacío como default si la clave no existe o es None
        campo_raw = partido.get('campo', '')
        hora_raw = partido.get('hora', '')
        equipo_local_raw = partido.get('equipo_local', 'Local')
        logo_local = cargaLogo(equipo_local_raw)
        equipo_visitante_raw = partido.get('equipo_visitante', 'Visitante')
        logo_visitante = cargaLogo(equipo_visitante_raw)

        goles_local_str = partido.get('goles_local', '')
        goles_visitante_str = partido.get('goles_visitante', '')
        penaltis_local_str = partido.get('penaltis_local', '')
        penaltis_visitante_str = partido.get('penaltis_visitante', '')

        # Escapar strings que van como contenido textual HTML o atributos 'alt'
        campo_safe = html.escape(str(campo_raw)) # Forzar a str por si acaso antes de escapar
        hora_safe = html.escape(str(hora_raw))
        equipo_local_safe = html.escape(str(equipo_local_raw))
        equipo_visitante_safe = html.escape(str(equipo_visitante_raw))

        # Para la presentación en HTML: mostrar "0" si el string de gol/penalti está vacío
        goles_local_display = goles_local_str if goles_local_str else ""
        goles_visitante_display = goles_visitante_str if goles_visitante_str else ""
        
        # Determinar si se debe mostrar el bloque de penaltis
        # Se muestran si ALGUNA de las celdas de penaltis tenía contenido
        mostrar_bloque_penaltis = bool(penaltis_local_str or penaltis_visitante_str)

        html_penaltis_render_str = ""
        if mostrar_bloque_penaltis:
            penaltis_local_display = penaltis_local_str if penaltis_local_str else "0"
            penaltis_visitante_display = penaltis_visitante_str if penaltis_visitante_str else "0"
            html_penaltis_render_str = f"""<div class="penalty-score">({penaltis_local_display} - {penaltis_visitante_display})</div>"""

        fecha_hora_render = f"Campo {campo_safe} - {hora_safe}"
        
        # Construcción del HTML final
        # Usamos variables intermedias para las partes más complejas por claridad
        team_left_html = f"""<div class="team team-left"><span class="team-name">{equipo_local_safe}</span><img src="{logo_local}" alt="{equipo_local_safe}" class="logo"></div>"""
        score_html = f"""<div class="score"><span class="score-number">{goles_local_display}</span><span class="score-separator">-</span><span class="score-number">{goles_visitante_display}</span>{html_penaltis_render_str}</div>"""
        team_right_html = f"""<div class="team team-right"><img src="{logo_visitante}" alt="{equipo_visitante_safe}" class="logo"><span class="team-name">{equipo_visitante_safe}</span></div>"""

        html_generado_final = f"""
        <div class="match-container">
            <div class="datetime">{fecha_hora_render}</div>
            <div class="details">
                {team_left_html}
                {score_html}
                {team_right_html}
            </div>
        </div>
        """
    except Exception as e:
        error_partido_str = str(partido) # Convertir a string para escapar
        try:
            # Intentar escapar el string del partido para el mensaje de error
            error_partido_str_safe = html.escape(error_partido_str)
        except:
            # Si el escapado del error falla, usar el string crudo (muy improbable)
            error_partido_str_safe = error_partido_str + " (Error al escapar datos del partido para mensaje)"

        print(f"ERROR GRAVE al crear HTML para el partido: {partido}")
        print(f"Excepción: {e}")
        import traceback
        traceback.print_exc()
        html_generado_final = f"<div style='color:red; border:1px solid red; padding:10px;'>Error procesando datos del partido: {html.escape(str(e))}.<br>Datos: {error_partido_str_safe}</div>"
    
    # --- DEBUG HTML FINAL ---
    # Descomenta y ajusta la condición para ver el HTML de un partido específico
    # (Asegúrate de que 'equipo_visitante_raw' existe en este punto si la usas en la condición)
    # if equipo_visitante_raw == "Mullier FCN": # Ejemplo
    #    print(f"--- HTML FINAL GENERADO ({partido.get('equipo_local', '')} vs {partido.get('equipo_visitante', '')}):\n{html_generado_final}\n---")

    return html_generado_final

