"""Epistemic noise (section 2 of `vse_simulation.ipynb`, cell 23).

Voters cast ballots on a *perceived* electorate: their true utilities blended with
noise at a knowledge level rho. Original to this project, not part of vse-sim.
"""

import random

import numpy as np
from numpy.lib.scimath import sqrt

from .vendored.voter_models import Electorate, Voter


def make_perceived_electorate(true_electorate, rho, noise=None):
    """Build the Electorate voters actually cast ballots on, given their true
    utilities and a knowledge/clarity parameter rho (see the formula above).

    At rho >= 1.0, returns true_electorate unchanged (no noise drawn at all),
    so a rho=1.0 run is bit-for-bit identical to the no-noise baseline.

    noise -- optional pre-drawn standard-normal values, one list per voter (same shape as
    true_electorate). When given, reuses this EXACT noise instead of drawing fresh -- lets a
    caller build several perceived electorates at different rho from the SAME underlying
    misperception (see draw_noise below), instead of each rho drawing an unrelated random
    perception. Section 21's continuous runoff_rho sweep needs this: without it, "how does the
    runoff improve as its own information level rises" is contaminated by "we also redrew a
    completely different random misperception at every point."
    """
    if rho >= 1.0:
        return true_electorate
    noise_weight = sqrt(1 - rho * rho)
    perceived = []
    for i, voter in enumerate(true_electorate):
        sigma = np.std(voter)
        voter_noise = noise[i] if noise is not None else [random.gauss(0, 1) for _ in voter]
        perceived.append(Voter(rho * u + noise_weight * sigma * z for u, z in zip(voter, voter_noise)))
    return Electorate(perceived)


def draw_noise(true_electorate):
    """One standard-normal draw per (voter, candidate) -- the raw misperception
    make_perceived_electorate scales by rho. Draw once per election, then pass the same `noise`
    into multiple make_perceived_electorate calls at different rho to keep them paired."""
    return [[random.gauss(0, 1) for _ in voter] for voter in true_electorate]
