# Cómo operar el cerebro

Cinco cosas que van a necesitar hacer y que nadie debería tener que preguntar. Están en
orden de frecuencia: la primera pasa todas las semanas, la última casi nunca. Los roles
(responsable del cerebro, editor, consulta) son los de la tabla de roles de
`_config/fuentes.md` de esta carpeta.

Regla que atraviesa las cinco: **el cerebro escribe, tú le dices qué**. Los cambios se
piden en el chat y el cerebro los escribe con su rastro. No es burocracia: si dos personas
editan el mismo archivo en Drive al tiempo, una de las dos versiones se pierde, y si alguien
cambia un playbook sin pasar por la bitácora, el registro deja de corresponder con el
proceso y ya no se sabe cuál de los dos está bien. La persona responsable del cerebro puede
además editar cualquier archivo a mano; si lo hace, que le avise al cerebro en el chat ("edité el
playbook de propuestas") para que archive la versión anterior y deje la línea en la
bitácora.

---

## 1. Pegar un transcript a mano

Cuando la reunión no la grabó Fathom (una llamada por teléfono, una reunión que nadie
programó, una conversación que vale la pena guardar).

1. Guarda el texto en un archivo. Lo que sea sirve: un `.md`, un `.txt`, lo que exporte la
   herramienta.
2. Ponle nombre con la fecha adelante: `2026-09-22-reunion-con-cliente.md`.
3. Déjalo en `reuniones/entrada/`.
4. Espera a la corrida de la rutina (la hora está en `_config/fuentes.md`), o pídelo en el
   chat del proyecto: **"procesa el transcript que dejé en entrada"**.

El cerebro lo lee, escribe el archivo de la reunión en `reuniones/`, agrega las decisiones
a la bitácora y actualiza los playbooks que cambiaron. El resumen de lo que hizo queda en
`salidas/`.

**Si el texto no trae minutos**, el cerebro lo dice y cita la reunión sin minuto. No es un
problema; solo es menos rastreable.

---

## 2. Agregar un documento que ya tenían

Un manual, un procedimiento, una plantilla, una presentación de inducción que aparece
después de la instalación.

1. Déjalo en `documentos/`, o pégalo en el chat. Si es un enlace de Drive, pega el enlace.
2. Pide en el chat: **"procesa el documento que dejé en documentos"**.

El cerebro lo lee, decide a qué proceso corresponde y escribe o completa ese playbook
**desde el documento**, con la fecha del documento y su nombre como origen. No lo
moderniza: si algo suena viejo, lo escribe tal cual y lo marca por confirmar, para que lo
corrijan en una reunión. El original no se toca.

Si el documento contradice algo que ya estaba escrito, el cerebro no elige solo: te muestra
las dos versiones con sus fechas y pregunta cuál vale.

---

## 3. Corregir una decisión mal extraída

Va a pasar. Las reuniones informales traen ruido y el filtro no es perfecto.

Díselo en el chat, en lenguaje normal:

> "La decisión del 18 de septiembre sobre los freelancers quedó mal. No dijimos que
> siempre se le manda primero al preferido, dijimos que depende del tipo de trabajo.
> Corrígela."

El cerebro hace tres cosas y te las reporta:

1. **Agrega una línea nueva** a la bitácora que corrige la anterior, con tu nombre en
   "Pedido por". No borra la vieja. Esa es la regla completa: en esta carpeta nada se
   borra, porque el día que alguien pregunte "¿esto por qué cambió?", la respuesta tiene
   que estar.
2. **Devuelve el playbook al texto correcto**, y el texto equivocado pasa a `## Historial`
   como pasó el anterior.
3. **Te muestra cómo quedó** antes de darlo por hecho.

**Si lo que quieres es revertir del todo**, dilo así: "esa decisión no existió, la
extrajiste mal". El cerebro deja la línea en la bitácora marcada como revertida, con la
fecha, y devuelve el playbook al texto que tenía antes. La línea se queda porque la
bitácora es el registro de lo que pasó, incluido el error.

Si la corrección toca valores o negociables y no la pide la persona responsable del cerebro,
queda como propuesta hasta que esa persona la apruebe.

---

## 4. Agregar un caso

Un caso es una historia con cliente, con decisión y con final. Es lo que el cerebro cita
cuando alguien pregunta "¿cómo manejamos algo así?".

Cuéntaselo en el chat, hablado, sin estructura:

> "Agrega un caso. El cliente tal empezó a mandar correos fuera de horario reclamándole al
> equipo. Entré yo, pedí una llamada con él y su jefe, y pusimos por escrito por qué canal
> se habla con el equipo. Duró seis meses más y no renovamos."

El cerebro arma `casos/AAAA-cliente.md` con las cinco partes que hacen citable un caso:
qué pasó, qué se hizo, cómo terminó, **qué se aprendió** y **qué valor se aplicó**. Las
dos últimas son las que importan, y si no se las contaste te las va a preguntar. Un caso
sin la lección es una anécdota, y el cerebro no cita anécdotas.

**Los casos viejos también valen**, y valen mucho: un caso de hace tres años que alguien
del equipo recuerda es exactamente el conocimiento que esta carpeta existe para no perder.

---

## 5. Qué hacer si la rutina no corrió

**Cómo te das cuenta:** no hay un archivo `ingesta-AAAA-MM-DD.md` nuevo en `salidas/`.

**Lo primero, y casi siempre es esto:** no había nada que ingerir. Si ese día no hubo
reunión o Fathom no publicó ningún transcript nuevo, la rutina corrió, no encontró nada y
no escribió archivo. Es correcto.

**Si sí hubo reunión grabada**, en orden:

1. **Espera a la corrida del día siguiente.** La rutina es acumulativa: lee hasta dónde
   llegó la última vez y recoge todo lo pendiente. Un día perdido se recupera solo al
   siguiente, y no hay que hacer nada. Esta es la respuesta correcta la mayoría de las
   veces.
2. **Si tienes prisa**, pídelo en el chat: **"corre la ingesta ahora"**. Hace lo mismo que
   la rutina. Correrla dos veces no rompe nada: la marca de agua evita que un transcript
   se procese dos veces.
3. **Si dos días seguidos no aparece nada** y sí hubo reuniones grabadas, es una de tres,
   y en este orden de probabilidad: el transcript no quedó compartido con el equipo de
   Fathom; la conexión de Fathom en la cuenta donde corre la rutina se venció y hay que
   volver a autorizarla; o la tarea programada se apagó. Escríbele a Molt con la fecha de
   la reunión que falta.

**Lo que NO hay que hacer:** ponerse a escribir los playbooks a mano mientras tanto. El
transcript no se pierde, y cuando la rutina vuelva a correr los recoge todos. Escribirlos
a mano crea justo el conflicto que la regla del escritor único evita.

---

## Cambiar quién tiene qué rol

Lo pide la persona responsable del cerebro en el chat: **"a partir de hoy Ana es editora"** o
**"desde hoy Ana es la responsable del cerebro"**. El cerebro actualiza la tabla de roles de
`_config/fuentes.md` con la fecha y deja la línea en la bitácora. Después hay que ajustar
los permisos de la carpeta en Drive para que coincidan: eso lo hace una persona, porque es
lo que de verdad decide quién puede cambiar la carpeta.
