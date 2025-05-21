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
    margin-right: 10px; /* Espacio entre el logo y el texto del título */
    /* Opcional: si quieres limitar el tamaño del contenedor del logo */
    /* max-width: 100px; */
}

.cabecera-torneo img.logo-patrocinador {
    display: block; /* Para evitar espacio extra debajo si es inline */
    max-height: 50px; /* 70 antes Ajusta el tamaño máximo del logo */
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
