# Reddit Multi-Subreddit Launch Strategy

## Subreddit Targets by Angle

### Tier 1: Primary Audience (Post First)

| Subreddit | Members | Angle | Post Title |
|-----------|---------|-------|------------|
| r/ClaudeAI | 7K+ | AI capabilities | "I gave Claude Code a wallet. Now it generates images and accesses real-time X data." |
| r/LocalLLaMA | 300K+ | Multi-model routing | "One wallet, 30+ models: Route between GPT, Grok, DeepSeek from Claude Code" |

### Tier 2: Crypto/Web3 Audience

| Subreddit | Members | Angle | Post Title |
|-----------|---------|-------|------------|
| r/base | 15K+ | Base L2 use case | "Real use case for USDC on Base: AI agent micropayments" |
| r/coinbase | 200K+ | USDC utility | "Built an AI agent that pays for its own capabilities with USDC" |
| r/ethdev | 100K+ | x402 protocol / dev tool | "x402 micropayments in action: AI agents paying for API calls" |
| r/ethereum | 2M+ | Novel ETH use case | "AI agents with wallets: micropayments for model access on Base" |
| r/CryptoCurrency | 7M+ | Adoption story | "Finally a crypto use case that isn't speculation: AI agent payments" |

### Tier 3: Developer Audience

| Subreddit | Members | Angle | Post Title |
|-----------|---------|-------|------------|
| r/programming | 6M+ | No API keys | "Tired of managing 5 AI API keys. Built a wallet-based solution." |
| r/webdev | 2M+ | Developer tooling | "One wallet replaces 5 API keys for AI model access" |
| r/SideProject | 500K+ | Indie builder story | "I built a wallet for Claude Code so it can pay for GPT, DALL-E, Grok" |

---

## Tailored Post Bodies

### For r/base and r/coinbase (Crypto angle)

```markdown
**TL;DR:** I built a Claude Code plugin that uses USDC on Base for AI micropayments.

**The problem:** AI developers juggle 5+ API keys (OpenAI, xAI, Google, DeepSeek). Each has its own billing, credentials, rate limits.

**The solution:** One wallet funded with USDC on Base. When Claude needs GPT, DALL-E, or Grok, it pays per-request via x402 micropayments.

**Why Base/USDC:**
- Fast, cheap transactions
- USDC is stable (no volatility)
- x402 protocol handles payment negotiation

**Cost examples:**
- GPT-5 call: $0.001
- Image generation: $0.05
- Real-time X data: $0.26

$1 USDC = ~1,000 GPT calls

**This is what crypto payments should be:** invisible, instant, useful.

Open source: [link]
```

### For r/ethdev (Developer angle)

```markdown
**TL;DR:** Implemented x402 micropayments for AI API access. Thought the community might find this interesting.

**What I built:** A Claude Code plugin that lets the AI agent pay for external model calls (GPT, Grok, DALL-E) using USDC on Base.

**How x402 works in practice:**
1. Agent needs capability (e.g., image generation)
2. Server returns 402 Payment Required + price
3. Agent signs payment authorization
4. Server verifies, executes, settles on-chain

**Stack:**
- Base L2 for settlement
- USDC for payments
- x402 protocol for negotiation
- Python SDK: `pip install blockrun-llm`

**Key design decisions:**
- Private key stays local (only signatures transmitted)
- Pay-per-request (no subscriptions)
- Agent-controlled spending (can set budgets)

Would love feedback from anyone who's worked with x402 or similar micropayment protocols.

GitHub: [link]
x402 spec: https://x402.org
```

### For r/LocalLLaMA (Multi-model angle)

```markdown
**TL;DR:** Built a router that lets Claude Code call GPT, Grok, DeepSeek, DALL-E via one wallet.

**The idea:** Different models are better at different things. Claude is great, but:
- Can't generate images → route to DALL-E
- No real-time X data → route to Grok
- Expensive for bulk tasks → route to DeepSeek

Instead of managing 5 API keys, you fund one wallet with $1-5 USDC.

**Cost comparison:**
| Model | Cost per call |
|-------|---------------|
| GPT-5 | $0.001 |
| DeepSeek | $0.0001 |
| Grok + live X | $0.26 |
| DALL-E 3 | $0.05 |

**Smart routing:** Plugin auto-detects when to use what:
- Mentions Twitter/X → Grok
- Image request → DALL-E
- Bulk processing → DeepSeek

Open source, MIT license: [link]
```

---

## Posting Schedule

Spread posts over 1-2 weeks to avoid looking like spam:

| Day | Subreddit | Time (PT) |
|-----|-----------|-----------|
| Day 1 | r/ClaudeAI | 9am |
| Day 2 | r/LocalLLaMA | 10am |
| Day 3 | r/base | 9am |
| Day 4 | r/ethdev | 10am |
| Day 5 | r/coinbase | 9am |
| Day 7 | r/SideProject | 10am |
| Day 8 | r/programming | 9am |

---

## Rules to Follow

1. **Don't cross-post** - Write unique content for each sub
2. **Engage with comments** - Reply to every comment in first 2 hours
3. **Don't be salesy** - Share the story, not the pitch
4. **Follow sub rules** - Some ban self-promotion, check first
5. **Use correct flair** - Each sub has different flair requirements

---

## Subreddits to AVOID (strict self-promo rules)

- r/technology (will get removed)
- r/startups (requires specific format)
- r/entrepreneur (very strict)

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Total upvotes across posts | 200+ |
| Comments to respond to | 50+ |
| GitHub stars from Reddit | 50+ |
| Wallets funded | 10+ |
| Users in GitHub Discussions | 20+ |
