# awesome-mcp-servers PR Submission

## Where to Add

Under **AI Providers / Aggregators** section (if exists) or create new category.

---

## Entry Format

```markdown
- [BlockRun](https://github.com/blockrunai/blockrun-mcp) 📇 ☁️ - Access 30+ AI models (GPT, Grok, DALL-E, DeepSeek) via USDC micropayments. No API keys required.
```

---

## PR Title

```
Add BlockRun MCP Server - Multi-model access via micropayments
```

---

## PR Description

```markdown
## What is BlockRun?

BlockRun is an MCP server that provides access to 30+ AI models through USDC micropayments on Base. Instead of managing multiple API keys (OpenAI, xAI, Google, DeepSeek), users fund a single wallet.

**Key features:**
- 30+ models: GPT-5, Grok, DALL-E, DeepSeek, Gemini
- No API keys required
- Pay-per-request via x402 micropayments
- Private key stays local

**Use cases:**
- Image generation (Claude can't generate images)
- Real-time X/Twitter data (Grok has live access)
- Cost optimization (DeepSeek is 10-50x cheaper)
- Rate limit overflow

**Install:**
```bash
claude mcp add blockrun npx @blockrun/mcp
```

**Links:**
- Website: https://blockrun.ai
- GitHub: https://github.com/blockrunai/blockrun-mcp
- Plugin version: https://github.com/BlockRunAI/blockrun-claude-code-wallet
```

---

## Steps to Submit

1. Fork punkpeye/awesome-mcp-servers
2. Add entry to README.md in appropriate section
3. Create PR with title and description above
4. Wait for review

---

## Alternative Lists to Submit

1. **punkpeye/awesome-mcp-servers** - Main list (32K stars)
2. **wong2/awesome-mcp-servers** - Alternative list
3. **mcpservers.org** - Web directory
4. **glama.ai/mcp/servers** - Glama directory
