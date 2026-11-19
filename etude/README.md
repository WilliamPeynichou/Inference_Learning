# Index de l’étude

**[Lire l’étude complète](etude.md)** : un seul document principal, avec ses figures intégrées et ses limites explicitées.

## Annexes et sources

- [Rapport du pilote ARC-AGI-3](annexes/rapport.md) et [données du pilote](donnees/essais.csv).
- [Observabilité et hypothèses](annexes/observabilite-rlm.md) et [protocole proposé](annexes/protocole.md).
- Exports de performance : [chat classique](donnees/performance-modeles-chat-30j.csv), [RLM](donnees/performance-modeles-RLM-30j.csv), [relevé chat](donnees/perfChat.md) et [relevé RLM](donnees/perfRLM.md).
- [Figures SVG](figures/) et [scripts de génération](scripts/).

Les exports contiennent chacun deux tableaux distincts. La section de tokens du RLM est vide : l’usage est inconnu, pas nul. Les outils du premier essai ARC-AGI-3 sont également à confirmer ; les restitutions divergent.

## Régénérer les figures

Depuis ce dossier, avec Python 3.8 ou plus récent et sans dépendance externe :

```sh
python3 scripts/generer_graphique.py
python3 scripts/generer_erreurs.py
```

Les scripts lisent `donnees/` et écrivent dans `figures/`, sans lancer le jeu ni modifier les données.
