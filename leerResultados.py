import gspread
import streamlit as st

# --- Función de ayuda crucial ---
def to_int_or_zero(value):
    """
    Convierte un valor a entero. Si el valor es None, una cadena vacía,
    una cadena con solo espacios, o no se puede convertir, devuelve 0.
    """
    if value is None:
        return 0
    if isinstance(value, str):
        value = value.strip()
        if not value: # Si está vacío después de strip
            return 0
    try:
        return int(value)
    except (ValueError, TypeError):
        # Podrías añadir un print de advertencia aquí si quieres loggear conversiones fallidas
        # print(f"Advertencia (to_int_or_zero): No se pudo convertir '{value}' a entero. Usando 0.")
        return 0

@st.cache_data
def leerResultadosSemifinales(_spreadsheet, nombreHoja):
    worksheet = _spreadsheet.worksheet(nombreHoja)
    lista_partidos_completa = []
    rango_resultados_partidos = 'B4:I5'
    rango_penaltis = 'E9:I10'

    try:
        datos_resultados = worksheet.get_values(rango_resultados_partidos)
        datos_penaltis_raw = worksheet.get_values(rango_penaltis)

        if not datos_resultados:
            print("Advertencia: No se encontraron datos en el rango de resultados de partidos.")
            return []

        if not datos_penaltis_raw:
            print("Advertencia: No se encontraron datos en el rango de penaltis. Se asumirán strings vacíos para penaltis.")
            datos_penaltis_raw = [['', '', '', ''] for _ in range(len(datos_resultados))]

        num_partidos_resultados = len(datos_resultados)
        num_partidos_penaltis = len(datos_penaltis_raw)

        for i in range(num_partidos_resultados):
            fila_resultado = datos_resultados[i]

            if len(fila_resultado) < 7:
                print(f"Advertencia: Fila de resultado {i+3} incompleta. Saltando.")
                continue

            # Todos los valores se leen como strings y se limpian
            hora_str = str(fila_resultado[0]).strip()
            campo_str = str(fila_resultado[2]).strip()
            equipo_local_str = str(fila_resultado[3]).strip()
            goles_local_str = str(fila_resultado[4]).strip() # Mantenido como string
            equipo_visitante_str = str(fila_resultado[5]).strip()
            goles_visitante_str = str(fila_resultado[6]).strip() # Mantenido como string

            penaltis_local_str = ""
            penaltis_visitante_str = ""

            if i < num_partidos_penaltis:
                fila_penalti = datos_penaltis_raw[i]
                if len(fila_penalti) >= 4:
                    penaltis_local_str = str(fila_penalti[1]).strip()    # Mantenido como string
                    penaltis_visitante_str = str(fila_penalti[3]).strip()# Mantenido como string

            partido_info = {
                "campo": campo_str,
                "hora": hora_str,
                "equipo_local": equipo_local_str,
                "goles_local": goles_local_str, # Guardado como string
                "equipo_visitante": equipo_visitante_str,
                "goles_visitante": goles_visitante_str, # Guardado como string
                "penaltis_local": penaltis_local_str,   # Guardado como string
                "penaltis_visitante": penaltis_visitante_str # Guardado como string
            }
            
            lista_partidos_completa.append(partido_info)

    except gspread.exceptions.APIError as e:
        print(f"Error de API de Google Sheets al leer resultados: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer resultados: {e}")
        import traceback
        traceback.print_exc()
        return []

    return lista_partidos_completa

@st.cache_data
def leerResultadosFinales(_spreadsheet, nombreHoja):
    worksheet = _spreadsheet.worksheet(nombreHoja)
    lista_partidos_completa = []
    rango_resultados_partidos = 'B14:I15'
    rango_penaltis = 'E19:I20'

    try:
        datos_resultados = worksheet.get_values(rango_resultados_partidos)
        datos_penaltis_raw = worksheet.get_values(rango_penaltis)

        if not datos_resultados:
            print("Advertencia: No se encontraron datos en el rango de resultados de partidos.")
            return []

        if not datos_penaltis_raw:
            print("Advertencia: No se encontraron datos en el rango de penaltis. Se asumirán strings vacíos para penaltis.")
            datos_penaltis_raw = [['', '', '', ''] for _ in range(len(datos_resultados))]

        num_partidos_resultados = len(datos_resultados)
        num_partidos_penaltis = len(datos_penaltis_raw)

        for i in range(num_partidos_resultados):
            fila_resultado = datos_resultados[i]

            if len(fila_resultado) < 7:
                print(f"Advertencia: Fila de resultado {i+3} incompleta. Saltando.")
                continue

            # Todos los valores se leen como strings y se limpian
            hora_str = str(fila_resultado[0]).strip()
            campo_str = str(fila_resultado[2]).strip()
            equipo_local_str = str(fila_resultado[3]).strip()
            goles_local_str = str(fila_resultado[4]).strip() # Mantenido como string
            equipo_visitante_str = str(fila_resultado[5]).strip()
            goles_visitante_str = str(fila_resultado[6]).strip() # Mantenido como string

            penaltis_local_str = ""
            penaltis_visitante_str = ""

            if i < num_partidos_penaltis:
                fila_penalti = datos_penaltis_raw[i]
                if len(fila_penalti) >= 4:
                    penaltis_local_str = str(fila_penalti[1]).strip()    # Mantenido como string
                    penaltis_visitante_str = str(fila_penalti[3]).strip()# Mantenido como string

            partido_info = {
                "campo": campo_str,
                "hora": hora_str,
                "equipo_local": equipo_local_str,
                "goles_local": goles_local_str, # Guardado como string
                "equipo_visitante": equipo_visitante_str,
                "goles_visitante": goles_visitante_str, # Guardado como string
                "penaltis_local": penaltis_local_str,   # Guardado como string
                "penaltis_visitante": penaltis_visitante_str # Guardado como string
            }
            
            lista_partidos_completa.append(partido_info)

    except gspread.exceptions.APIError as e:
        print(f"Error de API de Google Sheets al leer resultados: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer resultados: {e}")
        import traceback
        traceback.print_exc()
        return []

    return lista_partidos_completa

@st.cache_data
def leerResultadosFaseGrupos(_spreadsheet, nombreHoja):
    """
    Lee los datos de partidos y penaltis de una hoja de Google Sheets.
    Los valores se leen como strings. Las celdas vacías resultarán en strings vacíos.
    Se limpian los espacios al principio y al final.

    Args:
        worksheet: Un objeto worksheet de gspread.

    Returns:
        Una lista de diccionarios, donde cada diccionario representa un partido.
    """
    worksheet = _spreadsheet.worksheet(nombreHoja)
    lista_partidos_completa = []
    rango_resultados_partidos = 'B3:I8'
    rango_penaltis = 'E12:I17'

    try:
        datos_resultados = worksheet.get_values(rango_resultados_partidos)
        datos_penaltis_raw = worksheet.get_values(rango_penaltis)

        if not datos_resultados:
            print("Advertencia: No se encontraron datos en el rango de resultados de partidos.")
            return []

        if not datos_penaltis_raw:
            print("Advertencia: No se encontraron datos en el rango de penaltis. Se asumirán strings vacíos para penaltis.")
            datos_penaltis_raw = [['', '', '', ''] for _ in range(len(datos_resultados))]

        num_partidos_resultados = len(datos_resultados)
        num_partidos_penaltis = len(datos_penaltis_raw)

        for i in range(num_partidos_resultados):
            fila_resultado = datos_resultados[i]

            if len(fila_resultado) < 7:
                print(f"Advertencia: Fila de resultado {i+3} incompleta. Saltando.")
                continue

            # Todos los valores se leen como strings y se limpian
            hora_str = str(fila_resultado[0]).strip()
            campo_str = str(fila_resultado[2]).strip()
            equipo_local_str = str(fila_resultado[3]).strip()
            goles_local_str = str(fila_resultado[4]).strip() # Mantenido como string
            equipo_visitante_str = str(fila_resultado[5]).strip()
            goles_visitante_str = str(fila_resultado[6]).strip() # Mantenido como string

            penaltis_local_str = ""
            penaltis_visitante_str = ""

            if i < num_partidos_penaltis:
                fila_penalti = datos_penaltis_raw[i]
                if len(fila_penalti) >= 4:
                    penaltis_local_str = str(fila_penalti[1]).strip()    # Mantenido como string
                    penaltis_visitante_str = str(fila_penalti[3]).strip()# Mantenido como string

            partido_info = {
                "campo": campo_str,
                "hora": hora_str,
                "equipo_local": equipo_local_str,
                "goles_local": goles_local_str, # Guardado como string
                "equipo_visitante": equipo_visitante_str,
                "goles_visitante": goles_visitante_str, # Guardado como string
                "penaltis_local": penaltis_local_str,   # Guardado como string
                "penaltis_visitante": penaltis_visitante_str # Guardado como string
            }
            lista_partidos_completa.append(partido_info)

    except gspread.exceptions.APIError as e:
        print(f"Error de API de Google Sheets al leer resultados: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer resultados: {e}")
        import traceback
        traceback.print_exc()
        return []

    return lista_partidos_completa

# @st.cache_data # Cachear los datos leídos de la hoja
def leerTablaClasificacion(_spreadsheet, nombreHoja):
    """
    Lee los datos de la tabla de clasificación de una hoja de Google Sheets.
    Devuelve los datos como una lista de listas (para st.table o st.dataframe)
    o como un DataFrame de Pandas.

    Args:
        _spreadsheet: El objeto spreadsheet de gspread.
        nombreHoja: El nombre de la hoja dentro del spreadsheet.

    Returns:
        Un diccionario con "cabeceras" (lista) y "datos" (lista de listas),
        o None si ocurre un error o no se encuentran datos.
        Opcionalmente, podría devolver un DataFrame de Pandas.
    """
    try:
        worksheet = _spreadsheet.worksheet(nombreHoja)
        
        # Rango de la tabla de clasificación, incluyendo cabeceras
        # K2:T2 para cabeceras, K3:T6 para datos (ejemplo basado en tu imagen)
        # Ajusta este rango si tu tabla está en otra parte o tiene más/menos filas/columnas
        rango_tabla_clasificacion = 'K2:T6' 
        
        datos_tabla_raw = worksheet.get_values(rango_tabla_clasificacion)

        if not datos_tabla_raw or len(datos_tabla_raw) < 2: # Necesitamos al menos cabeceras y una fila de datos
            print(f"Advertencia: No se encontraron suficientes datos en el rango '{rango_tabla_clasificacion}' para la tabla de clasificación en la hoja '{nombreHoja}'.")
            return None

        cabeceras = datos_tabla_raw[0] # La primera fila son las cabeceras
        datos_filas = datos_tabla_raw[1:] # El resto son las filas de datos

        # Opcional: Limpiar los datos (convertir a string, strip, etc.) si es necesario.
        # Por ahora, los dejamos como los devuelve gspread (generalmente strings).
        # Si necesitas convertir columnas numéricas a números, puedes hacerlo aquí.
        
        # Ejemplo de limpieza y conversión si los números vienen como strings:
        datos_filas_limpias = []
        for fila in datos_filas:
            fila_limpia = []
            for i, valor_celda in enumerate(fila):
                # Si la columna es 'POSICIÓN', 'PUNTOS', 'PJ', 'PG', 'PE', 'PP', 'GF', 'GC', 'DG'
                # podrías intentar convertir a int, pero para st.table/st.dataframe, strings suelen estar bien.
                # Aquí solo hacemos un strip básico.
                fila_limpia.append(str(valor_celda).strip())
            datos_filas_limpias.append(fila_limpia)


        return {
            "cabeceras": cabeceras,
            "datos": datos_filas_limpias # o datos_filas si no haces limpieza explícita
        }

    except gspread.exceptions.WorksheetNotFound:
        print(f"Error: No se encontró la hoja '{nombreHoja}' en el spreadsheet.")
        return None
    except gspread.exceptions.APIError as e:
        print(f"Error de API de Google Sheets al leer la tabla de clasificación: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer la tabla de clasificación: {e}")
        import traceback
        traceback.print_exc()
        return None