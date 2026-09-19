"""Copied, with one small addition, from the `vse_sim` Python package at
https://github.com/electionscience/vse-sim. Extracted verbatim from section 1 of
`vse_simulation.ipynb` (cell 21); see that notebook for the original prose.

Method presets and reproducibility (`simulation.py` upstream, excerpt).
"""

import random

import numpy as np

from .strategies import OssChooser, ProbChooser, beHon, beStrat


import hashlib


def seedRandomGenerators(seed):
    """Seed the Python and NumPy global generators deterministically."""
    random.seed(seed)
    numpy_seed = int.from_bytes(
        hashlib.sha256(str(seed).encode()).digest()[:4], byteorder="little"
    )
    np.random.seed(numpy_seed)


# The battery of honest/strategic/mixed choosers used for every published VSE number.
baseRuns = [
           OssChooser([beHon, ProbChooser([(1/2, beStrat), (1/2, beHon)])]),

           ProbChooser([(1/4, beStrat), (3/4, beHon)]),
           ProbChooser([(1/2, beStrat), (1/2, beHon)]),
           ProbChooser([(3/4, beStrat), (1/4, beHon)]),
           ]
