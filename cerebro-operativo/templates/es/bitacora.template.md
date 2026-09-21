# Bitácora de decisiones

Append only. Una línea por decisión, la más nueva al final. Ninguna línea existente se
reescribe: si una decisión se revierte o se corrige, se agrega una línea nueva que lo diga,
y el playbook vuelve atrás con su Historial. El día que alguien pregunte "¿esto por qué
cambió?", la respuesta tiene que estar acá.

**Estados:**

- `aplicada`: cambió un playbook, y el texto anterior quedó en su Historial.
- `por confirmar`: se infirió de la conversación, nadie la dijo en firme. **No tocó ningún
  playbook** hasta que alguien la confirme.
- `propuesta`: toca `_config/valores-y-negociables.md` y espera la aprobación de <quien
  aprueba valores>.
- `abierta`: es una acción con dueño que todavía no se ejecutó.
- `revertida`: se anuló con una línea posterior; el playbook volvió a su texto anterior.

| Fecha | Decisión | Razón | Reunión y minuto | Playbook | Estado |
|---|---|---|---|---|---|

Vacía. La primera ingesta la llena.
