# English Mania Manual & AI Tooling (Ball-OTOP)

**TL;DR:** Repository for the English Mania Operations Manual and AI Custom Skills (GG-Research) deployment. 

**Impact:** Centralizes operational knowledge and provides the team with NotebookLM-powered AI research tools. Enables executives and PMs to generate zero-hallucination strategic insights, executive briefings, and 9 different studio artifacts (Slide Decks, Podcasts, Infographics) directly from raw cross-platform data.

**What it is:** 
A lightweight, edge-deployed web manual. The core content lives in `manual.html`, which documents our custom AI skills (e.g., GG-Research, /management-talk). It is injected into a Cloudflare Worker script (`worker.js`) for high-availability global deployment.

**Owner:** English Mania Ops / Engineering Team

**Deployment & Maintenance:**
1. Edit `manual.html` to update team workflows or add new AI skills.
2. Run `python update_worker.py` to compile the HTML into the worker script.
3. Deploy to production via `npx wrangler deploy`.
