# Préparer la publication

## Avant toute mise en ligne

- [ ] Confirmer le nom d’auteur, l’affiliation éventuelle, la date de publication et la version.
- [ ] Choisir les licences applicables au texte, aux figures, aux scripts et aux données. Ne pas attribuer de licence aux éléments tiers sans en avoir le droit.
- [ ] Vérifier que les exports de 30 jours, les modèles utilisés et les statistiques personnelles peuvent être rendus publics. Les agrégats ne contiennent pas les conversations, mais ils restent des données d’usage personnelles.
- [ ] Préciser les dates exactes de la fenêtre et les versions du harness, de Prime et des modèles quand elles sont connues.
- [ ] Retrouver les traces du pilote ARC-AGI-3 et réconcilier la divergence sur les outils du premier essai. En leur absence, conserver la réserve et présenter le texte comme un retour d’expérience préliminaire.
- [ ] Vérifier les droits relatifs aux noms, au jeu, aux captures et à toute donnée tierce. Aucune capture tierce n’est incluse intentionnellement.
- [ ] Relire la restitution et le brouillon LinkedIn ; ne pas affirmer que l’économie de tokens est mesurée par ces exports.

## GitHub

1. Créer un dépôt dédié et y placer **le contenu de ce dossier** à la racine. Ne pas publier automatiquement tout le monorepo Claake Code.
2. Ajouter les licences choisies et, si souhaité, un fichier `CITATION.cff` avec des métadonnées confirmées ; ne pas inventer de DOI ni de numéro de version.
3. Vérifier les liens du README et de l’étude, puis créer une release du dépôt d’étude une fois la version relue.

## Zenodo

Deux options : déposer une archive de l’étude manuellement, ou connecter le dépôt GitHub public à Zenodo **avant** de créer une release afin de l’archiver automatiquement. Vérifier la portée du dépôt et les licences avant de publier : une version archivée doit être considérée comme durablement accessible.

Zenodo attribue un DOI de version et un DOI conceptuel. Citer de préférence le DOI de la version précise ; ajouter les DOI et l’URL publique au README et à la citation après leur attribution. Un DOI est une référence pérenne, pas une validation scientifique ou une évaluation par les pairs.

## Portfolio

Présenter une synthèse avec un lien vers l’étude et, lorsqu’il existe, le DOI. Conserver les légendes et réserves des figures ; les SVG sont autonomes, mais leur rendu dépend des polices de substitution disponibles sur le navigateur.
