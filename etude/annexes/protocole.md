# Protocole proposé — non exécuté

## 1. Comparaison principale et ablations

| Contraste | Conditions | Question |
|---|---|---|
| A / B | **A** : harness classique avec `Grep`, `Glob`, `Read` et terminal, sans REPL persistant ni mémoire importée. **B** : IPython persistant seul, sans mémoire textuelle importée et avec Auto Compute désactivé. | Quel est l’effet du changement complet d’interface ? Ce contraste ne permet pas d’attribuer un écart à la seule persistance. |
| Persistance | Python réinitialisé à chaque appel / même Python et mêmes commandes autorisées, mais IPython persistant. Auto Compute désactivé ; pas de mémoire importée. | Quel travail est évité quand les objets survivent entre appels ? |
| Déclenchement | Même IPython persistant sans / avec Auto Compute. | Quel est l’effet du déclenchement automatique, distinct de la possibilité de calculer ? |
| Mémoire textuelle | Sessions neuves avec IPython initialement vide, sans / avec le même artefact textuel chargé explicitement au démarrage. | Qu’apporte le rappel d’une règle ou d’un résultat, à configuration égale ? |
| Format (si faisable) | Sessions neuves ; même méthode générique importée soit en texte, soit comme fonction Python dans le REPL. Même signature logique, préconditions, critères de décision et cas d’essai. | La représentation exécutable facilite-t-elle la réutilisation ? Ni le texte ni le code ne doit embarquer la réponse. |

En B, l’agent lit et structure les observations, calcule, conserve l’état et pilote le runner depuis IPython via l’interface autorisée. Pas d’accès à des outils de recherche ou de lecture spécialisés, même via wrappers, appels shell ou processus enfants. En A, le terminal n’est pas un moyen de recréer un REPL persistant ou d’importer des acquis. Toutes les conditions utilisent le même runner et accèdent au même contenu d’observation.

Dans l’ablation de persistance, les deux groupes peuvent relire les messages, sorties d’outils et observations confirmées de **leur essai courant** encore présents dans le contexte, selon les mêmes règles de troncature/compaction. Le groupe sans état peut reconstruire ses variables depuis ce contexte, mais chaque appel s’exécute dans un environnement neuf, sans répertoire inscriptible partagé, services ou processus persistants, ni stockage externe. Le runner conserve uniquement l’état nécessaire au jeu ; son interface ne sert pas de stockage auxiliaire. Hors bras de restauration, limiter la persistance supplémentaire du bras IPython à ses objets en mémoire. Appliquer et vérifier ces restrictions hors des prompts, avant l’évaluation.

Pour Auto Compute, fixer avant les essais le déclencheur (par exemple après chaque nouvelle grille confirmée), le travail demandé (structurer la grille, tester l’hypothèse courante si elle est calculable, conserver le résultat) et son plafond. Garder les mêmes capacités de calcul dans les deux bras : sans automatisme, l’agent peut déclencher le même travail lui-même. Compter tous les appels, tokens et temps supplémentaires dans le budget du bras automatique. Les actions de jeu restent soumises à la même interface et au même plafond.

### Deux tests distincts autour de la persistance

1. **Compaction, même session.** À une étape préenregistrée, placer une grille et une fonction testable dans le REPL, puis compacter le contexte selon une règle identique. Vérifier dans un appel suivant, sans reconstruction, l’existence des objets, l’empreinte de la grille et la sortie de la fonction sur un cas fixé. Consigner à part la récupération depuis le résumé du contexte, qui ne prouve pas la survie de l’objet.
2. **Restauration, nouvelle session.** Fermer le REPL, redémarrer avec un espace de noms neuf et comparer sans/avec une restauration explicite depuis un instantané autorisé et inventorié. Refaire les mêmes tests et mesurer le coût de restauration. Aucun historique conversationnel ni mémoire textuelle ne doit être réinjecté dans ce contraste. La survie à une compaction ne démontre pas la restauration.

## 2. Exploration, gel des acquis, évaluation

1. **Explorer** sur des jeux autorisés, avec un budget fixé d’avance. Consigner hors de portée des futurs agents chaque boucle observation → hypothèse → calcul vérifiable → action → vérification → conservation. Garder les hypothèses réfutées distinctes des acquis validés.
2. **Figer et inventorier** avant l’évaluation : version, empreinte, provenance, type (trajet, règle, fonction, état), vérification qui le soutient et conditions autorisées à l’importer. Séparer les artefacts spécifiques à un niveau des méthodes génériques ; vérifier les deux représentations d’une méthode sur les mêmes cas de développement.
3. **Évaluer en sessions neuves**, sur deux volets rapportés séparément :
   - **Rejeu `ls20`** : mesure la réutilisation d’une solution connue. Seuls les bras désignés reçoivent le trajet validé ; les témoins ne reçoivent rien.
   - **Transfert vers des jeux inédits** : utiliser des jeux tenus à l’écart de l’exploration et du gel. Seule la méthode apprise est exportable. Exclure trajets, grilles, coordonnées, identifiants codés en dur et toute réponse précalculée. Un témoin sans import permet de mesurer le bénéfice de la méthode.

L’apprentissage est ici un changement des connaissances ou procédures réutilisées à l’inférence, pas un changement des poids. Enregistrer séparément la découverte pendant un essai et le bénéfice d’un acquis importé.

## 3. Contrôles de comparabilité

- Fixer modèle/version et paramètres, objectif, version du runner, format et résolution des observations, règles d’interaction, limites de contexte, budgets (actions, temps, tokens/appels si mesurables) et politique d’arrêt. Seules les instructions d’interface et les variables testées diffèrent. Les observations disponibles sont équivalentes **à état identique** ; les trajectoires libres peuvent ensuite diverger.
- Réinitialiser le jeu à chaque essai. Comparer niveau de départ et empreinte de la grille initiale par paire jeu/graine ; isoler et documenter tout écart avant analyse. Enregistrer la graine du jeu et celle du modèle si disponibles.
- Préenregistrer le nombre de répétitions par jeu/condition, la métrique principale, les exclusions et la règle de comparaison. Appairer les conditions par jeu/état initial et contrebalancer l’ordre (AB/BA ou ordre randomisé par bloc). Ne partager aucun état entre répétitions indépendantes.
- Démarrer avec un espace isolé. Les agents évalués ne voient ni ce dossier, ni les anciens logs, plans ou résultats ni les traces des autres conditions ; exposer uniquement les artefacts explicitement autorisés dans le bras testé. Les observateurs consignent les traces séparément. Standardiser les interventions humaines (aucune aide au jeu, sauf si c’est une condition prévue) et les journaliser.

## 4. Mesures et analyse

- **Réussite** : validation du premier niveau confirmée par le runner avant l’arrêt. Rapporter numérateur et dénominateur sur tous les essais assignés, avec les timeouts séparés. **Niveaux à budget fixe** : compter les niveaux confirmés au plafond commun ; pour les essais arrêtés plus tôt sans pouvoir établir leur résultat au plafond, rapporter le nombre observé à l’arrêt à part. Prévoir une analyse de sensibilité où ce nombre est utilisé comme borne basse.
- **Coups jusqu’à la première validation** : compter les coups confirmés jusqu’à l’événement (inclus). Donner la distribution chez les réussites avec son dénominateur ; signaler les non-réussites comme censurées au dernier coup confirmé, sans les traiter comme des validations. Interpréter le nombre de coups avec le taux de réussite pour éviter de favoriser un bras à faible taux de réussite.
- **Ressources** : temps mural total, tokens entrée/sortie si exposés, appels par type (outil, modèle, calcul automatique, runner) et interventions humaines avec leur nature. Séparer actions tentées et confirmées ; préciser l’index et l’issue de toute action non confirmée. Ne pas assimiler budget de timeout et durée réellement mesurée.
- Publier les décomptes par bras et différences appariées à état initial égal, avec dispersion/incertitude et taille des échantillons. Ne pas agréger le rejeu et le transfert ni en déduire un score global ARC-AGI-3.

## 5. Fiche à remplir pour chaque essai

```text
ID / date / opérateur :
Volet (exploration / rejeu / transfert / compaction / restauration) :
Condition / paire / répétition / rang dans l’ordre :
Jeu / graine jeu / niveau initial / empreinte grille initiale :
Modèle / version / paramètres / graine si disponible :
Runner / version / objectif / observations accessibles :
Budgets (actions / temps / tokens / appels) :
Contrôles d’isolation vérifiés :
Persistance / règles de contexte / Auto Compute (déclencheur et plafond) :
Artefacts importés (type, version, empreinte, autorisation) :
Compaction ou restauration (étape, objets testés, résultats, coût) :
Première validation confirmée (oui/non, coup si connu) :
Niveaux confirmés au plafond / à l’arrêt :
Actions tentées / dernier coup confirmé / actions non confirmées et indices :
Motif d’arrêt / timeout configuré / temps mural mesuré :
Tokens entrée et sortie / appels par type :
Interventions humaines (nombre et nature) :
Acquis validés / références aux traces / écarts au protocole :
```

Utiliser « non renseigné » dans la fiche et des cellules vides à l’export pour les valeurs inconnues ; zéro signifie un décompte observé.
