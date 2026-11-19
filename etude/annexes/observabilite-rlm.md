# Observabilité RLM — du pilote ARC-AGI-3 aux usages du chat

**Statut :** observations utilisateur et plan de mesure, pas résultats quantifiés. Aucun nouvel essai n’a été exécuté pour cette note.

## Ce que le pilote permet de distinguer

Sur `ls20`, le pilote rapporte un trajet recalculé en **13 coups au lieu de 15**, en réutilisant des grilles et fonctions présentes dans le REPL. Les résultats rapportés concernent les coups ; les traces brutes permettant de les vérifier indépendamment ne sont pas disponibles et les appels modèle, tokens et temps ne sont pas renseignés. Les restitutions divergent sur les outils du premier trajet : ce contraste ne mesure pas l’effet causal de la persistance. Voir le [rapport du pilote](rapport.md).

On reprend la chaîne **observation → hypothèse → calcul → action → vérification → réemploi** et on instrumente chaque étape. Une action réussie, un tour court et un coût faible sont trois résultats différents.

## Observations à tester

| Observation rapportée | Mesure principale | Ce que la mesure doit départager |
|---|---|---|
| Sur Opus 5.5, Fable 5.2 et 6.2 Sol, la limite semble arriver moins vite. | Temps actif et tâches validées avant le premier signal de limite, par modèle et fenêtre de quota. Relever séparément le délai jusqu’à reprise. | Une limite atteinte plus tard n’est pas un reset retardé. Distinguer quota de compte, limite transitoire, fenêtre annoncée et simple nouvelle tentative réussie. |
| À froid, le circuit de tâches paraît plus long ; ensuite, avec Compute, les tours semblent se raccourcir. | À résultat comparable : appels modèle, appels Python, actions confirmées, temps actif et temps mural par tâche validée. Identifier la première création, le premier réemploi et les reconstructions d’objets. | Échauffement du runtime, réemploi d’une méthode, tâche plus facile ou simple réduction du texte. Ne pas attribuer l’écart à Auto Compute sans comparaison dédiée. |
| Le texte visible est très court, car aucun commentaire sur les tâches exécutées n’est demandé. | Taille du texte utilisateur et, quand exposés, tokens de sortie, de raisonnement et d’appels d’outils selon les conventions du provider. | Moins de commentaires peut réduire la sortie visible sans réduire le raisonnement ni le total. |
| La majorité des tokens affichés semble être en entrée ; les variables Python réutilisées pourraient y contribuer. | Entrée totale, composante cache lue/écrite si exposée, taille des retours Python réellement renvoyés au modèle, coût et nombre d’appels. | Un objet en mémoire ne consomme pas de tokens par sa seule présence. Son contenu peut compter s’il est sérialisé dans le contexte ; le code ou la référence qui le manipule compte également lorsqu’il est transmis. |

### Trois notions à journaliser séparément

- **État Python** : un objet, une fonction ou un plan survit entre appels au REPL. Noter création, modification, réemploi ou reconstruction, à l’aide d’un ID local et d’une empreinte si utile. Cela ne constitue ni un cache de prompt ni une preuve de restauration après fermeture.
- **Cache provider** : le fournisseur déclare, le cas échéant, des lectures ou écritures de cache de prompt. Ce mécanisme peut coexister avec un REPL persistant. Un champ absent signifie **non exposé**, pas zéro. Conserver les champs tels que définis par le provider : un total peut déjà inclure le cache ou le raisonnement ; ne pas les additionner deux fois.
- **Contexte transmis** : ce que le modèle reçoit réellement, y compris les résultats Python si le harness les réinjecte. Si le découpage en tokens par source n’est pas exposé, mesurer la taille des retours en octets et la signaler comme indicateur, pas comme attribution exacte des tokens.

## Trace minimale par essai

| Niveau | Champs à relever |
|---|---|
| Essai | ID, tâche et critère de réussite, modèle exact/provider, réglage de réflexion, harness/version, état froid ou chaud, acquis importés, consigne de sortie, budget, ordre de passage. |
| Appel ou action | Heure, ID du tour, type (modèle, Python, Auto Compute, runner), durée, issue ; action tentée et confirmée séparément. Pour Python : objet créé/réemployé/reconstruit, taille du retour transmis si observable. |
| Usage modèle | Champs d’usage exposés et leur sémantique, tokens d’entrée/sortie, raisonnement et cache si disponibles ; texte visible et coût séparés. Inclure le travail automatique et les nouvelles tentatives. |
| Limite | Type connu ou indéterminé, heure du premier blocage, indication de reset ou `Retry-After` si exposée, première reprise observée et fin de fenêtre. Distinguer temps actif, attente quota et temps mural. |

Ne pas consigner de secrets, de prompts bruts ni de valeurs Python privées. Garder les mesures inconnues vides et noter la couverture par modèle. Pour un essai sans blocage avant son terme, noter « aucun blocage observé jusqu’à l’arrêt » : ce n’est pas une durée illimitée.

## Premier plan de mesure

1. **Calibrer sur `ls20`.** Vérifier que le logger aligne un coup confirmé du runner avec un tour, les appels associés et les objets Python réutilisés. Rapporter à part le coût de la découverte et celui du rejeu. Ne pas transformer un écart de coups en économie de tokens.
2. **Comparer à tâche et modèle constants.** Apparier Python réinitialisé et Python persistant avec la même consigne courte et Auto Compute désactivé. Séparer dès le départ essai froid, réemploi dans le même essai et acquis importés. Comparer ensuite la sortie courte à une consigne demandant un compte rendu, puis Auto Compute activé/désactivé, en ne changeant qu’un facteur à la fois.
3. **Faire des blocs séparés pour les limites.** Pour chacun des trois modèles, relever le provider, le type de compte et l’état du quota au départ s’il est observable, équilibrer l’ordre et éviter de partager une même fenêtre avec d’autres usages non tracés. Préfixer les plafonds et comparer d’abord les différences **au sein d’un modèle**, pas les quotas bruts d’un provider à l’autre.
4. **Lire les résultats à qualité comparable.** Publier réussites/essais, puis ressources par tâche validée avec leurs dénominateurs et les coûts des échecs à part. Montrer séparément les tours froids et chauds, les attentes et les différences appariées. Si le raisonnement, le cache ou les appels internes ne sont pas exposés, ne pas conclure à une économie dans ces catégories.

Le [protocole principal](protocole.md) reste la référence pour l’isolation, les ablations et le transfert vers des jeux inédits.
