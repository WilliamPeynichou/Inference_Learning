# Study Index

**[Read the complete study](etude.md)** for the technical background, exploratory pilot, usage data, and limitations.

## Appendices and sources

- [ARC-AGI-3 pilot report](annexes/rapport.md) and [pilot data](donnees/essais.csv).
- [Observability and hypotheses](annexes/observabilite-rlm.md) and [proposed protocol](annexes/protocole.md).
- Performance exports: [classic chat](donnees/performance-modeles-chat-30j.csv), [RLM](donnees/performance-modeles-RLM-30j.csv), [classic interface snapshot](donnees/perfChat.md), and [RLM interface snapshot](donnees/perfRLM.md).
- [SVG figures](figures/) and [figure generators](scripts/).

Each performance export contains two distinct tables. RLM token usage is unavailable, not zero. The first ARC-AGI-3 trial's tools remain unconfirmed because accounts differ.

## Reproduce figures

From this directory, with Python 3.8 or later and no external dependencies:

```sh
python3 scripts/generer_graphique.py
python3 scripts/generer_erreurs.py
```

Scripts read `donnees/` and write to `figures/`; they do not run the game or alter source data.
