(function () {
    function withMathJax(container, onSuccess) {
        if (!container) return;

        if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
            window.MathJax.typesetPromise([container])
                .then(function () {
                    if (typeof onSuccess === "function") onSuccess();
                })
                .catch(function () {
                    // Ignore typesetting failures to avoid breaking interactions.
                });
            return;
        }

        // MathJax can load after this script; retry briefly before giving up.
        var attempts = 0;
        var maxAttempts = 30;
        var interval = setInterval(function () {
            attempts += 1;
            if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
                clearInterval(interval);
                window.MathJax.typesetPromise([container])
                    .then(function () {
                        if (typeof onSuccess === "function") onSuccess();
                    })
                    .catch(function () {
                        // Ignore typesetting failures to avoid breaking interactions.
                    });
            } else if (attempts >= maxAttempts) {
                clearInterval(interval);
            }
        }, 100);
    }

    function ensureTypeset(details) {
        if (!details || details.dataset.mathTypeset === "1") return;

        var content = details.querySelector(".proof-content") || details;
        withMathJax(content, function () {
            details.dataset.mathTypeset = "1";
        });
    }

    function maybeOpenFromHash() {
        var hash = window.location.hash;
        if (!hash || hash.length < 2) return;

        var target = document.getElementById(hash.slice(1));
        if (!target) return;

        var proofDetails = target.closest("details.proof-disclosure");
        if (!proofDetails) return;

        if (!proofDetails.open) {
            proofDetails.open = true;
        }
        ensureTypeset(proofDetails);
    }

    function initProofDisclosures() {
        var proofDetails = document.querySelectorAll("details.proof-disclosure");
        for (var i = 0; i < proofDetails.length; i++) {
            var details = proofDetails[i];
            details.addEventListener("toggle", function (event) {
                if (event.currentTarget.open) {
                    ensureTypeset(event.currentTarget);
                }
            });
        }

        maybeOpenFromHash();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initProofDisclosures);
    } else {
        initProofDisclosures();
    }

    window.addEventListener("hashchange", maybeOpenFromHash);
})();
