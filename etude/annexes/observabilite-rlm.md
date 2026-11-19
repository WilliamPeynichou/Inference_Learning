# RLM Observability: From the ARC-AGI-3 Pilot to Chat Usage

**Status:** user observations and measurement plan, not quantified findings. No new trial was run for this note.

## What the pilot can distinguish

The `ls20` pilot reports a recalculated path of **13 rather than 15 moves**, reusing grids and functions present in the REPL. Raw traces for independent verification are unavailable; model calls, tokens, and time are not reported. Accounts disagree on the tools used for the first path, so this contrast does not measure a causal persistence effect. See the [pilot report](rapport.md).

Instrument each stage: observation, hypothesis, computation, action, verification, and reuse. A successful action, a short turn, and a low cost are different outcomes.

## Observations to test

| Reported observation | Primary measure | Alternatives to distinguish |
|---|---|---|
| Rate limits appear to arrive later on Opus 5.5, Fable 5.2, and 6.2 Sol. | Active time and validated tasks before the first limit signal, by model and quota window; separately record time to resumption. | A later limit is not a later reset. Distinguish account quota, transient limits, announced windows, and successful retries. |
| Cold workflows seem longer; turns appear shorter as Compute is used. | At comparable outcome quality, model calls, Python calls, confirmed actions, active and wall time per validated task; identify first creation, reuse, and reconstruction. | Runtime warm-up, method reuse, easier tasks, or less visible text. Do not attribute the difference to Auto Compute without a dedicated contrast. |
| Visible text is short because task commentary is not requested. | Visible text size and provider-exposed output, reasoning, and tool-call tokens where available. | Less commentary may reduce visible output without reducing reasoning or total tokens. |
| Most displayed tokens appear to be input; reused Python variables might contribute. | Total input, cache reads/writes when exposed, size of Python outputs actually sent to the model, cost, and calls. | An in-memory object does not consume tokens merely by existing. Serialized content, transmitted code, and references can contribute. |

## Three concepts to log separately

- **Python state:** an object, function, or plan survives between REPL calls. Log creation, modification, reuse, and reconstruction using a local ID and optional fingerprint. This is neither provider prompt caching nor evidence of restoration after shutdown.
- **Provider cache:** provider-reported prompt cache reads or writes, if exposed. It may coexist with persistent Python. A missing field means **not exposed**, not zero. Respect provider definitions: totals may already include cache or reasoning.
- **Transmitted context:** what the model actually receives, including Python results if reinjected. If token attribution by source is unavailable, output size in bytes is a proxy, not an exact token breakdown.

## Minimum trial trace

| Level | Fields |
|---|---|
| Trial | ID, task and success criterion, exact model/provider, reasoning settings, harness/version, cold or warm state, imported artifacts, output instruction, budget, order. |
| Call or action | Time, turn ID, type (model, Python, Auto Compute, runner), duration, outcome, attempted and confirmed actions. For Python, object creation/reuse/reconstruction and returned size if observable. |
| Model usage | Exposed usage fields and semantics, input/output, reasoning, and cache tokens when available; visible text and cost separately. Include automated work and retries. |
| Limit | Type if known, first block time, reset or `Retry-After` if exposed, first observed resumption, and window end. Separate active, quota-wait, and wall time. |

Do not log secrets, raw prompts, or private Python values. Leave unknown values blank and report coverage by model. For a trial without a block, record “no block observed before stopping”; do not infer unlimited duration.

## Initial measurement plan

1. **Calibrate on `ls20`.** Align a runner-confirmed move with its turn, associated calls, and reused Python objects. Separate discovery cost from replay cost. Do not convert a difference in moves into token savings.
2. **Hold task and model constant.** Pair reset and persistent Python with the same short-output instruction and Auto Compute disabled. Separate cold runs, within-trial reuse, and imported artifacts. Compare short output with requested commentary, then Auto Compute off/on, changing one factor at a time.
3. **Use separate quota blocks.** For each model, record provider, account type, and starting quota if observable; balance order and avoid untracked usage sharing the same window. Set caps in advance and compare within models before comparing provider quotas.
4. **Compare at similar quality.** Report successes/trials and resources per validated task with denominators and failed-trial costs separately. Show cold and warm turns, waits, and paired differences. If reasoning, cache, or internal calls are not exposed, do not claim savings in those categories.

The [main protocol](protocole.md) covers isolation, ablations, and transfer to unseen games.
