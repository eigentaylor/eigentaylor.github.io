"""Practical vs. statistical significance, and the log of every gap reported.

A confidence interval that excludes zero says a difference is real. It does not say the
difference matters: a gap of 0.1 percentage points can be arbitrarily well established and
still be irrelevant to which voting method anyone should adopt. `_classify_gap` crosses the
two questions -- does the interval exclude zero, and does it sit inside the practical band
`config.GAP_THRESHOLD_PP` -- into the five-way taxonomy every "Significant?" column uses.

`SignificanceLog` replaces what was a module-level `defaultdict` appended to by seven cells
scattered through the notebook and then read by section 27, which re-checks every gap at a
stricter confidence level. Because a CI half-width scales linearly with z for a fixed
standard error, that re-check is arithmetic on what is already computed, not a new run:

    ci_at_z = ci_95 * (z / 1.96)

The hazard is that section 27 has no way to know whether all seven registering cells
actually ran -- run it alone and it silently under-reports. So the log now carries an
`expect()` manifest and `check_complete()` raises instead."""

from collections import defaultdict

from scipy.stats import norm

from .. import config as cfg

Z_95 = 1.96
Z_99 = norm.ppf(0.995)  # two-sided 99% CI multiplier, ~2.576


__all__ = [
    "SignificanceLog",
    "Z_95",
    "Z_99",
    "TAXONOMY_LABELS",
    "_classify_gap",
    "_verdict_text",
]


class SignificanceLog:
    """Every paired-gap row rendered anywhere, so section 27 can re-check them all.

    Keyed by (table_title, row_label) and overwriting rather than appending -- re-running a
    single cell without a full restart would otherwise pile up duplicates of its own rows.
    """

    def __init__(self):
        self.rows = defaultdict(list)
        self.expected = set()

    def expect(self, *table_titles):
        """Declare that these tables must have registered before section 27 reads the log."""
        self.expected.update(table_titles)

    def register(self, table_title, row_label, gap_pp, ci95_pp,
                 positive_name, negative_name, spotlight=False):
        """Record one already-displayed paired-gap row (gap and 95% CI half-width, both in
        percentage points).

        `positive_name` is whichever side a positive `gap_pp` favors, `negative_name` the
        other -- so section 27 can report "STAR better by 2.3pp" rather than a bare "Yes".
        `spotlight` marks a curated set of headline comparisons it highlights separately
        from its comprehensive not-significant-at-99% table.
        """
        entry = (row_label, gap_pp, ci95_pp, positive_name, negative_name, spotlight)
        rows = self.rows[table_title]
        for i, existing in enumerate(rows):
            if existing[0] == row_label:
                rows[i] = entry
                return
        rows.append(entry)

    def check_complete(self):
        """Raise if a table that should have registered rows has not.

        Section 27's whole job is to be comprehensive. Quietly reporting on half the
        comparisons because half the cells above it were skipped would be worse than
        failing.
        """
        missing = sorted(t for t in self.expected if not self.rows.get(t))
        if missing:
            raise RuntimeError(
                "the significance log is incomplete -- these tables have not been rendered "
                f"yet, so section 27 would under-report: {missing}. Run the cells above it.")
        return self

    def items(self):
        return self.rows.items()

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        return iter(self.rows)

    def __getitem__(self, key):
        return self.rows[key]


TAXONOMY_LABELS = {
    "DECISIVE": "Decisive", # CI is entirely beyond the threshold. There is a clear and practically significant difference between the two methods
    "NARROW_EDGE": "Narrow edge", # CI does not contain 0 but is firmly within the threshold
    "AMBIGUOUS_EDGE": "Ambiguous edge", # CI does not contain 0 but the gap could be outside the threshold
    "INDISTINGUISHABLE": "Indistinguishable", # CI contains 0 but is firmly within the threshold. Even if a direction exists, it is not likely of any practical significance
    "INCONCLUSIVE": "Inconclusive", # CI contains 0 and is potentially outside the threshold. If this is a crucial result, more niters are suggested.
}
# Edit TAXONOMY_LABELS above to change every table's wording at once. Edit GAP_THRESHOLD_PP in
# Section 5 (Parameters) to move the practical-significance bar everywhere at once.

def _classify_gap(gap_pp, ci_pp, threshold_pp=None):
    """5-way practical-significance taxonomy: cross gap-vs-CI (does the CI exclude 0?) with
    CI-vs-band (is the CI entirely inside/outside +/-threshold_pp?)."""
    threshold_pp = cfg.GAP_THRESHOLD_PP if threshold_pp is None else threshold_pp
    lo, hi = gap_pp - ci_pp, gap_pp + ci_pp
    contains_zero = lo <= 0 <= hi
    inside_band = (lo >= -threshold_pp) and (hi <= threshold_pp)
    outside_band = (lo > threshold_pp) or (hi < -threshold_pp)
    if not contains_zero:
        return "NARROW_EDGE" if inside_band else ("DECISIVE" if outside_band else "AMBIGUOUS_EDGE")
    return "INDISTINGUISHABLE" if inside_band else "INCONCLUSIVE"

def _verdict_text(gap_pp, ci_pp, positive_name, negative_name, threshold_pp=None):
    """Shared replacement for every hand-rolled "Significant?" string in this notebook --
    returns (bucket, display_text). positive_name is whichever side a positive gap_pp favors,
    same convention as _register_significance."""
    bucket = _classify_gap(gap_pp, ci_pp, threshold_pp)
    label = TAXONOMY_LABELS[bucket]
    if bucket in ("DECISIVE", "NARROW_EDGE", "AMBIGUOUS_EDGE"):
        better = positive_name if gap_pp > 0 else negative_name
        return bucket, f"{label} ({better} better)"
    return bucket, label
