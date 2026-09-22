# Fuentes: qué entra al cerebro, quién tiene qué rol y cómo corre la rutina

## Reuniones que entran

- **Sí entran:** las reuniones internas del equipo <nombre del equipo en Fathom>. En
  particular <la reunión recurrente principal, día y hora>, que es la fuente principal de
  decisiones.
- **No entran:** las reuniones con clientes, salvo que la persona responsable del cerebro
  marque una "para el cerebro".
- Dueño del equipo Fathom: **<Nombre>**. La rutina corre en la cuenta de **<Nombre>**,
  leyendo las grabaciones compartidas al equipo. Sin Fathom, los transcripts se pegan en
  `reuniones/entrada/` y cumplen la misma función.

## Zona horaria

<Zona IANA, por ejemplo America/Bogota>. Las fechas de la bitácora y los nombres de archivo de
`reuniones/` y `salidas/` van en hora local de <Organización>, no en UTC.

## Idioma

Español, fijado en la instalación, para todo lo que se escribe en esta carpeta: nombres de
carpetas y archivos, playbooks, bitácora, casos y respuestas. Ver `CLAUDE.md`. <Si los
clientes hablan otro idioma: los borradores para clientes van en ese idioma.>

## Roles

Salen de la entrevista de instalación y se cambian pidiéndoselo al cerebro en el chat (lo
cambia la persona responsable del cerebro). Tiene que haber exactamente una persona responsable; editor y
consulta pueden quedar vacíos.

| Persona | Rol | Desde | Fuente |
|---|---|---|---|
| **<Nombre>** | responsable del cerebro | <AAAA-MM-DD> | <entrevista AAAA-MM-DD> |
| <Nombre> | <editor o consulta> | <AAAA-MM-DD> | <entrevista AAAA-MM-DD> |

## Quién aprueba qué

| Qué | Quién | Nota |
|---|---|---|
| Cualquier cambio, en cualquier archivo | La persona responsable del cerebro, sin aprobación de nadie | Por el chat, o a mano avisándole al cerebro para que deje el rastro |
| Cambios a `playbooks/` y `casos/` pedidos en el chat | Editor o responsable | Quedan en la bitácora con quién los pidió |
| Cambios a `_config/valores-y-negociables.md` que no pide la persona responsable | Los aprueba la persona responsable | La rutina, un editor o consulta los proponen y esperan |
| Cambios a `playbooks/` que vienen de una decisión explícita en una reunión | La rutina los aplica sola | Queda el rastro en la bitácora y en el Historial del playbook |
| Que los procesos estén escritos y al día | La persona responsable del cerebro | Revisa lo que el cerebro propone y convoca la reunión de arranque cuando un proceso cambia de fondo |
| Ejecutar un cambio aprobado | **<Nombre>** | |
| Marcar una reunión con cliente "para el cerebro" | La persona responsable del cerebro | |

## Permisos de la carpeta en Drive

El cerebro no sabe quién le escribe; lo que protege la carpeta son sus permisos. Deben
coincidir con los roles:

- Responsable del cerebro y editores: **editor** en la carpeta de Drive.
- Consulta: **lector** en la carpeta de Drive.
- La cuenta donde corre la rutina: **editor**.

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
