# AGENTS.md

Guidance for AI coding agents working with BlockRun GTM (Go-to-Market) documentation.

## Project Overview

**blockrunGTM** is a collection of marketing, strategy, and go-to-market planning documents for BlockRun.

**Purpose:** GTM strategy, partnership research, content planning, and marketing materials
**Format:** Markdown documents, research notes, brand assets

## Repository Structure

```
blockrunGTM/
├── BLOCKRUN_GTM_MASTER.md           # Master GTM strategy document
├── CLAUDE_CODE_SKILL_GTM.md         # Claude Code skill distribution strategy
├── CONTENT_TRACKER.md               # Content calendar and tracking
├── CIRCLE_ALLIANCE_DIRECTORY.md     # Circle/USDC partner directory
├── CIRCLE_PARTNERS_RESEARCH.md      # Circle partner research notes
├── FINANCIAL_API_OUTREACH_TARGETS.md # Financial API partnership targets
├── CREWAI_BLOCKRUN_PLAN.md          # CrewAI integration planning
├── FLUORA_INTEGRATION_PLAN.md       # Fluora integration planning
├── api-analyzer/                    # API analysis tools
├── brandkit/                        # Brand assets and guidelines
├── drafts/                          # Work-in-progress content
├── archive/                         # Archived documents
└── Daily-reflection/                # Daily notes
```

## Document Types

### Strategy Documents
- `*_GTM_*.md` - Go-to-market strategy
- `*_PLAN.md` - Implementation plans
- `*_RESEARCH.md` - Research and analysis

### Tracking Documents
- `*_TRACKER.md` - Progress tracking
- `*_DIRECTORY.md` - Contact/resource directories
- `*_TARGETS.md` - Outreach targets

## Working with Documents

### Adding New Documents
- Use SCREAMING_SNAKE_CASE for filenames
- Include date in filename if time-sensitive
- Add to appropriate category in structure

### Updating Strategy
- Keep `BLOCKRUN_GTM_MASTER.md` as source of truth
- Reference master doc in derivative documents
- Archive outdated versions

### Research Notes
- Use `*_RESEARCH.md` suffix
- Include sources and dates
- Summarize key findings at top

## Brand Assets

Located in `brandkit/`:
- Logos and icons
- Color palettes
- Typography guidelines
- Marketing templates

## Content Workflow

1. Draft in `drafts/` directory
2. Review and refine
3. Move to root with proper naming
4. Track in `CONTENT_TRACKER.md`

## Notes

- This is documentation-only (no code to build/test)
- Focus on clarity and actionability
- Keep sensitive partnership details private
