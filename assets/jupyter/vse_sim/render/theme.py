"""Plot styling, shared by every chart (cell 4 of `vse_simulation.ipynb`).

`dark_background` only reskins the rcParams-driven defaults -- axes, ticks, grid, spines,
the legend frame. Anything that passes a literal colour has to flip through `FG_COLOR` /
`MUTED_COLOR` instead, which is why those exist alongside the style."""

import matplotlib.pyplot as plt


# Set to False if you want light-background plots (e.g. to match a light blog theme).
__all__ = [
    "DARK_MODE",
    "FG_COLOR",
    "MUTED_COLOR",
]


DARK_MODE = True
if DARK_MODE:
    plt.style.use("dark_background")

# "dark_background" only reskins rcParams-driven defaults (axes, ticks, grid, spines,
# legend frame). Anything below that passes a literal "black"/"white"/"dimgray" color
# doesn't respond to the switch and must flip through these instead.
FG_COLOR = "white" if DARK_MODE else "black"
MUTED_COLOR = "lightgray" if DARK_MODE else "dimgray"
