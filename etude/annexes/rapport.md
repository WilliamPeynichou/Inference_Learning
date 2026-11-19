# Rapport — Pilote ARC-AGI-3, jeu `ls20`

**Divergence à vérifier :** l’auteur rapporte après coup que le premier essai automatisé utilisait les outils classiques sans Python. Ce rapport conservait une restitution antérieure indiquant l’inverse. Les journaux bruts sont nécessaires pour trancher.

## Résultats observés

| Essai | Validation du niveau 1 | Fin de l’essai | Observation |
|---|---:|---|---|
| Jeu assisté manuellement | 26 coups | 30 actions, 1 niveau | L’utilisateur saisissait les actions et renvoyait les grilles. |
| Lancement direct interrompu | Non observée | 12 coups confirmés, 0 niveau observé | Timeout à 120 s ; résultat du coup 13 inconnu. |
| Premier essai automatisé complet | 15 coups | 30 actions, 1 niveau | Outils exacts non confirmés : les restitutions divergent. |
| Trajet recalculé | 13 coups | Arrêt volontaire à 13, 1 niveau | Recherche en largeur à partir de grilles et fonctions conservées dans le REPL. |
| Rejeu et exploration | 13 coups | 30 actions, 1 niveau | Trajet reproduit. Au coup 30, le motif 0/1 du niveau 2 inverse le dessin de haut en bas. |

Source unique : historique des essais fourni dans la demande. Les journaux bruts n’ont pas été retrouvés dans le dossier courant ; il n’y a donc pas de vérification indépendante des traces. Dates, coûts, tokens et latences non renseignés ne sont pas estimés. Voir le [CSV](../donnees/essais.csv) et le [graphique](../figures/ls20-coups.svg).

## D’où vient le gain de deux coups ?

Le trajet de 15 coups prenait **8 coups pour atteindre le motif**, puis **7 pour atteindre le cadre**. La recherche en largeur a ramené le premier segment à **6 coups**, sans raccourcir le second. Séquence vérifiée dans le pilote : **ACTION3 × 3 → ACTION1 × 4 → ACTION4 × 3 → ACTION1 × 3**. La baisse relative des coups jusqu’à la validation est de `(15 − 13) / 15 = 13,3 %` (arrondi).

Les essais joués jusqu’au plafond de 30 actions terminent tous **un niveau**. Le niveau 2 n’a pas été terminé ; l’inversion observée au coup 30 n’établit ni une règle générale ni une solution. Treize coups est le plus court trajet trouvé dans le modèle de transitions testé, pas un minimum absolu du jeu.

## Quatre mécanismes à ne pas confondre

- **État Python persistant.** Les grilles, variables et fonctions restent disponibles entre appels au même REPL. Le pilote illustre leur réemploi pour recalculer le trajet ; il ne mesure ni leur survie à une compaction du contexte ni leur restauration dans une nouvelle session.
- **Compute et Auto Compute.** Compute transforme une observation en calcul vérifiable et en objet réutilisable (ici, par exemple, un plan produit par la recherche en largeur). Auto Compute déclenche ce travail automatiquement ; le pilote n’en isole pas l’effet.
- **Mémoire textuelle du harness.** Le trajet a été enregistré localement après son calcul. Sauvegarder un résultat et le recharger explicitement n’est pas conserver un espace de noms Python. Cette mémoire n’a pas causé le passage de 15 à 13 coups.
- **Apprentissage à l’inférence.** Observer → formuler une hypothèse → calculer → agir → vérifier → conserver ce qui a été validé, sans modifier les poids du modèle. Ce cycle n’est pas présenté comme du *reinforcement learning* algorithmique : ni politique, ni récompense, ni mécanisme de mise à jour n’ont été définis pour une telle interprétation.

## Limites et hypothèses ouvertes

Les essais sont séquentiels, sur un seul jeu, avec des historiques, interventions et arrêts différents. Les outils du trajet de 15 coups restent à confirmer : ni ce contraste ni celui avec le manuel ne permettent d’attribuer un effet causal au REPL ou au harness. Le timeout n’est pas une réussite à 12 coups ; le résultat du coup suivant reste inconnu. Le rejeu valide la réutilisation sur `ls20`, pas le transfert d’une méthode vers un jeu inédit.

Le [protocole](protocole.md) propose de tester si l’état persistant réduit le travail de reconstruction, s’il reste utilisable après compaction, et si un déclenchement automatique améliore les résultats à budget égal ou consomme des ressources sans bénéfice. Il sépare aussi le rappel d’un trajet connu du transfert d’une méthode générique, et la portabilité du texte de celle d’une fonction testable.
