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

# En tu archivo donde defines estilosCSS.py o directamente en app.py

estilos_cabecera_css = """
<style>
/* === ESTILOS CABECERA === */
.cabecera-torneo-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 0px;
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

/* === ESTILOS PARA EL SEPARADOR HR ANTES DE LOS TABS === */
hr.st-hr { 
    margin-top: 10px !important;    
    margin-bottom: 0px !important; 
    border: none !important;
    border-top: 1px solid #dddddd !important; 
    height: 1px !important;
}

/* === MEDIA QUERY PARA MÓVILES === */
@media (max-width: 600px) 
    .resultadosFases-wrapper .titulo-linea {
        font-size: 1.15em; /* Tamaño de fuente del título reducido para móviles */
    }
    .cabecera-torneo-wrapper::after {
        margin-top: 2px;
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