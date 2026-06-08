/**
 * Minimal theorem/lemma/definition auto-numbering and \label/\ref cross-references.
 * Activate by adding `theorems: true` to front matter.
 * Optional front matter in Distill posts: `theorem_numbering: shared|separate`
 *
 * - Finds <strong> tags matching "Type [N]:" (Definition, Lemma, etc.)
 * - Works in blockquotes (> **Lemma:**) or plain paragraphs (**Lemma:**)
 * - Assigns auto-numbers (shared or per-type) and stable IDs for linking
 * - Collects \label{key} from theorem blocks and removes visible markers
 * - Resolves \ref{key} anywhere in the article into clickable links
 * - Supports theorem restatements via "Type \ref{key}:" without renumbering
 * - Supports proof links via \proofref{key} -> #proof-key
 *
 * IMPORTANT: This script must run BEFORE MathJax. MathJax may consume \ref{}
 * in text mode if this parser does not run first.
 */
(function () {
    var article = document.querySelector("d-article");
    if (!article) return;
    var thisScript = document.currentScript || document.querySelector('script[src*="theorem-setup.js"]');
    var numberingModeRaw = thisScript && thisScript.dataset ? thisScript.dataset.theoremNumbering : "";
    var numberingMode = numberingModeRaw === "separate" ? "separate" : "separate"; // default to "shared" if not specified or invalid

    var labelMap = {}; // key -> { number, id, type }
    var counters = {}; // theorem-type -> count
    var sharedCounter = 0;
    var pendingRestatements = [];

    var theoremTypes = ["Definition", "Lemma", "Theorem", "Remark", "Corollary", "Proposition", "Conjecture", "Axiom", "Example", "Assumption"];
    var typeReStr = theoremTypes.join("|");

    // Match: "Type", optional explicit number, optional parenthetical, then ":"
    var typeRe = new RegExp("^(" + typeReStr + ")\\s*\\d*\\s*(\\([^)]*\\))?\\s*:$", "i");
    // Match restatement: "Type \ref{key}:", optional parenthetical
    var restatementRe = new RegExp("^(" + typeReStr + ")\\s*\\\\ref\\{([^}]+)\\}\\s*(\\([^)]*\\))?\\s*:$", "i");
    var labelRe = /\\label\{([^}]+)\}/g;

    function toAnchorToken(str) {
        var token = String(str || "")
            .trim()
            .toLowerCase()
            .replace(/[^a-z0-9_-]+/g, "-")
            .replace(/^-+|-+$/g, "");
        return token || "item";
    }

    function warn(msg) {
        if (window.console && window.console.warn) {
            window.console.warn("[theorem-setup] " + msg);
        }
    }

    function safeSetId(el, idBase) {
        var id = idBase;
        var n = 2;
        while (document.getElementById(id) && document.getElementById(id) !== el) {
            id = idBase + "-" + n;
            n += 1;
        }
        el.id = id;
        return id;
    }

    function shouldSkipTextNode(node) {
        if (!node || !node.parentElement) return true;
        return !!node.parentElement.closest("pre, code, kbd, samp, script, style, textarea");
    }

    function collectAndStripLabels(block) {
        var labels = [];
        var tw = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
        var tnode;

        while ((tnode = tw.nextNode())) {
            var text = tnode.textContent;
            var match;
            var found = false;

            labelRe.lastIndex = 0;
            while ((match = labelRe.exec(text))) {
                labels.push(match[1]);
                found = true;
            }

            if (found) {
                tnode.textContent = text.replace(/\s*\\label\{[^}]+\}/g, "");
            }
        }

        return labels;
    }

    function registerLabels(labels, info) {
        for (var i = 0; i < labels.length; i++) {
            var key = labels[i];
            if (labelMap[key]) {
                warn("Duplicate label \\label{" + key + "}; keeping the first definition.");
                continue;
            }
            labelMap[key] = {
                number: info.number,
                id: info.id,
                type: info.type,
            };
        }
    }

    function findReferenceKeyFromPreviousBlock(block) {
        var prev = block.previousElementSibling;
        while (prev) {
            if (prev.dataset && prev.dataset.restatementOf) return prev.dataset.restatementOf;
            if (prev.dataset && prev.dataset.labelKey) return prev.dataset.labelKey;
            prev = prev.previousElementSibling;
        }
        return null;
    }

    function assignProofAnchor(proofBlock) {
        if (!proofBlock) return;
        proofBlock.classList.add("proof-block");
        if (proofBlock.id) return;

        var refKey = findReferenceKeyFromPreviousBlock(proofBlock);
        if (refKey) {
            safeSetId(proofBlock, "proof-" + toAnchorToken(refKey));
        }
    }

    // Step 1: Number ordinary theorem headers and collect labels.
    var strongs = article.querySelectorAll("strong, b");
    for (var i = 0; i < strongs.length; i++) {
        var strong = strongs[i];
        var text = strong.textContent.trim();

        var restatementMatch = text.match(restatementRe);
        if (restatementMatch) {
            pendingRestatements.push({
                strong: strong,
                type: restatementMatch[1],
                refKey: restatementMatch[2],
                paren: restatementMatch[3] || "",
            });
            continue;
        }

        var match = text.match(typeRe);
        if (!match) continue;

        var type = match[1];
        var paren = match[2] || "";
        var typeKey = type.toLowerCase();

        var num;
        if (numberingMode === "separate") {
            counters[typeKey] = (counters[typeKey] || 0) + 1;
            num = counters[typeKey];
        } else {
            sharedCounter += 1;
            num = sharedCounter;
        }

        var block = strong.closest("blockquote") || strong.parentElement;
        if (!block) continue;

        strong.textContent = type + " " + num + (paren ? " " + paren : "") + ":";

        safeSetId(block, "thm-" + typeKey + "-" + num);
        block.classList.add("theorem-block");
        block.dataset.theoremType = type;
        block.dataset.theoremNumber = String(num);

        var labels = collectAndStripLabels(block);
        if (labels.length > 0) {
            var canonical = labels[0];
            var labeledId = safeSetId(block, "thm-" + toAnchorToken(canonical));
            block.dataset.labelKey = canonical;

            registerLabels(labels, {
                number: num,
                id: labeledId,
                type: type,
            });
        }
    }

    // Step 1.5: Resolve theorem restatements without incrementing counters.
    for (var r = 0; r < pendingRestatements.length; r++) {
        var rest = pendingRestatements[r];
        var info = labelMap[rest.refKey];
        if (!info) {
            warn("Could not resolve \\ref{" + rest.refKey + "} in theorem restatement.");
            continue;
        }

        var restBlock = rest.strong.closest("blockquote") || rest.strong.parentElement;
        if (!restBlock) continue;

        rest.strong.textContent = rest.type + " " + info.number + (rest.paren ? " " + rest.paren : "") + ":";

        restBlock.classList.add("theorem-block", "theorem-restatement");
        restBlock.dataset.restatementOf = rest.refKey;
        restBlock.dataset.theoremType = rest.type;
        restBlock.dataset.theoremNumber = String(info.number);
        safeSetId(restBlock, "thm-restatement-" + toAnchorToken(rest.refKey));

        var restLabels = collectAndStripLabels(restBlock);
        if (restLabels.length > 0) {
            registerLabels(restLabels, {
                number: info.number,
                id: restBlock.id,
                type: rest.type,
            });
        }
    }

    // Step 1.6: Assign proof anchors when a block starts with "Proof".
    for (var p = 0; p < strongs.length; p++) {
        var strongNode = strongs[p];
        if (!/^Proof\s*:?$/i.test(strongNode.textContent.trim())) continue;

        var proofBlock = strongNode.closest("blockquote") || strongNode.parentElement;
        assignProofAnchor(proofBlock);
    }

    // Step 1.7: Assign proof anchors for dedicated proof disclosure widgets.
    var proofDisclosures = article.querySelectorAll("details.proof-disclosure");
    for (var d = 0; d < proofDisclosures.length; d++) {
        assignProofAnchor(proofDisclosures[d]);
    }

    // Step 2: Resolve \ref{key} and \proofref{key} into links.
    var tw2 = document.createTreeWalker(article, NodeFilter.SHOW_TEXT);
    var toReplace = [];
    var tnode2;

    while ((tnode2 = tw2.nextNode())) {
        if (shouldSkipTextNode(tnode2)) continue;
        if (tnode2.textContent.indexOf("\\ref{") !== -1 || tnode2.textContent.indexOf("\\proofref{") !== -1) {
            toReplace.push(tnode2);
        }
    }

    for (var j = 0; j < toReplace.length; j++) {
        var textNode = toReplace[j];
        var parts = textNode.textContent.split(/(\\proofref\{[^}]+\}|\\ref\{[^}]+\})/);
        if (parts.length <= 1) continue;

        var frag = document.createDocumentFragment();
        for (var k = 0; k < parts.length; k++) {
            var part = parts[k];

            var proofMatch = part.match(/^\\proofref\{([^}]+)\}$/);
            if (proofMatch) {
                var proofKey = proofMatch[1];
                var proofLink = document.createElement("a");
                proofLink.href = "#proof-" + toAnchorToken(proofKey);
                proofLink.textContent = "Proof";
                proofLink.className = "proof-ref";
                proofLink.title = "Proof in appendix";
                frag.appendChild(proofLink);
                continue;
            }

            var refMatch = part.match(/^\\ref\{([^}]+)\}$/);
            if (refMatch) {
                var refKey = refMatch[1];
                if (labelMap[refKey]) {
                    var theoremInfo = labelMap[refKey];
                    var link = document.createElement("a");
                    link.href = "#" + theoremInfo.id;
                    link.textContent = theoremInfo.number;
                    link.className = "thm-ref";
                    link.title = theoremInfo.type + " " + theoremInfo.number;
                    frag.appendChild(link);
                } else {
                    warn("Could not resolve \\ref{" + refKey + "}.");
                    frag.appendChild(document.createTextNode(part));
                }
                continue;
            }

            frag.appendChild(document.createTextNode(part));
        }

        if (textNode.parentNode) {
            textNode.parentNode.replaceChild(frag, textNode);
        }
    }
})();
