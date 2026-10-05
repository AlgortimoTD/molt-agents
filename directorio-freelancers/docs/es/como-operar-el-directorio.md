# Cómo operar el directorio

Seis cosas que vas a necesitar hacer y que nadie debería tener que preguntar. Están en orden
de frecuencia: la primera pasa cada vez que hay una producción, la última casi nunca. Los
roles (coordinación de producción, aprueba altas y bajas, consulta) son los de la tabla de
roles de `_config/empresa.md` de esta carpeta.

Regla que atraviesa las seis: **las fichas son tuyas y el directorio relee antes de
escribir**. Puedes corregir una ficha en el chat o abrirla en Drive y editarla a mano; el
directorio vuelve a leerla antes de tocarla, y el texto que reemplaza pasa a su
`## Historial` con la fecha. Nada se borra. Lo único que te pide es que, cuando edites a
mano, se lo digas en el chat ("corregí la ficha de Ariel"), para que archive la versión
anterior y nada quede sin rastro.

---

## 1. Armar una producción

Desde que llega el pedido hasta que una persona queda confirmada.

### Abrir la solicitud

Dile al directorio, en el chat del proyecto, lo que le dirías a un colega:

> "Necesito un fotógrafo mañana a las 7:00 para las vigas del puente nuevo en la vía norte,
> exige curso de seguridad en obra."

Si falta algo (la hora de fin, cuántas personas, el lugar), te lo pregunta antes de armar
nada. Con eso escribe un archivo nuevo en `solicitudes/` con la fecha y el nombre de la
producción, y te muestra:

- **Requisitos**: fecha y hora, lugar, trabajo, rol, el tipo de trabajo de tus reglas que
  aplica, la certificación exigida y el modo (secuencial o simultáneo) con su ventana de
  espera.
- **Lista corta**: las personas que sí pueden, en el orden de tus reglas, y la razón de cada
  posición ("preferido del tipo", "segunda principal", "hace el trabajo según su ficha, no
  es principal").
- **Excluidos y por qué**: quién hace ese trabajo pero queda fuera, con la razón escrita
  (curso vencido el tal fecha, curso sin fecha, estado en pausa, un límite de asignación).
  Nadie sale de la lista sin razón, y la razón siempre cita la ficha.
- **Mensajes**: un borrador por persona de la lista, en el canal y el idioma de su ficha,
  con lo que tus plantillas dicen que lleva siempre un mensaje.
- **Respuestas**, vacía, esperando.

La certificación se mira contra la fecha de la producción, no contra hoy. Alguien con curso
que vence el 10 entra a una producción del 7 y no entra a una del 15.

### Mandar los mensajes

El directorio no envía nada. Cada mensaje empieza con la línea "BORRADOR: para pegar y
enviar desde tu teléfono" y tú lo copias y lo pegas en WhatsApp o Messenger, a la persona o
al grupo que diga su ficha. Si el modo es secuencial, mandas primero el de la posición 1 y
esperas la ventana; si es simultáneo, mandas todos.

### Registrar quién respondió

Cuéntaselo como venga:

> "Ariel no puede. Bel dijo que sí a las 3:40."

El directorio anota hora, persona y respuesta en **Respuestas**, escribe el nombre en
**Quién quedó**, agrega un hecho con fecha en la ficha de cada uno (respondió, no respondió,
en cuánto tiempo) y deja listo el **Texto de la invitación**: título, fecha, hora, lugar y
quién va. La invitación de calendario la envías tú desde tu cuenta; el directorio no invita a
nadie.

Si nadie respondió en la ventana, dile **"nadie contestó"** y te propone el siguiente tramo
de la lista según tus reglas (ampliar a quien tenga la especialidad aunque no sea principal,
o lo que hayan escrito en "Cuando nadie responde").

### Cerrar la producción

Cuando el trabajo ya pasó:

> "Cierra la producción del puente. Bel entregó el material el jueves, a tiempo."

El directorio marca la solicitud como cerrada, escribe el **Cierre** con cómo entregó cada
persona, y pasa ese hecho, con fecha y con tu nombre, a la sección **Confiabilidad (hechos)**
de la ficha. Eso es lo que la próxima lista corta va a tener en cuenta.

---

## 2. Agregar o corregir a un freelancer

### Una persona nueva

Una frase basta:

> "Agrega a Nora Beltrán, camarógrafa de eventos, WhatsApp en el grupo de producción,
> escribe en español, curso de seguridad en obra vence en marzo de 2027."

El directorio crea su ficha en `freelancers/` con el bloque **Datos** (nombre, canal,
contacto, idioma, estado), sus **Especialidades**, sus **Certificaciones** y lo demás vacío.
Lo que no le dijiste queda como hueco en `memoria.md` ("sin fecha exacta de vencimiento") en
vez de inventado. Si tienes una lista (una hoja, una nota, un chat fijado), pégala entera y
el directorio la convierte en fichas y te dice qué le faltó a cada una.

Una ficha nueva queda activa de inmediato y el directorio anota el alta en `memoria.md`. La
persona que **aprueba altas y bajas** las ve en la auditoría de cada semana y es la única que
puede marcar a alguien como "no volver a llamar" o sacarlo del pool; si no está de acuerdo con
un alta, lo dice en el chat y la ficha pasa a "en pausa" o "no volver a llamar" con su razón.

### Corregir algo

En el chat ("cambia el canal de Dani a Messenger", "Greta ya no hace fotografía de obra") o
a mano en Drive, y después se lo dices. En los dos casos el texto anterior queda en el
`## Historial` de la ficha con la fecha.

### Los límites se escriben como restricciones

Un límite de asignación dice qué no se le pide a una persona: "no asignarle edición con
plazo corto", "no asignarle jornadas de más de ocho horas seguidas". Si se lo dictas como
una condición personal o de salud, el directorio lo escribe como la restricción que implica,
lo marca "Reformulado como restricción de asignación" con la fecha, y te lo dice. No es
desconfianza: las fichas describen a personas que no están en la conversación, y lo que la
producción necesita saber es qué trabajo no asignarle, no por qué.

### Hechos, no notas

El directorio no califica a nadie. Si le dices "Dani es poco confiable", te va a pedir el
hecho: "Dani entregó el video un día tarde el 22 de agosto". Eso es lo que escribe, con la
fecha y con quién lo dijo. El juicio sobre si llamarlo o no sigue siendo tuyo; lo que el
directorio hace es que ese juicio se tome con los hechos a la vista.

### Los tres estados

- **activo**: entra a las listas cortas.
- **en pausa**: no entra por ahora; la ficha dice hasta cuándo y por qué, con fecha
  ("fuera del país hasta el 15 de noviembre"). Lo pone coordinación.
- **no volver a llamar**: no entra más; la ficha dice por qué, con fecha. Lo decide la
  persona que aprueba altas y bajas, y si lo pide alguien más queda como propuesta.

---

## 3. Las certificaciones y el barrido de los lunes

Cada lunes a la hora que dice `_config/fuentes.md`, sin que nadie encienda un computador, el
directorio lee las certificaciones de todas las fichas y deja un reporte nuevo en
`salidas/vencimientos-AAAA-MM-DD.md`. Cada certificación cae en exactamente uno de seis
tramos, contados desde ese lunes:

| Tramo | Qué significa | Qué haces |
|---|---|---|
| vencida | la fecha ya pasó | esa persona no entra a producciones que exijan ese curso hasta que renueve |
| vence en 7 días | vence esta semana | avísale; todavía entra a producciones de esta semana anteriores a la fecha |
| vence en 30 días | vence en el mes | buen momento para pedir la renovación |
| vence en 60 días | vence en dos meses | solo para que lo tengas en el radar |
| sin fecha | la ficha nombra el curso pero no dice cuándo vence | nunca cuenta como vigente; pídele el carné y dile al directorio la fecha |
| sin soporte | tiene fecha pero no hay documento en `freelancers/soportes/` | pide el documento; mientras tanto la fecha sí vale para las listas |

Lo que vence después de 60 días no aparece en el reporte; sigue en la ficha.

### Guardar un certificado

Deja la foto o el PDF en `freelancers/soportes/` y dile al directorio de quién es:

> "Dejé en soportes el carné de alturas de Fausto, vence el 1 de diciembre de 2026."

El directorio escribe la fecha y el nombre del archivo en la tabla de **Certificaciones** de
su ficha, y la certificación sale del tramo "sin fecha" o "sin soporte" en el próximo
barrido.

### Una renovación

> "Dani renovó su curso de seguridad en obra, vence el 28 de septiembre de 2027."

La fecha vieja pasa al Historial, la nueva queda en la tabla, y Dani vuelve a entrar a las
listas cortas desde ese momento.

### Preguntar sin esperar al lunes

> "¿Quién tiene curso de seguridad en obra vigente el 15 de octubre?"

Responde con las personas y la fecha de vencimiento de cada una, leídas de las fichas. Si
quieres el barrido completo hoy, dile **"corre el barrido"**; correrlo dos veces el mismo
día no cambia nada.

---

## 4. Leer el directorio desde el teléfono

El archivo `salidas/directorio.md` es el índice de todo el pool: una fila por persona con
sus especialidades, su canal e idioma, su estado, sus certificaciones vigentes a la fecha
del último barrido y su última producción. Se regenera solo en cada barrido y cuando cambia
una ficha; no se edita a mano.

Ábrelo desde la aplicación de Drive en el teléfono, o pregúntale al directorio desde la
aplicación de Claude en el teléfono ("¿quién hace fotografía de obra?"): lee la misma
carpeta, sin que tu computador esté encendido.

---

## 5. Lo que el directorio nunca hace, y por qué

- **No manda mensajes a los freelancers.** Los deja escritos y tú los envías. Es a
  propósito: el que firma el mensaje eres tú, y los freelancers responden en el canal donde
  ya te conocen.
- **No reserva, no contrata, no paga, no invita al calendario.** Deja el texto de la
  invitación y la envías tú. Confirmar a alguien es un compromiso tuyo con esa persona.
- **No califica a nadie.** Escribe los hechos con fecha y autor que ustedes le cuentan. El
  juicio es del equipo.
- **No inventa.** Si una persona, una regla o una certificación no está escrita en la
  carpeta, te lo dice y te ofrece registrarla.

---

## 6. Cuando algo se ve raro

### Organizar la carpeta

Una vez por semana corre sola una revisión, y la puedes pedir cuando quieras:
**"organiza la carpeta"**. Deja un reporte en `salidas/auditorias/` con lo que encontró y lo
que arregló: fichas con el bloque de datos roto por una edición a mano, certificaciones sin
fecha o sin soporte, solicitudes cuya fecha ya pasó y no tienen cierre, el índice o la marca
de agua desactualizados, y los huecos de `memoria.md` que siguen abiertos. Lo mecánico lo
arregla y te lo dice; lo que requiere una decisión te lo deja como pregunta en una línea.

### Una ficha perdió su estructura

Pasa cuando se edita a mano y se borra un encabezado o una línea del bloque de datos. Dile
**"repara la ficha de Greta"**: el directorio la reconstruye con sus secciones, te muestra
qué quedó dónde y guarda lo anterior en el Historial. No pierde texto; en el peor caso
deja una línea en "Notas del equipo" con lo que no supo ubicar.

### Una solicitud quedó abierta

Si la fecha de la producción ya pasó y la solicitud sigue abierta o asignada sin cierre, la
revisión semanal te lo pregunta. Ciérrala con una frase (sección 1) o dile **"esa producción
no se hizo"** y queda marcada como sin cubrir, con la razón.

### El barrido del lunes no corrió

**Cómo te das cuenta:** no hay un `vencimientos-AAAA-MM-DD.md` nuevo en `salidas/` con la
fecha de este lunes.

1. **Pídelo en el chat:** "corre el barrido". Hace exactamente lo mismo que la tarea
   programada, y correrlo dos veces no cambia nada. Con eso ya tienes el reporte de la
   semana.
2. **Revisa la tarea programada** en la cuenta donde corre (está escrita en
   `_config/fuentes.md`): que siga encendida, con el día y la hora que acordaron. Si está
   apagada, vuelve a encenderla.
3. **Revisa la conexión con Drive** en esa misma cuenta: en la aplicación de Claude, en las
   conexiones, Google Drive debe aparecer autorizado. Si pide volver a autorizar, hazlo con
   tu propia sesión; el directorio nunca te pide la contraseña.

Con esas tres comprobaciones el barrido vuelve a correr el lunes siguiente por su cuenta.

---

## Cambiar quién tiene qué rol

Lo pide la persona que aprueba altas y bajas, en el chat: **"a partir de hoy Nora coordina
producción"**. El directorio actualiza la tabla de roles de `_config/empresa.md` con la fecha
y deja la anterior en el Historial. Después hay que ajustar los permisos de la carpeta en
Drive para que coincidan: eso lo hace una persona, porque es lo que de verdad decide quién
puede cambiar la carpeta.
