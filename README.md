# RLM Harnesses and Inference-Time Learning

An independent practitioner report on Claake Code: a persistent Python harness, an exploratory ARC-AGI-3 pilot, and 30 days of personal usage observability.

**[Read the complete study](etude/etude.md)** | [Data and protocol](etude/README.md) | [Publication checklist](PUBLICATION.md)

## Findings and limitations

- The `ls20` pilot reports a change from 15 to 13 game moves. Trials are sequential and uncontrolled; the first trial's exact tools remain to be verified.
- The exports describe one author's personal usage. Tasks are not paired and RLM token counters are unavailable, so token savings remain an unquantified observation.
- This is ongoing work, **not peer reviewed**. The author also develops the system studied.

## Repository structure

```text
etude/etude.md         Complete study
etude/annexes/         Pilot report, protocol, observability
etude/donnees/         Personal usage exports and pilot data
etude/figures/         Four SVG figures
etude/scripts/         Reproducible figure generators
PUBLICATION.md         GitHub and Zenodo checklist
```

## Reproduce the figures

With Python 3.8 or later and no external dependencies:

```sh
cd etude
python3 scripts/generer_graphique.py
python3 scripts/generer_erreurs.py
```

Each performance CSV contains **two consecutive tables with different headers** and must not be imported as a single table. Missing values are not zeros. The `ls20` figures rely on a reported reconstruction, not independently available raw logs.

## Citation and reuse

The study, original figures, and original data in `etude/` are available under **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. Scripts in `etude/scripts/` are under the **[MIT License](etude/scripts/LICENSE)**. See [LICENCES.md](LICENCES.md) for scope and third-party rights. An archive version and DOI will be added after Zenodo publication.
