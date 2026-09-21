# Fuentes: qué entra al cerebro, quién aprueba qué y cómo corre la rutina

## Reuniones que entran

- **Sí entran:** las reuniones internas del equipo <nombre del equipo en Fathom>. En
  particular <la reunión recurrente principal, día y hora>, que es la fuente principal de
  decisiones.
- **No entran:** las reuniones con clientes, salvo que <quien aprueba valores> marque una
  "para el cerebro".
- Dueño del equipo Fathom: **<Nombre>**. La rutina corre en la cuenta de **<Nombre>**,
  leyendo las grabaciones compartidas al equipo. Sin Fathom, los transcripts se pegan en
  `reuniones/entrada/` y cumplen la misma función.

## Zona horaria

<Zona IANA, por ejemplo America/Bogota>. Las fechas de la bitácora y los nombres de archivo de
`reuniones/` y `salidas/` van en hora local de <Organización>, no en UTC.

## Idioma

<Idioma> para playbooks, bitácora, casos y respuestas. Ver `CLAUDE.md`. <Si los clientes
hablan otro idioma: los borradores para clientes van en ese idioma.>

## Quién aprueba qué

| Qué | Quién | Nota |
|---|---|---|
| Cambios a `_config/valores-y-negociables.md` | **<Nombre>** | La rutina los propone y espera. Esa persona además edita el archivo directamente |
| Ejecutar un cambio aprobado | **<Nombre>** | |
| Cambios a `playbooks/` que vienen de una decisión explícita | La rutina los aplica sola | Queda el rastro en la bitácora y en el Historial del playbook |
| Marcar una reunión con cliente "para el cerebro" | **<Nombre>** | |
| Agregar un caso a `casos/` | Cualquiera del equipo, por el chat | |

## La rutina diaria de ingesta

Es la única pieza del sistema que consulta un servicio externo, y lo único que hace con él
es traer transcripts. Escribe solo en esta carpeta.

- **Cuenta:** la de Claude de **<Nombre>**. Una sola cuenta, para que no haya doble ingesta.
- **Dónde:** en la nube. No depende de que haya un computador encendido.
- **Cuándo:** <días>, <hora> hora de <zona>. <Margen respecto a la reunión principal.>

El prompt literal de la tarea programada. No se parafrasea al configurarla:

> Corre la ingesta del cerebro: lee la marca de agua, pide a Fathom las reuniones internas
> nuevas, procesa cada transcript con el actualizador de playbooks, actualiza bitácora y
> playbooks en la carpeta de Drive, deja el resumen en salidas/.

Cada corrida deja un archivo `salidas/ingesta-AAAA-MM-DD.md`. Si no está, o no había nada
que ingerir o la rutina no corrió: ver "Qué hacer si la rutina no corrió" en
`salidas/como-operar-el-cerebro.md`.

## Qué NO entra, nunca

- Mensajería directa con clientes (WhatsApp, Messenger u otras). El cerebro no se conecta a
  ninguna.
- Cualquier cosa que implique escribir fuera de esta carpeta.
