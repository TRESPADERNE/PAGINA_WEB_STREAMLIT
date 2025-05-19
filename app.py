import streamlit as st
from html import partidos, estilosCSS, crear_html_partido
from autenticacion import autentica
from googleSheet import leeCelda, clear_leeCelda

if st.session_state.get("contador") is None:
    st.session_state.contador = 0

if st.query_params.get("reset") == "true":  
    clear_leeCelda()
    st.query_params.reset = "false"

st.session_state.contador += 1
spreadsheet = autentica()

worksheet = spreadsheet.worksheet("Hoja 1")  # Cambia el nombre de la hoja según sea necesario
valor = leeCelda(worksheet, 1, 1)  # Cambia la fila y columna según sea necesario
st.write(f"Valor de la celda A1: {valor}")
st.write(f"Contador: {st.session_state.contador}")
st.markdown(estilosCSS, unsafe_allow_html=True)



# --- Título de la App ---
st.subheader("Resultados de Partidos")

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


# --- Notas Adicionales ---
st.markdown("---")
st.caption("Notas:")
st.caption("- Se han ajustado los estilos CSS para pantallas pequeñas (<600px).")
st.caption("- Nombres largos como 'BORUSSIA DORTMUND' ahora deberían mostrarse en dos líneas en móviles.")
st.caption("- Los tamaños de fuente y logos se han reducido en móviles.")