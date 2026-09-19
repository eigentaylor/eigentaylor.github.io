"""Chooser names, published reference ranges, and the strategy axis.

Presentation constants lifted from cells 50, 52 and 57 of `vse_simulation.ipynb`. Nothing
here computes anything; these are the labels and the outside numbers this project checks
itself against."""

import re


# How each chooser's internal name is written in a table (cell 50).
__all__ = [
    "CHOOSER_LABELS",
    "label_for",
    "KNOWN_RANGES",
    "STRATEGY_AXIS",
]


CHOOSER_LABELS = {
    "honBallot": "100% honest",
    "stratBallot": "100% strategic",
    "Oss.hon_strat.": "100% one-sided strategic",
    "smartOss": "smart one-sided strategic",
}


def label_for(chooser):
    if chooser in CHOOSER_LABELS:
        return CHOOSER_LABELS[chooser]
    m = re.match(r"^Prob\.strat(\d+)_hon\d+\.$", chooser)
    if m:
        return f"{m.group(1)}% strategic"
    m = re.match(r"^Oss\.hon_Prob\.strat(\d+)_hon\d+\.\.$", chooser)
    if m:
        return f"{m.group(1)}% one-sided strategic"
    return chooser  # fall back to the raw internal name: still shown, not dropped


# VSE ranges documented elsewhere for these methods, for the section 11 sanity check
# against published values (cell 52).
KNOWN_RANGES = {
    "Plurality": "~75%",
    "Approval": "89-95%",
    "STAR": "91-98%",
    "Condorcet (Schulze)": "86-98%",
    "RCV (IRV)": "up to 87%",
    "Score5": "84-96%"
}


# Where each chooser sits on the "% of electorate voting strategically" axis (cell 57).
STRATEGY_AXIS = {
    "100% honest": 0,
    "25% strategic": 25,
    "50% strategic": 50,
    "75% strategic": 75,
    "100% strategic": 100,
}
