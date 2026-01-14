# BlockRun Claude Code Skill - GTM Strategy

**Last Updated:** January 14, 2026
**Status:** Ready to Launch
**Review:** GPT-4o second opinion incorporated
**Contact:** care@blockrun.ai | [x.com/BlockRunAI](https://x.com/BlockRunAI)

---

## Executive Summary

BlockRun extends Claude Code with capabilities it doesn't have: **images, real-time X data, rate limit overflow**.

**Core Value Prop:** "One wallet, all models, no API keys"

### Products

| Product | Install | Target |
|---------|---------|--------|
| **Plugin** (Primary) | `pip install blockrun-llm && git clone https://github.com/BlockRunAI/blockrun-claude-code-wallet ~/.claude/skills/blockrun` + `pip install blockrun-llm` | Everyone |
| MCP (Alternative) | `claude mcp add blockrun npx @blockrun/mcp` | MCP enthusiasts |

Both share wallet at `~/.blockrun/`. **Always recommend Plugin first.**

---

## Part 1: Why BlockRun Wins

### The Problem We Solve

| Pain Point | Traditional | BlockRun |
|------------|-------------|----------|
| API keys | Manage 5+ keys | One wallet |
| Billing | 5 accounts | One USDC balance |
| Setup | 30+ minutes | 60 seconds |
| Config | Complex env vars | Zero config |

### Killer Use Cases (Claude CAN'T Do These)

| Use Case | Why External Model? | Hook |
|----------|---------------------|------|
| **Real-time X/Twitter** | Only Grok has live X access | "Claude can't do this" |
| **AI reviewing AI** | GPT finds bugs Claude missed | "Second opinion catches more" |
| **Image generation** | Claude can't generate images | "Now Claude can draw" |
| **Rate limit overflow** | Keep working when throttled | "Never stop working" |
| **Cost optimization** | DeepSeek is 10-50x cheaper | "Save 90%" |

### Competitive Landscape

| Competitor | Stars | Method | Our Edge |
|------------|-------|--------|----------|
| [Claudish](https://github.com/MadAppGang/claudish) | 484 | CLI | No API keys needed |
| [claude_code-multi-AI-MCP](https://github.com/RaiAnsar/claude_code-multi-AI-MCP) | - | MCP | Simpler (Skill) |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | - | Router | One wallet billing |
| [deepseek-code](https://github.com/yksanjo/deepseek-code) | - | CLI | 30+ models, not just 1 |

**We are the ONLY crypto-native Claude Code integration.**

---

## Part 2: Customer Segmentation

### Primary Personas

| Persona | Description | Pain Points | Hook |
|---------|-------------|-------------|------|
| **AI Power User** | Daily Claude Code user, builds skills/hooks, 10+ hrs/week | Rate limits, missing capabilities, API key sprawl | "Extend Claude's capabilities" |
| **Indie Developer** | Solo builder, cost-conscious, ships fast | Managing multiple API accounts, billing complexity | "One wallet, all models" |
| **Enterprise Dev** | Works in regulated environment, needs audit trail | Procurement friction for new APIs, compliance | "Crypto-native billing, no PII" |
| **AI Researcher** | Compares models, needs diverse outputs | Setting up each provider separately | "A/B test models instantly" |
| **Content Creator** | Needs images + text, non-technical | Can't generate images in Claude | "Now Claude can draw" |

### Segment Prioritization

```
Priority 1: AI Power Users (Claude Code daily users)
├── Highest signal, best feedback, have audiences
├── Target size: ~10,000 active Claude Code users
└── Conversion goal: 1% = 100 active wallets

Priority 2: Indie Developers
├── Cost-sensitive, will appreciate savings
├── Target size: ~50,000 (indie AI builders)
└── Conversion goal: 0.5% = 250 active wallets

Priority 3: Content Creators (Phase 2)
├── Larger market, lower technical bar needed
└── Wait until onboarding is smoother
```

---

## Part 3: Pricing Strategy

### Cost Structure

| Model | Our Cost | Our Price | Margin | User Sees |
|-------|----------|-----------|--------|-----------|
| GPT-4o | $0.0025/1K | $0.003/1K | 20% | "$0.001 per query" |
| Grok + Search | $0.25 | $0.30 | 20% | "$0.30 for live X data" |
| DeepSeek | $0.00014/1K | $0.0002/1K | 43% | "10,000 calls per $1" |
| DALL-E 3 | $0.04 | $0.05 | 25% | "$0.05 per image" |

### Pricing Philosophy

1. **Transparent:** Show cost before each call
2. **No minimums:** Pay only for what you use
3. **No subscriptions:** USDC balance = your account
4. **No hidden fees:** What you see is what you pay

### Messaging by Audience

| Audience | Price Message |
|----------|---------------|
| Cost-conscious | "$1 = 1,000 GPT-4o calls or 10,000 DeepSeek calls" |
| Convenience-focused | "No credit cards, no invoices, just USDC" |
| Power users | "Budget controls: set daily limits, track spending" |

---

## Part 4: Market Research

### Validated Pain Points (from Reddit/X/Discord)

| Source | Pain Point | Frequency | Our Solution |
|--------|------------|-----------|--------------|
| r/ClaudeAI | "Claude can't generate images" | Weekly | DALL-E via BlockRun |
| X threads | "Hit rate limits during long sessions" | Daily | Overflow to other models |
| MCP Discord | "Managing API keys is a nightmare" | Frequent | One wallet, no keys |
| GitHub issues | "Need real-time data Claude doesn't have" | Common | Grok Live Search |

### Competitor Analysis (Deep Dive)

| Competitor | Strengths | Weaknesses | Our Counter |
|------------|-----------|------------|-------------|
| **Claudish** (484 stars) | Simple CLI, established | Requires API keys, single model | No keys, 30+ models |
| **claude-code-router** | Smart routing | Complex setup, needs all keys | Zero config, one wallet |
| **Direct API integration** | Full control | 30+ min setup per provider | 60 seconds total |

### Market Size Estimate

```
Claude Code users (estimated):     100,000+
├── Daily active:                   20,000
├── Power users (10+ hrs/week):     5,000
└── Potential early adopters:       500-1,000

TAM (if 10% of power users):       500 users × $10/mo = $5,000/mo
SAM (realistic Year 1):            100 users × $5/mo = $500/mo
```

---

## Part 5: Feedback & Iteration Plan

### Early Adopter Program

**Week 1-2: Private Beta**
- [ ] Invite 10 power users from Tier 1 & 2 targets
- [ ] 1:1 onboarding calls (15 min each)
- [ ] Collect friction points during setup
- [ ] Daily check-ins via DM

**Week 3-4: Iterate**
- [ ] Fix top 3 friction points before public launch
- [ ] Add most-requested feature
- [ ] Document common questions for FAQ

### Feedback Collection

| Channel | Method | Frequency |
|---------|--------|-----------|
| GitHub Issues | Bug reports, feature requests | Respond < 24h |
| Discord/Slack | Real-time chat with early users | Daily check |
| X/Twitter | Public feedback, testimonials | Monitor mentions |
| 1:1 Calls | Deep dive with power users | Weekly (first month) |

### Iteration Triggers

| Signal | Action |
|--------|--------|
| 3+ users report same issue | Prioritize fix |
| Setup takes > 5 min | Simplify onboarding |
| Users ask "how do I X?" | Add to docs/skill |
| Churn after first use | Investigate, fix friction |

---

## Part 6: Risk Mitigation

### Identified Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Power users don't engage** | Medium | High | Have backup list of 20+ targets; don't rely on 3 people |
| **USDC friction too high** | High | High | Create fiat on-ramp guide; partner with Coinbase for easy buy |
| **Technical setup too complex** | Medium | High | Auto-wallet creation; one-command install; video tutorial |
| **Anthropic changes plugin system** | Low | Critical | Also maintain MCP version; stay close to Anthropic team |
| **x402 protocol issues** | Low | Medium | Have fallback to direct API calls if needed |
| **Competitor copies us** | Medium | Low | Move fast; build community moat; first-mover advantage |

### Contingency Plans

**If power user strategy fails (Week 4):**
→ Pivot to broader Reddit/HN launch without endorsements
→ Focus on "Claude can't do X" pain point content

**If USDC onboarding is too hard:**
→ Add Coinbase Commerce for credit card top-up
→ Create step-by-step video for non-crypto users

**If plugin install is confusing:**
→ Create web-based wallet setup at blockrun.ai/setup
→ Add `/blockrun setup` command with guided flow

### Kill Criteria

Stop and reassess if after 30 days:
- [ ] < 20 active wallets
- [ ] < $50 total transactions
- [ ] < 2 organic mentions on X/Reddit

---

## Part 7: Power User Outreach (Primary)

**Learning from superpowers:** Jesse Vincent didn't chase followers. He built something useful, then ONE power user (Simon Willison) with the right audience amplified it to 18.8k stars.

**Our strategy:** Target Claude Code power users first. They have harder problems, give better feedback, and have audiences. One authentic endorsement from a trusted builder beats months of generic marketing.

### Why Claude Code Power Users First

| Reason | Details |
|--------|---------|
| **Higher signal** | They're using Claude Code daily, frustrated with agent limitations (can't pay for external services autonomously) |
| **Amplification** | One solid demo/thread from Simon or Boris > broad crypto outreach |
| **Low barrier** | Share a simple skill that lets agents "pay" in workflows |
| **Natural fit** | They orchestrate agent fleets, build skills/hooks, solve autonomy problems - x402 is the next level |

### Tier 1: Must Reach (Highest Influence)

| Person | Handle | Why Target | Hook |
|--------|--------|------------|------|
| **Simon Willison** | [@simonw](https://x.com/simonw) | Datasette/Django creator, massive dev/AI reach, boosted superpowers | "Agents paying for external APIs during research" |
| **Boris Cherny** | [@bcherny](https://x.com/bcherny) | Head of Claude Code at Anthropic, threads go viral | "MCP for agent-to-agent payments" |
| **Felix Rieseberg** | [@felixrieseberg](https://x.com/felixrieseberg) | Claude Engineering, ships Cowork, fleet-of-Claudes mindset | "Enable more autonomous agent actions" |

### Tier 2: Active Power Users (High Engagement)

| Person | Handle | Why Target | Hook |
|--------|--------|------------|------|
| **Sankalp** | [@dejavucoder](https://x.com/dejavucoder) | Deep Claude Code blogs, multi-agent setups, indie dev circles | "Agents paying for paid APIs" |
| **Ado** (Anthropic DevRel) | Look for "Advent of Claude" posts | Daily power-user tricks, SDK for agents, hooks | "Payment capabilities in agent loops" |
| **CloudAI-X** | [@cloudxdev](https://x.com/cloudxdev) | Builds plugins with reviewer/debugger/auditor agents | "Payment agent as another agent type" |

### Tier 3: Broader Reach

| Person | Handle | Why Target | Hook |
|--------|--------|------------|------|
| **Allie K. Miller** | [@alliekmiller](https://x.com/alliekmiller) | 2M+ followers, bridges to broader adoption | "Non-engineers automating workflows with payments" |
| **Teresa Torres** | [@ttorres](https://x.com/ttorres) | Product-focused, competitive research systems | "Extend to paid data sources" |
| **Pranav Dhoolia** | [@pranav_dhoolia](https://x.com/pranav_dhoolia) | Custom skills for design/RFC | "Skills that can transact" |
| **Alec Newcomb** | [@alecnewcomb](https://x.com/alecnewcomb) | 37+ skills, multi-model stacks | "Complete the multi-model story with payments" |

### Outreach Playbook

**DO:**
```
1. Engage genuinely on their posts first (don't cold pitch)
2. Reply with value: "Saw your fleet setup—curious if you've thought
   about agents paying for external tools/data? Building something for that"
3. Demo value fast: share a quick skill or gist
4. Make it easy to try: one pip install, auto-wallet
```

**DON'T:**
```
- Cold DM with product pitch
- Tag them in promotional threads
- Ask for retweets/endorsements
```

### Engagement Timeline

**Week 1-2:**
- [ ] Follow all Tier 1 & 2 targets
- [ ] Engage meaningfully on 3+ posts from each
- [ ] Build relationship before any ask

**Week 3:**
- [ ] Share demo in reply to relevant thread (not self-promotion)
- [ ] "Hey, this might help with [their specific problem]"

**Week 4:**
- [ ] If positive response, offer early access / feedback session
- [ ] Ask what would make it useful for their workflow

---

## Part 8: Distribution Channels (Secondary)

### Channel Priority Matrix

| Priority | Channel | Action | Impact |
|----------|---------|--------|--------|
| **P0** | Power user endorsement | See Part 2 | **HIGHEST** - this is how superpowers won |
| **P1** | [anthropics/skills](https://github.com/anthropics/skills) | PR | **OFFICIAL** recognition |
| **P1** | [mcpservers.org](https://mcpservers.org/submit) | Submit MCP | Primary MCP discovery |
| **P1** | [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | PR | 12K+ servers directory |
| **P2** | r/ClaudeAI | Post | Reddit viral potential |
| **P2** | MCP Discord #showcase | Share | Direct MCP users |
| **P2** | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | PR | GitHub exposure |
| **P3** | X/Twitter | Thread | Social virality |
| **P3** | Hacker News | Show HN | Tech community |

### Awesome Lists Checklist

**For Skill:**
- [ ] [anthropics/skills](https://github.com/anthropics/skills) - **OFFICIAL!**
- [ ] [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [ ] [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [ ] [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills)

**For MCP:**
- [ ] [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [ ] [modelcontextprotocol.io](https://modelcontextprotocol.io) registry

### Package Registries

- [x] PyPI: `blockrun-llm`
- [x] npm: `@blockrun/mcp`
- [ ] MCP Registry submission

---

## Part 9: Launch Timeline

### Week 1: Distribution Blitz

**Day 0-1 (TODAY):**
- [ ] PR to [anthropics/skills](https://github.com/anthropics/skills) (OFFICIAL)
- [ ] Submit MCP to [mcpservers.org/submit](https://mcpservers.org/submit)
- [ ] Add GitHub topics: `claude-skill`, `claude-code`, `anthropic`, `x402`

**Day 2-3:**
- [ ] PR to [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [ ] PR to [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [ ] PR to [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [ ] PR to [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills)

**Day 4-5:**
- [ ] Share in MCP Discord #showcase
- [ ] Submit to PulseMCP newsletter
- [ ] Submit to Smithery.ai, Glama.ai

**Day 6-7:**
- [ ] Post to r/ClaudeAI
- [ ] Post to r/LocalLLaMA
- [ ] Launch Twitter thread
- [ ] Tag @anthropic @ClaudeAI

### Week 2: Content Marketing

- [ ] Write Medium article: "I Made Claude Call GPT to Review Its Own Code"
- [ ] Write Dev.to tutorial: "From 0 to GPT in Claude Code in 60 Seconds"
- [ ] Record 30-second demo GIF: install → wallet → call GPT
- [ ] Create comparison infographic

### Week 3: Community

- [ ] Prepare Show HN post
- [ ] Respond to all GitHub issues within 24h
- [ ] Collect user testimonials
- [ ] YouTube demo video (English + Chinese)

---

## Part 10: Content Templates

### Twitter Thread (Ready to Post)

```
🚀 I made Claude call GPT to review its own code

No API keys. Just one wallet.

pip install blockrun-llm

Then: "have gpt review this code"

🧵 Why you need this...

---

1/ Claude is great, but sometimes you need:

🐦 Real-time X data → Only Grok has it
🔍 Second opinion → GPT catches different bugs
🎨 Images → Claude can't generate them
💰 Cheap tasks → DeepSeek is 10x cheaper

BlockRun gives Claude these superpowers.

---

2/ The old way:

❌ Create 5 accounts
❌ Manage 5 API keys
❌ Pay 5 bills
❌ Configure 5 env vars

---

3/ The BlockRun way:

✅ pip install blockrun-llm
✅ Send $5 USDC
✅ "ask grok what's trending on X"

One wallet. All models. Done.

---

4/ Cool things you can do:

"blockrun grok what's on X about bitcoin?" → Grok answers
"blockrun GPT review my code" → AI reviewing AI
"blockrun generate a logo" → DALL-E creates it
"blockrun deepseek summarize this" → Save 90%

---

5/ Try it:

pip install blockrun-llm && git clone https://github.com/BlockRunAI/blockrun-claude-code-wallet ~/.claude/skills/blockrun
pip install blockrun-llm

GitHub: github.com/BlockRunAI/blockrun-claude-code-wallet

#ClaudeCode #AI #BuildInPublic
```

### Reddit Post (r/ClaudeAI)

```
Title: I built a plugin that lets Claude call GPT, Grok, DeepSeek - no API keys

Body:

Hey r/ClaudeAI,

I got tired of managing 5 different API keys. So I built BlockRun.

**What it does:**
- Extend Claude with capabilities it doesn't have
- Real-time X data (Grok), images (DALL-E), second opinions (GPT)
- Pay-per-request with USDC - no API keys

**Install:**
pip install blockrun-llm && git clone https://github.com/BlockRunAI/blockrun-claude-code-wallet ~/.claude/skills/blockrun
pip install blockrun-llm

**Cool use cases:**
- "blockrun grok what's trending on X?" → Grok answers (Claude can't)
- "blockrun GPT review this code" → AI reviewing AI
- "blockrun generate a logo" → DALL-E creates it
- "blockrun deepseek summarize this" → 10x cheaper for simple tasks

GitHub: github.com/BlockRunAI/blockrun-claude-code-wallet

Would love feedback! What use cases would you want?
```

### Hacker News (Show HN)

```
Title: Show HN: Claude Code skill for accessing GPT, Grok, DALL-E via USDC micropayments

Body:

I built a Claude Code skill that lets Claude call other AI models - GPT for second opinions, Grok for real-time X data, DALL-E for images.

The key insight: different models are good at different things. GPT catches bugs Claude misses. Only Grok has real-time X data. Claude can't generate images.

Instead of managing 5 API keys, you just need one USDC wallet. Pay per request via x402 protocol.

pip install blockrun-llm

Then just say: "have gpt review my code" or "what's trending on X"

GitHub: [link]

Built on x402 (by Coinbase + Cloudflare). Private key never leaves your machine.
```

---

## Part 11: Key Messages

### English

| Audience | Message |
|----------|---------|
| General | "One wallet, all models, no API keys" |
| Developers | "Stop managing 5+ API keys" |
| Cost-conscious | "$1 = 1,000 GPT-4 calls" |
| Crypto-native | "x402 micropayments on Base" |

### Chinese

| Audience | Message |
|----------|---------|
| General | "一个钱包，所有模型，不用 API key" |
| Developers | "别再管理 5 个 API key 了" |
| Cost-conscious | "$1 = 1000 次 GPT-4 调用" |

### Viral Hook

The "AI reviewing AI" visual will spread:

```
User: "have gpt review my code"

Claude: [calls GPT-4]

GPT-4: "Actually, Claude's implementation has a bug on line 23..."
```

---

## Part 12: Success Metrics

### Week 1 Targets (Realistic)

| Metric | Target | Notes |
|--------|--------|-------|
| GitHub stars | 50+ | Organic from awesome lists + Reddit |
| Beta testers onboarded | 5-10 | From Tier 1 & 2 power users |
| Setup friction points identified | 3+ | From 1:1 onboarding calls |
| Awesome list PRs submitted | 4+ | anthropics/skills, awesome-mcp, etc. |
| First funded wallet | 7 days | More realistic than 48h |

### Week 2-4 Targets

| Metric | Target | Notes |
|--------|--------|-------|
| GitHub stars | 100+ | After Reddit/HN posts |
| Active wallets | 20+ | From beta + early adopters |
| First organic transaction | Day 14 | After friction fixes |
| Positive testimonial | 1+ | From beta user for marketing |

### Month 1 Targets

| Metric | Target | Notes |
|--------|--------|-------|
| GitHub stars | 200+ | Conservative; 500+ is stretch goal |
| Active wallets | 50 | Focus on engagement over volume |
| Total transactions | 200 | Quality users > quantity |
| Revenue | $100 | Realistic for bootstrapped launch |
| Awesome list inclusions | 3+ | Not all PRs will merge quickly |
| Power user endorsement | 1 | Key milestone for amplification |

---

## Part 13: Repos & Links

| Repo | URL | Status |
|------|-----|--------|
| Plugin | github.com/BlockRunAI/blockrun-claude-code-wallet | Ready to publish |
| MCP | github.com/blockrunai/blockrun-mcp | Published |
| Python SDK | github.com/blockrunai/blockrun-llm | Published |

| Link | URL |
|------|-----|
| Website | https://blockrun.ai |
| Docs | https://blockrun.ai/docs |
| Buy USDC | https://coinbase.com |
| Bridge to Base | https://bridge.base.org |
| x402 Protocol | https://x402.org |

---

## Part 14: Competitive Intel

### What Makes Us Different

```
┌─────────────────────────────────────────────────────────┐
│  Getting GPT in Claude Code                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Traditional:                  BlockRun:                │
│  ────────────                  ─────────                │
│  1. Create OpenAI account      1. pip install           │
│  2. Add payment method            blockrun-llm          │
│  3. Generate API key           2. Send $5 USDC          │
│  4. Configure env vars         3. Use GPT ✓             │
│  5. Install proxy/bridge                                │
│  6. Finally use GPT                                     │
│                                                         │
│  ~30 minutes                   ~60 seconds              │
└─────────────────────────────────────────────────────────┘
```

### Why We Win

1. **Zero friction:** One pip install, auto-creates wallet
2. **No API keys:** Wallet = identity
3. **Unified billing:** One USDC balance for all models
4. **Crypto-native:** Built on x402, first of its kind
5. **Dual entry:** Skill for everyone, MCP for power users

---

## Action Items: TODAY

### Priority 1: Private Beta Setup
1. [ ] **Identify 10 beta testers** - Pull from Tier 1 & 2 list
2. [ ] **Create onboarding doc** - Step-by-step with screenshots
3. [ ] **Set up feedback channel** - Discord/Slack for beta users
4. [ ] **Prepare 1:1 call script** - 15 min onboarding + friction collection

### Priority 2: Distribution
5. [ ] **PR to anthropics/skills** - OFFICIAL directory, highest priority
6. [ ] **Submit to mcpservers.org** - Primary MCP discovery
7. [ ] **Add GitHub topics** - `claude-skill`, `claude-code`, `anthropic`, `x402`

### Priority 3: Content (After Beta Feedback)
8. [ ] **Draft Twitter thread** - Use template above, wait for testimonial
9. [ ] **Draft Reddit post** - Post after 3+ friction fixes

---

## Friction Mitigation Checklist

### USDC Onboarding (High Friction Risk)

| Friction Point | Solution | Status |
|----------------|----------|--------|
| "What is USDC?" | Add explainer in docs | [ ] |
| "Where do I buy USDC?" | Link to Coinbase, add guide | [ ] |
| "How do I send to Base?" | Bridge guide with screenshots | [ ] |
| "Is my money safe?" | Security FAQ, key never leaves machine | [ ] |

### Technical Setup (Medium Friction Risk)

| Friction Point | Solution | Status |
|----------------|----------|--------|
| pip install fails | Add troubleshooting section | [ ] |
| Plugin install unclear | Video walkthrough | [ ] |
| Wallet not found | Auto-create on first use ✓ | [x] |
| Balance shows 0 | Clear "fund your wallet" prompt | [ ] |

---

*Focus: Beta feedback first, then distribution. Fix friction before scaling.*
