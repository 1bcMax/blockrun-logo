# r/coinbase Post (Day 5)

## Title
Built an AI agent that pays for its own capabilities with USDC on Base

## Body

Wanted to share a project that uses USDC for something other than trading.

**The problem:** I use Claude Code for development. It's great, but can't generate images, has no real-time data, and I end up managing 5 different AI API accounts.

**The solution:** I gave Claude a wallet. When it needs something it can't do, it pays for it with USDC.

**Example:**

```
Me: "Generate a logo for my startup"
Claude: "I can't generate images. Want me to use DALL-E via BlockRun?"
Me: "Yes"
→ Claude pays $0.05 USDC, gets the image
```

**Why USDC on Base:**

- Stable value (no "oops my AI spent $500 because ETH pumped")
- Micropayments actually work ($0.001 per API call)
- Fast and cheap on Base L2
- Easy to fund from Coinbase

**What $1 USDC gets:**

| Model | Calls per $1 |
|-------|--------------|
| GPT-5 | ~1,000 |
| DeepSeek | ~10,000 |
| DALL-E images | ~20 |
| Grok (real-time X) | ~4 |

**How to fund the wallet:**

1. Install plugin, wallet auto-creates
2. Get wallet address (it's just an Ethereum address)
3. Send $1-5 USDC on Base from Coinbase
4. Done

Private key stays on your machine. Only signatures sent to servers.

Open source: https://github.com/BlockRunAI/blockrun-claude-code-wallet

---

I think this is what crypto payments should look like - invisible, useful, no speculation. Curious what you all think.
