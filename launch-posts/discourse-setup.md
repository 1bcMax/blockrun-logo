# BlockRun Discourse Forum Setup

## Why Discourse over Discord

| Discourse | Discord |
|-----------|---------|
| Threaded discussions, searchable | Chat disappears |
| SEO-friendly, Google indexes it | Private, not searchable |
| Long-form content works well | Best for quick chat |
| Knowledge base builds over time | Hard to find old info |
| Email notifications | Requires app |

**Discourse is better for:** Documentation, feature discussions, bug reports, tutorials
**Discord is better for:** Real-time chat, community hang out

---

## Hosting Options

### Option 1: Discourse Hosted (Recommended for speed)
- **URL:** https://www.discourse.org/pricing
- **Cost:** $100/month (Standard) or $50/month (Basic)
- **Setup time:** 10 minutes
- **Custom domain:** community.blockrun.ai

### Option 2: Self-Hosted (Free, more work)
- **Host on:** DigitalOcean, AWS, or your own server
- **Cost:** ~$10-20/month for VPS
- **Setup time:** 1-2 hours
- **Guide:** https://github.com/discourse/discourse/blob/main/docs/INSTALL.md

### Option 3: Free Tier (Limited)
- **Discourse for Teams:** Free for small communities
- **URL:** https://www.discourse.org/teams

---

## Forum Structure

### Categories

```
📢 Announcements (staff only)
   └── Changelog
   └── Blog Posts

💬 General
   └── Introductions
   └── Showcase (what you built)

🔧 Support
   └── Installation Help
   └── Troubleshooting
   └── Bug Reports

💡 Feedback
   └── Feature Requests
   └── Ideas & Suggestions

🛠️ Development
   └── Python SDK
   └── TypeScript SDK
   └── MCP Server
   └── Contributing

📚 Resources
   └── Tutorials
   └── Use Cases
   └── FAQ
```

---

## Initial Content to Seed

Create these topics before launch:

### 1. Welcome Post (Pinned)
```markdown
# Welcome to BlockRun Community 👋

BlockRun gives Claude Code a wallet to access 30+ AI models without API keys.

**Getting Started:**
1. Install: `pip install blockrun-llm && git clone https://github.com/BlockRunAI/blockrun-claude-code-wallet ~/.claude/skills/blockrun`
2. Fund wallet with $1-5 USDC on Base
3. Start using GPT, Grok, DALL-E from Claude

**Quick Links:**
- [GitHub](https://github.com/BlockRunAI/blockrun-claude-code-wallet)
- [USDC Guide](link)
- [Docs](link)

**Community Guidelines:**
- Be helpful and respectful
- Search before posting
- Share what you build!

Questions? Post in #support or email care@blockrun.ai
```

### 2. FAQ Topic (Pinned in Support)
```markdown
# Frequently Asked Questions

**Q: How do I get USDC on Base?**
A: See our [USDC Guide](link)

**Q: Is my wallet secure?**
A: Your private key stays on your machine at ~/.blockrun/. Only signatures are sent to our server.

**Q: What if I run out of funds?**
A: Claude will tell you when balance is low. Top up anytime.

**Q: Can I set a spending limit?**
A: Yes! Use `--set-budget 5.00` to limit daily spend.
```

### 3. Roadmap Topic (Pinned in Announcements)
```markdown
# BlockRun Roadmap 🗺️

**Now:**
- ✅ 30+ LLM models
- ✅ Image generation (DALL-E, Nano Banana)
- ✅ Real-time X via Grok

**Next:**
- 🔄 Video generation
- 🔄 Music/audio generation
- 🔄 More image models

**Future:**
- 💭 Agent-to-agent payments
- 💭 Custom model hosting

Vote on features in #feature-requests!
```

---

## Discourse Settings

### Essential Settings
- **Site name:** BlockRun Community
- **Site description:** Community forum for BlockRun - give Claude Code a wallet
- **Contact email:** care@blockrun.ai
- **Logo:** Use blockrun-agent-skill.png

### Trust Levels (default is fine)
- TL0: New users (limited posting)
- TL1: Basic (after reading + time)
- TL2: Member (can invite, edit wiki)
- TL3: Regular (more permissions)
- TL4: Leader (moderation powers)

### Plugins to Enable
- **Solved** - Mark topics as solved (great for support)
- **Voting** - Upvote feature requests
- **GitHub** - Link to GitHub issues
- **RSS** - Auto-post blog/changelog

---

## Custom Domain Setup

1. Create subdomain: `community.blockrun.ai`
2. Point CNAME to Discourse host
3. Enable SSL (Discourse handles this)

---

## Launch Checklist

- [ ] Choose hosting option
- [ ] Set up forum with categories
- [ ] Create 3 seed topics (Welcome, FAQ, Roadmap)
- [ ] Add logo and branding
- [ ] Configure email settings
- [ ] Set up custom domain
- [ ] Invite 5-10 beta testers
- [ ] Add link to GitHub README
- [ ] Add link to website footer
- [ ] Mention in Reddit/Twitter launch posts
