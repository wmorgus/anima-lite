#!/usr/bin/env python3
"""
session-cost.py — SessionEnd hook, first mechanical sensor (PIN-3/5).

Reads the hook JSON payload from stdin, parses the session's transcript
JSONL, sums token usage across assistant messages grouped by model, and
writes a session-cost row to .anima-lite/metrics/sessions/ per
.claude/skills/ari-port/metrics-spec.md.

This is a metrics hook, not a discipline hook: it must never break a
session. Every failure path exits 0 silently. Nothing here estimates —
missing fields are treated as 0 for summation, and if the transcript or
the .anima-lite/ guard can't be satisfied, the hook simply writes nothing.
"""
import json
import os
import sys
from datetime import date


def main():
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return
        payload = json.loads(raw)
    except Exception:
        return

    try:
        cwd = payload.get("cwd") or ""
        session_id = payload.get("session_id") or "unknown-session"
        transcript_path = payload.get("transcript_path") or ""

        if not cwd:
            return

        # Guard: only write if this cwd is an anima-lite project directory.
        anima_lite_dir = os.path.join(cwd, ".anima-lite")
        if not os.path.isdir(anima_lite_dir):
            return

        if not transcript_path or not os.path.isfile(transcript_path):
            return

        usage_by_model = {}
        message_count = 0

        with open(transcript_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except Exception:
                    continue

                message = entry.get("message", entry)
                if not isinstance(message, dict):
                    continue
                if message.get("role") != "assistant":
                    continue

                usage = message.get("usage") or entry.get("usage")
                if not isinstance(usage, dict):
                    continue

                model = message.get("model") or entry.get("model") or "unknown"

                bucket = usage_by_model.setdefault(
                    model,
                    {
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "cache_read_input_tokens": 0,
                        "cache_creation_input_tokens": 0,
                    },
                )
                bucket["input_tokens"] += usage.get("input_tokens", 0) or 0
                bucket["output_tokens"] += usage.get("output_tokens", 0) or 0
                bucket["cache_read_input_tokens"] += (
                    usage.get("cache_read_input_tokens", 0) or 0
                )
                bucket["cache_creation_input_tokens"] += (
                    usage.get("cache_creation_input_tokens", 0) or 0
                )
                message_count += 1

        today = date.today().isoformat()
        session_prefix = session_id[:8]
        out_dir = os.path.join(anima_lite_dir, "metrics", "sessions")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{today}-{session_prefix}.md")

        lines = []
        lines.append(f"# Session cost: {today} {session_prefix}")
        lines.append(f"Session ID: {session_id}")
        lines.append(f"Date: {today}")
        lines.append("")
        lines.append("## Tokens by model")
        lines.append("| Model | Input | Output | Cache read | Cache creation |")
        lines.append("|---|---|---|---|---|")
        if usage_by_model:
            for model, bucket in sorted(usage_by_model.items()):
                lines.append(
                    "| {model} | {i} | {o} | {cr} | {cc} |".format(
                        model=model,
                        i=bucket["input_tokens"],
                        o=bucket["output_tokens"],
                        cr=bucket["cache_read_input_tokens"],
                        cc=bucket["cache_creation_input_tokens"],
                    )
                )
        else:
            lines.append("| not traced | 0 | 0 | 0 | 0 |")
        lines.append("")
        lines.append("## Message count")
        lines.append(f"{message_count} assistant messages")
        lines.append("")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    except Exception:
        # Fail silent — a metrics hook must never break a session.
        return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
