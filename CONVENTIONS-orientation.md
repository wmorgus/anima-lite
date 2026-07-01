# Orientation and Compaction Conventions

## Caveman is the default, not a mode you opt into

You start every session in caveman. It stays on until the session ends. It is not something you toggle when things feel dense — it is the floor.

You may drop to prose only when one of the four auto-clarity exceptions from the caveman skill applies: a security warning, an irreversible operation, a multi-step sequence the user must follow in order, or an explicit request to clarify. If you drop, name the exception inline before the prose, in one fragment: `[clarity: irreversible op]`. Then write the prose. Then return to caveman.

If none of the four apply, caveman stays — even when prose would read more smoothly. Smoothness is not an exception. Wanting to explain is not an exception. The absence of a named exception means the rule holds. You self-apply this without asking; the exception list is closed, so you can always check it yourself.

The failure mode this prevents: drifting into prose one justified-feeling sentence at a time until the register is gone and no single step was ever named as the drop. Every drop is a discrete, labeled event or it did not happen.

## Agent-initiated compaction runs through haircut

You may initiate compaction yourself when context pressure is high. The signal is concrete: you are re-reading files you already read this session to recover state, or your working set no longer fits in what you can hold, or a ari-port blip log has grown past the point where you can cite earlier decisions without scrolling. Any one of these is enough. Do not wait for the user.

The sequence is fixed: run `/haircut`, write the haircut output as the state anchor, then compact. Never compact before the anchor is written — the pre-compact hook does not inject caveman rules (its `PreCompact` hookEventName fails schema validation), so the anchor is the only thing that survives into the next window. If you skip it, the next window opens in default register with no task memory.

The haircut message is what the next window wakes up to. It must contain, in caveman: (1) register assertion — caveman on, exceptions closed-list; (2) task state — which ari-lite stage you are in (map / argue / port / validate), the current branch contract ID, and the last committed blip; (3) live constraints — what the contract forbids translating freely (claim changes awaiting confirmation), and any halt-back condition you were watching; (4) next action — the single next step, stated so the fresh context can act without re-deriving it.

Write the anchor to be read cold. The next window has no memory of why you were mid-task — only what the anchor says. If the anchor cannot orient a blank agent to the exact next move, it is not done, and you have not earned the compact yet.
