# BlockRun

**The Trust Layer for AI Agent Payments**

---

## The Pattern

Every payment system requires trust infrastructure before it scales.

| Era | Payment System | Trust Layer | Time to Scale |
|-----|----------------|-------------|---------------|
| 1958 | Consumer credit | FICO | 30 years |
| 1994 | E-commerce | SSL/Verisign | 10 years |
| 2007 | Mobile payments | Device fingerprinting | 5 years |
| 2026 | AI agent payments | **?** | — |

x402 v2 launched December 2025. AI agents can now pay for services with USDC—automatically, programmatically, irreversibly.

**The payment rails exist. The trust layer doesn't.**

BlockRun is building it.

---

## The Problem

x402 payments are **irreversible**. No refunds. No chargebacks. No customer service.

When an AI agent pays for a service, it needs to know: *Will this service actually deliver?*

Right now, there's no way to know.

**What we found analyzing 700+ x402 services:**

- Services disappear after collecting payments
- Response times vary 100x between providers offering identical APIs
- No standardized uptime reporting
- No historical reliability data
- Agents pay first, discover quality after

An AI agent managing a $10,000 portfolio has no way to evaluate whether a $0.10 API call will return valid data or drain funds to a dead endpoint.

**The ecosystem is growing. Trust is not.**

---

## BlockRun

We're building trust infrastructure in three phases:

### Phase 1: AI Gateway (LIVE)

The wedge. Proves we can deliver reliable AI services via x402.

- **31 LLM models** — GPT-4o, Claude, Gemini, DeepSeek and so on
- **Pay-per-use** — USDC on Base, no minimums
- **No accounts** — Wallet is identity
- **Transparent pricing** — Provider cost + 5%, published

Live on Base mainnet since January 2026. Users onboarding now.

### Phase 2: Trust Ratings (Q1 2026)

The product. Quality scores for every x402 service.

- **Uptime monitoring** — Continuous availability checks
- **Latency tracking** — Response time distributions over time
- **Delivery verification** — Did the service return valid responses?
- **Pattern analysis** — Detecting manipulation and fraud signals

Open methodology. Verifiable scoring. The x402 ecosystem's first reliability layer.

### Phase 3: Agent Credit Bureau (2027)

The moat. Financial infrastructure for autonomous entities.

- Agent identity and transaction history
- Reputation scores for AI agents themselves
- Credit and settlement services for machine-to-machine commerce

---

## Why Infrastructure

We're not building an application that uses x402.

We're building the layer that **every x402 application needs**.

```
┌─────────────────────────────────────────────┐
│            Applications                      │
│   Trading bots, research agents, AI tools   │
├─────────────────────────────────────────────┤
│            Trust Layer                       │
│   Ratings, verification, routing            │
│              ▲ BlockRun                      │
├─────────────────────────────────────────────┤
│            Protocol                          │
│   x402, USDC, Base                          │
│   Coinbase, Circle, Cloudflare              │
└─────────────────────────────────────────────┘
```

Applications come and go. **Infrastructure compounds.**

---

## The Moat

Raw transaction data is on-chain. Anyone can read it.

**Our moat is interpretation, not information.**

| Asset | Why It Compounds |
|-------|------------------|
| **Methodology** | Scoring algorithms refined through thousands of edge cases |
| **Historical depth** | 18 months of daily measurements by mid-2027 |
| **SDK relationships** | Embedded in developer workflows, not easily displaced |
| **Brand trust** | Services want BlockRun verification; agents trust BlockRun scores |

A competitor starting in Q3 2026 can see the same blockchain data.

They cannot replicate 8 months of uptime measurements, latency distributions, and calibrated fraud signals.

**Trust infrastructure is built through track record.**

---

## Distribution

Developer tools grow through SDK integrations, not marketing.

| Integration | Developer Reach | Status |
|-------------|-----------------|--------|
| Polymarket Agent | 10,000+ agent developers | submit |
| GOAT SDK | 150,000+ npm downloads | In progress |
| solana-agent-kit | Solana agent ecosystem | On roadmap |
| LangChain | Millions of developers | On roadmap |

**Each integration = distribution to their entire developer base.**

We ship code to repositories. Developers discover us through their tools.


---

## Traction

| Metric | Status |
|--------|--------|
| AI Gateway | **Live** — Base mainnet, January 2026 |
| Models available | 31 |
| Services indexed | 300+ |
| Autonomous agent demo | **Live** — Polymarket trading agent |
| Coinbase x402 repo | PR merged, feature requests open |
| PayAI partnership | Data sharing active |
| User onboarding | **Active** — Solana support requested |

**Live Demo: Autonomous Polymarket Trading Agent**

We built a fully autonomous agent that proves the thesis:

- **Manages own wallet** — USDC balance on Polygon
- **Uses BlockRun AI Gateway** — Analyzes markets via GPT, Claude, Gemini
- **Places real trades** — Autonomous decisions, real money
- **Runs 24/7** — Deployed and run

It's a working agent using BlockRun's infrastructure to access AI models, analyze prediction markets, and execute trades—completely autonomously.

**The product is live. Users are asking for more chains.**

---

## Business Model

Two revenue streams, one flywheel:

| Stream | Fee | Purpose |
|--------|-----|---------|
| AI Gateway | 5% markup | Proves delivery, generates cash |
| Trust Routing | 5% of routed volume | Where we scale |

**Unit economics:**

- Average transaction: $0.10
- Gateway margin: $0.005 per transaction
- Trust Routing fee: $0.005 per transaction

| Monthly Transactions | Monthly Revenue |
|---------------------|-----------------|
| 1M | $5K - $10K |
| 10M | $50K - $100K |
| 100M | $500K - $1M |

We're capturing margin on the growth curve.

---

## Why Me

I spent the last decade building trust infrastructure for payments.

**Circle** — Head of Data Science
- Built the data infrastructure underlying USDC
- Designed monitoring systems for billions in stablecoin flows
- Shipped the analytics that institutions use to trust Circle

**Capital One** — Director of Data Science
- Led anti-fraud AI for consumer credit
- Built systems evaluating millions of transactions daily

**Microsoft** — Azure ML Tech Lead
- Scaled ML infrastructure for enterprise customers

The x402 ecosystem needs what I built at Circle: **trust infrastructure that makes money move safely**.

The difference: this time it's for machines, not institutions.

---

## The Ask

**$2M Seed**

| Use of Funds | Allocation |
|--------------|------------|
| Engineering | 40% — Senior infra + ML engineer, accelerate Trust Ratings |
| Integrations | 30% — SDK partnerships, AgentKit launch, multi-chain |
| Operations | 30% — Infrastructure, go-to-market, community |

**Milestones:**

| Quarter | Target |
|---------|--------|
| Q2 2026 | Trust Ratings beta, AgentKit integration live |
| Q4 2026 | $10K MRR, Solana support, 10+ SDK integrations |
| Q2 2027 | $50K MRR, multi-chain live |
| Q4 2027 | $100K MRR, 100K daily transactions |

**24-month runway** to establish BlockRun as the default trust layer for x402.

---

## Why Now

**The window is about 18 months.**

x402 v2 launched December 2025. 

Three outcomes are possible:

1. **Coinbase builds it themselves** — Unlikely. They're focused on protocol, not application-layer trust.

2. **A competitor emerges** — Possible. But we have code merged into their repo, partnerships with facilitators, and a live product.

3. **BlockRun becomes the standard** — This is what we're executing toward.

Infrastructure credibility compounds. The team that ships first, ships longest.

**We shipped first.**

---

## Contact

**Vicky Fu**
vicky@blockrun.ai

**Links:**
- Live product: [blockrun.ai](https://blockrun.ai)
- AI Gateway Demo: [x.com/BlockRunAI/status/2006125447596118289](https://x.com/BlockRunAI/status/2006125447596118289)
- **Autonomous Polymarket Agent**: [polymarket-agent-tokyo.run.app](https://polymarket-agent-tokyo.run.app)
- x402 Research: [x.com/bc1beat/status/2007180567436255725](https://x.com/bc1beat/status/2007180567436255725)
- GitHub: [github.com/BlockRunAI](https://github.com/BlockRunAI)

---

## Appendix: Technical Proof Points

**Open Source Contributions:**
- `github.com/coinbase/x402/pull/857` — Merged
- `github.com/coinbase/x402/issues/869` — Feature request
- `github.com/Polymarket/agents/pull/124` — Integration PR

**Live Infrastructure:**
- AI Gateway on Base mainnet
- 31 models, USDC payments, sub-second settlement
- Monitoring 618+ x402 services daily
- **Autonomous Polymarket trading agent** — Live at polymarket-agent-tokyo.run.app

**Live Demos:**
- **Polymarket Agent** — Autonomous trader with own USDC wallet, uses BlockRun AI Gateway for market analysis, places real trades 24/7
- **AI Gateway** — Pay-per-use access to GPT-4, Claude, Gemini, DeepSeek via USDC micropayments

**Research:**
- "State of x402 2025" report — 2,000+ engagements
- Comprehensive ecosystem mapping
- Transaction pattern analysis across all major facilitators