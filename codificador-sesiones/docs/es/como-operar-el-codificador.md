# Cómo operar el codificador

Seis cosas que van a hacer con el codificador, en orden de frecuencia. Los roles (líder de
investigación, investigadora, consulta) son los de `_config/equipo.md`.

Regla que atraviesa las seis: **tú decides, el codificador escribe con rastro.** Las categorías,
los cambios al libro de códigos y lo que se concluye de un cruce son decisiones del equipo. El
codificador las escribe con fecha, razón y la cita que las sostiene, para que cualquiera pueda ver
de dónde salió cada cosa.

---

## 1. Codificar una sesión

Después de moderar:

1. Abre el proyecto de la carpeta en Cowork.
2. Di **"codifica la sesión de hoy del grupo 3"** (si está en Fathom) o **"codifica el transcript
   que está en entrada"** (si lo pegaste a mano, ver el punto 2).

El codificador deja la sesión en `estudios/<estudio>/sesiones/` con su resumen, las participantes
(con código, nunca con nombre), la codificación con cita y minuto, lo que quedó sin categoría y las
categorías que propone. La matriz se regenera sola. Revisa la sesión como revisas hoy: si un código
está mal, díselo ("P2 no es deportista, es recreación") y lo corrige.

Varias investigadoras pueden codificar sesiones distintas al mismo tiempo: cada sesión es su propio
archivo.

## 2. Pegar un transcript a mano

Cuando la sesión no está en Fathom (Nota, una transcripción manual):

1. Guarda el texto en un archivo con la fecha y el grupo en el nombre:
   `2026-09-26-g2-grupo-focal.md`.
2. Déjalo en `estudios/<estudio>/sesiones/entrada/`.
3. Di **"codifica el transcript que está en entrada"**.

Si el texto no trae minutos, el codificador usa el más cercano y lo anota.

## 3. Cambiar el libro de códigos

Pídelo en el chat, con la razón:

- **"acepta recreación al aire libre como categoría de actividades"**: entra al libro como
  emergente aceptada y las citas que la sostenían pasan a ser códigos.
- **"retira la categoría X, la estamos partiendo en Y y Z"**: queda retirada con la fecha, y sus
  filas quedan por recodificar.
- **"renombra X a Y"**, **"agrega la variable Z con las categorías A, B y C"**.

Cada cambio queda en el Historial del libro. También puedes editar el libro a mano; si lo haces,
avísale al codificador para que deje la línea en el Historial.

## 4. Cruzar variables

Di **"cruza deporte con alimentación por grupo"**. El cruce va en tres pasos y el codificador se
detiene al final de cada uno:

1. Cuántas participantes caen en cada categoría, por grupo, con el tamaño de cada grupo.
2. Las relaciones que aparecen, cada una con su conteo y tres citas.
3. Qué se sostiene, qué no alcanza y qué hipótesis del estudio toca.

En cada pausa responde qué te parece ("sigue", "junta estas dos categorías para este cruce", "deja
fuera el grupo 1"). Tu respuesta queda escrita en el archivo del cruce. El codificador nunca habla de
causas ni elige los hallazgos: eso es de ustedes.

## 5. Preguntar qué dijo la gente

**"¿Qué dijo la gente del grupo 2 sobre el dinero?"** responde con los conteos por grupo y las
citas, cada una con su sesión y su minuto.

## 6. Correr la prueba de fidelidad

**"Corre la prueba de fidelidad"** codifica una sesión del estudio de ejemplo y la compara con la
codificación que hicieron ustedes a mano. El informe queda en `_ejemplos/<estudio>/salidas/` con el
porcentaje de coincidencia y cada diferencia, para que marquen si fue un error del codificador, un
criterio que no estaba escrito o una mejora aceptable. Córranla cuando cambien los criterios de
calidad o suban un ejemplo nuevo.

---

## Si algo no sale como esperabas

- **No encuentra la carpeta:** abre la carpeta como proyecto en Cowork, o dile cómo se llama en
  Drive.
- **No encuentra la sesión en Fathom:** revisa que la grabación esté compartida con tu cuenta y que
  su título siga la regla de `_config/equipo.md`; si no, pega el transcript en `entrada/`.
- **La matriz no cuadra con las sesiones:** di "regenera la matriz"; se rehace desde los archivos
  de las sesiones.
- **Aparece un archivo con "(1)" en el nombre:** Drive detectó dos cambios al mismo archivo a la
  vez. Dile al codificador cuál quedó bien y él deja una sola versión con el cambio de la otra.
