"""Génère une comparaison descriptive des erreurs de tour par modèle commun."""
import csv
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "donnees"
FIGURES = ROOT / "figures"


def measured(filename):
    with (DATA / filename).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    i = next(i for i, row in enumerate(rows) if row and row[0] == "measured_harness")
    return {r[2]: dict(zip(rows[i], r)) for r in rows[i+1:] if r and r[3] == "false"}


def main():
    classic = measured("performance-modeles-chat-30j.csv")
    rlm = measured("performance-modeles-RLM-30j.csv")
    common = sorted(classic.keys() & rlm.keys())
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="560" viewBox="0 0 960 560" role="img" aria-labelledby="title desc">',
           '<title id="title">Erreurs de tour enregistrées par modèle</title>',
           '<desc id="desc">Comparaison descriptive des erreurs de tour dans les exports de chat classique et RLM, par modèle commun. Les tâches ne sont pas appariées et les causes des erreurs peuvent différer.</desc>',
           '<style>text{font-family:system-ui,sans-serif;fill:#172637;font-size:16px}.title{font:bold 29px Georgia,serif}.small{font-size:14px;fill:#405266}.header{font-size:14px;font-weight:bold;fill:#345577}</style>',
           '<rect width="960" height="560" fill="white"/>',
           '<text x="40" y="38" class="header">FIGURE 4 / USAGE PERSONNEL SUR 30 JOURS</text>',
           '<text x="40" y="80" class="title">Erreurs de tour enregistrées, par modèle</text>',
           '<text x="40" y="111" class="small">Tâches non appariées · toutes erreurs confondues · effectifs différents</text>',
           '<text x="40" y="153" class="header">MODÈLE</text><text x="330" y="153" class="header">CHAT CLASSIQUE</text><text x="610" y="153" class="header">RLM</text>']
    for i, model in enumerate(common):
        y = 194 + 53 * i
        svg += [f'<path d="M40 {y-25}H920" stroke="#dde4ea"/>', f'<text x="40" y="{y}">{escape(model)}</text>']
        for x, record in [(330, classic[model]), (610, rlm[model])]:
            errors, turns = int(record['errors']), int(record['turns'])
            svg.append(f'<text x="{x}" y="{y}">{errors} / {turns} ({100*errors/turns:.1f} %)</text>')
    svg += ['<path d="M40 440H920" stroke="#9caab7"/>',
            '<text x="40" y="470" class="small">Un taux nul avec peu de tours ne démontre pas l’absence de risque. Les erreurs</text>',
            '<text x="40" y="492" class="small">peuvent provenir du modèle, du fournisseur, du harness ou d’un autre composant.</text>',
            '<text x="40" y="525" class="small">Source : sections measured_harness des exports CSV fournis ; données agrégées.</text>', '</svg>']
    (FIGURES / 'erreurs-par-modele.svg').write_text('\n'.join(svg)+'\n', encoding='utf-8')

if __name__ == '__main__':
    main()
