# Proposed Protocol: Not Executed

## 1. Main comparison and ablations

| Contrast | Conditions | Question |
|---|---|---|
| A / B | **A:** classic harness with `Grep`, `Glob`, `Read`, and terminal, without a persistent REPL or imported memory. **B:** persistent IPython only, without imported textual memory and with Auto Compute disabled. | What is the effect of the complete interface change? This contrast cannot attribute a difference to persistence alone. |
| Persistence | Python reset after each call versus the same Python and allowed commands with persistent IPython. Auto Compute disabled; no imported memory. | What reconstruction is avoided when objects survive between calls? |
| Triggering | Same persistent IPython without versus with Auto Compute. | What is the effect of automatic triggering, distinct from the ability to compute? |
| Textual memory | Fresh sessions with initially empty IPython, without versus with the same text artifact explicitly loaded at startup. | What does recalling a rule or result contribute under otherwise equal conditions? |
| Format, if feasible | Fresh sessions with the same generic method imported as text or as a Python function. Match logical signature, preconditions, decision criteria, and test cases. | Does executable representation facilitate reuse? Neither representation may contain the answer. |

In B, the agent reads and structures observations, computes, retains state, and controls the runner from IPython through the authorized interface. No specialized search or reading tools may be accessed, including through wrappers, shell calls, or child processes. In A, the terminal must not recreate a persistent REPL or import prior knowledge. All conditions use the same runner and observation content.

For the persistence ablation, both groups may reread messages, tool outputs, and confirmed observations from **their current trial** still in context, under identical truncation and compaction rules. The stateless group may rebuild variables from that context, but each call runs in a fresh environment with no shared writable directory, persistent services or processes, or external storage. The runner retains only game state and is not auxiliary storage. Outside restoration arms, limit additional IPython persistence to in-memory objects. Enforce and verify these restrictions outside prompts before evaluation.

For Auto Compute, specify the trigger, requested work, and cap before trials. Both arms retain the same computational capabilities: without automation, the agent can invoke the work itself. Count all extra calls, tokens, and time in the automated arm. Game actions use the same interface and budget.

### Distinct persistence tests

1. **Compaction within a session.** At a preregistered step, put a grid and testable function in the REPL, then compact context under the same rule. On a later call, without reconstruction, check object existence, grid fingerprint, and function output on a fixed case. Record recovery from the textual summary separately; it does not establish object survival.
2. **Restoration in a new session.** Close the REPL, restart with a fresh namespace, and compare no restoration against explicit restoration from an authorized, inventoried snapshot. Repeat the tests and measure restoration cost. Do not reintroduce conversation history or textual memory. Survival through compaction does not demonstrate restoration.

## 2. Exploration, artifact freeze, evaluation

1. **Explore** authorized games under a fixed budget. Record observation, hypothesis, verifiable computation, action, verification, and retention outside future agents' reach. Separate rejected hypotheses from validated artifacts.
2. **Freeze and inventory** version, fingerprint, provenance, type, supporting verification, and authorized import conditions. Separate level-specific artifacts from generic methods; test both representations on the same development cases.
3. **Evaluate in fresh sessions**, reporting separately:
   - **`ls20` replay:** reuse of a known solution. Only designated arms receive the validated path.
   - **Transfer to unseen games:** use games withheld from exploration and artifact freeze. Export only the generic method, not paths, grids, coordinates, hard-coded identifiers, or precomputed answers. Include a no-import control.

Learning here means a change in knowledge or procedures reused at inference, not a change in weights. Record within-trial discovery separately from benefits of imported artifacts.

## 3. Comparability controls

- Fix model/version and settings, objective, runner version, observation format and resolution, interaction rules, context limits, budgets, and stopping policy. Available observations are equivalent at the same state; free trajectories may subsequently diverge.
- Reset the game for each trial. Pair by game/seed, starting level, and initial grid fingerprint; document deviations. Record game and model seeds when available.
- Preregister repetitions, primary metric, exclusions, and comparison rule. Pair by initial state and counterbalance or randomize order by block. Do not share state between independent repetitions.
- Isolate evaluated agents from this folder, prior logs, plans, outcomes, and other conditions' traces. Expose only authorized artifacts. Observers log separately. Standardize and record human intervention.

## 4. Measures and analysis

- **Success:** runner-confirmed first-level completion before stopping. Report numerator and denominator for all assigned trials and separate timeouts. At a fixed action budget, count levels confirmed at the shared cap; report early-stopped trials separately. A sensitivity analysis may use observed levels as a lower bound.
- **Moves to first completion:** count confirmed moves through the event. Report the distribution and denominator among successes; treat failures as censored at their last confirmed move, not as successes. Interpret alongside success rate.
- **Resources:** total wall time, input/output tokens if exposed, calls by type, and human interventions. Separate attempted and confirmed actions, and identify unconfirmed outcomes. Do not equate configured timeout with observed duration.
- Report per-arm counts and paired differences at equal initial state, sample size, dispersion, and uncertainty. Do not combine replay with transfer or infer an overall ARC-AGI-3 score.

## 5. Trial record

```text
ID / date / operator:
Track: exploration / replay / transfer / compaction / restoration
Condition / pair / repetition / order:
Game / seed / starting level / initial grid fingerprint:
Model / version / settings / seed if available:
Runner / version / objective / available observations:
Budgets: actions / time / tokens / calls
Verified isolation controls:
Persistence / context rules / Auto Compute trigger and cap:
Imported artifacts: type / version / fingerprint / authorization
Compaction or restoration: step / objects / results / cost
First level confirmed: yes/no, move if known
Levels confirmed at cap / at stop:
Actions attempted / last confirmed / unconfirmed outcomes and indices:
Stop reason / configured timeout / measured wall time:
Input and output tokens / calls by type:
Human interventions and nature:
Validated artifacts / trace references / protocol deviations:
```

Mark unknowns as not reported and leave export cells empty. Zero denotes an observed count.
