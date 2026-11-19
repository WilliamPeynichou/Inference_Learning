# Harness RLM et apprentissage à l’inférence

Retour d’expérience indépendant sur Claake Code : fonctionnement d’un harness RLM, pilote exploratoire ARC-AGI-3 et observabilité d’un usage personnel sur 30 jours.

**[Lire l’étude complète](etude/etude.md)** · [Données et protocole](etude/README.md)

## Résultats et limites en bref

- Le pilote `ls20` rapporte un trajet passant de 15 à 13 coups de jeu. Les essais sont séquentiels et non contrôlés ; l’attribution exacte des outils du premier essai reste à vérifier.
- Les exports décrivent l’usage personnel d’un auteur. Les tâches ne sont pas appariées et les compteurs de tokens RLM ne sont pas disponibles : l’économie de tokens reste une observation non chiffrée.
- Ce document est un retour d’expérience en cours, **non évalué par les pairs** ; son auteur développe le système étudié.

## Structure

```text
etude/etude.md         Texte intégral de l’étude
etude/annexes/         Rapport du pilote, protocole et observabilité
etude/donnees/         Exports personnels et données du pilote
etude/figures/         Visuels SVG intégrés à l’étude
etude/scripts/         Générateurs reproductibles des figures
PUBLICATION.md         Vérifications GitHub et Zenodo avant diffusion
```

## Reproduire les figures

Avec Python 3.8 ou plus récent, sans dépendance externe :

```sh
cd etude
python3 scripts/generer_graphique.py
python3 scripts/generer_erreurs.py
```

Les fichiers CSV de performance contiennent **deux tableaux successifs avec des en-têtes différents** ; il ne faut pas les charger comme un seul tableau. Leurs valeurs manquantes ne sont pas des zéros. Les chiffres du pilote proviennent d’une restitution, les journaux bruts n’étant pas disponibles.

## Citation et réutilisation

L’auteur, la version, le DOI éventuel et les licences doivent être confirmés avant publication. Voir [PUBLICATION.md](PUBLICATION.md). Aucune licence de réutilisation n’est accordée par ce fichier ; ne pas présumer que les noms de produits ou les données de tiers sont libres de droits.
