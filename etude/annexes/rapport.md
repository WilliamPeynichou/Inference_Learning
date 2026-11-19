# Pilot Report: ARC-AGI-3 `ls20`

**Discrepancy requiring verification:** the author later reported that the first automated trial used classic tools without Python. The earlier account stated the opposite. Raw logs are needed to resolve this.

## Reported observations

| Trial | First-level completion | Trial end | Observation |
|---|---:|---|---|
| Manually assisted | 26 moves | 30 actions, 1 level | The user entered actions and relayed grids. |
| Interrupted direct run | Not observed | 12 confirmed moves, 0 levels observed | Timeout at 120 s; outcome of move 13 unknown. |
| First complete automated trial | 15 moves | 30 actions, 1 level | Exact tools unconfirmed: accounts differ. |
| Recalculated path | 13 moves | Voluntary stop at 13, 1 level | Breadth-first search using grids and functions retained in the REPL. |
| Replay and exploration | 13 moves | 30 actions, 1 level | Path reproduced. At move 30, the level-two 0/1 pattern inverted the drawing vertically. |

The only source is the trial history described in the request. Raw logs were not found in the working folder, so traces have not been independently verified. Unreported dates, costs, tokens, and latencies are not estimated. See the [CSV](../donnees/essais.csv) and [figure](../figures/ls20-coups.svg).

## Where did the two-move difference arise?

The reported 15-move path used **8 moves to reach the pattern**, then **7 to reach the frame**. Breadth-first search reduced the first segment to **6 moves**, leaving the second unchanged. Sequence reported as verified in the pilot: **ACTION3 × 3 → ACTION1 × 4 → ACTION4 × 3 → ACTION1 × 3**. The relative decrease is `(15 - 13) / 15 = 13.3%`, rounded.

All trials played to the 30-action cap ended with **one completed level**. Level two was not completed; the observed inversion does not establish a general rule or solution. Thirteen moves is the shortest path found in the tested transition model, not a proven global minimum.

## Four distinct mechanisms

- **Persistent Python state:** grids, variables, and functions remain available between calls to the same REPL. The pilot illustrates reuse but does not measure survival through compaction or restoration in a new session.
- **Compute and Auto Compute:** Compute transforms an observation into a verifiable computation and reusable object, such as a breadth-first-search plan. Auto Compute triggers work automatically; its effect is not isolated here.
- **Textual harness memory:** the path was recorded locally after calculation. Saving and explicitly reloading a result is not the same as preserving a Python namespace. This memory did not cause the reported 15-to-13 change.
- **Inference-time learning:** observe, hypothesize, compute, act, verify, and retain validated work without changing model weights. This is not presented as algorithmic reinforcement learning: no policy, reward, or update mechanism has been defined for that interpretation.

## Limitations and open hypotheses

Trials are sequential, cover one game, and differ in histories, interventions, and stopping points. The tools used for the 15-move trial remain unconfirmed; neither that contrast nor the manual trial identifies a causal REPL or harness effect. A timeout is not a success at 12 moves, and the next outcome remains unknown. Replay validates reuse on `ls20`, not transfer to an unseen game.

The [protocol](protocole.md) proposes tests for reconstruction costs, compaction, automatic triggering, replay versus generic-method transfer, and text versus testable Python functions.
