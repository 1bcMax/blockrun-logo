# r/ethdev Post (Day 4)

## Title
x402 micropayments in practice: AI agents paying for API calls on Base

## Body

Implemented x402 for a real use case - thought the community might find the architecture interesting.

**What I built:** A Claude Code plugin where the AI agent pays for external API calls (GPT, Grok, DALL-E) using USDC on Base.

**x402 flow in practice:**

```
1. Agent: POST /v1/chat/completions
2. Server: 402 Payment Required
   Headers:
   - X-Payment-Amount: 0.001
   - X-Payment-Token: USDC
   - X-Payment-Network: base
3. Agent: Signs EIP-712 payment authorization
4. Agent: Retries with X-Payment-Signature header
5. Server: Verifies signature, executes request, settles
```

**Key design decisions:**

**Private key stays local.** Only signatures are transmitted. Server can verify without holding keys.

**Pay-per-request, not subscriptions.** Agent only pays for what it uses. $0.001 per GPT call, $0.0001 per DeepSeek call.

**Budget controls.** Agent can set daily spending limits:
```python
client = LLMClient()
client.set_budget(1.00)  # Max $1/day
```

**Stack:**
- Base L2 for settlement
- USDC for stable payments
- EIP-712 for typed signatures
- Python SDK: `pip install blockrun-llm`

**Python example:**

```python
from blockrun_llm import LLMClient

client = LLMClient()  # Auto-creates wallet at ~/.blockrun/

# Agent pays for the call
response = client.chat("openai/gpt-5.2", "Explain x402 protocol")

# Check what it cost
spending = client.get_spending()
print(f"Total: ${spending['total_usd']:.4f}")
```

**Open questions I'm still thinking about:**

1. Better UX for wallet funding (currently requires manual USDC transfer)
2. Multi-sig for team wallets?
3. Streaming payments for long-running requests?

GitHub: https://github.com/BlockRunAI/blockrun-claude-code-wallet
x402 spec: https://x402.org

Would love feedback from anyone who's worked with 402 payments or similar patterns.
