# Group 02

## Practical details

Students:

- Sandra Grabisch
- Nico Schöck

### Wednesday (July 03)

Summary of feedback after first week

Below, you'll find a summary of our discussion.

**Activity:**

- Existing useful code for tasks (a) and (b) from the basic requirement.
- Customizing the labels of nodes and edges. Good! A convenient way to do this is by using the `convert_to_graph` function.

### Wednesday (July 10)

Summary of feedback after second week

Below, you'll find a summary of our discussion.

**Activity:**

- Trying to finish task (c), but there are some issues in the code where the matrix A is constructed.

## Questions

- Nico and I are currently struggling with implementing subtask e) on the circuit solver project. Our code is attached in this email and we have no clue why we don‘t get a picture as output for subtask e). Can you help us or give us a hint why our code isn‘t working?

The issues is the format `unknowns` are not correct. See `add_solution` in `schemutils` for details. I've attached the correct one.

The old python file:

```python
def visualize_solution(s, loesung, spannung_unbekannte, stromstaerke_unbekannte):
    # Kombinieren der Listen der Spannungs- und Stromunbekannten
    unbekannte = [(float(knoten[0]),) for knoten in sorted(vertices)] + [
        (float(kante[0]),) for kante in sorted(edges.keys())
    ]

    # Sicherstellen, dass loesung ein np.ndarray ist
    x = np.concatenate(
        [loesung[: len(spannung_unbekannte)], loesung[len(spannung_unbekannte) :]]
    )

    # Fügen Sie die Lösung zur Zeichnung hinzu
    s = schemutils.add_solution(s, unbekannte, x)

    # Zeichnung anzeigen
    s.draw()
```

The correct one:

```python
def visualize_solution(s, loesung, spannung_unbekannte, stromstaerke_unbekannte):
    unknowns = sorted(vertices) + sorted(edges)
    s = schemutils.add_solution(s, unknowns, loesung)

    # Zeichnung anzeigen
    s.draw()
```

```python
# Erstellung des linearen Gleichungssystems
def lgs_erstellung(vertices, edges):
    anzahl_knoten = len(vertices)
    anzahl_kanten = len(edges)

    # Erstellung der Koeffizentenmatrix sowie der rechten Seite des linearen Gleichungssystems
    A = np.zeros((anzahl_knoten + anzahl_kanten, anzahl_knoten + anzahl_kanten))
    b = np.zeros(anzahl_knoten + anzahl_kanten)

    knoten_index = {knoten: idx for idx, knoten in enumerate(sorted(vertices))}
    kante_index = {kante: idx for idx, kante in enumerate(sorted(edges.keys()))}

    # Berechung der Spannung mit der Knoten-Gleichungen (Kirchhoff'sches Knotenstromgesetz)
    for knoten, knoten_idx in knoten_index.items():
        reihe = knoten_idx
        for kante, (komponente, wert) in edges.items():
            xa, ya, xb, yb = kante
            if (xa, ya) == knoten:
                spalte = anzahl_knoten + kante_index[kante]
                A[reihe, spalte] = 1
            elif (xb, yb) == knoten:
                spalte = anzahl_knoten + kante_index[kante]
                A[reihe, spalte] = -1

    # Berechung der Stromstärke mit der Kanten-Gleichungen (Verhalten der einzelnen Komponenten)
    for kante, (komponente, wert) in edges.items():
        # you can print the info to check if it is correct.
        print(komponente)
        xa, ya, xb, yb = kante
        reihe = anzahl_knoten + kante_index[kante]

        # Draht
        if komponente == "-":
            spalte_a = knoten_index[(xa, ya)]
            spalte_b = knoten_index[(xb, yb)]
            A[reihe, spalte_a] = 1
            A[reihe, spalte_b] = -1
            b[reihe] = 0
        # Widerstand
        elif komponente == "Ω":  # use Ω instead of Ω
            spalte_a = knoten_index[(xa, ya)]
            spalte_b = knoten_index[(xb, yb)]
            A[reihe, spalte_a] = 1
            A[reihe, spalte_b] = -1
            A[reihe, reihe] = -wert
            b[reihe] = 0
        # Spannungsquelle
        elif komponente == "V":
            spalte_a = knoten_index[(xa, ya)]
            spalte_b = knoten_index[(xb, yb)]
            A[reihe, spalte_a] = 1
            A[reihe, spalte_b] = -1
            b[reihe] = wert
        # Stromquelle
        elif komponente == "A":
            A[reihe, reihe] = 1
            b[reihe] = wert

    return A, b

```
