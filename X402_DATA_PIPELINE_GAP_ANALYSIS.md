# x402 Data Pipeline - Gap Analysis & Recommendations

*Analysis Date: January 2026*

## Executive Summary

After comparing the x402-data pipeline with x402scan.com data, I identified several gaps. **Solana tracking has been addressed.**

| Gap | Impact | Priority | Status |
|-----|--------|----------|--------|
| No Solana transaction tracking | **Critical** - Missing ~$150/day volume | 🔴 P0 | ✅ DONE |
| Missing facilitator discovery endpoints | N/A - Settlement ≠ Discovery | 🟡 P2 | ⬜ Won't fix |
| No x402scan data integration | **Low** - On-chain data is sufficient | 🟢 P3 | ⬜ Deprioritized |
| No historical volume snapshots | **Low** - Can query from raw data | 🟢 P3 | ⬜ Optional |

---

## 1. Missing Facilitator Discovery Endpoints 🔴 P0

### Current vs Required

**Current FACILITATORS dict (10 endpoints):**
```python
FACILITATORS = {
    "cdp_coinbase": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources",
    "payai": "https://facilitator.payai.network/discovery/resources",
    "questflow": "https://facilitator.questflow.ai/discovery/resources",
    "anyspend": "https://mainnet.anyspend.com/x402/discovery/resources",
    "aurracloud": "https://x402-facilitator.aurracloud.com/discovery/resources",
    "thirdweb": "https://api.thirdweb.com/v1/payments/x402/discovery/resources",
    "ultravioletadao": "https://facilitator.ultravioletadao.xyz/discovery/resources",
    "kamiyo": "https://kamiyo.ai/api/v1/x402/discovery/resources",
    "polygon": "https://x402.polygon.technology/discovery/resources",
    "dexter": "https://x402.dexter.cash/discovery/resources",
}
```

**Missing HIGH-VOLUME facilitators (from x402scan):**

| Facilitator | Volume | Txns | Likely Discovery Endpoint |
|-------------|--------|------|---------------------------|
| **Daydreams** | $2.76M | 11.8M | `https://router.daydreams.systems/discovery/resources` |
| **Virtuals** | $1.44M | 883K | TBD (need to find) |
| **Heurist** | $30K | 7.9M | `https://facilitator.heurist.ai/discovery/resources` |
| **OpenX402** | $179K | 697K | `https://openx402.ai/discovery/resources` |
| **X402rs** | $468K | 698K | `https://facilitator.x402.rs/discovery/resources` |
| **CodeNut** | $110K | 478K | `https://www.codenut.ai/discovery/resources` (TBD) |

**Total missing volume: ~$5M (12% of ecosystem)**

### Recommended Action

Add these to `fetch_discovery.py`:

```python
# Add to FACILITATORS dict:
"daydreams": "https://router.daydreams.systems/discovery/resources",  # $2.76M volume
"heurist": "https://facilitator.heurist.ai/discovery/resources",      # 7.9M txns
"openx402": "https://openx402.ai/discovery/resources",                # $179K
"x402rs": "https://facilitator.x402.rs/discovery/resources",          # $468K
# Need to discover:
# "virtuals": "https://??/discovery/resources",  # $1.44M
# "codenut": "https://??/discovery/resources",   # $110K
```

---

## 2. x402scan Data Integration 🟠 P1

x402scan.com provides aggregated metrics that the pipeline doesn't collect:

### Missing Data Points from x402scan

| Metric | Description | Use Case |
|--------|-------------|----------|
| Total Volume | $42.49M all-time | Dashboard metrics |
| Total Transactions | 154M | Dashboard metrics |
| Per-Facilitator Volume | Coinbase $26.83M, PayAI $4.56M, etc. | Facilitator rankings |
| Per-Facilitator Buyers | 215K, 64K, etc. | User adoption metrics |
| Per-Facilitator Sellers | 27K, 20K, etc. | Service provider metrics |
| Daily/Weekly Snapshots | N/A currently | Trend analysis |

### Recommended New Script: `fetch_x402scan_stats.py`

```python
# Scrape or API-call x402scan.com for:
# 1. Total ecosystem stats
# 2. Per-facilitator metrics
# 3. Save to new Supabase table: x402_facilitator_stats
```

### New Database Table

```sql
CREATE TABLE x402_facilitator_stats (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facilitator_name TEXT NOT NULL,
  snapshot_date DATE NOT NULL,
  total_transactions BIGINT,
  total_volume_usd DECIMAL(18,2),
  unique_buyers INTEGER,
  unique_sellers INTEGER,
  chains TEXT[], -- ['base', 'solana']
  UNIQUE(facilitator_name, snapshot_date)
);

CREATE INDEX idx_facilitator_stats_date ON x402_facilitator_stats(snapshot_date);
```

---

## 3. Facilitator Health Monitoring 🟡 P2

### Problem

Pipeline doesn't know when a facilitator endpoint goes down or changes.

### Recommended: Add health checks

```python
# New function in fetch_discovery.py
def check_facilitator_health():
    """Check if each facilitator discovery endpoint is alive"""
    health = {}
    for name, url in FACILITATORS.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'BlockRun/1.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                health[name] = {
                    'status': 'healthy',
                    'response_time_ms': ...,
                    'item_count': len(json.loads(response.read())),
                }
        except Exception as e:
            health[name] = {'status': 'unhealthy', 'error': str(e)}
    return health
```

### New Table

```sql
CREATE TABLE facilitator_health (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facilitator_name TEXT NOT NULL,
  checked_at TIMESTAMP WITH TIME ZONE NOT NULL,
  status TEXT, -- 'healthy', 'unhealthy', 'slow'
  response_time_ms INTEGER,
  item_count INTEGER,
  error_message TEXT
);
```

---

## 4. Missing facilitators_addresses.json Entries 🟡 P2

### Current Coverage

`facilitators_addresses.json` has **22 facilitators** for transaction tracking.

### Potentially Missing

From x402.org ecosystem that might have on-chain activity:

| Facilitator | Status in addresses.json |
|-------------|--------------------------|
| Kobaru | ❌ Missing |
| AutoIncentive | ❌ Missing |
| WorldFun | ❌ Missing |
| Nevermined | ❌ Missing |

### Action

Monitor x402scan for new facilitators with significant volume, then add their on-chain addresses.

---

## 5. Historical Volume Snapshots 🟢 P3

### Problem

No historical tracking of ecosystem growth.

### Recommended: Daily Snapshot Job

```python
# New script: create_daily_snapshot.py
# Runs daily to capture:
# - Total resources count
# - Total origins count
# - Total volume (if available)
# - Per-facilitator resource counts
```

### New Table

```sql
CREATE TABLE ecosystem_snapshots (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  snapshot_date DATE NOT NULL UNIQUE,
  total_origins INTEGER,
  total_resources INTEGER,
  total_accepts INTEGER,
  active_origins_7d INTEGER,
  -- Add volume if x402scan integration done
  total_volume_usd DECIMAL(18,2),
  total_transactions BIGINT
);
```

---

## Implementation Priority

### Phase 1 (This Week) - Critical Gaps

1. [ ] Add missing high-volume facilitator endpoints to `fetch_discovery.py`
2. [ ] Test new endpoints for data format compatibility
3. [ ] Run discovery pipeline with new endpoints

### Phase 2 (Next Week) - Analytics

4. [ ] Create `fetch_x402scan_stats.py` script
5. [ ] Create `x402_facilitator_stats` table
6. [ ] Add daily job to capture facilitator metrics

### Phase 3 (This Month) - Monitoring

7. [ ] Add facilitator health checks
8. [ ] Create ecosystem snapshots table
9. [ ] Build dashboard for monitoring

---

## Comparison: Current vs Proposed

| Data Source | Current | Proposed |
|-------------|---------|----------|
| Discovery endpoints | 10 | 16+ |
| On-chain addresses | 22 facilitators | 26+ facilitators |
| x402scan metrics | ❌ None | ✅ Daily snapshots |
| Facilitator health | ❌ None | ✅ Hourly checks |
| Historical trends | ❌ None | ✅ Daily snapshots |

---

## Quick Wins (Copy-Paste Ready)

### 1. Add Missing Endpoints

In `fetch_discovery.py`, update FACILITATORS:

```python
FACILITATORS = {
    # Existing...
    "cdp_coinbase": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources",
    "payai": "https://facilitator.payai.network/discovery/resources",
    "questflow": "https://facilitator.questflow.ai/discovery/resources",
    "anyspend": "https://mainnet.anyspend.com/x402/discovery/resources",
    "aurracloud": "https://x402-facilitator.aurracloud.com/discovery/resources",
    "thirdweb": "https://api.thirdweb.com/v1/payments/x402/discovery/resources",
    "ultravioletadao": "https://facilitator.ultravioletadao.xyz/discovery/resources",
    "kamiyo": "https://kamiyo.ai/api/v1/x402/discovery/resources",
    "polygon": "https://x402.polygon.technology/discovery/resources",
    "dexter": "https://x402.dexter.cash/discovery/resources",
    # NEW - High volume facilitators (Jan 2026)
    "daydreams": "https://router.daydreams.systems/discovery/resources",
    "heurist": "https://facilitator.heurist.ai/discovery/resources",
    "openx402": "https://openx402.ai/discovery/resources",
    "x402rs": "https://facilitator.x402.rs/discovery/resources",
}
```

### 2. Test Results (Jan 2026)

**Tested endpoints - FAILED (return HTML, not JSON):**
- `https://router.daydreams.systems/discovery/resources` → HTML page
- `https://facilitator.heurist.xyz/discovery/resources` → HTML page
- `https://openx402.ai/discovery/resources` → "Cannot GET" error
- `https://facilitator.x402.rs/discovery/resources` → Empty/timeout

**Why these facilitators have high volume but no discovery endpoint:**
- They focus on **payment settlement** (processing transactions)
- They don't host a public **service registry** (discovery)
- The services they process are registered via **other facilitators** (like Coinbase CDP)

**Key insight:** Facilitator volume ≠ Discovery endpoint availability
- Coinbase CDP handles both: settlement + discovery
- Others like Daydreams, Heurist mainly do settlement only

---

## Revised Priority

### ✅ COMPLETED: Solana Transaction Tracking

**Status: DONE (Jan 2026)**

Added `fetch_solana_transactions.py` to track USDC transfers on Solana:
- Uses Helius API (free tier: 100k requests/month)
- Tracks transactions signed by facilitator addresses
- Found 3 active Solana facilitators: PayAI, Dexter, Corbits
- Sample 24-hour data: ~2,300 txns, ~$150 USDC volume

Key insight: On Solana, facilitator addresses **sign** transactions but USDC flows to
separate settlement addresses. Script handles this architecture difference.

### Remaining Priorities

#### P1: Monitor existing discovery endpoints health
- Ensure 10 current endpoints stay healthy

#### P2: Research facilitator discovery endpoints
- Contact teams directly:
   - Daydreams
   - Heurist
   - OpenX402
   - X402rs
   - Ask if they plan to expose discovery endpoints

---

## Notes

- **Virtuals Protocol**: Likely uses Coinbase CDP as facilitator (no own discovery)
- **CodeNut**: Likely uses Coinbase CDP as facilitator (no own discovery)
- **Key learning**: x402scan.com is the authoritative source for ecosystem metrics
- x402scan may have an API or may need scraping (check for API docs first)
