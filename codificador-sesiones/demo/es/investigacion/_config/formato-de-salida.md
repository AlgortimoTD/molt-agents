# Formato de salida

> DOCUMENTO FICTICIO: estudio de demostración. Personas, datos y citas inventados.

Origen: `_config/plantillas/descarga-rapida.csv` (2025-11-03), revisado con Lucía Mora el 2026-09-15.

## Columnas de la matriz

La matriz es un CSV con encabezado, UTF-8, separado por comas, que abre en Excel. Cada fila es
un código: una participante, una variable, una categoría y la cita que la sostiene. Si una
participante dijo dos cosas que caen en dos categorías de la misma variable, son dos filas.

| Columna | Qué lleva | Clave |
|---|---|---|
| estudio | el código del estudio | study |
| sesion | el identificador de la sesión (nombre del archivo sin .md) | session |
| fecha | fecha de la sesión, AAAA-MM-DD | date |
| grupo | el grupo objetivo, como lo nombra el estudio | group |
| participante | el código de la participante (o "participante no identificado"), nunca su nombre | participant |
| variable | la variable del libro de códigos | variable |
| categoria | la categoría del libro | category |
| cita | la frase textual, entre comillas, sin recortar el sentido | quote |
| minuto | el minuto como lo da el transcript (0:42, 12:40, 1:05:10), desde el inicio de la grabación | minute |
| estado | codificada o por recodificar | state |
| nota | cita dudosa, minuto aproximado, u otra aclaración corta, sin nombres de nadie | note |

La columna **Clave** no se cambia: es cómo las skills saben qué columna es cuál. El nombre de la
columna y su orden sí se pueden cambiar para que coincidan con el Excel del equipo.

## Cómo se escribe una cita

- Textual, en el idioma en que se dijo, con las muletillas si cambian el sentido y sin ellas si
  no.
- Entre comillas dobles en el archivo de la sesión; en la matriz, la celda lleva solo el texto.
- Lo que se omite va como `(...)`.
- Lo bastante larga para entenderse sola, lo bastante corta para caber en una celda: una a tres
  frases.

## Cómo se nombra una categoría

- En minúscula inicial salvo nombres propios, en sustantivo o adjetivo corto: "deportista",
  "recreación", "motivación personal".
- Una categoría nueva se nombra por lo que agrupa, no por la primera respuesta que la trajo.

## Cómo se identifica a una participante

- Código por sesión: P1, P2, ... en el orden en que hablan por primera vez en la sesión.
- Nunca el nombre, ni en la matriz ni en las citas.
