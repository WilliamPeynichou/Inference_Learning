"""Generate three study figures without external dependencies."""

import csv
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "donnees"
FIGURES = ROOT / "figures"


def text(x, y, value, style="body", anchor="start"):
    return f'<text x="{x}" y="{y}" class="{style}" text-anchor="{anchor}">{escape(str(value))}</text>'


def line(x1, y1, x2, y2, color="#c9d0d7"):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}"/>'


def figure(file, height, index, kind, title, description, content):
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>', f'<desc id="desc">{escape(description)}</desc>',
        '''<style>
  text{font-family:system-ui,sans-serif;fill:#182637}
  .title{font-family:Georgia,serif;font-size:32px;font-weight:700}
  .body{font-size:16px}.note{font-size:14px;fill:#405266}
  .meta{font-size:13px;letter-spacing:1.4px;font-weight:700;fill:#345577}
  .strong{font-size:16px;font-weight:700}.light{font-size:16px;font-weight:700;fill:white}
</style>''',
        f'<rect width="960" height="{height}" fill="#fff"/>',
        text(48, 40, f"FIGURE {index:02d}    /    {kind}", "meta"), text(48, 82, title, "title"),
        line(48, 105, 912, 105, "#8695a4"), *content, "</svg>",
    ]
    (FIGURES / file).write_text("\n".join(svg) + "\n", encoding="utf-8")


def pilot(rows):
    # Segment decomposition: pilot report; totals: CSV.
    series = [("auto-complet", "Classic chat", 8), ("recalcule", "RLM", 6)]
    totals = [int(rows[key]["coups_validation_n1"]) for key, _, _ in series]
    gap = totals[0] - totals[1]
    percent = f"{100 * gap / totals[0]:.1f}"
    axis_max = ((max(totals) + 4) // 5) * 5
    x0, scale = 244, 560 / axis_max
    items = [text(48, 138, "ARC-AGI-3 | ls20 | Two sequential trials, one game", "note")]
    for x, color, label in [(244, "#294e70", "To pattern"), (443, "#d7e1ea", "Pattern to frame")]:
        items += [f'<rect x="{x}" y="158" width="14" height="14" fill="{color}"/>', text(x + 23, 170, label, "note")]
    for tick in range(0, axis_max + 1, 5):
        x = round(x0 + tick * scale, 2)
        items += [line(x, 190, x, 309), text(x, 331, tick, "note", "middle")]
    for y, (_, label, first), total in zip((218, 277), series, totals):
        items.append(text(48, y + 5, label, "strong"))
        for offset, count, color, style in [(0, first, "#294e70", "light"), (first, total - first, "#d7e1ea", "strong")]:
            x, width = x0 + offset * scale, count * scale
            items += [f'<rect x="{x:.2f}" y="{y-16}" width="{width:.2f}" height="32" fill="{color}"/>', text(round(x + width/2, 2), y + 6, count, style, "middle")]
        items.append(text(round(x0 + total * scale + 15, 2), y + 6, total, "strong"))
    items += [text(524, 361, "Game moves to first-level completion", "body", "middle"),
              line(48, 385, 912, 385), text(48, 414, f"Descriptive difference: -{gap} moves (-{percent}%), entirely before the pattern.", "strong"),
              text(48, 443, "Tool attribution unconfirmed. No controlled A/B or chat-turn measurements.", "note"),
              text(48, 469, "Sources: essais.csv and pilot report. Raw logs unavailable.", "note")]
    figure("ls20-coups.svg", 496, 1, "DESCRIPTIVE RESULT", f"Level 1: {totals[0]} then {totals[1]} game moves",
           f"Classic chat: {totals[0]} moves, 8 before the pattern. RLM: {totals[1]} moves, 6 before the pattern. The second segment remains 7. Uncontrolled comparison.", items)


def mechanism():
    steps = [("Observation", "Game grids"), ("Python state", "Objects and functions"), ("Computation", "Breadth-first search"), ("Verification", "Confirmed moves")]
    items = [text(48, 138, "Interpretive diagram of the ls20 pilot, not a performance measure.", "note")]
    for index, (label, detail) in enumerate(steps):
        x = 48 + index * 220
        items += [f'<rect x="{x}" y="173" width="204" height="87" fill="#f3f6f9" stroke="#aebcca"/>',
                  text(x + 14, 204, label, "strong"), text(x + 14, 234, detail, "note")]
        if index < len(steps) - 1:
            items.append(text(x + 212, 220, "→", "strong", "middle"))
    items += [text(48, 298, "Reuse: retained grids and functions support path recalculation.", "body"),
              text(48, 327, "To test: reconstruction savings and transfer to an unseen game.", "note"),
              text(48, 354, "Source: pilot report. No weight update or causal effect established.", "note")]
    figure("rlm-mecanisme.svg", 382, 2, "CONCEPTUAL DIAGRAM", "From observation to reuse",
           "The game grid is represented as Python objects. Breadth-first search uses retained objects and functions. The runner confirms moves. Transfer remains untested.", items)


def hypotheses():
    rows = [
        ("Turns and reuse", "Longer perceived cold-start workflow,", "then shorter as Compute is used.", "Calls, time, and objects reused", "per validated task at comparable quality."),
        ("Tokens and cache", "Little visible output; input appears", "dominant. Python output role is unknown.", "Separate input, output, reasoning,", "provider cache, and Python outputs sent."),
        ("Provider limits", "Limits perceived later on Opus 5.5,", "Fable 5.2, and 6.2 Sol.", "Work before blocking and resumption time,", "by model and quota window."),
    ]
    items = [text(48, 139, "Reported observation", "meta"), text(492, 139, "Proposed measure", "meta"), line(472, 121, 472, 403)]
    for y, (label, a, b, c, d) in zip((168, 247, 326), rows):
        items += [line(48, y - 10, 912, y - 10), text(48, y + 11, label, "strong"), text(48, y + 34, a, "note"),
                  text(48, y + 54, b, "note"), text(492, y + 22, c), text(492, y + 45, d)]
    items += [line(48, 403, 912, 403), text(48, 433, "Source: unquantified user observations, separate from pilot results.", "note")]
    figure("rlm-hypotheses.svg", 462, 3, "MEASUREMENT PLAN", "Three observations to test against traces",
           "Qualitative hypotheses about cold and warm turns, tokens and cache, and provider limits. No quantified results.", items)


def main():
    with (DATA / "essais.csv").open(encoding="utf-8", newline="") as source:
        rows = {row["id"]: row for row in csv.DictReader(source) if row["jeu"] == "ls20"}
    pilot(rows)
    mechanism()
    hypotheses()


if __name__ == "__main__":
    main()
