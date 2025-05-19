import gspread

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

def leerResultados(worksheet):
    """
    Lee los datos de partidos y penaltis de una hoja de Google Sheets.
    Los valores se leen como strings. Las celdas vacías resultarán en strings vacíos.
    Se limpian los espacios al principio y al final.

    Args:
        worksheet: Un objeto worksheet de gspread.

    Returns:
        Una lista de diccionarios, donde cada diccionario representa un partido.
    """
    lista_partidos_completa = []
    rango_resultados_partidos = 'B3:H8'
    rango_penaltis = 'E12:H17'

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

# --- Ejemplo de uso (necesitarías tu configuración de gspread antes) ---
if __name__ == '__main__':
    from autenticacion import autentica
    spreadsheet = autentica()

    worksheet = spreadsheet.worksheet("Grupo A")  # Cambia el nombre de la hoja según sea necesario
    partidos = leerResultados( worksheet)

    if partidos:
        for idx, partido in enumerate(partidos):
            print(f"\n--- Partido {idx+1} ---")
            for key, value in partido.items():
                print(f"  {key}: {value}")
    else:
        print("No se pudieron leer los datos de los partidos.")