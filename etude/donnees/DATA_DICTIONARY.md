# Data Dictionary

## `essais.csv`

The original French column names and categorical identifiers are retained for compatibility with the figure generator. Descriptions are translated; this file is a retrospective reconstruction, not a raw event log.

| Field | Meaning |
|---|---|
| `id` | Trial identifier |
| `jeu` | Game identifier |
| `mode` | `manuel`: manually assisted; `automatise`: automated |
| `essai` | Trial description |
| `coups_validation_n1` | Confirmed moves to first-level completion; blank if not observed |
| `actions_tentees` | Attempted actions, if known |
| `dernier_coup_confirme` | Last confirmed move |
| `niveaux_termines_observes` | Levels observed completed at stop |
| `motif_arret` | Stop reason: `budget`, `timeout`, or `volontaire` (voluntary) |
| `timeout_s` | Configured timeout in seconds, not measured duration |
| `action_issue_inconnue` | Action number with unknown outcome |
| `observation` | Reported contextual note |

Blank values are unknown or not applicable; they are not zeros. The tools used in the first automated trial remain disputed.

## Performance exports

The two `performance-modeles-*-30j.csv` files are preserved verbatim. Each contains **two independently headed tables separated by a blank line**. The first table describes historical response and tool counters. The `measured_harness` table groups recorded turns by harness, provider, model, and subagent status. Durations are milliseconds; `median_tokens_per_second` is whole-turn throughput, including waiting and tools, not pure generation speed. An empty value is unavailable, not zero.

For RLM, the first table has no rows and all `usage_turns` values are zero, meaning no measured usage records in these groups. This is not evidence of zero consumption. The Markdown `perfChat.md` and `perfRLM.md` files transcribe interface snapshots with English labels; N/A replaces the original missing-value glyph and decimal commas remain. They are primary-source transcriptions; their counts sometimes differ from the CSVs for reasons not yet established.
