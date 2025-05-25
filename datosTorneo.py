import streamlit as st

@st.cache_data
def denominacionesFase():
    return ["Grupo A", "Grupo B", "Fase Oro", "Fase Plata"]

@st.cache_data
def aliasEquipos():
    mapeo = {
            "Burgos CF": "BUR",
            "CD Parquesol": "PAR",
            "Mullier FCN": "MUL",
            "CD Palencia FF": "PAL",
            'Burgos CF "B"': "BURB",
            "Gimnástica Segoviana": "GSEG",
            "Real Valladolid CF": "RVAL",
            "CD San José": "SJOS"
        }
    
    return mapeo