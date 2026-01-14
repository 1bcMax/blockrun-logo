# r/SideProject Post (Day 7)

## Title
I built a wallet for Claude Code so it can pay for GPT, DALL-E, Grok on its own

## Body

**The problem I was solving:**

I use Claude Code daily. It's incredible, but:
- Can't generate images
- No real-time Twitter/X data
- When I need GPT's opinion, I have to switch contexts
- Managing 5 API keys (OpenAI, xAI, Google, DeepSeek) is annoying

**What I built:**

BlockRun - a plugin that gives Claude a crypto wallet. When it needs a capability it doesn't have, it pays for it.

```
Me: "Generate a hero image for my landing page"
Claude: "I can't generate images. Want me to use DALL-E?"
Me: "Yes"
→ Image appears. Cost: $0.05
```

**The magic:** No API keys. Instead of 5 accounts, you fund one wallet with $1-5 USDC. Claude pays per-request.

**Tech stack:**
- Python SDK (`pip install blockrun-llm`)
- USDC on Base for payments
- x402 protocol for micropayments
- Local wallet (private key never leaves your machine)

**Costs:**
- GPT-5 call: $0.001 (1,000 calls per $1)
- DeepSeek call: $0.0001 (10,000 calls per $1)
- Image generation: $0.05
- Real-time X search: $0.26

**What I learned building this:**

1. Crypto micropayments actually work now (Base L2 is fast/cheap)
2. AI agents with wallets is a weird but useful paradigm
3. "No API keys" is a better pitch than I expected

**Stats so far:**
- Open source (MIT license)
- Works with Claude Code today
- 30+ models available

GitHub: https://github.com/BlockRunAI/blockrun-claude-code-wallet

---

Would love feedback. What features would make this more useful for your workflow?
