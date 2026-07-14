# Ball-OTOP -- Personal AI Skills

Custom AI Skills I maintain for Claude Code / Cowork.
Full workflow guide: **[manual.englishmania.co.th](https://manual.englishmania.co.th/)**

---

## Installation

```powershell
git clone https://github.com/bornja55/Ball-OTOP.git
cd Ball-OTOP
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

`install.ps1` copies custom skills to `~\.claude\skills\` automatically.

Then install the upstream skill packs:

```bash
# Karpathy Principles
/plugin marketplace add forrestchang/andrej-karpathy-skills

# 9arm Engineering Skills
npx skills add thananon/9arm-skills

# Matt Pocock Skills (30+ skills)
npx skills@latest add mattpocock/skills
# After install: run /setup-matt-pocock-skills once per project
```

---

## Custom Skills (this repo)

Organized by category matching [englishmania manual Toolbox](https://manual.englishmania.co.th/#tools)

### Planning & Alignment (skills/planning/)

| Skill | Description |
|-------|-------------|
| /ask-matt | **Master Router** -- describe your situation, get routed to the right skill. Supports MCP: draw.io, StitchMCP, NotebookLM GG-Research |

### Content & Communication (skills/content/)

| Skill | Description |
|-------|-------------|
| /englishmania-manual | Full workflow router covering all Project Lifecycle phases (Setup -> Define -> Plan -> Build -> Debug -> Communicate) |

### Handoff & Unblocking (skills/handoff/)

| Skill | Description |
|-------|-------------|
| /check-context | Estimate token usage in the current conversation to decide when to Handoff. *(Antigravity only)* |

---

## Credits -- Upstream Skills

Most of the 36+ skills come from these open-source repos. Thank you! <3

| Repo | Author | Install |
|------|--------|---------|
| [mattpocock/skills](https://github.com/mattpocock/skills/) | @mattpocock | 
px skills@latest add mattpocock/skills |
| [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | @thananon (9arm) | 
px skills add thananon/9arm-skills |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | @multica-ai | /plugin marketplace add forrestchang/andrej-karpathy-skills |
| [danuphon-san/notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) | @danuphon-san | 
px -y notebooklm-mcp-cli |
| [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) | @lgazo | 
px -y drawio-mcp-server |

---

**Maintainer:** Ball
