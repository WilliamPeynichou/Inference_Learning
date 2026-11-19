# Ébauche de post LinkedIn — Harness et apprentissage à l’inférence

## Texte à publier

**Un agent apprend-il à mieux travailler si son environnement conserve ses calculs, sans modifier les poids du modèle ?**

Je pars d’un petit pilote sur ARC-AGI-3 (`ls20`). Le premier trajet automatisé valide le niveau 1 en **15 coups de jeu**. En réutilisant les grilles et fonctions conservées dans un REPL Python persistant, le RLM recalcule un trajet en **13 coups**, ensuite rejoué avec succès. Les deux coups sont gagnés avant le motif (8 → 6) ; après, le trajet reste à 7 coups.

C’est un résultat descriptif, pas un A/B : un seul jeu et deux essais séquentiels ; les outils utilisés lors du premier essai restent à vérifier. Et ces −13,3 % concernent les **coups de jeu**, pas les tours de chat ni les tokens.

Ce qui m’intéresse surtout, ce sont trois observations d’usage que je n’ai pas encore chiffrées :

→ **À froid**, avec une base sans acquis, le circuit de tâches me paraît plus long. Quand Compute intervient et que les variables, fonctions et plans commencent à être réutilisés, j’observe des tours plus courts. Reste à vérifier si le travail diminue réellement à résultat comparable, et quelle part tient au réemploi plutôt qu’au déclenchement automatique.

→ **Côté tokens**, je ne demande pas de compte rendu des tâches exécutées : la sortie visible est très courte et l’entrée semble dominer l’usage affiché. Cela ne dit pas si le modèle raisonne moins. Les objets Python évoluent et se réutilisent dans le REPL ; seuls les éléments transmis au modèle entrent dans son contexte. Je n’ai pas établi si ni combien de cache de prompt le fournisseur utilise : ce cache et l’état Python sont deux choses différentes.

→ **Côté limites**, sur Opus 5.5, Fable 5.2 et 6.2 Sol, j’ai l’impression de pouvoir travailler plus longtemps avant le blocage. Ce n’est pas encore mesuré, et atteindre une limite plus tard ne signifie pas que le quota se réinitialise plus vite.

J’ouvre donc un axe de recherche sur le **harness et l’apprentissage à l’inférence** : qu’est-ce qu’un agent peut conserver, vérifier puis réutiliser sans réentraînement ? Et qu’est-ce qui se transfère sur une tâche inédite, plutôt que de simplement rejouer une solution connue ?

Le prochain test comparera, à modèle et tâche identiques, **Python réinitialisé et Python persistant**, sans Auto Compute. On fera ensuite varier séparément le déclenchement automatique et la consigne de sortie, en mesurant les appels, le temps et les tokens exposés par tâche validée.

📄 Étude, trois figures et protocole : **[lien public de l’étude à insérer]**

Si vous mesurez déjà la réutilisation d’état ou les coûts d’inférence dans un harness agent, je serais curieux de comparer vos méthodes.

## À préparer avant publication

- Remplacer le lien provisoire par l’URL publique de l’étude (aucun lien public n’est supposé ici).
- Utiliser la [figure 1](../etude/figures/ls20-coups.svg) en ouverture, puis la [figure 2](../etude/figures/rlm-mecanisme.svg) pour le mécanisme et la [figure 3](../etude/figures/rlm-hypotheses.svg) pour les mesures à venir ; exporter en PNG si nécessaire pour le carrousel.
