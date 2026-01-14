# r/LocalLLaMA Post (Day 2)

## Title
One wallet, 30+ models: Route between GPT, Grok, DeepSeek, DALL-E from Claude Code

## Flair
Resources

## Body

Different models are better at different things. I got tired of managing 5 API keys to access them all, so I built a unified router.

**The idea:** Give Claude Code a wallet. When it needs a capability, it pays the right model:

| Task | Routes to | Why | Cost |
|------|-----------|-----|------|
| Generate image | DALL-E | Claude can't do images | $0.05 |
| Real-time X/Twitter | Grok | Only model with live X access | ~$0.26 |
| Code review | GPT-5 | Different perspective catches different bugs | $0.001 |
| Bulk summarization | DeepSeek | 10x cheaper for simple tasks | $0.0001 |

**Smart routing built-in:**
- Mentions Twitter/X → auto-routes to Grok
- Image request → auto-routes to DALL-E
- `--cheap` flag → routes to DeepSeek
- `--fast` flag → routes to GPT-5-mini

**Cost comparison:**

$1 USDC gets you:
- ~1,000 GPT-5 calls
- ~10,000 DeepSeek calls
- ~20 DALL-E images
- ~4 Grok queries with live X search

**No API keys.** One wallet funded with USDC on Base. Pay per request via x402 micropayments.

**Install:**
```
/plugin install github:BlockRunAI/blockrun-claude-code-wallet
pip install blockrun-llm
```

**Python SDK:**
```python
from blockrun_llm import LLMClient

client = LLMClient()
response = client.chat("openai/gpt-5.2", "Review this code for bugs")
print(response)

# Check spending
print(f"Spent: ${client.get_spending()['total_usd']:.4f}")
```

Open source (MIT): https://github.com/BlockRunAI/blockrun-claude-code-wallet

---

What models would you add to the routing? Thinking about adding Mixtral, Llama, etc.
