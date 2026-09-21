> **DOCUMENTO FICTICIO.** Configuración de una agencia inventada, escrita para demostrar el agente.

# Fuentes: qué entra al cerebro, quién aprueba qué y cómo corre la rutina

## Reuniones que entran

- **Sí entran:** las reuniones internas del equipo Fathom "Faro". En particular la reunión
  semanal de los lunes a las 9 de la mañana, que es la fuente principal de decisiones.
- **No entran:** las reuniones con clientes, salvo que Marina marque una "para el cerebro".
- Dueño del equipo Fathom: **Tomás**. La rutina corre en la cuenta de **Marina**, leyendo las
  grabaciones compartidas al equipo. Sin Fathom, los transcripts se pegan en
  `reuniones/entrada/`.

## Zona horaria

America/Bogota. Las fechas de la bitácora y los nombres de archivo van en hora local.

## Idioma

Español para todo, incluidos los borradores para clientes.

## Quién aprueba qué

| Qué | Quién | Nota |
|---|---|---|
| Cambios a `_config/valores-y-negociables.md` | **Marina** | La rutina los propone y espera. Marina además edita el archivo directamente |
| Ejecutar un cambio aprobado | **Tomás** | |
| Cambios a `playbooks/` que vienen de una decisión explícita | La rutina los aplica sola | Queda el rastro en la bitácora y en el Historial |
| Marcar una reunión con cliente "para el cerebro" | **Marina** | |
| Agregar un caso a `casos/` | Cualquiera del equipo, por el chat | |

## La rutina diaria de ingesta

- **Cuenta:** la de Claude de **Marina**.
- **Dónde:** en la nube. No depende de un computador encendido.
- **Cuándo:** lunes a viernes, 13:00 hora de Bogotá. La reunión semanal es a las 9, así que a
  la 1 el transcript ya está publicado con margen.

El prompt literal de la tarea programada:

> Corre la ingesta del cerebro: lee la marca de agua, pide a Fathom las reuniones internas
> nuevas, procesa cada transcript con el actualizador de playbooks, actualiza bitácora y
> playbooks en la carpeta de Drive, deja el resumen en salidas/.

## Qué NO entra, nunca

- Mensajería directa con clientes. El cerebro no se conecta a ninguna.
- Cualquier cosa que implique escribir fuera de esta carpeta.
