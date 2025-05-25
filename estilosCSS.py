# ------------- Estilos CSS -------------
estilosCSS ="""
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

/* Móviles medianos (tu breakpoint original, ajustado un poco si es necesario) */
@media (max-width: 600px) {
    .match-container {
        /* padding ya es fluido. Si necesitas más compacto: */
        /* padding: clamp(0.375rem, 1.5vw, 0.5rem) clamp(0.25rem, 1vw, 0.3125rem); /* ej: 6px 4px */
    }

    .datetime {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* font-size: clamp(0.75rem, 2vw, 0.8rem); */
        margin-bottom: 0.375rem; /* 6px */
    }

    .team {
        flex-basis: 38%; /* Se puede mantener este ajuste o dejar que flexbox y min-width de score decidan */
    }

    .team-name {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* font-size: clamp(0.75rem, 2.8vw, 0.85rem); */
        margin: 0 clamp(0.1875rem, 1vw, 0.25rem); /* ej: 0 3px a 0 4px */
        white-space: normal; /* Importante: permitir que el texto se divida en líneas */
        overflow: visible;
        text-overflow: clip;
        max-width: none; /* Permitir que el texto use el espacio disponible en flex */
        line-height: 1.15;
    }

    .logo {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* width: clamp(1.25rem, 4.5vw, 1.5rem); ej: 20px a 24px */
        /* height: clamp(1.25rem, 4.5vw, 1.5rem); */
    }

    .score {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* font-size: clamp(1.3rem, 4.5vw, 1.6rem); */
        /* min-width: clamp(35px, 8vw, 50px); */
        padding: 0 clamp(0.1rem, 0.4vw, 0.125rem); /* ej: 0 1.5px a 0 2px */
        flex-basis: 20%; /* Puede necesitar más espacio si los nombres de equipo se encogen */
    }

    .penalty-score {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* font-size: clamp(0.65rem, 1.8vw, 0.75rem); */
        margin-top: 0.125rem; /* 2px */
    }

    /* Tabla de Clasificación en móviles medianos */
    .tabla-clasificacion {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* font-size: clamp(0.7rem, 2.2vw, 0.8rem); */
    }
    .tabla-clasificacion th, .tabla-clasificacion td {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* padding: clamp(0.1875rem, 0.8vw, 0.25rem) clamp(0.0625rem, 0.5vw, 0.125rem); ej: 3px 1px a 4px 2px */
    }
    .tabla-clasificacion td.col-equipo .logo-clasificacion {
        /* El clamp ya debería ajustarse. Si quieres forzar más pequeño: */
        /* width: clamp(0.9375rem, 3vw, 1.125rem); ej: 15px a 18px */
        /* height: clamp(0.9375rem, 3vw, 1.125rem); */
        /* margin-right: clamp(0.125rem, 0.8vw, 0.1875rem); ej: 2px a 3px */
    }
    /* Ocultar columnas menos importantes en móviles (mantenido como comentario) */
    /* .tabla-clasificacion .col-pj, .tabla-clasificacion .col-pe { display: none; } */
    /* .tabla-clasificacion th:nth-child(4), .tabla-clasificacion td:nth-child(4) { display: none; } */ /* PJ */
}

/* Móviles más pequeños (ej. hasta 480px) */
@media (max-width: 480px) {
    /* Aquí los valores MÍNIMOS de clamp serán los más relevantes.
       Ajusta los valores base de clamp si ves que algo queda demasiado grande/pequeño. */

    .team {
        flex-basis: 37%; /* Podrías necesitar ajustar los flex-basis más agresivamente */
    }
    .score {
        flex-basis: 22%;
        /* Asegurar que el score no sea demasiado pequeño */
        font-size: clamp(1.2rem, 4vw, 1.4rem); /* Ajusta el mínimo de clamp si es necesario */
    }
    .team-name {
        /* Asegurar que el nombre no sea demasiado pequeño */
        font-size: clamp(0.7rem, 2.5vw, 0.8rem); /* Ajusta el mínimo de clamp */
    }
    .logo {
        width: clamp(1.125rem, 4vw, 1.25rem); /* 18px a 20px */
        height: clamp(1.125rem, 4vw, 1.25rem);
    }

    /* Ajustes finos para la tabla en móviles muy pequeños */
    .tabla-clasificacion {
        font-size: clamp(0.65rem, 2vw, 0.75rem); /* ej: 10.4px, escala, max 12px */
    }
     .tabla-clasificacion th, .tabla-clasificacion td {
        padding: clamp(0.125rem, 0.6vw, 0.1875rem) clamp(0.05rem, 0.4vw, 0.1rem); /* ej: 2px ~1px a 3px ~1.5px */
    }
    .tabla-clasificacion td.col-equipo .logo-clasificacion {
        width: clamp(0.875rem, 2.8vw, 1rem); /* 14px a 16px */
        height: clamp(0.875rem, 2.8vw, 1rem);
    }
}

</style>
"""

# En tu archivo donde defines estilosCSS.py o directamente en app.py

estilos_cabecera_css = """
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

estilos_resultadosFases = """
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
# Estilos CSS para los logos finales (puedes añadir esto a tu string estilosCSS principal
# o inyectarlo aquí si solo se usa para esta sección)
estilos_logos_finales = """
<style>
/* Contenedor para el subheader "Con la colaboración de:" */
.subheader-compacto {
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
    margin-top: 5px !important;
    margin-bottom: 5px !important;
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