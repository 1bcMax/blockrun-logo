# BlockRun x402 V2 Showcase Demo
## 给 x402 Foundation 的技术演示

**日期：** 2025年12月25日
**版本：** 2.0
**状态：** 🚀 LIVE - Private Launch Day

> **Note:** 完整版演示脚本请参见 `BLOCKRUN_DEMO_SCRIPT.md`

---

## 🎯 演示概述

BlockRun 是一个完整实现 x402 V2 Wallet Identity 的生产级 AI 网关。本文档提供技术演示脚本和验证步骤。

---

## ✅ 已实现的 x402 V2 功能

### 1. **Wallet-based Identity** ✅ 完整实现

**客户端（SDK）：**
```typescript
// @blockrun/llm - TypeScript SDK
import { LLMClient } from '@blockrun/llm';

// 用户只需提供钱包私钥 - 无需账户、无需 API key
const client = new LLMClient({
  privateKey: process.env.WALLET_PRIVATE_KEY
});

// 钱包自动支付并调用 AI
const response = await client.chat('gpt-4o', 'Hello, x402!');
console.log(response);
```

**服务端（API）：**
- 通过 Coinbase CDP V2 Facilitator 验证支付
- 从验证结果提取 `payer` 钱包地址作为用户 ID
- 数据库记录钱包地址而非传统用户账户
- 完全 permissionless，无需注册

### 2. **Auto Discovery** ✅ 刚刚实现

**Endpoint：** `https://api.blockrun.ai/.well-known/x402/`

**返回信息：**
- x402 版本声明（V2）
- 20+ 可用模型列表
- 透明定价（每个模型的 input/output 价格）
- 支付要求（Base USDC，Coinbase CDP Facilitator）
- SDK 和文档链接

### 3. **Dynamic Recipients** 🔶 未使用（计划中）

当前使用固定收款地址 `PAYMENT_ADDRESS`。
**计划 Q1 2026：** 与合作伙伴（Virtuals、GOAT）进行收入分成。

### 4. **Multi-chain** 🔶 部分实现

- **Production：** Base mainnet
- **计划 Q2 2026：** Solana mainnet

---

## 🎬 演示脚本（3分钟版）

### Part 1: Auto Discovery（30秒）

```bash
# 演示 x402 V2 自动发现
curl https://api.blockrun.ai/.well-known/x402/ | jq

# 输出展示：
# {
#   "x402Version": 2,
#   "name": "BlockRun",
#   "services": [
#     {
#       "name": "LLM Chat Completion",
#       "models": ["gpt-5.2", "gpt-4o", "claude-opus-4", ...],
#       "pricing": { "gpt-4o": { "inputPerMillionTokens": "2.50" } },
#       "payment": {
#         "network": "eip155:8453",
#         "token": "USDC",
#         "facilitator": "coinbase-cdp"
#       }
#     }
#   ]
# }
```

**说明：**
- ✅ x402 V2 compliant
- ✅ 机器可读
- ✅ 透明定价
- ✅ 明确支付要求

---

### Part 2: Wallet Identity - 端到端流程（2分钟）

```bash
# 准备：生成一个新钱包（演示用）
export DEMO_PRIVATE_KEY="0x..."
export DEMO_ADDRESS="0x..."

# 1. 检查钱包余额（需要一点 USDC on Base）
# 假设已有 $1 USDC

# 2. 安装 SDK
npm install @blockrun/llm

# 3. 一行代码调用（无需注册、无需 API key）
node -e "
const { LLMClient } = require('@blockrun/llm');
const client = new LLMClient({
  privateKey: process.env.DEMO_PRIVATE_KEY
});

(async () => {
  console.log('钱包地址:', client.getWalletAddress());
  console.log('调用 GPT-4o (大约 $0.001 USDC)...');

  const response = await client.chat('gpt-4o', 'What is x402 protocol?');
  console.log('响应:', response);

  console.log('支付已自动从钱包扣除！');
})();
"
```

**展示要点：**
1. **无账户注册** - 直接用钱包
2. **无 API key** - 私钥即身份
3. **自动支付** - SDK 处理 x402 流程
4. **钱包 = 用户 ID** - 后端识别钱包地址

---

### Part 3: 后端验证流程（30秒）

```bash
# 查看后端日志（演示支付验证过程）

# 1. 客户端发起请求（无支付）
# → 服务器返回 402 Payment Required

# 2. SDK 签名 USDC TransferWithAuthorization
# → EIP-712 签名，包含：from, to, value, nonce

# 3. SDK 重新请求，附带支付签名
# → Header: X-Payment: <base64-encoded-payload>

# 4. 服务器调用 CDP Facilitator 验证
# → POST https://api.cdp.coinbase.com/platform/v2/x402/verify

# 5. CDP 返回验证结果
# → { isValid: true, payer: "0x..." }

# 6. 提取钱包地址，记录到数据库
# → wallet_address: "0x..."

# 7. 调用 LLM，返回结果
```

**技术细节展示：**
- ✅ EIP-712 签名标准
- ✅ CDP V2 Facilitator 集成
- ✅ Wallet address extraction
- ✅ Transparent logging

---

## 📊 技术验证清单

### x402 V2 Compliance Checklist

| 功能 | 状态 | 证明 |
|------|------|------|
| **Wallet Identity** | ✅ | SDK 只需 privateKey，后端提取 payer 地址 |
| **Auto Discovery** | ✅ | `/.well-known/x402/` 返回标准格式 |
| **EIP-712 Signature** | ✅ | TransferWithAuthorization 签名 |
| **CDP Facilitator** | ✅ | 使用 CDP V2 verify/settle endpoints |
| **Base Mainnet** | ✅ | USDC on Base (0x833589...) |
| **Permissionless** | ✅ | 无注册、无 KYC、无账户系统 |
| **Transparent Pricing** | ✅ | Auto discovery 暴露所有价格 |

---

## 🔬 代码审查要点

### 1. SDK 实现（`blockrun-llm-ts`）

**关键文件：**
- `src/client.ts` - LLMClient 类
- `src/x402.ts` - x402 V2 支付签名

**核心代码：**
```typescript
// src/client.ts:50-58
constructor(options: LLMClientOptions) {
  if (!options.privateKey) {
    throw new Error("Private key required. Pass privateKey in options.");
  }
  // ✅ 从私钥创建钱包账户
  this.account = privateKeyToAccount(options.privateKey);
  this.apiUrl = (options.apiUrl || DEFAULT_API_URL).replace(/\/$/, "");
  this.timeout = options.timeout || DEFAULT_TIMEOUT;
}

// src/x402.ts:61-95
export async function createPaymentPayload(
  account: Account,
  recipient: string,
  amount: string,
  network: string = "eip155:8453",
  options: CreatePaymentOptions = {}
): Promise<string> {
  // ✅ EIP-712 签名 USDC TransferWithAuthorization
  const signature = await signTypedData({
    privateKey: (account as unknown as { source: string }).source as `0x${string}`,
    domain: USDC_DOMAIN,
    types: TRANSFER_TYPES,
    primaryType: "TransferWithAuthorization",
    message: {
      from: account.address,  // ✅ 钱包地址 = 用户身份
      to: recipient,
      value: BigInt(amount),
      validAfter: BigInt(validAfter),
      validBefore: BigInt(validBefore),
      nonce,
    },
  });

  // ✅ 创建 x402 V2 payload
  const paymentData = {
    x402Version: 2,
    resource: { url, description, mimeType },
    accepted: { scheme, network, amount, asset, payTo, ... },
    payload: { signature, authorization: {...} },
    extensions: {},
  };

  return btoa(JSON.stringify(paymentData));
}
```

### 2. API 实现（`blockrun/src`）

**关键文件：**
- `src/app/api/v1/chat/completions/route.ts` - 主 API endpoint
- `src/lib/x402.ts` - x402 验证和结算
- `src/app/api/.well-known/x402/route.ts` - Auto Discovery

**核心代码：**
```typescript
// route.ts:107-125
// ✅ 验证支付
const verification = await verifyPayment(paymentHeader, expectedAmount);

if (!verification.valid) {
  return NextResponse.json(
    { error: "Payment verification failed", details: verification.error },
    { status: 402 }
  );
}

// x402.ts:136-148
// ✅ 调用 CDP Facilitator 验证
const response = await fetch(`${CDP_FACILITATOR_URL}/verify`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${jwt}`,
  },
  body: JSON.stringify({
    x402Version: 2,
    paymentPayload,
    paymentRequirements,
  }),
});

// x402.ts:166-168
// ✅ 提取钱包地址
if (result.isValid) {
  return { valid: true, payload: paymentPayload, payer: result.payer };
}

// route.ts:149 (已修复！)
// ✅ 记录钱包地址到数据库
recordTransaction({
  wallet_address: verification.payer || "unknown",  // ✅ 使用实际钱包地址
  model: modelId,
  // ...
});
```

---

## 📈 生产数据展示

### 示例交易记录（Supabase）

```sql
SELECT
  wallet_address,
  model,
  input_tokens,
  output_tokens,
  price_charged,
  tx_hash,
  created_at
FROM transactions
WHERE wallet_address != 'unknown'
ORDER BY created_at DESC
LIMIT 5;
```

**示例输出：**
```
wallet_address                              | model        | price_charged | tx_hash
0x1234...5678                              | gpt-4o       | 0.002500      | 0xabc...def
0x8765...4321                              | gpt-5.2      | 0.003500      | 0x123...456
0x1111...2222                              | claude-opus-4| 0.001200      | 0x789...abc
```

**证明：**
- ✅ 真实的钱包地址（不是 "unknown"）
- ✅ 链上交易哈希可验证
- ✅ 完全 permissionless（无用户表）

---

## 🌐 在线验证

### 1. Auto Discovery Endpoint

```bash
curl https://api.blockrun.ai/.well-known/x402/ | jq '.x402Version'
# 输出: 2

curl https://api.blockrun.ai/.well-known/x402/ | jq '.services[0].payment'
# 输出: {
#   "network": "eip155:8453",
#   "token": "USDC",
#   "facilitator": "coinbase-cdp",
#   ...
# }
```

### 2. SDK 公开发布

```bash
# TypeScript SDK
npm info @blockrun/llm

# Python SDK
pip show blockrun-llm
```

### 3. GitHub 仓库

- SDK: `https://github.com/blockrun/blockrun-llm-ts`
- Docs: `https://docs.blockrun.ai`

---

## 💡 独特价值主张

### 为什么 BlockRun 是理想的 x402 V2 Showcase？

**1. 高频用例（High-Frequency）**
- AI 推理 = 每秒多次调用
- 比 NFT mint 或一次性服务频繁得多
- 展示 x402 micropayments 的真实场景

**2. Agent Autonomy（Agent 自主性）**
```typescript
// 传统方式：Agent 无法自主支付
const agent = new TradingAgent({
  llmApiKey: process.env.OPENAI_KEY  // ❌ 需要人类的 API key
});

// BlockRun + x402 V2：Agent 真正自主
const agent = new TradingAgent({
  llm: new LLMClient({
    privateKey: agent.wallet.privateKey  // ✅ Agent 用自己的钱包支付
  })
});
```

**3. 生产级实现（Production-Ready）**
- 不是 demo 或 prototype
- 真实 SDK 发布到 npm/PyPI
- API 已在生产环境运行
- 有真实用户和交易

**4. 生态系统影响（Ecosystem Impact）**
- 连接 Base AI agent 生态（Virtuals、GOAT、AgentKit）
- 教育开发者 x402 V2 使用
- 开源 SDK 成为参考实现

---

## 📝 演示后的 Q&A 准备

### 常见问题：

**Q: 钱包私钥的安全性？**
A: 私钥永远不离开客户端。签名在本地完成，只发送签名后的 payload 到服务器。服务器通过 CDP Facilitator 验证签名，无需接触私钥。

**Q: 如果用户钱包没有 USDC？**
A: SDK 会返回清晰的错误："Insufficient USDC balance"。用户需要先在 Base 上获取 USDC（通过 Coinbase、桥接等）。

**Q: Gas fee 是多少？**
A: EIP-712 签名是链下操作，无 gas。实际 USDC 转账由 CDP Facilitator 批量处理，gas 费已包含在服务定价中。

**Q: 支持其他链吗？**
A: 当前 Base mainnet。Q2 2026 计划 Solana（x402 交易量已超过 Base）。x402 V2 的多链标准让扩展很容易。

**Q: 和 OpenRouter 的区别？**
A: OpenRouter 仍需账户和信用卡。BlockRun 100% permissionless，钱包即身份，完全符合 x402 V2 vision。

---

## 🎁 提供给 x402 Foundation

### 1. 技术资源
- ✅ 完整源代码审查权限
- ✅ 测试账户和演示环境
- ✅ 技术文档和架构图

### 2. 合作内容
- ✅ x402 V2 集成教程（博客文章）
- ✅ 开发者研讨会（Workshop）
- ✅ 参考实现（SDK 开源）
- ✅ Case study: "AI Agents on x402 V2"

### 3. 社区推广
- ✅ 在 Base 生态推广 x402
- ✅ 与 Virtuals/GOAT 合作示范 x402
- ✅ 参加 x402 相关活动和会议

---

## 📞 联系方式

**演示请求：**
- Email: hello@blockrun.ai
- 视频通话：可提供实时 demo
- 时间：本周任何时间

**技术讨论：**
- GitHub: github.com/blockrun/blockrun-llm-ts
- Discord: [Your Discord]
- Twitter: @blockrun_ai

---

## ✅ 下一步 (Updated Dec 25)

### 1. 已完成 ✅
- [x] 完整 demo script 编写 (BLOCKRUN_DEMO_SCRIPT.md)
- [x] 部署 Auto Discovery endpoint
- [x] SDK 准备完成
- [x] Private launch LIVE (Dec 25)

### 2. 今日重点 (Dec 25 - Private Launch Day):
- [ ] 发送本文档 + demo script 给 x402 Foundation
- [ ] 提供测试账户（钱包地址 + 一点 USDC）
- [ ] 邀请 x402 Foundation 安排技术演示

### 3. 本周完成 (Dec 26-31):
- [ ] 撰写 x402 V2 集成博客
- [ ] 联系 Virtuals, GOAT, AgentKit
- [ ] 收集早期用户反馈

### 4. 公开发布前 (Jan 1-5):
- [ ] 获得 x402 Foundation 认可
- [ ] 列为官方 showcase
- [ ] 准备联合发布公告
- [ ] Hackathon submission (Jan 5)

### 5. 公开发布 (Jan 6-7):
- [ ] Public launch announcement
- [ ] 合作伙伴 co-announcement
- [ ] 开始社区推广

---

**🚀 BlockRun Private Beta is LIVE!**

我们已经是一个完整的 x402 V2 Wallet Identity 实现。让我们展示给世界！

**Contact:**
- Email: hello@blockrun.ai
- Demo available anytime this week
