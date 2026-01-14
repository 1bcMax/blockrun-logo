# BlockRun.AI Integration Targets
## Priority Projects for x402 AI Gateway Adoption

**Last Updated:** January 8, 2026
**Strategy:** Replace OpenAI/OpenRouter with BlockRun.AI's x402-powered API

**What is BlockRun.AI?**
- Pay-as-you-go AI gateway for ChatGPT and all major LLMs (OpenAI, Anthropic, Google, DeepSeek, xAI)
- x402 service catalog to discover all x402-enabled services on the market
- Pay with USDC on Base, no account needed
- OpenAI-compatible API

---

## EARLY USER OUTREACH TRACKER

### Active Conversations

| Name/Project | Twitter | Status | Date | Notes |
|--------------|---------|--------|------|-------|
| **Panche (Agentokratia)** | [@PIsajeski](https://x.com/PIsajeski) | ✅ DM Sent | Jan 3 | KromatikaFi founder, building Agentokratia (RapidAPI for AI agents on x402). Proposed design partnership for trust scores. Best potential partner so far. |
| **Vivek Kotecha** | [@vbkotecha](https://x.com/vbkotecha) | ✅ DM Sent | Jan 3 | x402Disputes founder, ex-VMware. Complementary: he does post-tx disputes, we do pre-tx trust. Partnership potential. |
| **SniperX** | [@sniperxfun](https://x.com/sniperxfun) | ✅ DM Sent | Jan 3 | x402 AI trading agent, pre-launch $SXAI. Needs AI for trading/alpha detection. |
| **x portal** | [@xportalai](https://x.com/xportalai) | ✅ DM Sent | Jan 3 | Virtuals agent, "tools for autonomous actors." Needs AI for agent infra. |

### To Contact

| Name/Project | Twitter | Why Target | Pitch Angle |
|--------------|---------|------------|-------------|

---

## Priority Ranking: Impact × Ease of Integration

| Rank | Project | Stars | Impact | Ease | Score | Why Easy |
|------|---------|-------|--------|------|-------|----------|
| 🥇 | **AI Hedge Fund** | 44.3K | 10 | 10 | **100** | Multi-LLM config already exists |
| 🥈 | **TradingAgents** | 27.3K | 9 | 9 | **81** | Has `backend_url` config |
| 🥉 | **AI-Trader** | 10.5K | 8 | 9 | **72** | LangChain architecture |
| 4 | **OctoBot** | 5.1K | 7 | 10 | **70** | Already supports custom base_url |
| 5 | **ElizaOS** | 60K | 10 | 7 | **70** | Needs plugin development |
| 6 | **Solana Agent Kit** | 1.6K | 8 | 9 | **72** | OpenAI config, Vercel AI SDK |
| 7 | **FinRobot** | 4.9K | 7 | 8 | **56** | AI4Finance ecosystem |
| 8 | **AgentKit** | Official | 8 | 7 | **56** | Coinbase fit, needs example |
| 9 | **GOAT SDK** | 150K dl | 8 | - | **PR#527** | Already submitted |

**Scoring:**
- **Impact (1-10):** Stars, distribution, API usage potential
- **Ease (1-10):** Configurable base_url, multi-LLM support, active maintainer

---

## How Integration Works

BlockRun is OpenAI-compatible. Any project using OpenAI or OpenRouter can switch with 1-2 lines:

```python
# Before (OpenAI)
client = OpenAI(api_key="sk-...")

# After (BlockRun) - wallet pays automatically
from blockrun_llm import LLMClient
client = LLMClient(private_key="0x...")
```

---

## TIER 1: CRITICAL - HIGHEST IMPACT (Do This Week)

### 1. ElizaOS (60K+ Stars)
**The largest Web3 AI agent framework**

| Attribute | Value |
|-----------|-------|
| GitHub | [elizaOS/eliza](https://github.com/elizaOS/eliza) |
| Stars | 60,000+ |
| Status | V2 launched, supports 20+ blockchains |
| Current LLM | OpenAI, Anthropic, OpenRouter, Llama |
| Integration Type | Create `plugin-blockrun` |

**Why Critical:**
- Biggest Web3 agent framework by far
- Already has plugin architecture at [elizaos-plugins](https://github.com/elizaos-plugins)
- $20B+ market cap ecosystem built on it
- They use OpenRouter - perfect replacement opportunity

**Integration Path:**
```typescript
// packages/plugin-blockrun/src/index.ts
import { Plugin } from '@elizaos/core';
import { BlockRunClient } from '@blockrun/llm';

export const blockrunPlugin: Plugin = {
  name: 'blockrun',
  description: 'x402-powered LLM access with USDC micropayments',
  providers: [BlockRunLLMProvider],
  actions: []
};
```

**Action Items:**
- [ ] Study existing plugins: `plugin-openai`, `plugin-anthropic`
- [ ] Fork elizaos-plugins repo
- [ ] Create `plugin-blockrun` package
- [ ] Submit PR to registry

---

### 2. OctoBot (5.1K Stars)
**Most popular open-source trading bot with AI**

| Attribute | Value |
|-----------|-------|
| GitHub | [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) |
| Stars | 5,100+ |
| Language | Python |
| AI Support | OpenAI GPT, Ollama |
| Users | Active trading community |

**Why Critical:**
- Already has OpenAI integration
- Users have crypto wallets
- Perfect use case: traders pay for AI signals with USDC

**Current Code (in OctoBot-Tentacles):**
```python
# Services/Services_bases/gpt_service/gpt.py
import openai
client = openai.AsyncOpenAI(
    api_key=self._get_api_key(),
    base_url=self._get_base_url(),  # Supports custom URL!
)
```

**Integration Path:**
Option A: **No code change needed!**
- Users set custom base URL: `https://api.blockrun.ai/v1`
- Set "API key" to: `wallet:0xPRIVATE_KEY`
- BlockRun server parses wallet key from header

Option B: **SDK integration**
- Add BlockRun as LLM provider option
- PR to OctoBot-Tentacles repo

**Action Items:**
- [ ] Join OctoBot Discord: [discord.com/invite/vHkcb8W](https://discord.com/invite/vHkcb8W)
- [ ] Post in #development channel
- [ ] Email: contact@drakkar.software
- [ ] Create PR after community validation

---

### 3. GOAT SDK (150K+ Downloads) ✅ PR SUBMITTED
**Crossmint-backed onchain agent framework**

| Attribute | Value |
|-----------|-------|
| GitHub | [goat-sdk/goat](https://github.com/goat-sdk/goat) |
| Downloads | 150,000+ |
| Funding | Crossmint $23.6M |
| Status | **PR #527 Submitted** |

**Status:** Full plugin implementation complete
- Package: `@goat-sdk/plugin-blockrun`
- Tools: chatCompletion, generateImage, getModels
- PR: https://github.com/goat-sdk/goat/pull/527

**Next Steps:**
- [ ] Follow up with GOAT team for review
- [ ] DM @AlfromSpain on Twitter
- [ ] Email Crossmint partnerships

---

### 4. Coinbase AgentKit
**Official Coinbase AI agent toolkit**

| Attribute | Value |
|-----------|-------|
| GitHub | [coinbase/agentkit](https://github.com/coinbase/agentkit) |
| Type | Official Coinbase tool |
| Features | Smart Wallet, Solana support, OpenAI integration |
| Contact | CDP Discord, developer-platform@coinbase.com |

**Why Critical:**
- Same ecosystem as x402
- Uses CDP infrastructure (like BlockRun)
- Natural fit for "agent pays for its own AI"

**Integration Path:**
```typescript
// Drop-in replacement
const llm = new OpenAI({
  baseURL: "https://api.blockrun.ai/v1",
  apiKey: "wallet-auth"  // x402 handles payment
});

// Or native
import { BlockRunClient } from '@blockrun/llm-ts';
const wallet = await CdpAgentkit.configureWithWallet();
const llm = new BlockRunClient({
  privateKey: wallet.exportPrivateKey()
});
```

**Action Items:**
- [ ] Build working example
- [ ] Post in CDP Discord
- [ ] Submit to AgentKit examples folder
- [ ] Email developer-platform@coinbase.com

---

### 5. Virtuals Protocol (21K+ Agents)
**Largest AI agent tokenization platform on Base**

| Attribute | Value |
|-----------|-------|
| Website | [virtuals.io](https://virtuals.io) |
| Agents | 21,000+ agent tokens |
| Daily New Agents | 1,000+ |
| SDK | GAME SDK |
| Contact | Discord, Twitter @virtuals_io |

**Why Critical:**
- Every agent needs LLM access
- Currently using centralized API keys
- Perfect x402 use case

**Integration Path:**
```typescript
// GAME SDK + BlockRun
import { Game } from '@virtuals/game-sdk';
import { BlockRunClient } from '@blockrun/llm-ts';

const agent = new Game({
  llm: new BlockRunClient({
    privateKey: agent.wallet.privateKey
  })
});
```

**Action Items:**
- [ ] Join Virtuals Discord
- [ ] DM on Twitter: @virtuals_io
- [ ] Propose GAME SDK integration
- [ ] Offer to build POC

---

## TIER 2: HIGH VALUE (Next 2 Weeks)

### 6. AI Hedge Fund (44.3K Stars) ⭐ NEW [PRIORITY]
**Famous investor agents for stock analysis**

| Attribute | Value |
|-----------|-------|
| GitHub | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) |
| Stars | 44,300+ |
| Language | Python 58% + TypeScript 37% |
| LLM Providers | OpenAI, Groq, Anthropic, DeepSeek, Ollama |
| License | MIT |
| Features | 12 investor agents, backtesting, web app |

**Why CRITICAL:**
- 44.3K stars = massive distribution potential
- Multi-LLM support already = easy to add BlockRun
- 12+ agents = high API usage (Buffett, Munger, Burry, Cathie Wood, etc.)
- Web app + CLI = multiple user interfaces
- Backtesting = repeated API calls

**Investor Agents (all use LLM):**
- Warren Buffett, Charlie Munger, Bill Ackman
- Cathie Wood, Michael Burry, Ben Graham
- Aswath Damodaran, Peter Lynch, etc.

**Integration Path:**
```python
# Add to LLM provider config
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] PRIORITY: Contact @virattt (author)
- [ ] Submit PR adding BlockRun as LLM provider
- [ ] Highlight pay-per-use for educational users
- [ ] Propose integration demo video

---

### 6b. AI-Trader (10.5K Stars) ⭐ NEW
**Autonomous multi-model trading benchmark**

| Attribute | Value |
|-----------|-------|
| GitHub | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) |
| Stars | 10,500+ |
| Language | Python 3.10+ |
| LLM Providers | OpenAI, Claude, Qwen |
| Markets | NASDAQ 100, SSE 50, Crypto (10 coins) |
| Protocol | MCP (Model Context Protocol) |
| License | MIT |
| Dashboard | [ai4trade.ai](https://ai4trade.ai) |

**Why High Value:**
- 10.5K stars = significant distribution
- MCP protocol = BlockRun could build MCP server
- Academic backing (HKU) = credibility for partnerships
- Multi-market support (stocks, A-shares, crypto)
- LangChain architecture = easy base_url customization

**Current Architecture:**
```python
# Uses langchain-openai + langchain-mcp-adapters
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters import MCPClient

# BlockRun can plug in here
llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Integration Paths:**
1. **LangChain provider**: Add BlockRun as base_url option
2. **MCP Server**: Create BlockRun MCP server for tools
3. **Crypto agent**: Perfect for x402 wallet payments

**Action Items:**
- [ ] Contact HKU team (academic outreach)
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Propose BlockRun MCP server contribution
- [ ] Highlight crypto agent use case

---

### 7. TradingAgents (27.3K Stars)
**Multi-agent LLM financial trading framework**

| Attribute | Value |
|-----------|-------|
| GitHub | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) |
| Stars | 27,300+ |
| Language | Python |
| LLM Provider | OpenAI exclusively (gpt-4o, o1-preview) |
| Framework | LangGraph, LangChain |
| License | Apache 2.0 |

**Why High Value:**
- 27.3K stars = massive distribution potential
- OpenAI-exclusive = perfect replacement opportunity
- Academic/research backing = credibility for BlockRun
- Already has `backend_url` config = easy integration
- Python codebase = matches BlockRun SDK

**Current Code:**
```python
# tradingagents/default_config.py
DEFAULT_CONFIG = {
    "llm_provider": "openai",
    "backend_url": "https://api.openai.com/v1",  # Can be changed!
    "deep_think_llm": "o4-mini",
    "quick_think_llm": "gpt-4o-mini",
}
```

**Integration Path:**
Option A: **No code change needed!**
- Users set `backend_url`: `https://api.blockrun.ai/v1`
- BlockRun handles wallet auth via headers

Option B: **Native integration**
```python
# Add to default_config.py
"llm_provider": "blockrun",  # New option
"backend_url": "https://api.blockrun.ai/v1",
```

**Action Items:**
- [ ] Open GitHub issue to propose integration
- [ ] Submit PR adding BlockRun as LLM provider option
- [ ] Contact maintainers (Yijia Xiao, Edward Sun)
- [ ] Highlight cost savings for academic researchers

---

### 8. CryptoTrade (149 Stars) ⭐ NEW
**LLM-based reflective crypto trading agent (EMNLP 2024)**

| Attribute | Value |
|-----------|-------|
| GitHub | [Xtra-Computing/CryptoTrade](https://github.com/Xtra-Computing/CryptoTrade) |
| Stars | 149+ |
| Language | Python |
| LLM Provider | OpenAI (GPT-4-turbo) |
| Paper | [EMNLP 2024](https://aclanthology.org/2024.emnlp-main.63.pdf) |
| License | CC BY-NC-SA |
| Security Review | ✅ PASS - No hardcoded credentials, env-based config |

**Why High Value:**
- Academic credibility (EMNLP 2024 publication)
- Multi-analyst architecture = high API usage (on-chain, news, reflection, trader)
- Reflective mechanism creates feedback loop for strategy refinement
- OpenAI-exclusive = perfect BlockRun replacement opportunity
- Research community = early adopter potential

**Current Code:**
```python
# Uses openai==1.30.5
# Multi-analyst roles synthesize data for trading decisions
# Confidence scale: [-1, 1] for buy/sell signals
```

**Integration Path:**
```python
# Replace OpenAI with BlockRun
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Contact academic team (Xtra-Computing, NUS)
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Highlight cost benefits for research experiments
- [ ] Propose x402 integration for autonomous trading

---

### 8b. AlpacaTradingAgent (102 Stars) ⭐ NEW
**Multi-agent LLM trading for Alpaca markets**

| Attribute | Value |
|-----------|-------|
| GitHub | [huygiatrng/AlpacaTradingAgent](https://github.com/huygiatrng/AlpacaTradingAgent) |
| Stars | 102+ |
| Language | Python |
| LLM Provider | OpenAI (gpt-5-mini recommended) |
| Framework | LangGraph |
| License | Apache-2.0 |
| Security Review | ✅ PASS - Env-based config, no hardcoded secrets |

**Why High Value:**
- Apache-2.0 license = easy integration
- LangGraph architecture = modern agent framework
- 5 specialized agents (Market, Sentiment, News, Fundamental, Macro)
- Alpaca integration = stocks AND crypto trading
- Documentation recommends cost-effective models = BlockRun sweet spot

**Current Architecture:**
```python
# Uses LangGraph for agent orchestration
# Configurable "deep_think_llm" and "quick_think_llm" models
# High API call volume (noted in docs)
```

**Integration Path:**
```python
# Add BlockRun as backend option
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Open GitHub issue proposing BlockRun
- [ ] Submit PR adding BlockRun as LLM provider
- [ ] Highlight pay-per-use for high API call volume
- [ ] DM maintainer @huygiatrng

---

### 9. FinRobot (4.9K Stars) ⭐ NEW
**AI agent platform for financial analysis**

| Attribute | Value |
|-----------|-------|
| GitHub | [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) |
| Stars | 4,900+ |
| Language | Python |
| LLM Provider | OpenAI GPT-4 |
| Organization | AI4Finance Foundation |
| Features | Equity research, market forecasting, trading strategy |

**Why High Value:**
- AI4Finance Foundation (same as FinRL - 12K stars)
- Multi-agent financial analysis platform
- Commercial FinRobot Pro offering = proven demand
- Financial Chain-of-Thought prompting = high API usage
- Plug-and-play LLM architecture

**Agent Types:**
- Market Forecasting Agent → BlockRun
- Document Analysis Agent → BlockRun
- Trading Strategy Agent → BlockRun

**Integration Path:**
```python
# Add to multi-source LLM foundation layer
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Connect with AI4Finance Foundation
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Highlight cost savings for research users
- [ ] Propose partnership for FinRobot Pro

---

### 10. Freqtrade (39.9K Stars)
**Most popular open-source trading bot**

| Attribute | Value |
|-----------|-------|
| GitHub | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) |
| Stars | 39,900+ |
| Feature | FreqAI module for ML/AI strategies |
| Language | Python |

**Integration:** Add BlockRun as LLM provider for FreqAI strategies

---

### 10. Jesse Trading Bot (6.5K Stars)

| Attribute | Value |
|-----------|-------|
| GitHub | [jesse-ai/jesse](https://github.com/jesse-ai/jesse) |
| Stars | 6,500+ |
| Focus | Backtesting + live trading |

---

### 11. LangChain/LlamaIndex
**Dominant AI frameworks**

| Framework | Stars | Integration Type |
|-----------|-------|------------------|
| LangChain | 100K+ | Custom LLM provider |
| LlamaIndex | 40K+ | Custom LLM provider |

**Integration:** Create BlockRun as a custom LLM class

```python
from langchain.llms.base import LLM
from blockrun_llm import LLMClient

class BlockRunLLM(LLM):
    client: LLMClient

    def _call(self, prompt: str) -> str:
        return self.client.chat("openai/gpt-4o", prompt)
```

---

### 12. CryptoPrinter
**GPT-4 crypto trading via Robinhood**

| Attribute | Value |
|-----------|-------|
| GitHub | [gravelBridge/CryptoPrinter](https://github.com/gravelBridge/CryptoPrinter) |
| LLM | GPT-4 |
| Trading | Robinhood API |

---

### 13. Web3 AI Trading Agent (Chainstack)
**BASE + Uniswap V4 example**

| Attribute | Value |
|-----------|-------|
| GitHub | [chainstacklabs/web3-ai-trading-agent](https://github.com/chainstacklabs/web3-ai-trading-agent) |
| Chain | BASE |
| Protocol | Uniswap V4 |

**Why:** Same chain as BlockRun - perfect fit

---

### 14. Cookie DAO
**AI agent data indexer (7TB data)**

| Attribute | Value |
|-----------|-------|
| Website | [cookie.fun](https://cookie.fun) |
| Data | 7TB real-time AI agent data |
| Chains | Solana, Base, BNB |

**Integration:** BlockRun as data source + joint analytics

---

### 15. ZerePy
**Python AI agent for Twitter/Farcaster**

| Attribute | Value |
|-----------|-------|
| GitHub | [blorm-network/ZerePy](https://github.com/blorm-network/ZerePy) |
| Platforms | Twitter, Farcaster |
| LLMs | OpenAI, Anthropic |

---

## TIER 3: ECOSYSTEM EXPANSION (Month 2-3)

### 16. Sibyl (55+ Stars) ⭐ NEW
**AI-powered crypto insights & trading dashboard**

| Attribute | Value |
|-----------|-------|
| GitHub | [nMaroulis/sibyl](https://github.com/nMaroulis/sibyl) |
| Stars | 55+ |
| Language | Python (86.5%) |
| LLM Providers | OpenAI, HuggingFace, Local (Llama) |
| Exchanges | Binance, Coinbase |
| Tech Stack | LangChain, FastAPI, Streamlit, PyTorch, ChromaDB |
| License | Self-hosted, encrypted credentials |

**Why Integrate:**
- LangChain + langchain_openai = easy custom base_url
- Comprehensive AI platform (Oracle, RAG, ML forecasting)
- Self-hosted design = perfect for wallet-based auth
- ChromaDB RAG = BlockRun could power embeddings too
- Privacy-focused (local LLM support)

**Features BlockRun Can Enhance:**
- Oracle module (LLM assistant) → BlockRun API
- Wiki RAG chatbot → BlockRun embeddings
- Reporter sentiment analysis → BlockRun GPT

**Integration Path:**
```python
# In LangChain config
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x...",  # BlockRun wallet auth
)
```

**Action Items:**
- [ ] Open GitHub issue proposing BlockRun integration
- [ ] Submit PR adding BlockRun as LLM provider option
- [ ] Highlight x402 micropayments for self-hosted users

---

### 17. AI-Hedge-Fund-Crypto (478 Stars) ⭐ NEW
**LLM-powered crypto hedge fund framework**

| Attribute | Value |
|-----------|-------|
| GitHub | [51bitquant/ai-hedge-fund-crypto](https://github.com/51bitquant/ai-hedge-fund-crypto) |
| Stars | 478+ |
| Language | Python 3.12+ |
| LLM Providers | OpenAI, Groq, OpenRouter, Gemini, Anthropic, Ollama |
| Framework | LangGraph, LangChain |
| Exchange | Binance |

**Why Integrate:**
- 6 LLM providers already = easy to add BlockRun as 7th
- LangGraph architecture = modern, flexible
- YAML config = no code changes needed
- Ensemble strategy signals = high API usage potential

**Integration Path:**
```python
# Add to LLM providers config
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Submit PR adding BlockRun as 7th provider option
- [ ] Highlight pay-per-use for backtesting users
- [ ] Contact @51bitquant on GitHub

---

### 18. FinMem (797 Stars) ⭐ NEW
**Academic LLM trading agent with layered memory**

| Attribute | Value |
|-----------|-------|
| GitHub | [pipiku915/FinMem-LLM-StockTrading](https://github.com/pipiku915/FinMem-LLM-StockTrading) |
| Stars | 797+ |
| Language | Python 98.1% |
| LLM Providers | OpenAI, HuggingFace TGI |
| Publications | AAAI 2024, ICLR 2024, IJCAI 2024 |
| Unique Feature | Layered memory architecture |

**Why Integrate:**
- Academic credibility (3 major AI conferences)
- Always uses OpenAI embeddings = guaranteed API calls
- Research community = early adopter potential
- Layered memory = high API usage for processing

**Integration Path:**
```python
# In .env configuration
OPENAI_API_KEY = "wallet:0x..."
OPENAI_BASE_URL = "https://api.blockrun.ai/v1"
```

**Action Items:**
- [ ] Contact academic team (Shirley Yu)
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Highlight cost benefits for research experiments
- [ ] Propose collaboration on x402 paper

---

### 19. FinRL-DeepSeek (292 Stars) ⭐ NEW
**LLM-infused reinforcement learning for trading**

| Attribute | Value |
|-----------|-------|
| GitHub | [benstaf/FinRL_DeepSeek](https://github.com/benstaf/FinRL_DeepSeek) |
| Stars | 292+ |
| Language | Python + Jupyter |
| LLM Providers | DeepSeek, Llama, Qwen |
| Paper | arXiv:2502.07393 |
| Parent Project | FinRL (12K stars) |

**Why Integrate:**
- LLM + RL hybrid = innovative architecture
- Uses LLM for sentiment + risk analysis
- Part of FinRL ecosystem (12K stars parent)
- Academic paper = research credibility
- FinRL Contest 2025 integration

**Integration Path:**
```python
# Replace DeepSeek API with BlockRun
import openai
client = openai.OpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Contact benstaf (author) on GitHub
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Highlight multi-model access via single API
- [ ] Connect with AI4Finance Foundation

---

### 20. fagent (41 Stars) ⭐ NEW
**Serverless AI agent for Farcaster/Twitter/Telegram**

| Attribute | Value |
|-----------|-------|
| GitHub | [0xKoda/fagent](https://github.com/0xKoda/fagent) |
| Stars | 41+ |
| Language | TypeScript (100%) |
| LLM Provider | OpenRouter (OpenAI, Claude, etc.) |
| Platforms | Farcaster, Twitter/X, Telegram |
| Infrastructure | Cloudflare Workers (serverless) |
| Security Review | ✅ PASS - Clean dependencies, env-based config |

**Why Integrate:**
- Uses OpenRouter = BlockRun can offer as alternative
- Serverless architecture = perfect for pay-per-use model
- Farcaster integration = Web3 native social
- Twitter/Telegram support = broader reach
- Modern stack (Cloudflare Workers, KV storage)

**Features:**
- Two-tier memory (24h conversation + 30-day long-term)
- Custom action system
- Scheduled jobs
- Multi-platform posting

**Integration Path:**
```typescript
// Replace OpenRouter with BlockRun
const client = new OpenAI({
  baseURL: "https://api.blockrun.ai/v1",
  apiKey: "wallet:0x..."
});
```

**Action Items:**
- [ ] DM @0xKoda on Twitter/Farcaster
- [ ] Submit PR adding BlockRun as LLM provider option
- [ ] Highlight x402 for serverless pay-per-use
- [ ] Propose Farcaster community co-marketing

---

### 21. LLM_trader (22 Stars) ⭐ NEW
**LLM-powered crypto trading analysis with OpenRouter**

| Attribute | Value |
|-----------|-------|
| GitHub | [qrak/LLM_trader](https://github.com/qrak/LLM_trader) |
| Stars | 22+ |
| Language | Python (99.3%) |
| LLM Providers | Google Gemini (primary), OpenRouter (fallback), LM Studio |
| Exchanges | Binance, KuCoin, Gate.io, MEXC, Hyperliquid |
| License | MIT |
| Security Review | ✅ PASS - Env-based config, paper trading only |

**Why Integrate:**
- Uses OpenRouter = BlockRun can integrate alongside
- Multi-exchange support = broad crypto coverage
- Vision capabilities (chart analysis)
- Paper trading = low-risk adoption
- MIT license = easy integration

**Data Sources:**
- CryptoCompare (news)
- Alternative.me (sentiment)
- CCXT (multi-exchange data)

**Integration Path:**
```python
# Add BlockRun as LLM provider option
from openai import OpenAI
client = OpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Open GitHub issue proposing BlockRun
- [ ] Submit PR adding BlockRun as provider option
- [ ] Highlight multi-model access benefit

---

### 22. LLM-TradeBot (100+ Stars) ⭐ NEW
**Multi-agent AI trading with 5 LLM providers**

| Attribute | Value |
|-----------|-------|
| GitHub | [EthanAlgoX/LLM-TradeBot](https://github.com/EthanAlgoX/LLM-TradeBot) |
| Stars | 100+ |
| Language | Python 3.11+ |
| LLM Providers | DeepSeek, OpenAI, Claude, Qwen, Gemini |
| Exchange | Binance Futures (Bybit, OKX planned) |
| License | AGPL-3.0 |
| Contact | [@ethan_han999](https://x.com/ethan_han999) |

**Why Integrate:**
- Multi-LLM architecture = easy to add BlockRun as provider
- Uses OpenAI-compatible APIs (single openai package for all)
- Dashboard settings for switching providers
- Active development (119 commits, Dec 2025)
- Similar to NoFx architecture

**Integration Path:**
Add BlockRun as 6th LLM provider option in dashboard:
```python
# In LLM provider config
LLM_PROVIDERS = {
    "blockrun": {
        "base_url": "https://api.blockrun.ai/v1",
        "description": "x402-powered, pay with USDC"
    },
    # ... existing providers
}
```

**Action Items:**
- [ ] DM @ethan_han999 on Twitter
- [ ] Submit PR adding BlockRun as provider
- [ ] Highlight no API key needed benefit

---

### 23. LLMAgentCrypto (165 Stars) ⭐ NEW
**LLM + FinBERT crypto trading bot tutorial**

| Attribute | Value |
|-----------|-------|
| GitHub | [nicknochnack/LLMAgentCrypto](https://github.com/nicknochnack/LLMAgentCrypto) |
| Stars | 165+ |
| Language | Python |
| LLM Providers | LLM (via prompts) + FinBERT sentiment |
| Features | Multiple bot strategies, sentiment analysis |
| License | Educational |
| Security Review | ✅ PASS - Educational project, env-based config |

**Why Integrate:**
- Popular tutorial channel (Nick Nochnack = 200K+ YouTube subs)
- Multiple bot implementations for comparison
- Uses LLM prompts for recommendations
- Educational = great for BlockRun exposure
- FinBERT + LLM hybrid = multi-model use case

**Bot Types:**
- Random Bot (baseline)
- Sentiment Bot (FinBERT)
- LLM Recommendation Bot
- Dip-buying strategies

**Integration Path:**
```python
# In llmprompts.py or bot config
from openai import OpenAI
client = OpenAI(
    base_url="https://api.blockrun.ai/v1",
    api_key="wallet:0x..."
)
```

**Action Items:**
- [ ] Comment on YouTube video with BlockRun integration
- [ ] Submit PR adding BlockRun as LLM option
- [ ] Highlight pay-per-use for tutorial users
- [ ] Offer to sponsor a follow-up tutorial

---

### 24. Solana Agent Kit (1.6K Stars) ⭐ NEW [HIGH PRIORITY]
**Official Solana AI agent toolkit - 60+ blockchain actions**

| Attribute | Value |
|-----------|-------|
| GitHub | [sendaifun/solana-agent-kit](https://github.com/sendaifun/solana-agent-kit) |
| Stars | 1,600+ |
| Language | TypeScript |
| LLM Providers | OpenAI, Claude, any (via Vercel AI SDK, LangChain) |
| Actions | 60+ (trading, NFT, lending, staking, bridging) |
| Ecosystem | Solana AI Hackathon winner |
| Security Review | ✅ PASS - Open source, env-based config |

**Why HIGH PRIORITY:**
- 1.6K stars = significant adoption in Solana ecosystem
- Framework-agnostic = works with LangChain, Vercel AI SDK, OpenAI
- 60+ blockchain actions = high API usage potential
- Solana AI Hackathon backing = ecosystem support
- Natural fit: AI agents paying for LLM with x402

**Features:**
- Token operations (swap, bridge, transfer)
- NFT operations (mint, list, metadata)
- DeFi operations (stake, lend, borrow)
- DALL-E integration for NFT artwork
- Cross-chain bridging

**Integration Path:**
```typescript
// Replace OpenAI with BlockRun
import { SolanaAgentKit } from "solana-agent-kit";

const agent = new SolanaAgentKit({
    openai: {
        baseURL: "https://api.blockrun.ai/v1",
        apiKey: "wallet:0x..."
    }
});
```

**Action Items:**
- [ ] PRIORITY: Contact SendAI team
- [ ] Submit PR adding BlockRun as LLM provider
- [ ] Highlight x402 for agent-pays-for-AI use case
- [ ] Propose Solana USDC payments integration

---

### 25. Solana-Trading-AI-Agent (69 Stars) ⭐ NEW
**Autonomous Solana trading with LangChain + Vercel AI SDK**

| Attribute | Value |
|-----------|-------|
| GitHub | [terauss/Solana-Trading-AI-Agent](https://github.com/terauss/Solana-Trading-AI-Agent) |
| Stars | 69+ |
| Language | TypeScript (97.7%) |
| Framework | Next.js, LangChain, Vercel AI SDK |
| DEXes | Jupiter, Orca, Raydium, Meteora |
| Features | Perpetual trading, lending, portfolio rebalancing |
| Security Review | ⚠️ Needs detailed code review |

**Why Integrate:**
- LangChain + Vercel AI SDK = modern AI stack
- Multi-DEX Solana trading = high API usage
- TypeScript = matches BlockRun TS SDK
- Social sentiment analysis = additional AI calls
- Portfolio automation = repeated API calls

**Features BlockRun Can Enhance:**
- AI market analysis
- Social sentiment scoring
- Portfolio rebalancing decisions
- Trading signal generation

**Integration Path:**
```typescript
// Replace LangChain LLM provider
import { ChatOpenAI } from "@langchain/openai";

const llm = new ChatOpenAI({
    configuration: {
        baseURL: "https://api.blockrun.ai/v1",
        apiKey: "wallet:0x..."
    }
});
```

**Action Items:**
- [ ] Review codebase for LLM configuration points
- [ ] Submit PR adding BlockRun as provider option
- [ ] Highlight x402 for Solana-native payments

---

### AI Agent Frameworks

| Project | Stars | Focus |
|---------|-------|-------|
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 4K+ | Multi-agent framework |
| [Swarms](https://github.com/kyegomez/swarms) | 3K+ | Enterprise multi-agent |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 50K+ | Multi-agent software dev |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 15K+ | Autonomous agents |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 25K+ | Agent orchestration |

### Coding Assistants

| Project | Stars | Integration |
|---------|-------|-------------|
| [Aider](https://github.com/paul-gauthier/aider) | 25K+ | Multi-model coding |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 45K+ | Autonomous coder |

### RAG & Infrastructure

| Project | Stars | Integration |
|---------|-------|-------------|
| [RAGFlow](https://github.com/infiniflow/ragflow) | 30K+ | RAG engine |
| [n8n](https://github.com/n8n-io/n8n) | 60K+ | Workflow automation |
| [Langflow](https://github.com/langflow-ai/langflow) | 40K+ | Visual AI builder |

### MCP (Model Context Protocol)

| Project | Integration |
|---------|-------------|
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | Create BlockRun MCP server |
| [DeFi Trading MCP](https://github.com/edkdev/defi-trading-mcp) | 28 stars, 17+ chains, 40+ tools |
| [Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server) | Official, stocks/ETFs/crypto/options |
| Hummingbot | Has MCP server, add BlockRun |

### 26. DeFi Trading MCP (28 Stars) ⭐ NEW
**Autonomous DeFi trading agent via MCP protocol**

| Attribute | Value |
|-----------|-------|
| GitHub | [edkdev/defi-trading-mcp](https://github.com/edkdev/defi-trading-mcp) |
| Stars | 28+ |
| Language | TypeScript/Node.js |
| Protocol | MCP (Model Context Protocol) |
| Chains | 17+ (Ethereum, Base, Polygon, Arbitrum, Optimism...) |
| Tools | 40+ trading tools |
| Security Review | ⚠️ Requires wallet private key |

**Why Integrate:**
- MCP = emerging standard for LLM tool access
- 17+ blockchain support = broad coverage
- 40+ trading tools = high API usage potential
- Claude integration = Anthropic partnership opportunity
- BlockRun could build complementary MCP server for LLM access

**Partnership Opportunity:**
- BlockRun MCP server for LLM access
- Users can pair DeFi Trading MCP (actions) + BlockRun MCP (LLM)
- Joint marketing with MCP ecosystem

**Action Items:**
- [ ] Build BlockRun MCP server
- [ ] Contact edkdev for partnership
- [ ] List in awesome-web3-mcp-servers
- [ ] Create tutorial: "DeFi Trading + BlockRun LLM"

---

## ALREADY SUBMITTED (8 PRs)

| Repository | PR # | Status | Type |
|------------|------|--------|------|
| goat-sdk/goat | #527 | Pending | Full plugin |
| Polymarket/agents | #124 | Pending | LangChain connector |
| polymarket-kalshi-btc-arbitrage-bot | #4 | Pending | AI layer |
| NoFxAiOS/nofx | #1292 | Pending | Go client |
| ai-trading-agent | #5 | Pending | Config option |
| xpaysh/awesome-x402 | #5 | Pending | Listing |
| Merit-Systems/awesome-x402 | #24 | Pending | Listing |
| wbnns/awesome-base | #11 | Pending | Listing |

---

## WEEKLY INTEGRATION SCHEDULE

### Week 1 (Dec 30 - Jan 5)
- [ ] ElizaOS plugin development
- [ ] OctoBot Discord outreach
- [ ] AgentKit example
- [ ] Follow up GOAT PR #527

### Week 2 (Jan 6-12)
- [ ] Virtuals Protocol outreach
- [ ] Submit ElizaOS plugin
- [ ] LangChain custom provider
- [ ] MCP server development

### Week 3 (Jan 13-19)
- [ ] Freqtrade integration
- [ ] Cookie DAO partnership
- [ ] ZerePy integration
- [ ] Jesse trading bot

### Week 4 (Jan 20-26)
- [ ] MetaGPT integration
- [ ] CrewAI integration
- [ ] PraisonAI integration
- [ ] n8n workflow

---

## OUTREACH TEMPLATES

### For Trading Bots (OctoBot, Freqtrade, Jesse)

```
Subject: BlockRun.AI - Pay-as-you-go ChatGPT & LLMs for trading bots

Hi [Project] team,

I noticed [Project] supports OpenAI for AI-powered trading strategies. I built BlockRun.AI - a pay-as-you-go gateway for ChatGPT and all major LLMs (OpenAI, Anthropic, Google, DeepSeek, xAI) via x402 on Base.

Benefits for your users:
- Access ChatGPT (GPT-4o) and 28+ models via one API
- Pay with USDC per request, no subscriptions
- No API key management (wallet = identity)
- OpenAI-compatible drop-in replacement

Bonus: We also run the x402 service catalog - users can discover all x402-enabled services at blockrun.ai/discover

Integration options:
1. Custom base URL (works today, no code change)
2. Native SDK integration (blockrun-llm)

Would love to discuss integration. Happy to provide free credits for testing.

Best,
Vicky
BlockRun.AI - https://blockrun.ai
```

### For Agent Frameworks (ElizaOS, GOAT)

```
Subject: BlockRun.AI plugin - Pay-as-you-go ChatGPT for autonomous agents

Hi [Framework] team,

BlockRun.AI enables AI agents to pay for their own ChatGPT & LLM access with USDC micropayments via x402 on Base.

This solves the "API key problem" for autonomous agents:
- Access ChatGPT (GPT-4o) and 28+ models
- Agent wallet = payment method (no API keys)
- True agent autonomy with pay-per-request
- OpenAI-compatible API

I've built a plugin for [Framework]:
[Link to PR or code]

Bonus: BlockRun.AI also features an x402 service catalog at /discover - helping users find all x402-enabled services on the market.

Would love to contribute this to the official plugin registry.

Best,
Vicky
vicky@blockrun.ai | https://blockrun.ai
```

---

## METRICS TO TRACK

| Metric | Week 1 | Week 4 | Month 2 |
|--------|--------|--------|---------|
| PRs Submitted | 8 | 15 | 25 |
| PRs Merged | 0 | 5 | 15 |
| Official Integrations | 0 | 3 | 10 |
| Discord Communities Joined | 5 | 10 | 15 |

---

## QUICK REFERENCE: GITHUB TOPICS TO SEARCH

Find more targets by searching these GitHub topics:
- [ai-trading](https://github.com/topics/ai-trading)
- [crypto-bot](https://github.com/topics/crypto-bot)
- [ai-agent](https://github.com/topics/ai-agent)
- [ai-agent-framework](https://github.com/topics/ai-agent-framework)
- [llm](https://github.com/topics/llm)
- [trading-bot](https://github.com/topics/trading-bot)
- [web3](https://github.com/topics/web3)

---

## Sources

- [Top AI Trading Bots - Medium](https://medium.com/@gwrx2005/top-10-ai-powered-crypto-trading-repositories-on-github-0041862546b6)
- [OctoBot GitHub](https://github.com/Drakkar-Software/OctoBot)
- [ElizaOS Documentation](https://elizaos.github.io/eliza/docs/intro)
- [ElizaOS Plugins Registry](https://github.com/elizaos-plugins)
- [GOAT SDK](https://github.com/goat-sdk/goat)
- [Web3 AI Trading Agent](https://github.com/chainstacklabs/web3-ai-trading-agent)

---

*This is the priority integration list. Focus on Tier 1 this week.*
