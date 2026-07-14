---
name: check-context
description: Report estimated token usage for the current conversation.
disable-model-invocation: true
---

# Check Context

Calculate and report the current conversation's token **footprint**.

## Steps

1. **Locate**: Extract the current conversation ID from your system prompt. The target file is `$env:USERPROFILE\.gemini\antigravity\brain\<conversation-id>\.system_generated\logs\transcript_full.jsonl`.
2. **Measure**: Run a PowerShell command to get the file size of the target file in bytes. Use `$env:USERPROFILE` to resolve the path dynamically, e.g. `(Get-Item "$env:USERPROFILE\.gemini\antigravity\brain\<id>\.system_generated\logs\transcript_full.jsonl").Length`.
3. **Recover**: If the file is not found, the path is wrong. A conversation log always exists. Search `"$env:USERPROFILE\.gemini\antigravity\brain\"` to find the correct `transcript_full.jsonl` path, fix your path variable, and re-measure.
4. **Calculate**: Divide the file size in bytes by 4 to estimate the **footprint**. Round to the nearest integer.
5. **Report**: Output exactly this string to the user: `ใช้ไปแล้ว [footprint] Tokens`. Do not add conversational filler.

**Completion criterion**: The exact Thai report string is output to the user.
