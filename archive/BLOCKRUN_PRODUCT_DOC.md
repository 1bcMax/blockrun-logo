# BlockRun Product Document
## Crypto-Native AI Gateway

**最后更新: 2025年12月25日**
**状态: Private Launch Day 🚀**

---

## 一、产品概述

### 什么是 BlockRun？

BlockRun 是一个 **crypto-native AI gateway**，让用户通过 USDC micropayments (Base 链) 访问任何 AI 服务，无需账户、信用卡或 KYC。

### 一句话定位

> "The simplest way for crypto wallets to access AI — one line of code, no API keys, pay per request."

### 核心价值主张

| 传统 AI API | BlockRun |
|-------------|----------|
| 需要账户注册 | 钱包即身份 |
| 需要信用卡 | USDC micropayments |
| 需要 KYC | 100% permissionless |
| 预付费/月费 | 按次付费 |
| API key 管理 | 无需 API key |
| Agent 无法自主支付 | Agent 自主支付 ✅ |

---

## 二、产品功能

### 2.1 LLM Gateway

**OpenAI 兼容 API**，支持 20+ 顶级模型：

| Provider | Models | 定价示例 |
|----------|--------|----------|
| OpenAI | GPT-5.2, GPT-4o, o1, o1-mini | $1.75/$14.00 per M tokens |
| Anthropic | Claude Opus 4, Sonnet 4, Haiku 4.5 | $1.00/$5.00 per M tokens |
| Google | Gemini 3 Pro, Gemini 2.5 Pro/Flash | Varies |
| xAI | Grok 4 Fast | Varies |
| DeepSeek | DeepSeek V3, DeepSeek R1 | Low cost |
| Meta | Llama 3.3 70B, Llama 3.1 405B | $0.12/$0.30 per M tokens |
| Mistral | Mistral Large | Varies |
| Alibaba | Qwen 2.5 72B | Varies |

### 2.2 Service Discovery

浏览 **618+ x402-enabled AI 服务**：
- 按类别筛选 (LLM, Image, Voice, Data)
- 按网络筛选 (Base, Ethereum, Solana)
- 搜索功能
- 服务详情页

### 2.3 Unified Router

通过单一接口调用任何 x402 服务：
- 统一 API 格式
- 自动路由
- 价格比较

---

## 三、技术架构

### 3.1 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 16, React 19, Tailwind CSS, Radix UI |
| Backend | Node.js, Hono framework |
| Database | Supabase (PostgreSQL) |
| Blockchain | Base mainnet (USDC) |
| Payment | x402 V2 protocol, Coinbase CDP Facilitator |
| Wallet | WalletConnect, wagmi |

### 3.2 支付流程

```
1. Client → GET /v1/chat/completions
2. Server → 402 Payment Required + pricing details
3. SDK → Sign USDC payment on Base (private key stays local)
4. CDP Facilitator → Verify payment
5. Server → Call LLM provider, return response
6. Supabase → Log transaction
```

### 3.3 x402 V2 支持 (2025年12月)

- ✅ 钱包身份 (Wallet-based identity)
- ✅ 自动 API 发现 (Auto API discovery)
- ✅ 动态支付接收方 (Dynamic payment recipients)
- ✅ 多链支持 (Multi-chain)

---

## 四、SDK

### 4.1 TypeScript SDK (`@blockrun/llm-ts`)

```typescript
import { BlockRunClient } from '@blockrun/llm-ts';

const client = new BlockRunClient({
  privateKey: process.env.WALLET_PRIVATE_KEY,
});

// Simple usage
const response = await client.chat('openai/gpt-5.2', 'Hello!');

// With options
const response = await client.chat('anthropic/claude-opus-4', {
  messages: [{ role: 'user', content: 'Explain x402 protocol' }],
  temperature: 0.7,
});
```

### 4.2 Python SDK (`blockrun-llm`)

```python
from blockrun import BlockRunClient

client = BlockRunClient(
    private_key=os.environ["WALLET_PRIVATE_KEY"]
)

# Simple usage
response = client.chat("openai/gpt-5.2", "Hello!")

# With options
response = client.chat(
    "anthropic/claude-opus-4",
    messages=[{"role": "user", "content": "Explain x402 protocol"}],
    temperature=0.7
)
```

### 4.3 API 兼容性

**100% OpenAI 兼容**：
- `/v1/chat/completions`
- `/v1/completions`
- `/v1/models`

可直接替换 OpenAI SDK base URL。

---

## 五、定价策略

### 5.1 当前定价 (Beta)

| 阶段 | Markup |
|------|--------|
| Beta (现在) | **0%** |
| 长期 | 2-5% (透明) |

### 5.2 对比竞争对手

| Platform | Markup | 透明度 |
|----------|--------|--------|
| BlockRun | 0% → 2-5% | ✅ 透明 |
| OpenRouter | 5% (信用卡 5.5%) | 部分透明 |
| Daydreams | 未知 | ❌ 不透明 |
| Enterprise AI | 15-60% | ❌ 隐藏 |

### 5.3 最低支付

- 最低: **$0.001** per request
- 无最低充值
- 无月费

---

## 六、目标用户

### 6.1 Primary: AI Agent 开发者

**Pain points:**
- Agent 需要自主支付 AI 费用
- 不想管理 API keys
- 需要 permissionless 访问

**BlockRun 解决方案:**
- Agent 钱包自动支付
- 无 API key
- 100% permissionless

### 6.2 Secondary: Crypto-Native 开发者

**Pain points:**
- 不想用信用卡/KYC
- 想用 crypto 支付
- 隐私需求

**BlockRun 解决方案:**
- 钱包即身份
- USDC 支付
- 无数据收集

### 6.3 Tertiary: Web3 项目

**Pain points:**
- 需要给用户提供 AI 功能
- 不想中心化依赖
- 想集成 crypto 支付

**BlockRun 解决方案:**
- 去中心化 gateway
- x402 标准协议
- 简单集成

---

## 七、竞争分析

### 7.1 vs Daydreams Router

| 维度 | Daydreams | BlockRun |
|------|-----------|----------|
| 代币依赖 | $DREAMS 必需 | 无 (纯 USDC) |
| 设置时间 | ~30 分钟 | ~5 分钟 |
| API 兼容 | 自定义 | OpenAI compatible |
| Markup | 不透明 | 透明 |
| 专注 | Gaming + trading | Pure AI gateway |

**BlockRun 优势:** 更简单、更透明、无代币依赖

### 7.2 vs OpenRouter

| 维度 | OpenRouter | BlockRun |
|------|------------|----------|
| 支付 | 信用卡/Crypto | 纯 Crypto (x402) |
| 账户 | 需要 | 不需要 |
| x402 | ❌ | ✅ |
| 定位 | Web2 开发者 | Crypto AI agents |

**BlockRun 优势:** Agent 自主支付、无账户

### 7.3 vs thirdweb Nebula

| 维度 | Nebula | BlockRun |
|------|--------|----------|
| 功能 | 链上推理 + 交易 | LLM gateway |
| x402 | ✅ | ✅ |
| 关系 | **互补** | - |

**策略:** 合作而非竞争

---

## 八、产品路线图

### 8.1 已完成 ✅

- [x] x402 支付集成 (CDP V2)
- [x] OpenAI, Anthropic, Google provider 集成
- [x] Landing page & Discovery UI
- [x] LLM 定价表
- [x] TypeScript SDK (`@blockrun/llm-ts`)
- [x] Python SDK (`blockrun-llm`)
- [x] 618+ 服务发现
- [x] x402 V2 完整支持 (钱包身份、自动发现、动态支付)
- [x] Auto Discovery endpoint (`/.well-known/x402/`)
- [x] Complete demo script for partnerships
- [x] Private launch preparation

### 8.2 进行中 🚧 (Dec 25 - Private Launch Day)

- [x] Private launch to early users
- [ ] MCP Server for Claude Desktop (in development)
- [ ] GOAT SDK plugin POC
- [ ] AgentKit integration example
- [ ] Partnership outreach (Virtuals, GOAT, x402 Foundation)

### 8.3 计划中 📋

**短期 (Q1 2026):**
- [ ] Smart routing (自动选择最优价格/延迟)
- [ ] 用量分析 dashboard
- [ ] 批量请求优化

**中期 (Q2 2026):**
- [ ] Image models (DALL-E, Flux)
- [ ] Voice models (ElevenLabs)
- [ ] Solana 网络支持
- [ ] Multi-facilitator 支持

**长期 (Q3-Q4 2026):**
- [ ] 更多链支持
- [ ] 部分开源
- [ ] Enterprise features

---

## 九、关键指标

### 9.1 当前状态

| 指标 | 数值 |
|------|------|
| 支持的模型 | 20+ |
| 发现的服务 | 618+ |
| 支持的链 | Base (mainnet) |
| SDK | TypeScript, Python |

### 9.2 目标 (Beta)

| 指标 | 目标 |
|------|------|
| 日活跃交易 | 100+ |
| 早期用户项目 | 10+ |
| 集成的 agent 框架 | 5+ |

### 9.3 目标 (Q1 2026)

| 指标 | 目标 |
|------|------|
| 日活跃交易 | 500+ |
| 合作项目 | 10+ |
| GitHub stars | 1000+ |

---

## 十、Launch 计划

| 里程碑 | 日期 | 状态 |
|--------|------|------|
| Private launch | 2025年12月25日 | 🚀 **TODAY** |
| Hackathon submission | 2026年1月5日 | 📋 Preparing |
| Public launch | 2026年1月6-7日 | 📋 Planned |

### Current Phase: Private Launch (Dec 25)

**今日重点:**
- ✅ 发布给早期用户和测试者
- ✅ Demo script 完成，可用于合作伙伴演示
- 🔄 收集早期反馈
- 🔄 开始联系 Tier 1 合作伙伴

### Beta 策略

- **0% markup** 吸引早期用户
- 聚焦 **Base 生态 AI agent** 项目
- 与 **Virtuals, GOAT, AgentKit** 合作
- **x402 Foundation showcase** 申请中

---

## 十一、品牌信息

### Tagline Options

1. "AI for crypto wallets"
2. "Pay per request, no API keys"
3. "The permissionless AI gateway"
4. "One line of code to frontier AI"

### Key Messages

1. **Simple:** "5 分钟设置，一行代码调用"
2. **Transparent:** "0% markup (beta), 透明定价"
3. **Permissionless:** "无账户、无 KYC、钱包即身份"
4. **Agent-native:** "Agent 自主支付，真正的自主"

### Differentiators

1. x402 V2 原生支持
2. OpenAI 100% 兼容
3. 最简单的 crypto AI 集成
4. Agent 自主支付能力

---

## 十二、资源链接

### 产品
- Website: [TBD]
- Docs: [TBD]
- GitHub: [TBD]

### SDKs
- npm: `@blockrun/llm-ts`
- PyPI: `blockrun-llm`

### 协议
- x402: https://x402.org
- x402 V2 公告: https://www.x402.org/writing/x402-v2-launch
- Coinbase CDP: https://docs.cdp.coinbase.com

---

## 十三、FAQ

### Q: 为什么选择 Base 而不是其他链？

A:
1. x402 官方 facilitator 在 Base
2. Coinbase 生态支持
3. 低 gas fee
4. Virtuals Protocol 等 AI agent 项目在 Base

### Q: 会支持 Solana 吗？

A: 计划 Q2 2026 支持。目前 Solana x402 交易量已超过 Base，但 facilitator 基础设施还不如 Base 成熟。

### Q: 与 OpenRouter 有什么区别？

A:
1. OpenRouter 需要账户，BlockRun 不需要
2. OpenRouter 主要面向 Web2，BlockRun 面向 crypto agents
3. BlockRun 支持 agent 自主支付

### Q: 如何保证安全？

A:
1. Private key 永远不离开本地
2. x402 协议经过审计
3. CDP Facilitator 由 Coinbase 运营

### Q: 最低消费是多少？

A: $0.001，真正的 micropayments。

---

## 十四、更新日志

### v1.2 (2025-12-25) - Private Launch Day 🚀
- Private launch to early users
- x402 V2 完整支持已确认
- Demo script 完成 (BLOCKRUN_DEMO_SCRIPT.md)
- Partnership outreach templates ready
- Auto Discovery endpoint live

### v1.1 (2025-12-23)
- Mission and values document created
- Banner designs completed
- Value proposition refined

### v1.0 (2025-12-22)
- 初始版本
- 包含产品概述、技术架构、SDK、定价、路线图

---

*待补充:*
- [ ] 详细 API 文档
- [ ] 集成案例
- [ ] 性能基准测试
- [ ] 安全审计报告
