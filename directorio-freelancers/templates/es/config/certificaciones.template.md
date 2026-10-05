# Certificaciones

Las certificaciones que <Organización> reconoce, con el nombre que usa el equipo. El
rastreador de vencimientos compara las fichas contra esta lista y los tramos de abajo; una
certificación que aparezca en una ficha y no esté acá se reporta para que el equipo decida si
entra.

<!-- Vigente desde AAAA-MM-DD (origen: entrevista de instalación) -->

## Catálogo

| Certificación (como la dice el equipo) | Quién la exige | Vigencia típica | Soporte que se guarda |
|---|---|---|---|
| <curso de trabajo en alturas> | <obras y clientes industriales> | <1 año> | <foto del carné o PDF> |
| <curso de seguridad en obra> | <constructoras> | <1 año> | <PDF> |
| <licencia de dron> | <toda producción con dron> | <2 años> | <PDF> |

## Tramos de aviso

El barrido semanal clasifica cada certificación de cada ficha en exactamente uno de estos
tramos, contando desde el día del barrido:

| Tramo | Significa |
|---|---|
| vencida | la fecha ya pasó |
| vence en 7 días | vence en los próximos 7 días |
| vence en 30 días | vence entre 8 y 30 días |
| vence en 60 días | vence entre 31 y 60 días |
| sin fecha | la ficha la nombra pero no dice cuándo vence; nunca cuenta como vigente |
| sin soporte | tiene fecha pero no hay documento en `freelancers/soportes/` |

Lo que vence después de 60 días no se reporta; sigue en la ficha.

## Regla de vigencia

Para una producción, una certificación vale si su fecha de vencimiento es posterior a la
fecha de la producción, no a la de hoy. Una persona con curso que vence el 10 de noviembre no
entra a una producción del 15.

## Historial

Sin entradas. Este archivo nace el AAAA-MM-DD con la instalación.
