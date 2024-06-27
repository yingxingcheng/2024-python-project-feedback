import numpy as np
import schemdraw
import schemdraw.elements as elm
import matplotlib
import matplotlib.pyplot as plt
from pprint import pprint
from schemutils import convert_to_graph, add_solution


def demo_drawing():
    d = schemdraw.Drawing(unit=5)
    d += elm.SourceV().label("20V")
    d += elm.Resistor().right().label("400Ω")
    d += elm.Dot()
    d.push()
    d += elm.Resistor().down().label("100Ω")
    d += elm.Dot()
    d.pop()
    d += elm.Line().right()
    d += elm.SourceI().down().label("1A")
    # Draw the bottom wires in two steps, such that they
    # have a start or end point at the node at the bottom
    # dot.
    d += elm.Line().left()
    d += elm.Line().left()
    return d


d = demo_drawing()
# d.draw()
d.save("demo.svg")
