# Nano Banana Demo Video Plan

> **Product:** [nano-banana-blockrun](https://github.com/BlockRunAI/nano-banana-blockrun)
> **What:** Claude Code skill for AI image generation with USDC micropayments
> **Price:** $0.05 - $0.12 per image (USDC on Base)

---

## Recording Setup

### Tool: Kap (installed at /Applications/Kap.app)
- Open Kap from Applications
- Click the menu bar icon
- Select recording area (your terminal window)
- Set to record at 30fps, high quality
- Export as MP4 for social media

### Terminal Preparation
1. Increase font size: `Cmd + +` (press multiple times)
2. Use a clean prompt (hide long paths)
3. Clear terminal: `clear`
4. Have Claude Code ready with the skill installed

---

## Demo Script (45 seconds)

### [0:00-0:05] HOOK
**Action:** Show Claude Code terminal, type slowly
**Type:** `generate an image of what it looks like inside Claude's mind when thinking`

**Text overlay (add in post):** "Generate images in Claude Code with USDC"

---

### [0:05-0:15] SKILL ACTIVATION
**Action:** Press Enter, show the skill being invoked
**What happens:** Nano Banana skill activates, shows model selection

**Text overlay:** "No API keys. Just your wallet."

---

### [0:15-0:30] PAYMENT FLOW
**Action:** Show the x402 payment prompt
**What to highlight:**
- Price shown: ~$0.05
- "USDC on Base"
- Wallet signing (DON'T show private key or full address)

**Text overlay:** "$0.05 per image - Pay only for what you use"

---

### [0:30-0:40] IMAGE RESULT
**Action:** Say "open the generated image"
**What happens:** Claude Code runs `open <filename>` and macOS Preview displays the image
**Show:** The generated visualization of Claude's mind in Preview app

**Text overlay:** "Powered by BlockRun.ai x402"

---

### [0:40-0:45] CALL TO ACTION
**Action:** Pause on result

**Text overlay:**
```
Try it yourself:
github.com/BlockRunAI/nano-banana-blockrun
```

---

## Social Media Copy

---

### Reddit Posts

#### r/ClaudeAI

**Title:** I built a skill that lets Claude Code generate images using USDC micropayments - no API keys needed

**Body:**
```
Hey everyone! I wanted to share a Claude Code skill I built called Nano Banana.

**What it does:** Generates images directly in Claude Code using Google's Nano Banana model or DALL-E 3.

**How payment works:** Instead of API keys or subscriptions, you pay per image ($0.05-$0.12) with USDC on Base blockchain. Your wallet signs the payment locally - private keys never leave your machine.

**Why I built it:** I wanted to show that the x402 protocol (HTTP 402 Payment Required) can make AI accessible without the friction of API key management and subscription tiers.

[DEMO VIDEO]

Try it: https://github.com/BlockRunAI/nano-banana-blockrun

Would love feedback! Is this something you'd actually use?
```

---

#### r/ethdev

**Title:** Built a Claude Code skill using x402 micropayments on Base - here's how the payment flow works

**Body:**
```
Hey devs! I built a Claude Code skill for AI image generation that uses USDC micropayments on Base. Wanted to share the technical implementation.

**How x402 works:**
1. Client requests image generation
2. Server returns HTTP 402 with price ($0.05)
3. Client signs payment with wallet (EIP-712 signing, local - keys never leave machine)
4. Server verifies signature, generates image, settles on Base

**Tech stack:**
- x402 protocol for payment handling
- USDC on Base for settlement
- EIP-712 typed data signing

The interesting part: no API keys, no accounts. Your wallet address IS your identity.

[DEMO VIDEO]

Code: https://github.com/BlockRunAI/nano-banana-blockrun

Happy to discuss the implementation details!
```

---

#### r/opensource

**Title:** Open source Claude Code skill for AI image generation with crypto micropayments

**Body:**
```
Just open-sourced a Claude Code skill I built: AI image generation paid with USDC micropayments.

**What it does:**
- Generates images using Google's Nano Banana model or DALL-E 3
- Pay-per-image ($0.05-$0.12) instead of API keys or subscriptions
- Uses x402 protocol (HTTP 402 Payment Required)

**Why open source it:**
I wanted to show a working example of x402 micropayments for AI services. The code shows how to handle the payment flow, wallet signing, and API integration.

[DEMO VIDEO]

GitHub: https://github.com/BlockRunAI/nano-banana-blockrun

Contributions welcome - especially for adding more image models!
```

---

#### r/LocalLLaMA

**Title:** Built a Claude Code skill for image generation - uses micropayments instead of API keys

**Body:**
```
Hey everyone! Sharing a Claude Code skill I built for image generation.

**The interesting part:** Instead of API keys, it uses USDC micropayments ($0.05/image) via the x402 protocol. Your wallet signs locally - no custody, no accounts needed.

**Models available:**
- Google Nano Banana
- DALL-E 3

I know this sub loves local/open models - this is more about the payment mechanism than the models themselves. But curious what you think about this approach for accessing AI services.

[DEMO VIDEO]

GitHub: https://github.com/BlockRunAI/nano-banana-blockrun
```

---

#### r/SideProject

**Title:** I built a Claude Code skill for AI image generation with USDC payments - here's what I learned

**Body:**
```
Just shipped my side project: a Claude Code skill that generates images using USDC micropayments.

**The idea:** What if you could pay for AI services the same way you pay for a coffee? No subscriptions, no API keys, just tap and pay.

**Tech stack:**
- Claude Code skill (Python)
- x402 protocol for payments
- USDC on Base blockchain
- Google Nano Banana + DALL-E 3 for image generation

**What I learned:**
1. The x402 protocol is surprisingly elegant for micropayments
2. Local wallet signing means users keep custody of their keys
3. $0.05/image is actually sustainable with current AI pricing

[DEMO VIDEO]

Try it: https://github.com/BlockRunAI/nano-banana-blockrun

Happy to answer questions about the build!
```

---

#### r/basechain

**Title:** Built an AI image generation tool on Base using x402 micropayments

**Body:**
```
Hey Base community! Built something on Base I wanted to share.

**What it is:** A Claude Code skill that generates AI images, paid with USDC micropayments on Base.

**Why Base?**
- Low fees make micropayments viable ($0.05/image)
- Fast settlement
- USDC liquidity

**How it works:**
1. Request image in Claude Code
2. Server returns price via x402 protocol
3. Sign with your wallet (local, non-custodial)
4. Image generates, payment settles on Base

No API keys. No accounts. Your wallet is your identity.

[DEMO VIDEO]

GitHub: https://github.com/BlockRunAI/nano-banana-blockrun

Building on Base has been great - curious what else the community is working on!
```

---

#### r/coolgithubprojects

**Title:** Claude Code skill for AI image generation with USDC micropayments

**Body:**
```
Built a Claude Code skill that generates images using micropayments instead of API keys.

- Pay $0.05-$0.12 per image with USDC
- Uses x402 protocol (HTTP 402 Payment Required)
- Local wallet signing - keys never leave your machine
- Supports Google Nano Banana and DALL-E 3

[DEMO VIDEO]

https://github.com/BlockRunAI/nano-banana-blockrun
```

---

#### r/CryptoTechnology

**Title:** Implementation of x402 protocol for AI micropayments - technical walkthrough

**Body:**
```
Sharing a project that implements the x402 protocol (HTTP 402 Payment Required) for real-world use.

**The implementation:**
A Claude Code skill that generates AI images. Instead of API keys, it uses USDC micropayments on Base.

**Technical flow:**
1. Client sends request to image generation endpoint
2. Server responds with HTTP 402 + payment details (price, recipient, token)
3. Client constructs EIP-712 typed data and signs with local wallet
4. Client retries request with payment header
5. Server verifies signature, generates image, settles payment

**Why this matters:**
x402 eliminates the need for:
- Account creation
- API key management
- Prepaid credits
- Subscription tiers

Your wallet address becomes your identity. Pay-per-use at the protocol level.

[DEMO VIDEO]

Code: https://github.com/BlockRunAI/nano-banana-blockrun

Happy to discuss the protocol implementation details.
```

---

#### r/commandline

**Title:** Generate AI images from your terminal with USDC micropayments

**Body:**
```
Built a Claude Code skill that brings AI image generation to the command line.

**How it works:**
- Type a prompt in Claude Code
- Skill generates image using Nano Banana or DALL-E 3
- Pay $0.05 per image with USDC (no API keys needed)
- Open result with `open <filename>` in Preview

The payment uses the x402 protocol - your wallet signs locally, private keys never leave your machine.

[DEMO VIDEO]

For CLI enthusiasts who want AI image gen without leaving the terminal.

GitHub: https://github.com/BlockRunAI/nano-banana-blockrun
```

---

#### r/indiehackers

**Title:** Launched a Claude Code skill with crypto micropayments - $0.05/image, no API keys

**Body:**
```
Just shipped something I've been working on: a Claude Code skill for AI image generation with a different payment model.

**The idea:**
Instead of API keys + subscriptions, you pay per image ($0.05) with USDC. Your wallet is your identity - no accounts needed.

**How I built it:**
- Claude Code skill in Python
- x402 protocol for payment handling
- USDC on Base for settlement
- Google Nano Banana + DALL-E 3 for image generation

**What I learned:**
1. Micropayments at $0.05 actually work when fees are low (Base)
2. x402 protocol is elegant - HTTP 402 finally has a use
3. "Wallet as identity" removes so much friction

[DEMO VIDEO]

GitHub: https://github.com/BlockRunAI/nano-banana-blockrun

Would love to hear what other indie hackers think about this payment model for AI tools.
```

---

### X.com (Twitter) Thread

#### Tweet 1 (Hook - with video)
```
I built a Claude Code skill that generates images with USDC micropayments.

No API keys. No subscriptions. Just $0.05/image.

Here's how it works: [VIDEO]
```

#### Tweet 2 (Problem)
```
The problem with AI APIs today:

- Create account
- Generate API key
- Add credit card
- Prepay credits
- Manage rate limits

All that friction... just to generate one image.
```

#### Tweet 3 (Solution)
```
x402 flips this:

1. Send request
2. Server says "that'll be $0.05"
3. Sign payment with your wallet (locally)
4. Get your image

Your wallet IS your identity. No accounts needed.
```

#### Tweet 4 (How it works)
```
How the payment works:

- Uses EIP-712 signing (same as signing any tx)
- Private key NEVER leaves your machine
- Payment settles on Base in USDC
- Instant, verifiable, non-custodial
```

#### Tweet 5 (CTA)
```
Try it yourself:

github.com/BlockRunAI/nano-banana-blockrun

Built on @x402protocol

This is what USDC utility looks like.
```

---

## Hashtags

**Primary:** #ClaudeCode #x402 #Web3 #AI #Base #USDC

**Secondary:** #OpenSource #Stablecoins #AIArt #Micropayments #DeFi #BuildInPublic

**For different platforms:**
- Reddit: Don't use hashtags (against culture)
- X.com: Use 3-5 hashtags max per tweet
- Best combo: #ClaudeCode #x402 #AI #Web3

---

## Best Posting Times (US-focused)

| Platform | Best Time (ET) | Why |
|----------|---------------|-----|
| Reddit (r/ClaudeAI) | Tue-Thu 9-11am | Dev audience online |
| Reddit (r/SideProject) | Tue-Thu 10am-12pm | Builders browsing |
| Reddit (r/ethdev) | Mon-Wed 10am-12pm | Ethereum devs active |
| Reddit (r/opensource) | Weekdays 9-11am | Dev community |
| Reddit (r/LocalLLaMA) | Weekdays 10am-1pm | AI enthusiasts |
| Reddit (r/basechain) | Weekdays 10am-12pm | Base community |
| Reddit (r/coolgithubprojects) | Weekdays anytime | Low traffic, always visible |
| Reddit (r/CryptoTechnology) | Weekdays 9-11am | Technical crypto devs |
| Reddit (r/commandline) | Weekdays 10am-12pm | CLI enthusiasts |
| Reddit (r/indiehackers) | Tue-Thu 9-11am | Indie builders |
| X.com | Tue-Wed 9am-12pm | Tech Twitter peak |

**Posting strategy:**

Day 1 (Morning):
1. r/ClaudeAI (most relevant, start here)
2. r/SideProject (2hr later)
3. r/coolgithubprojects (2hr later)

Day 1 (Evening):
4. X.com thread

Day 2:
5. r/ethdev
6. r/basechain
7. r/indiehackers

Day 3:
8. r/opensource
9. r/LocalLLaMA
10. r/CryptoTechnology
11. r/commandline

---

## Post-Recording Checklist

- [ ] Record demo in Kap
- [ ] Export as MP4 (high quality)
- [ ] Export as GIF (for thumbnails/previews)
- [ ] Save to `nano-banana-assets/` folder
- [ ] Upload to GitHub repo (optional)

**Day 1 - Morning:**
- [ ] Post to r/ClaudeAI
- [ ] Post to r/SideProject (2hr later)
- [ ] Post to r/coolgithubprojects (2hr later)

**Day 1 - Evening:**
- [ ] Post X.com thread

**Day 2:**
- [ ] Post to r/ethdev
- [ ] Post to r/basechain
- [ ] Post to r/indiehackers

**Day 3:**
- [ ] Post to r/opensource
- [ ] Post to r/LocalLLaMA
- [ ] Post to r/CryptoTechnology
- [ ] Post to r/commandline

**Ongoing:**
- [ ] Monitor and respond to comments
- [ ] Cross-post wins/feedback to X.com

---

## Quick Reference

**GitHub:** https://github.com/BlockRunAI/nano-banana-blockrun

**Key messages:**
- No API keys needed
- $0.05-$0.12 per image
- USDC on Base
- Private keys never leave your machine
- x402 protocol

**Demo command:** `generate an image of what it looks like inside Claude's mind when thinking`
