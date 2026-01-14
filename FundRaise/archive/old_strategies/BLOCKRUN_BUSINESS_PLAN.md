# BlockRun Business Plan

**Prepared for:** Investor Review
**Date:** December 2025
**Version:** 3.1

---

## Executive Summary

**BlockRun is the trust layer for autonomous AI payments.**

x402 has exploded in 2025: over **100M transactions** and **$600M+ in volume** processed, powering AI agents and micropayments. But irreversible payments demand trust: *Is the service legitimate? Will it deliver? Is the price fair?*

We provide those answers.

**Two products:**

1. **AI Gateway (blockrun.ai)** — *Live in beta*. Pay-per-use access to 31+ frontier LLMs (GPT-5 series, Gemini 2.5, o1, Claude, DeepSeek). No API keys. No subscriptions. OpenAI-compatible. This is our trust anchor—proving reliability as an x402 service.

2. **Trust + Routing API** — *In development*. Quality scores, legitimacy detection, uptime monitoring, price benchmarking across the x402 ecosystem. Agents route payments through us for verified services—we charge 5%.

```
The Trust Flywheel:
┌─────────────────────────────────────────────────────────────────┐
│  AI Gateway proves BlockRun is trustworthy (live now)           │
│       ↓                                                         │
│  We rate other services (legitimacy, uptime, price fairness)    │
│       ↓                                                         │
│  Agents trust our ratings → route payments through us           │
│       ↓                                                         │
│  More routing data → better ratings → more trust                │
└─────────────────────────────────────────────────────────────────┘
```

| Metric | Detail |
|--------|--------|
| **Core Value** | Trust signals for irreversible payments |
| **Products** | AI Gateway (live) + Trust/Routing API (building) |
| **AI Models** | 31+ (GPT-5 series, o1, Gemini 2.5, Claude, DeepSeek) |
| **Ecosystem Coverage** | 700+ services, 3,500+ endpoints tracked |
| **Revenue Model** | AI markup (2-5%) + Routing premium (5%) |
| **Stage** | AI Gateway live on Base mainnet (beta) |
| **Founder** | Vicky Fu - Head of Data Science @ Circle (2021-2024) |
| **Funding Ask** | $750K angel round |

**Why Now:** x402 has processed 100M+ transactions worth $600M+. The ecosystem is exploding—but agents still lack trust signals for unknown services. First mover in trust wins.

---

## The x402 Opportunity

### What is x402?

x402 revives HTTP status code 402—"Payment Required"—enabling any web resource to require payment before access. The protocol failed in 1997 because payment infrastructure didn't exist. Today, stablecoins settle in seconds for fractions of a cent.

### The Market is Real (and Exploding)

| Metric | Value | Context |
|--------|-------|---------|
| **Total Transactions** | 100M+ | Peaks at millions/day |
| **Total Volume** | $600M+ USDC | Q4 2025 explosion |
| **Active Buyers** | 20,000+ | Expanding weekly |
| **Active Services** | 700+ | New entries daily |
| **Average Transaction** | $0.24 | Micropayment sweet spot |

*Data from x402scan.com and BlockRun ecosystem analysis (December 2025).*

**Major ecosystem developments in 2025:**
- x402 Foundation launched (Coinbase + Cloudflare governance)
- Multi-chain support: Base, Solana, Polygon
- Enterprise integrations: Anthropic MCP, Google AP2, Circle Gateway

**Why micropayments matter:** A $0.01 transaction on credit card rails costs $0.30+ in fees—3,000% overhead. Stablecoin rails reduce this to fractions of a cent.

### AI Agents Dominate

| Category | % of Ecosystem |
|----------|----------------|
| **AI Agent** | **46%** |
| Developer Tools | 17% |
| Blockchain Data | 14% |
| Payment | 11% |
| Other | 12% |

AI agents are 46% of x402 services—validating the core thesis that autonomous agents need native payment infrastructure.

### Why Now: The Long-Tail is Already Here

A fair question: *"If 90% of agent payments are just calling GPT-4o, does the long-tail market even exist yet?"*

**The data says yes:**

| Metric | Value | Implication |
|--------|-------|-------------|
| **Total x402 services** | 700+ | Only ~10 are "known" (OpenAI, Claude, etc.) |
| **Non-AI services** | 54% | Blockchain data, DeFi, dev tools—all unknown |
| **Unique service providers** | 300+ | Long-tail is the majority |
| **New services/week** | 20-30 | Market is diversifying rapidly |

**The pattern:** Early x402 adoption was concentrated in AI inference (known providers). But as the ecosystem matures, agents are discovering they need more—DeFi data, on-chain analytics, specialized AI models, agent-to-agent services. **These are all "unknown" services where trust signals matter.**

We're not waiting for the market. The long-tail is 90% of services today. The question is: who helps agents navigate it?

---

## The Trust Problem

### x402 Solved Payments. It Didn't Solve Trust.

x402 enables any service to accept micropayments. But **payments are irreversible**. Once an agent sends USDC, there's no chargeback, no dispute resolution, no recourse.

This creates a fundamental problem: **How does an agent know it can trust a service before paying?**

### The Reality of the Ecosystem

| Finding | Data |
|---------|------|
| **Gaming is rampant** | ~40-50% of transactions show manipulation patterns |
| **Organic activity** | 50-60% of transactions are legitimate |
| **No quality signals** | Facilitators don't track uptime, response times, or success rates |
| **Price opacity** | No way to know if a price is fair vs. ecosystem benchmarks |

**Important nuance on gaming:** The 40-50% figure is transaction count, not volume. Gaming transactions are typically low-value (incentive farming, airdrop hunting). The legitimate 50-60% represents the real economic activity—and it's growing faster. As x402 V2 matures and real use cases dominate, gaming percentage continues to decline. **BlockRun's value is helping agents avoid the noise and route to legitimate services.**

### Why This Matters for Agents

Consider an autonomous agent that needs blockchain data:

1. It discovers 5 services offering "ETH/USDC price feeds"
2. Prices range from $0.01 to $0.50 per request
3. **Which one is legitimate?** The cheap one might be a scam. The expensive one might be overpriced.
4. **Which one will actually deliver?** No uptime history. No quality metrics.
5. **The agent pays... and hopes.**

This is why the ecosystem hasn't scaled. **Agents won't autonomously spend money without trust signals.**

### The "CDP Is Enough" Question

A fair objection: *"Most agents just need GPT-4o. Coinbase CDP handles that. Why pay BlockRun 5%?"*

**Answer: CDP is enough for known, trusted services.** If you're calling OpenAI through CDP, you know OpenAI will deliver.

But x402's promise is bigger than "pay OpenAI." It's a marketplace of thousands of services—DeFi data, blockchain analytics, specialized AI models, agent-to-agent services. **For the long tail, trust is the bottleneck.**

| Scenario | CDP Enough? | BlockRun Value |
|----------|-------------|----------------|
| Call GPT-4o | Yes | None—use CDP directly |
| Call unknown DeFi data service | No | Quality score, uptime, legitimacy |
| Find best price across 5 AI providers | No | Price comparison, routing |
| Discover new services in a category | No | Search + trust signals |

**We don't compete with CDP for known services. We enable the long tail that CDP can't trust-rate.**

---

## The Products

### Product 1: AI Gateway (blockrun.ai) — The Trust Anchor

**Pay-per-use access to 31+ frontier AI models. Live in beta. Proving that BlockRun delivers.**

The AI Gateway isn't just a revenue stream. It's how we establish credibility before asking agents to trust our ratings of others.

```
Agent → USDC Wallet → blockrun.ai → GPT-5 / o1 / Gemini 2.5 → Response
```

| Feature | Detail |
|---------|--------|
| **Models** | 31+ including GPT-5 series, o1, Gemini 2.5, Claude, DeepSeek |
| **API** | OpenAI-compatible (drop-in replacement) |
| **Payment** | USDC micropayments via x402 on Base |
| **Pricing** | Pay-per-request, transparent (0% markup during beta) |
| **Status** | Live on Base mainnet |

**How It Works:**
1. Agent calls blockrun.ai API (OpenAI-compatible)
2. BlockRun returns 402 Payment Required with price
3. Agent signs x402 payment (USDC on Base)
4. BlockRun calls AI provider, returns response
5. Payment settles on-chain

**Why the Gateway Matters Strategically:**

| Function | Why It Matters |
|----------|----------------|
| **Prove reliability** | Every successful request builds our reputation |
| **Demonstrate the model** | Show agents how x402 payments work |
| **Generate trust data** | Our own uptime/response metrics are the benchmark |
| **Create switching costs** | Once agents use our endpoint, they trust our ecosystem |

**Why agents use this:**
- No API keys to manage
- No subscriptions or upfront costs
- Wallet-based identity (no accounts)
- Access 31+ frontier models through one endpoint (continuously expanding)
- **They know BlockRun delivers because they've used it**

---

### Product 2: Trust + Routing API — The Intelligence Layer

**The question isn't "where can I find x402 services?" It's "which ones can I trust?"**

```
Agent: "I need blockchain data for ETH/USDC"
    ↓
BlockRun Trust API
    ↓
Returns options with trust scores:
  - Service A: 94% uptime, 53ms avg response, $0.02, VERIFIED ORGANIC
  - Service B: 72% uptime, 340ms avg response, $0.01, SUSPECTED GAMING
  - Service C: 99% uptime, 12ms avg response, $0.05, VERIFIED ORGANIC
    ↓
Agent selects trusted option → BlockRun routes payment
    ↓
BlockRun charges 5% for the trust signal
```

### What We Track (That No One Else Does)

| Trust Signal | How We Measure | Why It Matters |
|--------------|----------------|----------------|
| **Legitimacy** | Transaction pattern analysis | 40-50% of tx show gaming—we flag it |
| **Uptime** | Continuous monitoring | Does the service actually respond? |
| **Response time** | Latency tracking | Is it fast enough for real-time agents? |
| **Delivery rate** | Success/failure tracking | Does payment = delivery? |
| **Price fairness** | Ecosystem benchmarking | Is this price reasonable? |

### The Data We've Built

| Data Point | Coverage |
|------------|----------|
| **Projects scored** | 300+ |
| **Endpoints monitored** | 3,500+ |
| **Facilitators aggregated** | 6+ (Coinbase, PayAI, Daydreams, etc.) |
| **Networks** | Base, Solana |
| **Transaction history analyzed** | 100M+ transactions |

### Why Agents Pay 5%

| Without BlockRun | With BlockRun |
|------------------|---------------|
| Hope the service is legitimate | Legitimacy score (organic vs. gamed) |
| No quality data | Uptime, response time, delivery rate |
| No price context | Benchmark against ecosystem |
| Pay and pray | Pay with confidence |

**The 5% isn't for aggregation. It's for trust.**

---

### How the Products Connect: The Trust Flywheel

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│   1. AI Gateway proves we're trustworthy                          │
│      (Agent uses blockrun.ai → works → builds confidence)         │
│                           │                                        │
│                           ▼                                        │
│   2. Trust API rates the ecosystem                                 │
│      (We score 300+ services: uptime, legitimacy, price)          │
│                           │                                        │
│                           ▼                                        │
│   3. Agents trust our ratings → route through us                  │
│      (Why guess when BlockRun already verified?)                   │
│                           │                                        │
│                           ▼                                        │
│   4. More routing → more data → better ratings → more trust       │
│      (Flywheel compounds)                                          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**AI Gateway** = The anchor. We prove ourselves first.
**Trust API** = The product. Ratings that agents pay for.

---

## Business Model

### Two Revenue Streams

**1. AI Gateway Markup (2-5%)**

We pass through AI provider costs with a margin.

| Model | Provider Cost | BlockRun Price | Margin |
|-------|---------------|----------------|--------|
| GPT-4o-mini | $0.005 | $0.00525 | 5% |
| Claude Haiku | $0.008 | $0.0084 | 5% |
| GPT-5 | $0.05 | $0.0525 | 5% |

Current status: **0% margin (beta)**. Post-beta: 2-5%.

**2. Routing Premium (5%)**

Every transaction routed through Discovery API includes a 5% fee.

| Example | Service Cost | BlockRun Fee (5%) | Agent Pays |
|---------|--------------|-------------------|------------|
| Other AI service | $0.01 | $0.0005 | $0.0105 |
| Blockchain data | $0.50 | $0.025 | $0.525 |
| DeFi analytics | $1.00 | $0.05 | $1.05 |

### Why Agents Pay

| For AI Gateway | For Discovery Routing |
|----------------|----------------------|
| 31+ models, one endpoint | 3,500+ services, one API |
| No API keys | No facilitator integrations |
| OpenAI-compatible | Quality-ranked results |
| Pay-per-use | Best price guarantee |

### Unit Economics

| Metric | AI Gateway | Discovery Routing |
|--------|------------|-------------------|
| Avg transaction | $0.01 | $0.14 |
| BlockRun margin | 5% ($0.0005) | 5% ($0.007) |

### Additional Revenue (Future)

| Stream | Model | Status |
|--------|-------|--------|
| **Premium Analytics** | Subscription for service providers | Planned |
| **Enterprise API** | Custom SLA + volume discounts | Future |

### The Aggregation Moat

| Asset | Why It's Defensible |
|-------|---------------------|
| **Cross-facilitator data** | No one else aggregates all 6+ facilitators |
| **Quality scores** | Built from transaction history we observe |
| **Routing intelligence** | Improves with every transaction |
| **Trust reputation** | First mover in trust infrastructure |

Competitors can launch a routing layer, but they can't replicate:
- Our historical data across facilitators
- Quality signals built over time
- Trust established with agent developers

---

## Market Opportunity

### Total Addressable Market

| Market | Size | Source |
|--------|------|--------|
| **AI Agent Economy (2030)** | $30 trillion | a16z / Gartner |
| **AI Infrastructure (2025)** | $202 billion | Crunchbase |
| **Stablecoin Payments (2025)** | $2+ trillion/year | Circle |

### x402 Ecosystem Today

| Metric | Value |
|--------|-------|
| Active facilitators | 12+ |
| Production domains | 98.9% |
| Market concentration (HHI) | 168.5 (highly competitive) |
| Top 3 providers market share | 16.9% |

The market is extremely fragmented with no dominant players. This is the time to establish position.

---

## Competitive Landscape

### Why No One Else Does This

| Player | What They Do | Why They Can't Do What We Do |
|--------|--------------|------------------------------|
| **Coinbase CDP** | Facilitator for Base | Won't route to competing facilitators |
| **PayAI** | Facilitator | Won't send traffic to CDP |
| **Daydreams** | Agent platform + facilitator | Token-gated, closed ecosystem |
| **x402scan.com** | Ecosystem analytics | Passive data; no routing, no trust scoring |

### BlockRun vs. x402scan (The Closest Comparison)

x402scan.com is an excellent open-source ecosystem browser. Here's how we differ:

| Dimension | x402scan | BlockRun |
|-----------|----------|----------|
| **Function** | Passive analytics (view tx, volume) | Active routing + trust scoring |
| **Trust Signals** | None (raw data only) | Legitimacy, uptime, price fairness |
| **Routing** | No | Yes (agents pay through us) |
| **Revenue Model** | Open source, no monetization | 5% routing premium |
| **Use Case** | Humans exploring ecosystem | Agents making payment decisions |

**x402scan answers "what's happening in x402?" BlockRun answers "should I trust this service?"**

These are complementary. We use x402scan data as one input into our trust scores.

**Facilitators compete with each other.** They have no incentive to aggregate or rate.

BlockRun is neutral. We rate and route across all of them.

### Head-to-Head: BlockRun vs. Daydreams

Daydreams is often cited as the closest competitor. Here's the real comparison:

| Dimension | BlockRun | Daydreams |
|-----------|----------|-----------|
| **Access Model** | Open, permissionless | Token-gated ($DREAMS required) |
| **AI Gateway** | 31+ models, OpenAI-compatible | Limited to their agent platform |
| **Cross-facilitator** | Aggregates all 6+ facilitators | Only their own facilitator |
| **Trust Data** | 300+ projects scored, legitimacy detection | No quality signals |
| **Target User** | Any agent, any framework | Daydreams platform users only |
| **Network** | Base (USDC) | Base ($DREAMS token) |
| **Business Model** | 5% routing premium | Token appreciation |

**The key difference:** Daydreams is building a closed ecosystem with their own agent platform. BlockRun is infrastructure for any agent, any framework, any facilitator.

### Competitive Advantages

| Advantage | Detail |
|-----------|--------|
| **Neutral position** | Not a facilitator, so we can aggregate all |
| **Open access** | No tokens, no accounts, just wallet + USDC |
| **Trust data moat** | Quality scores no individual facilitator has |
| **Cross-facilitator visibility** | Only player seeing all 6+ facilitators |
| **Circle expertise** | 3 years building USDC data infrastructure |

---

## Technical Moat: How We Score Trust

### The Trust Scoring System

Every service gets a composite trust score (0-100) based on:

| Signal | Weight | How We Measure |
|--------|--------|----------------|
| **Legitimacy** | 30% | Transaction pattern analysis (organic vs. gamed) |
| **Uptime** | 25% | Continuous endpoint probing (5-min intervals) |
| **Response Time** | 20% | Latency tracking across requests |
| **Delivery Rate** | 15% | Success/failure ratio on verified payments |
| **Price Fairness** | 10% | Deviation from ecosystem median |

### Legitimacy Detection (Our Core IP)

How do we know if a service is gaming transactions?

| Pattern | Signal | Detection |
|---------|--------|-----------|
| **Self-dealing** | Same wallet pays and receives | Graph analysis |
| **Burst patterns** | 1000 tx in 1 min, then nothing | Time-series anomaly |
| **Round-trip tx** | A→B→A loops | Flow tracking |
| **Fake volume** | High tx count, low unique wallets | Concentration metrics |

**Current finding:** ~40-50% of x402 transactions show gaming patterns. This is our core differentiation—we identify legitimate services.

### Data Collection Infrastructure

| Component | Function | Scale |
|-----------|----------|-------|
| **Endpoint Monitor** | Probes 3,500+ endpoints every 5 min | 1M+ probes/day |
| **Transaction Analyzer** | Processes x402 tx from all facilitators | 100M+ tx analyzed |
| **Price Index** | Benchmarks prices by service category | Real-time |
| **API Layer** | Serves trust scores to agents | <100ms latency |

### Why This Is Hard to Replicate

1. **Historical data** - We've analyzed 100M+ transactions. New entrants start at zero.
2. **Cross-facilitator view** - Individual facilitators only see their own tx.
3. **Algorithm refinement** - Legitimacy detection improves with every false positive/negative we catch.
4. **Network effects** - More agents routing → more delivery data → better scores.

---

## Go-to-Market Strategy

### Phase 1: Agent Framework Integrations (Q1 2026)

| Target | Integration | Why |
|--------|-------------|-----|
| Coinbase AgentKit | Native BlockRun routing | Largest agent framework |
| GOAT SDK | Discovery plugin | Growing agent ecosystem |
| LangChain | Tool integration | Mainstream AI developers |

**Goal:** Make BlockRun the default way agents discover and pay for x402 services.

### Phase 2: Service Provider Onboarding (Q1-Q2 2026)

- Aggregate all 6+ facilitators into unified API
- Quality scoring and ranking algorithms
- Service providers want visibility → list with us

### Phase 3: Routing Dominance (Q2-Q4 2026)

- Agents use BlockRun because we have all services
- Services want BlockRun because we have all agents
- **Network effects compound**

---

## Team

### Founder

**Vicky Fu - Founder & CEO**

| Experience | Detail |
|------------|--------|
| **Circle (2021-2024)** | Head of Data Science |
| **Built** | USDC data infrastructure |
| **Published** | "The State of x402" ecosystem analysis |
| **Education** | Stanford GSB Executive Program |

### Why This Founder

1. **Built USDC data infrastructure** - Knows stablecoin payments inside-out
2. **Data science background** - Discovery/analytics is core competency
3. **Circle network** - Direct relationships with potential acquirer
4. **Shipped fast** - x402 V2 integration in 2 weeks, ecosystem analysis published

### Hiring Plan (Post-Raise)

| Role | Priority |
|------|----------|
| Senior Backend Engineer | High |
| DevRel / Growth | Medium |

---

## Current Traction

### What's Live Now

| Product | Status | Details |
|---------|--------|---------|
| **AI Gateway** | Live (beta) | 31+ models, OpenAI-compatible, 0% markup |
| **x402 Integration** | Live | Full V2 support with CDP facilitator |
| **Service Directory** | Live | 618+ x402 services indexed and tracked |
| **Trust Scoring** | In development | Algorithm built, scoring services |
| **Routing API** | In development | Architecture complete, Q1 2026 launch |

### Key Milestones Achieved

| Milestone | Date | Significance |
|-----------|------|--------------|
| **"State of x402" Published** | Oct 2025 | Established thought leadership, cited by ecosystem |
| **AI Gateway Beta Launch** | Dec 2025 | First x402-native AI gateway live on Base |
| **31+ Models Integrated** | Dec 2025 | GPT-5 series, o1, Gemini 2.5, Claude, DeepSeek |
| **CDP Facilitator Integration** | Dec 2025 | Production-ready x402 V2 payments |

### Early Signals

- **Ecosystem recognition:** "State of x402" report cited by x402scan, shared by CDP team
- **Developer interest:** Inquiries from agent framework teams post-publication
- **Technical validation:** Successfully processing x402 payments on Base mainnet

---

## Financial Projections

### Growth Drivers (What Makes the Numbers Real)

Each milestone unlocks the next growth phase:

| Milestone | Expected Impact | Timeline |
|-----------|-----------------|----------|
| **AgentKit Integration Live** | 500-1K daily transactions from Coinbase agent ecosystem | Q1 2026 |
| **Trust Scores Public** | Service providers promote BlockRun listings → organic growth | Q1 2026 |
| **GOAT SDK Plugin** | Access to second-largest agent framework | Q2 2026 |
| **First Enterprise Customer** | $5K+/month single contract | Q2 2026 |
| **LangChain Tool** | Mainstream AI developer access | Q3 2026 |

### 18-Month Projection

| Milestone | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 |
|-----------|---------|---------|---------|---------|---------|---------|
| **Key Driver** | AgentKit | GOAT + Enterprise | LangChain | Referrals | Network effects | Scale |
| Daily Routed Tx | 1K | 10K | 50K | 200K | 500K | 1M |
| Avg Tx Value | $0.10 | $0.12 | $0.14 | $0.14 | $0.14 | $0.14 |
| Monthly Revenue | $150 | $1.8K | $10.5K | $42K | $105K | $210K |
| Team Size | 1 | 2 | 3 | 3 | 4 | 5 |

### Why These Numbers (Not Just Assumptions)

| Assumption | Evidence |
|------------|----------|
| **1K daily tx from AgentKit** | AgentKit has 10K+ developers; we need 0.01% to try BlockRun |
| **10x growth Q1→Q2** | GOAT SDK + first enterprise customer compound |
| **Avg tx value $0.14** | This IS the current x402 ecosystem average |
| **5% take rate** | Standard marketplace rate; trust premium justifies it |

### Path to Profitability

| Milestone | Monthly Revenue | Monthly Burn | Status |
|-----------|-----------------|--------------|--------|
| Break-even | $50K | $50K | Q4 2026 |
| Profitable | $100K+ | $50K | Q1 2027 |

---

## Funding

### Current Round

| Term | Detail |
|------|--------|
| **Round** | Angel |
| **Amount** | $750K |
| **Instrument** | SAFE (YC standard) |

### Use of Funds

| Category | Amount | % |
|----------|--------|---|
| Engineering | $300K | 40% |
| Operations | $150K | 20% |
| Marketing/BD | $150K | 20% |
| Infrastructure | $75K | 10% |
| Legal/Buffer | $75K | 10% |

### Runway

| Scenario | Runway |
|----------|--------|
| $750K raise | 15-18 months |

### Comparable Raises

- KiteAI: $15M seed (Feb 2025), $18M Series A (Sep 2025) - PayPal, General Catalyst
- PIN AI: $10M pre-seed (Sep 2024) - a16z CSX

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| x402 adoption slow | Dual product reduces dependency on single revenue stream |
| Competition from platforms | Data moat from cross-facilitator aggregation |
| AI provider API changes | Multi-provider abstraction layer |
| Regulatory uncertainty | B2B infrastructure, not consumer-facing |

---

## Path to Next Round

### What $750K Buys

| Milestone | Metric | Unlocks |
|-----------|--------|---------|
| **AgentKit integration** | Live in Q1 2026 | Access to largest agent ecosystem |
| **Trust API v1** | 300+ services scored | Product-market fit signal |
| **First enterprise customer** | $5K+/month contract | Revenue validation |
| **10K daily transactions** | Q2 2026 | Seed round positioning |

### Seed Round Criteria

We'll raise Seed when we hit:
- **$50K MRR** (break-even trajectory)
- **3+ enterprise customers** (revenue diversification)
- **100K+ daily transactions** (scale proof)

Target: Q4 2026, $3-5M Seed at $15-25M valuation

### Why Acquirers Will Care (Eventually)

| Acquirer | What They'd Get |
|----------|-----------------|
| **Circle** | Trust infrastructure for USDC agent economy |
| **Coinbase** | Quality layer for AgentKit + x402 ecosystem |
| **Stripe** | Entry into crypto-native AI payments |

But exit is not the focus of this round. Getting to Seed is.

---

## Why Invest Now

1. **Trust is the Bottleneck** - x402 solved payments. 40-50% of transactions show gaming patterns (by count, not volume). Agents won't spend autonomously without trust signals. We provide them.

2. **The Data Moat is Building** - Every transaction we observe improves our trust scores. Competitors can't replicate historical data.

3. **5% on Growing Volume** - x402 has processed $600M+ in volume (Q4 2025 explosion). As agents trust our ratings, 5% of routed transactions compounds.

4. **First Mover in Trust** - Facilitators provide payment rails, not quality signals. We're the first trust layer for autonomous payments.

5. **Founder-Market Fit** - Head of Data Science at Circle for 3 years. Published "The State of x402" ecosystem analysis. Built to analyze and rate.

---

## The Ask

**$750K angel round on SAFE**

- YC standard SAFE
- Pro-rata rights for checks >$50K
- Quarterly investor updates

---

## Contact

**Vicky Fu**
Founder & CEO, BlockRun

- Website: https://blockrun.ai
**Contact:** Vicky Fu
**Website:** vicky@blockrun.ai

---

*This business plan is confidential and intended for potential investors only.*
