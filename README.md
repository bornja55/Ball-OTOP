# Ball-OTOP - AI Skills Collection

~40 AI skills organized by workflow phase, matching [manual.englishmania.co.th](https://manual.englishmania.co.th/).

## Quick Install

```powershell
git clone https://github.com/bornja55/Ball-OTOP.git
cd Ball-OTOP
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Installs all skills to `~\.claude\skills\`. Restart Claude Code / Cowork after.

---

## Skill Categories

Organized by [Toolbox section](https://manual.englishmania.co.th/#tools) of the manual.

### 1. Project Setup (`skills/1-project-setup/`)
| Skill | Source |
|-------|--------|
| `karpathy-guidelines` | andrej-karpathy-skills |
| `setup-matt-pocock-skills` | mattpocock/skills |
| `git-guardrails-claude-code` | mattpocock/skills |
| `setup-pre-commit` | mattpocock/skills |
| `setup-ts-deep-modules` | mattpocock/skills |

### 2. Planning & Alignment (`skills/2-planning/`)
| Skill | Source |
|-------|--------|
| `ask-matt` | **Custom** (master router + MCP routing) |
| `grill-with-docs` | mattpocock/skills |
| `grill-me` | mattpocock/skills |
| `grilling` | mattpocock/skills |
| `to-spec` | mattpocock/skills |
| `to-tickets` | mattpocock/skills |
| `wayfinder` | mattpocock/skills |
| `domain-modeling` | mattpocock/skills |
| `prototype` | mattpocock/skills |

### 3. Building & Prototyping (`skills/3-building/`)
| Skill | Source |
|-------|--------|
| `implement` | mattpocock/skills |
| `tdd` | mattpocock/skills |
| `resolving-merge-conflicts` | mattpocock/skills |
| `migrate-to-shoehorn` | mattpocock/skills |

### 4. Quality Assurance (`skills/4-qa/`)
| Skill | Source |
|-------|--------|
| `code-review` | mattpocock/skills |
| `scrutinize` | 9arm-skills |
| `codebase-design` | mattpocock/skills |
| `improve-codebase-architecture` | mattpocock/skills |

### 5. Incident Response (`skills/5-incident/`)
| Skill | Source |
|-------|--------|
| `debug-mantra` | 9arm-skills |
| `diagnosing-bugs` | mattpocock/skills |
| `post-mortem` | 9arm-skills |

### 6. Delegation & Ops (`skills/6-delegation/`)
| Skill | Source |
|-------|--------|
| `management-talk` | 9arm-skills |
| `qwen-agent` | 9arm-skills |
| `triage` | mattpocock/skills |
| `research` | mattpocock/skills |
| `obsidian-vault` | mattpocock/skills |

### 7. Content & Communication (`skills/7-content/`)
| Skill | Source |
|-------|--------|
| `englishmania-manual` | **Custom** (full workflow router) |
| `edit-article` | mattpocock/skills |
| `writing-great-skills` | mattpocock/skills |
| `writing-beats` | mattpocock/skills |
| `writing-fragments` | mattpocock/skills |
| `writing-shape` | mattpocock/skills |

### 8. Team Upskilling (`skills/8-upskilling/`)
| Skill | Source |
|-------|--------|
| `teach` | mattpocock/skills |
| `scaffold-exercises` | mattpocock/skills |
| `wizard` | mattpocock/skills |

### 9. Handoff & Unblocking (`skills/9-handoff/`)
| Skill | Source |
|-------|--------|
| `check-context` | **Custom** (Antigravity token counter) |
| `claude-handoff` | mattpocock/skills |
| `handoff` | mattpocock/skills |
| `loop-me` | mattpocock/skills |
| `qwenchance` | 9arm-skills |

---

## MCPs (install separately)

These are MCP tools, not skills. Install once globally:

```bash
# draw.io diagrams
npx -y drawio-mcp-server --editor

# NotebookLM (GG-Research)
npx -y notebooklm-mcp-cli
```

---

## Credits

| Repo | Author |
|------|--------|
| [mattpocock/skills](https://github.com/mattpocock/skills/) | @mattpocock |
| [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | @thananon (9arm) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | @multica-ai |
| [danuphon-san/notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) | @danuphon-san |
| [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) | @lgazo |

---

**Maintainer:** Ball
