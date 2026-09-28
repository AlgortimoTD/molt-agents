# Builds demo/es/material-para-subir/: the fictional files a research team hands over when the
# session coder is installed (a quick-download template, a previous study coded by hand, the
# current study's codebook and design, a moderator guide and a new session). Everything is
# invented. Deterministic: the same script always writes the same content.
#
# Run it in a container, never on the host:
#   docker run --rm -v "<plugin>/demo/es:/w" -w /w python:3.12-slim \
#     sh -c "pip install -q openpyxl==3.1.5 python-docx==1.1.2 && python build-material-para-subir.py"
import os
import shutil

from docx import Document
from openpyxl import Workbook
from openpyxl.styles import Font

OUT = "material-para-subir"
FICT = "DOCUMENTO FICTICIO: material de demostración. Personas, empresas, datos y citas inventados."

if os.path.exists(OUT):
    shutil.rmtree(OUT)


def path(rel):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def text(rel, body):
    with open(path(rel), "w", encoding="utf-8", newline="\n") as f:
        f.write(body)


def fixed_props(obj):
    # Stable metadata so rebuilding does not produce a different file for the same content.
    obj.creator = "Equipo Brújula (ficticio)"
    obj.lastModifiedBy = "Equipo Brújula (ficticio)"


def workbook(rel, sheets):
    wb = Workbook()
    wb.remove(wb.active)
    for title, rows in sheets:
        ws = wb.create_sheet(title)
        for r in rows:
            ws.append(r)
        for c in ws[1]:
            c.font = Font(bold=True)
        for col in ws.columns:
            width = max(len(str(c.value or "")) for c in col)
            ws.column_dimensions[col[0].column_letter].width = min(max(12, width + 2), 70)
    fixed_props(wb.properties)
    wb.save(path(rel))


def document(rel, title, blocks):
    d = Document()
    d.add_heading(title, level=1)
    d.add_paragraph(FICT).italic = True
    for kind, content in blocks:
        if kind == "h":
            d.add_heading(content, level=2)
        elif kind == "p":
            d.add_paragraph(content)
        elif kind == "li":
            for item in content:
                d.add_paragraph(item, style="List Bullet")
        elif kind == "ol":
            for item in content:
                d.add_paragraph(item, style="List Number")
    cp = d.core_properties
    cp.author = "Equipo Brújula (ficticio)"
    cp.last_modified_by = "Equipo Brújula (ficticio)"
    d.save(path(rel))


# ── 01: the quick-download template the team fills after each session ──────────
workbook("01-plantilla-descarga-rapida.xlsx", [
    ("Descarga", [
        ["Estudio", "Sesión", "Fecha", "Grupo", "Participante", "Variable", "Respuesta sintética", "Cita", "Min", "Comentario"],
    ]),
    ("Cómo se llena", [
        ["Columna", "Qué va"],
        ["Participante", "Código P1, P2... en el orden en que hablan. Nunca el nombre."],
        ["Respuesta sintética", "La categoría del libro de códigos en la que cae la respuesta."],
        ["Cita", "Lo que dijo, textual. Si se corta algo, (...)."],
        ["Min", "El minuto de la grabación, como lo da Fathom."],
        ["Comentario", "Dudas: cita poco clara, no se sabe quién habló."],
        ["Aviso", FICT],
    ]),
])

# ── 02: a previous study coded by hand, three focus groups ───────────────────────
PREV = "02-estudio-anterior-movilidad-2025/"
S1 = """Movilidad al trabajo 2025 · G1 · grupo focal · 2025-11-03
{fict}
Exportado de Fathom. Moderó Sara Quintero.

0:00 - Sara Quintero
  Gracias por venir. Cuéntenme cómo llegan al trabajo y por qué de esa forma.

0:42 - P1
  Yo cojo el metro todos los días. En carro me demoro el doble por el trancón.

1:30 - P2
  Yo voy en bici. Me sale gratis y además es mi ejercicio del día.

2:15 - P3
  Camino. Vivo a quince cuadras y la verdad me gusta llegar despierta.

3:05 - Sara Quintero
  ¿Alguien ha cambiado de forma de moverse este año?

3:20 - P1
  Antes iba en la moto, pero la gasolina subió mucho y ya no me alcanzaba.
"""
S2 = """Movilidad al trabajo 2025 · G2 · grupo focal · 2025-11-05
{fict}
Exportado de Fathom. Moderó Andrés Pardo.

0:00 - Andrés Pardo
  Buenos días. ¿Cómo se mueven al trabajo?

0:35 - P1
  En carro. Tengo que dejar a los niños en el colegio y en bus no alcanzo.

1:10 - Mariana Gómez
  Yo en bus, el alimentador y después el troncal. Es lo que me alcanza con el sueldo.

1:55 - P3
  En moto. Es lo más rápido, me ahorro casi una hora al día.

2:40 - Andrés Pardo
  ¿Y qué es lo que más pesa cuando eligen?

2:55 - P1
  El tiempo, con los niños todo es contra el reloj.

3:30 - Mariana Gómez
  La plata, sin duda.
"""
S3 = """Movilidad al trabajo 2025 · G1 · grupo focal · 2025-11-10
{fict}
Exportado de Fathom. Moderó Sara Quintero.

0:00 - Sara Quintero
  Empezamos. ¿Cómo llegan al trabajo?

0:30 - P1
  En bici compartida, la de la ciudad. Me encanta porque me mantengo en forma.

1:15 - P2
  Metro y después camino un poco. Es lo más barato que encontré.

2:00 - P3
  Me lleva mi hermano en el carro, trabajamos cerca.

2:45 - Sara Quintero
  ¿Qué les haría cambiar de medio?

3:05 - P3
  Si el metro llegara a mi barrio, lo cogería. En carro se pierde mucho tiempo.
"""
for name, body in [("2025-11-03-g1-grupo-focal.txt", S1), ("2025-11-05-g2-grupo-focal.txt", S2), ("2025-11-10-g1-grupo-focal.txt", S3)]:
    text(PREV + "transcripciones/" + name, body.format(fict=FICT))

H = ["Estudio", "Sesión", "Fecha", "Grupo", "Participante", "Variable", "Respuesta sintética", "Cita", "Min", "Comentario"]
M = [
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P1", "Medio de transporte", "Transporte público", "Yo cojo el metro todos los días.", "0:42", ""],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P1", "Motivo de elección", "Tiempo", "En carro me demoro el doble por el trancón.", "0:42", ""],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P1", "Motivo de elección", "Costo", "la gasolina subió mucho y ya no me alcanzaba", "3:20", "por qué dejó la moto"],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P2", "Medio de transporte", "Activo", "Yo voy en bici.", "1:30", ""],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P2", "Motivo de elección", "Costo", "Me sale gratis", "1:30", ""],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P2", "Motivo de elección", "Salud", "además es mi ejercicio del día", "1:30", ""],
    ["MOV25", "2025-11-03 G1", "2025-11-03", "G1", "P3", "Medio de transporte", "Activo", "Camino. Vivo a quince cuadras", "2:15", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "P1", "Medio de transporte", "Vehículo propio", "En carro.", "0:35", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "P1", "Motivo de elección", "Tiempo", "con los niños todo es contra el reloj", "2:55", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "Mariana Gómez", "Medio de transporte", "Transporte público", "Yo en bus, el alimentador y después el troncal.", "1:10", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "Mariana Gómez", "Motivo de elección", "Costo", "La plata, sin duda.", "3:30", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "P3", "Medio de transporte", "Vehículo propio", "En moto.", "1:55", ""],
    ["MOV25", "2025-11-05 G2", "2025-11-05", "G2", "P3", "Motivo de elección", "Tiempo", "me ahorro casi una hora al día", "1:55", ""],
    ["MOV25", "2025-11-10 G1", "2025-11-10", "G1", "P1", "Medio de transporte", "Activo", "En bici compartida, la de la ciudad.", "0:30", ""],
    ["MOV25", "2025-11-10 G1", "2025-11-10", "G1", "P1", "Motivo de elección", "Salud", "me mantengo en forma", "0:30", ""],
    ["MOV25", "2025-11-10 G1", "2025-11-10", "G1", "P2", "Medio de transporte", "Transporte público", "Metro y después camino un poco.", "1:15", "combina, se codifica el principal"],
    ["MOV25", "2025-11-10 G1", "2025-11-10", "G1", "P2", "Motivo de elección", "Costo", "Es lo más barato que encontré.", "1:15", ""],
    ["MOV25", "2025-11-10 G1", "2025-11-10", "G1", "P3", "Medio de transporte", "Vehículo propio", "Me lleva mi hermano en el carro", "2:00", "carro del hogar"],
]
workbook(PREV + "matriz-codificada-a-mano.xlsx", [
    ("Matriz", [H] + M),
    ("Categorías", [
        ["Variable", "Categoría", "Qué entra"],
        ["Medio de transporte", "Transporte público", "bus, metro, tren"],
        ["Medio de transporte", "Vehículo propio", "carro o moto de la persona o de su hogar"],
        ["Medio de transporte", "Activo", "a pie o en bicicleta, propia o compartida"],
        ["Motivo de elección", "Tiempo", "elige por lo que tarda"],
        ["Motivo de elección", "Costo", "elige por lo que paga"],
        ["Motivo de elección", "Salud", "elige por su cuerpo o su bienestar físico, dicho así"],
    ]),
])
document(PREV + "hallazgos.docx", "Movilidad al trabajo 2025: hallazgos para Movilidad Andina S.A.S.", [
    ("h", "Resumen para el cliente"),
    ("li", [
        "El costo pesa más que el tiempo en quienes usan transporte público.",
        "Quienes van en bicicleta la eligen por salud y por costo a la vez.",
        "El carro aparece ligado a llevar a los hijos, no a la comodidad.",
    ]),
    ("p", "Estos hallazgos son solo contexto: el codificador no redacta hallazgos."),
])

# ── 03: the current study ──────────────────────────────────────────────────────
CUR = "03-estudio-actual-ocio-familias-2026/"
workbook(CUR + "libro-de-codigos.xlsx", [
    ("Libro de códigos", [
        ["Variable", "Bloque de la guía", "Categoría", "Definición", "Ejemplo"],
        ["Actividades de tiempo libre", "1", "Deportista", "deporte organizado o individual, practicado por alguien de la familia", "los domingos es fútbol"],
        ["Actividades de tiempo libre", "1", "Cultural", "museos, teatro, cine, lectura, conciertos", "fuimos al museo"],
        ["Actividades de tiempo libre", "1", "En casa", "series, juegos de mesa, videojuegos, cocinar juntos", "nos quedamos viendo series"],
        ["Quién decide", "2", "Decide un adulto", "el plan lo define una sola persona adulta", "yo decido y ellos se suben"],
        ["Quién decide", "2", "Decisión compartida", "se habla y se acuerda entre varios", "lo votamos"],
        ["Quién decide", "2", "Deciden los hijos", "los hijos eligen y los adultos acompañan", "ellos escogen"],
        ["Freno principal", "3", "Dinero", "no lo hacen por lo que cuesta", "no alcanza"],
        ["Freno principal", "3", "Tiempo", "no lo hacen por falta de tiempo o de energía", "llegamos muertos el viernes"],
        ["Freno principal", "3", "Distancia", "no lo hacen por lo lejos que queda", "queda lejísimos"],
    ]),
])
document(CUR + "diseno-del-estudio.docx", "Tiempo libre en familia 2026: diseño del estudio", [
    ("p", "Código: OCIO26. Cliente: una caja de compensación. Campo: 2026-09-21 a 2026-10-09. Lidera: Lucía Mora."),
    ("h", "Objetivos"),
    ("ol", ["Entender cómo planean las familias su tiempo libre del fin de semana.", "Identificar qué les impide hacer lo que quisieran."]),
    ("h", "Hipótesis del cliente"),
    ("ol", ["Las familias con adolescentes deciden en conjunto; las de niños pequeños, un adulto.", "El dinero es el principal freno para salir de casa."]),
    ("h", "Grupos objetivo"),
    ("li", ["G1: familias con hijos menores de 10 años, 2 grupos focales.", "G2: familias con hijos adolescentes, 2 grupos focales."]),
])
document(CUR + "guia-moderador-g1.docx", "Guía del moderador · G1", [
    ("ol", [
        "Rompehielo: ¿qué hicieron el fin de semana pasado? (actividades de tiempo libre)",
        "¿Quién propone el plan y quién lo decide? (quién decide)",
        "¿Qué les gustaría hacer y no hacen? ¿Por qué? (freno principal)",
    ]),
])

# ── 04: the first new session to code after the install ────────────────────────
text("04-sesion-nueva/OCIO26 G1 grupo focal 2026-09-21.txt", f"""OCIO26 · G1 · grupo focal · 2026-09-21
{FICT}
Exportado de Fathom. Moderó Sara Quintero.

0:00 - Sara Quintero
  Bienvenidas. Para empezar, ¿qué hicieron el fin de semana pasado con la familia?

0:35 - Marcela
  Los domingos es fútbol. Mi hijo juega en una escuelita y vamos todos a verlo.

1:20 - Diana
  Nosotros nos fuimos al parque a hacer picnic, llevamos comida y pasamos la tarde allá.

2:05 - Jorge
  Nosotros nos quedamos en casa viendo películas. Con dos niños chiquitos salir es un operativo.

3:10 - Sara Quintero
  ¿Y quién decide el plan en la casa?

3:25 - Marcela
  Yo decido y ellos se suben, la verdad.

4:00 - Diana
  Lo hablamos entre los dos, mi esposo y yo, y a veces le preguntamos a la niña.

4:40 - Jorge
  Yo propongo, pero mi esposa decide.

5:30 - Sara Quintero
  ¿Qué les gustaría hacer y no hacen?

5:50 - Marcela
  Ir a cine más seguido, pero para cuatro sale carísimo.

6:30 - Diana
  Ir a la finca de mis papás, pero queda a tres horas.

7:15 - Jorge
  Salir más, pero llegamos muertos el viernes.
""")
print("material written to", OUT)
