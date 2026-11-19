"""Génère les trois figures de l’étude, sans dépendance externe."""

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
    # Décomposition jusqu’au motif : rapport.md ; totaux : essais.csv.
    series = [("auto-complet", "Chat avec outils", 8), ("recalcule", "RLM", 6)]
    totals = [int(rows[key]["coups_validation_n1"]) for key, _, _ in series]
    gap = totals[0] - totals[1]
    percent = f"{100 * gap / totals[0]:.1f}".replace(".", ",")
    axis_max = ((max(totals) + 4) // 5) * 5
    x0, scale = 244, 560 / axis_max
    items = [text(48, 138, "ARC-AGI-3 · Jeu ls20 · Deux essais séquentiels, un seul jeu", "note")]
    for x, color, label in [(244, "#294e70", "Jusqu’au motif"), (443, "#d7e1ea", "Du motif au cadre")]:
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
    items += [text(524, 361, "Coups de jeu jusqu’à la validation du niveau 1", "body", "middle"),
              line(48, 385, 912, 385), text(48, 414, f"Écart descriptif : −{gap} coups (−{percent} %), intégralement avant le motif.", "strong"),
              text(48, 443, "Attribution des outils à vérifier. Pas d’A/B contrôlé ni de mesure des tours de chat.", "note"),
              text(48, 469, "Sources : essais.csv et rapport.md. Les journaux bruts ne sont pas disponibles.", "note")]
    figure("ls20-coups.svg", 496, 1, "RÉSULTAT DESCRIPTIF", f"Niveau 1 : {totals[0]} puis {totals[1]} coups de jeu",
           f"Chat avec outils : {totals[0]} coups dont 8 avant le motif. RLM : {totals[1]} dont 6 avant le motif. Le second segment reste à 7. Comparaison non contrôlée.", items)


def mechanism():
    steps = [("Observation", "Grilles du jeu"), ("État Python", "Objets et fonctions"), ("Calcul", "Recherche en largeur"), ("Vérification", "Coups validés")]
    items = [text(48, 138, "Schéma de lecture du pilote ls20 ; pas une mesure de fréquence ou de performance.", "note")]
    for index, (label, detail) in enumerate(steps):
        x = 48 + index * 220
        items += [f'<rect x="{x}" y="173" width="204" height="87" fill="#f3f6f9" stroke="#aebcca"/>',
                  text(x + 14, 204, label, "strong"), text(x + 14, 234, detail, "note")]
        if index < len(steps) - 1:
            items.append(text(x + 212, 220, "→", "strong", "middle"))
    items += [text(48, 298, "Réemploi : les grilles et fonctions conservées servent au recalcul du trajet.", "body"),
              text(48, 327, "À tester : économie de reconstruction et transfert d’une méthode à un jeu inédit.", "note"),
              text(48, 354, "Source : rapport.md. Ni mise à jour des poids ni effet causal établi.", "note")]
    figure("rlm-mecanisme.svg", 382, 2, "SCHÉMA CONCEPTUEL", "De l’observation au réemploi du calcul",
           "La grille du jeu est représentée en objets Python. Une recherche en largeur utilise les objets et fonctions conservés. Le runner confirme les coups. Le transfert reste à tester.", items)


def hypotheses():
    rows = [
        ("Tours et réemploi", "Circuit perçu plus long à froid,", "puis plus court à mesure que Compute intervient.", "Appels, temps et objets réutilisés", "par tâche validée, à qualité comparable."),
        ("Tokens et cache", "Peu de texte visible ; l’entrée paraît", "dominante. Rôle des retours Python inconnu.", "Séparer entrée, sortie, raisonnement,", "cache provider et retours Python transmis."),
        ("Limites provider", "Limite perçue plus tard sur Opus 5.5,", "Fable 5.2 et 6.2 Sol.", "Travail avant blocage et délai de reprise,", "par modèle et fenêtre de quota."),
    ]
    items = [text(48, 139, "Observation d’usage", "meta"), text(492, 139, "Mesure proposée", "meta"), line(472, 121, 472, 403)]
    for y, (label, a, b, c, d) in zip((168, 247, 326), rows):
        items += [line(48, y - 10, 912, y - 10), text(48, y + 11, label, "strong"), text(48, y + 34, a, "note"),
                  text(48, y + 54, b, "note"), text(492, y + 22, c), text(492, y + 45, d)]
    items += [line(48, 403, 912, 403), text(48, 433, "Source : observations utilisateur non chiffrées, distinctes des résultats du pilote.", "note")]
    figure("rlm-hypotheses.svg", 462, 3, "PLAN DE MESURE", "Trois observations à confronter aux traces",
           "Tableau qualitatif des hypothèses sur les tours à froid et à chaud, les tokens et le cache, et les limites provider. Aucun résultat quantifié.", items)


def main():
    with (DATA / "essais.csv").open(encoding="utf-8", newline="") as source:
        rows = {row["id"]: row for row in csv.DictReader(source) if row["jeu"] == "ls20"}
    pilot(rows)
    mechanism()
    hypotheses()


if __name__ == "__main__":
    main()
