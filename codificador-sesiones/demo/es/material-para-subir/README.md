# Material para subir (demo de la instalación)

> DOCUMENTO FICTICIO: material de demostración. Personas, empresas, datos y citas inventados.

Esto es lo que una investigadora entregaría al instalar el codificador: la plantilla donde vacían
las respuestas, un estudio que ya codificaron a mano, el libro de códigos y el diseño del estudio
de ahora, la guía del moderador y una sesión nueva. Todo en los formatos reales (Excel, Word y el
texto que exporta Fathom), para mostrar la instalación de punta a punta sin tocar nada real.

Es del equipo ficticio **Brújula**. Cuando se instala con este material, el resultado es una carpeta
como la de la demo ya instalada (`demo/es/investigacion/`), pero construida en vivo.

## Qué hay

| Archivo | Qué es | Qué debería pasar al subirlo |
|---|---|---|
| `01-plantilla-descarga-rapida.xlsx` | El Excel que llenan después de cada sesión, con una hoja de instrucciones | Queda intacto en `_config/plantillas/` y de él sale el formato de salida: sus columnas, en su orden, con "Respuesta sintética" como la categoría |
| `02-estudio-anterior-movilidad-2025/` | Tres grupos focales codificados a mano: la matriz en Excel (18 filas y una hoja de categorías), las tres transcripciones de Fathom y los hallazgos | Antes de guardarlo, el codificador detecta que **no está anonimizado**: una participante aparece con nombre en la matriz y en una transcripción, y el cliente aparece en el título de los hallazgos. Lo dice, pregunta, y guarda la versión con códigos. Reconstruye el libro de códigos desde la hoja de categorías y reserva una sesión para la prueba de fidelidad |
| `03-estudio-actual-ocio-familias-2026/` | El libro de códigos en Excel (3 variables, 9 categorías), el diseño del estudio en Word y la guía del grupo G1 | Crea el estudio con su libro de códigos, sus objetivos, sus dos hipótesis y sus dos grupos, y guarda la guía |
| `04-sesion-nueva/OCIO26 G1 grupo focal 2026-09-21.txt` | Un grupo focal recién moderado, sin codificar | Es la primera sesión codificada de la instalación: 8 filas con cita y minuto, y un picnic en el parque que queda sin categoría |

## Cómo se hace la demo

1. En una sesión nueva de Cowork o Claude Code, con el plugin instalado, di:
   **"prueba la instalación del codificador con el material de ejemplo"**.
2. El codificador crea `Investigación (prueba)` en tu Drive, al lado de cualquier carpeta real, y
   hace la entrevista. Responde con el guion de abajo.
3. Cuando pida los formatos y el estudio anterior, dile que están en el material de ejemplo (o
   arrástralos al chat, que es lo que haría una investigadora).
4. Al final codifica la sesión nueva y ofrece la prueba de fidelidad. Acéptala.

## Guion de la entrevista

| Te pregunta | Respondes |
|---|---|
| Quiénes son y qué rol tiene cada una | "Lucía Mora es la directora de investigación y lidera; Sara Quintero y Andrés Pardo son investigadores y moderan; Tomás Rey es estratega y solo consulta." |
| Dónde graban las sesiones | "En Fathom, en el equipo Brújula investigación. Las sesiones empiezan con el código del estudio." |
| En qué idioma son las sesiones | "En español." |
| Cuándo dos respuestas son la misma categoría | "Agrupamos por tipo de actividad, no por actividad: bici y caminar son activo." |
| Cuándo hay una categoría nueva | "Cuando lo dicen al menos dos personas y no cabe en ninguna sin forzarla." |
| Un código bueno y uno malo | "Bueno: tiempo, sobre 'me ahorro casi una hora al día'. Malo: codificar salud sobre 'me gusta llegar despierta'; eso no dice salud." |
| Mínimos para los cruces | "Tres participantes por relación." |
| El nombre sin anonimizar | "Sí, cámbialo por su código." |
