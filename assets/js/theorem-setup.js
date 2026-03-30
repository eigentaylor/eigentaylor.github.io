/**
 * Minimal theorem/lemma/definition auto-numbering and \label/\ref cross-references.
 * Activate by adding `theorems: true` to front matter.
 *
 * - Finds <strong> tags matching "Type [N]:" (Definition, Lemma, etc.)
 * - Works in blockquotes (> **Lemma:**) or plain paragraphs (**Lemma:**)
 * - Assigns per-type auto-numbers and stable IDs for linking
 * - Collects \label{key} from blockquote text and removes the visible marker
 * - Resolves \ref{key} anywhere in the article into clickable links
 *
 * IMPORTANT: This script must run BEFORE MathJax. Since both are loaded with
 * `defer`, document order determines execution order. MathJax's processRefs
 * will consume \ref{} in text mode if we don't get there first.
 */
(function () {
    var article = document.querySelector("d-article");
    if (!article) return;

    var labelMap = {}; // key -> { number, id, type }
    var counters = {}; // type -> count

    // list of supported theorem types
    var theoremTypes = ["Definition", "Lemma", "Theorem", "Remark", "Corollary", "Proposition", "Conjecture", "Axiom"];


    // Match: "Type", optional number, optional parenthetical, then ":"
    var typeRe =
        /^(Definition|Lemma|Theorem|Remark|Corollary|Proposition|Conjecture|Axiom|Example)\s*\d*\s*(\([^)]*\))?\s*:$/i;
    var labelRe = /\\label\{([^}]+)\}/;

    /* ── Step 1: Auto-number theorem blocks and collect labels ── */
    var strongs = article.querySelectorAll("strong, b");
    for (var i = 0; i < strongs.length; i++) {
        var strong = strongs[i];
        var match = strong.textContent.match(typeRe);
        if (!match) continue;

        var type = match[1];
        var paren = match[2] || "";
        var key = type.toLowerCase();

        counters[key] = (counters[key] || 0) + 1;
        var num = counters[key];
        var id = "thm-" + key + "-" + num;

        var block = strong.closest("blockquote") || strong.parentElement;

        strong.textContent = type + " " + num + (paren ? " " + paren : "") + ":";
        block.id = id;
        block.classList.add("theorem-block");

        // Walk text nodes inside this block to find \label{key}
        var tw = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
        var tnode;
        while ((tnode = tw.nextNode())) {
            var lm = tnode.textContent.match(labelRe);
            if (lm) {
                labelMap[lm[1]] = { number: num, id: id, type: type };
                tnode.textContent = tnode.textContent.replace(/\s*\\label\{[^}]+\}/, "");
            }
        }
    }

    /* ── Step 2: Resolve \ref{key} into clickable links ── */
    var tw2 = document.createTreeWalker(article, NodeFilter.SHOW_TEXT);
    var toReplace = [];
    var tnode2;
    while ((tnode2 = tw2.nextNode())) {
        if (tnode2.textContent.indexOf("\\ref{") !== -1) {
            toReplace.push(tnode2);
        }
    }

    for (var j = 0; j < toReplace.length; j++) {
        var textNode = toReplace[j];
        var parts = textNode.textContent.split(/(\\ref\{[^}]+\})/);
        if (parts.length <= 1) continue;

        var frag = document.createDocumentFragment();
        for (var k = 0; k < parts.length; k++) {
            var rm = parts[k].match(/^\\ref\{([^}]+)\}$/);
            if (rm && labelMap[rm[1]]) {
                var info = labelMap[rm[1]];
                var link = document.createElement("a");
                link.href = "#" + info.id;
                link.textContent = info.number;
                link.className = "thm-ref";
                link.title = info.type + " " + info.number;
                frag.appendChild(link);
            } else {
                frag.appendChild(document.createTextNode(parts[k]));
            }
        }
        textNode.parentNode.replaceChild(frag, textNode);
    }
})();
