# Fuentes y rutina

<!-- Vigente desde AAAA-MM-DD (origen: entrevista de instalación) -->

## Idioma

Idioma de la carpeta: **español** (fijado al instalar; no cambia). Los mensajes a cada
freelancer salen en el idioma de su ficha.

## El barrido semanal

| Qué | Valor |
|---|---|
| Cuenta en la que corre | <cuenta de Claude de la persona en coordinación de producción> |
| Día y hora | <lunes 8:00>, zona <America/Chicago> |
| Dónde corre | en la nube, sin computador encendido |
| Qué toca | lee las fichas y `_config/certificaciones.md`; escribe `salidas/vencimientos-AAAA-MM-DD.md`, regenera `salidas/directorio.md` y avanza `_estado/ultimo-barrido.json` |
| Qué no toca | ninguna ficha, ninguna solicitud; no envía nada |

Prompt literal de la tarea programada (no se parafrasea):

> Corre el barrido del directorio: revisa las certificaciones de todas las fichas, escribe
> el reporte de vencimientos en salidas/, regenera el índice y avanza la marca de agua.

## El calendario

| Qué | Valor |
|---|---|
| Calendario que se lee | <nombre del calendario donde ya se ponen las producciones, o "ninguno"> |
| Para qué | fecha, hora y duración de la producción; choques con lo ya agendado |
| Escritura | ninguna. La invitación la envía una persona con el texto que deja la solicitud |

## Permisos de Drive por rol

| Rol | Permiso en la carpeta |
|---|---|
| coordinación de producción | editor |
| aprueba altas y bajas | editor |
| consulta | lector |
| cuenta de la rutina | editor |

Quién puede cambiar esta carpeta lo deciden estos permisos, no el agente.

## Historial

Sin entradas. Este archivo nace el AAAA-MM-DD con la instalación.
