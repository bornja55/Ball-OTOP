*Read in another language: [🇹🇭 ภาษาไทย](#-คู่มือภาษาไทย) · [🇬🇧 English](#-english-guide)*

# 🧠 Ball-OTOP — คลัง AI Skills สำหรับทีม

![Skills](https://img.shields.io/badge/Skills-40%2B-6f42c1?style=for-the-badge&logo=openai)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-D97706?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)

---

## 🇹🇭 คู่มือภาษาไทย

### ทำไมต้องมี Ball-OTOP?

แทนที่จะต้องจำคำสั่งกว่า **40 ตัว** ด้วยตัวเอง — แค่บอก AI ว่ากำลังทำอะไร มันจะเลือก Skill ที่ถูกต้องมาให้เอง

ตัวอย่าง: พิมพ์ `/ask-matt "เจอบั๊กประหลาด หาต้นตอไม่เจอ"` → AI จะแนะนำให้ใช้ `/debug-mantra` แล้วเดินหน้าต่อเลย

---

### 📦 วิธีติดตั้ง (Quick Install)

**ขั้นตอนที่ 1 — Clone และติดตั้ง Skills:**
```powershell
git clone https://github.com/bornja55/Ball-OTOP.git
cd Ball-OTOP
powershell -ExecutionPolicy Bypass -File .\install.ps1
```
`install.ps1` จะ copy skill ทุกตัวไปที่ `~\.claude\skills\` อัตโนมัติ จากนั้น Restart Claude Code / Cowork เพื่อโหลด Skills ใหม่

**ขั้นตอนที่ 2 — ติดตั้ง MCP Tools (ทำครั้งเดียว):**

| MCP | หน้าที่ | คำสั่งติดตั้ง |
|-----|---------|--------------|
| 🗺️ **draw.io** | วาด Flowchart และแผนภาพระบบ พร้อมสี CI องค์กร | `npx -y drawio-mcp-server --editor` |
| 📚 **NotebookLM** (GG-Research) | วิเคราะห์คลังข้อมูลขนาดใหญ่ข้ามแพลตฟอร์ม ผลลัพธ์อ้างอิงแหล่งที่มา 100% | `npx -y notebooklm-mcp-cli` |
| 🎨 **StitchMCP** | สร้างและแก้ไข UI Design / Design System อัตโนมัติ | ดู [StitchMCP Docs](https://stitch.withgoogle.com/faq) |

---

### 🗂️ 40 Skills แบ่งตาม Workflow

ทุก Skill อยู่ใน `skills/` จัดหมวดตาม [Toolbox ของ manual.englishmania.co.th](https://manual.englishmania.co.th/#tools)

#### 1️⃣ Project Setup — ตั้งค่าโปรเจกต์ก่อนเริ่ม
| Skill | หน้าที่ |
|-------|---------|
| `karpathy-guidelines` | กฎเหล็ก 4 ข้อ: ห้ามเดา, เรียบง่ายก่อน, แตะเฉพาะที่สั่ง, มุ่งเป้า |
| `setup-matt-pocock-skills` | ตั้งค่าโครงสร้าง Issue/Label สำหรับ Repo ใหม่ |
| `git-guardrails-claude-code` | ติดตั้งระบบป้องกัน AI ลบ Branch หรือ Force Push |
| `setup-pre-commit` | บังคับ Format โค้ดและเช็ก Type ก่อน Commit ทุกครั้ง |
| `setup-ts-deep-modules` | ตั้งค่า TypeScript สำหรับโครงสร้าง Deep Modules |

#### 2️⃣ Planning & Alignment — วางแผนและเคลียร์ภาพก่อนลงมือ
| Skill | หน้าที่ |
|-------|---------|
| `ask-matt` ⭐ **Custom** | **Master Router** — บอกสถานการณ์ แล้วระบบ route ไปหา Skill ที่ถูก รองรับ draw.io, StitchMCP, NotebookLM |
| `grill-with-docs` | ซักไซ้ไอเดียผู้ใช้จนกว่าสเปกจะชัดเจน |
| `grill-me` / `grilling` | ให้ AI จับผิดแผนของเราก่อนเริ่มทำ |
| `to-spec` | แปลงบทสนทนาเป็น Spec Document |
| `to-tickets` | แตก Spec เป็น Ticket ยิบย่อยให้ทีมทำงานขนานกัน |
| `wayfinder` | สำหรับโปรเจกต์ใหญ่มาก สร้างแผนที่นำทางแบบเห็นทีละก้าว |
| `domain-modeling` | สร้างศัพท์กลางของทีม ป้องกันต่างคนต่างเรียกสิ่งเดียวกันไม่ตรงกัน |
| `prototype` | สร้าง Proof-of-Concept แบบโยนทิ้งได้ เพื่อทดสอบสมมติฐาน |

#### 3️⃣ Building & Prototyping — ลงมือสร้าง
| Skill | หน้าที่ |
|-------|---------|
| `implement` | เขียนโค้ดตาม Spec อย่างเป็นระบบ |
| `tdd` | เขียน Test นำก่อน แล้วค่อยเขียนโค้ดให้ผ่าน |
| `resolving-merge-conflicts` | แก้ไฟล์ชนกันจาก Git อย่างปลอดภัย |
| `migrate-to-shoehorn` | คลีนโค้ด TypeScript `as` assertion ในไฟล์ Test |

#### 4️⃣ Quality Assurance — ตรวจสอบก่อนขึ้น Production
| Skill | หน้าที่ |
|-------|---------|
| `code-review` | รีวิวโค้ดว่าตรงมาตรฐานและตรง Spec ไหม |
| `scrutinize` | ตรวจแบบคนนอก ถามว่า "มีวิธีที่ง่ายกว่านี้ไหม?" |
| `codebase-design` | วิเคราะห์โครงสร้าง Module ว่าแยกส่วนกันดีพอหรือยัง |
| `improve-codebase-architecture` | สแกนหาจุดที่โค้ดซับซ้อนเกินจำเป็นทั้ง Repo |

#### 5️⃣ Incident Response — จัดการเหตุฉุกเฉิน
| Skill | หน้าที่ |
|-------|---------|
| `debug-mantra` | กฎ 4 ข้อ 9arm: สร้างซ้ำ → ย้อนรอย → ตั้งสมมติฐาน → พิสูจน์ |
| `diagnosing-bugs` | วนลูปสืบสวนบั๊กอย่างเป็นระบบ |
| `post-mortem` | เขียน RCA รายงานชันสูตรหลังแก้ปัญหาเสร็จ |

#### 6️⃣ Delegation & Ops — มอบหมายงานและสื่อสาร
| Skill | หน้าที่ |
|-------|---------|
| `management-talk` | แปลศัพท์เทคนิคเป็นภาษาผู้บริหาร เน้นผลกระทบธุรกิจ |
| `qwen-agent` | โยนงานกรรมกร (เปลี่ยนชื่อไฟล์, Format) ให้ AI ตัวถูกกว่าทำแทน |
| `triage` | จัดลำดับ Backlog ว่าอันไหนด่วน อันไหนรอได้ |
| `research` | ส่ง Agent ไปอ่าน Docs แทนเรา สรุปกลับมาให้ |
| `obsidian-vault` | ค้นหาและเพิ่มโน้ตใน Obsidian Vault |

#### 7️⃣ Content & Communication — งานเขียนและสื่อสาร
| Skill | หน้าที่ |
|-------|---------|
| `englishmania-manual` ⭐ **Custom** | **Workflow Router** ครอบคลุมทุก Phase ตาม Project Lifecycle |
| `edit-article` | ปรับปรุงบทความให้สละสลวยขึ้น |
| `writing-great-skills` | ช่วยเขียน Custom Skill ใหม่อย่างมีประสิทธิภาพ |
| `writing-beats` | จัดจังหวะการเล่าเรื่อง (Story Beats) |
| `writing-fragments` | ปรับท่อนข้อความสั้นๆ ให้ทรงพลัง |
| `writing-shape` | ปรับโครงสร้างภาพรวมของงานเขียน |

#### 8️⃣ Team Upskilling — พัฒนาทีม
| Skill | หน้าที่ |
|-------|---------|
| `teach` | AI เป็นติวเตอร์ 1-on-1 สอนเรื่องที่ต้องการ |
| `scaffold-exercises` | สร้างโครงสร้างแบบฝึกหัดสำหรับอบรมทีม |
| `wizard` | ระบบ Onboarding นำทางตั้งค่าเครื่องมือทีละขั้นตอน |

#### 9️⃣ Handoff & Unblocking — ส่งมอบงานและแก้ติด
| Skill | หน้าที่ |
|-------|---------|
| `check-context` ⭐ **Custom** | ตรวจ Token ที่ใช้ไป ประเมินว่าควร Handoff เปิดแชทใหม่หรือยัง *(Antigravity)* |
| `claude-handoff` / `handoff` | สรุปงานทั้งหมดเป็นเอกสารส่งมอบ ให้สานต่อในแชทใหม่ได้ทันที |
| `loop-me` | กระชากสติ AI เมื่อมันเริ่มทำงานวนลูปกลับไปกลับมา |
| `qwenchance` | ควบคุมไม่ให้ AI ออกทะเลจนหมด Context บนงานซับซ้อน |

---

### 🤝 เครดิตต้นฉบับ

| Repo | เจ้าของ |
|------|---------|
| [mattpocock/skills](https://github.com/mattpocock/skills/) | @mattpocock |
| [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | @thananon (9arm) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | @multica-ai |
| [danuphon-san/notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) | @danuphon-san |
| [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) | @lgazo |

**ผู้ดูแล:** Ball

---
---

## 🇬🇧 English Guide

### What is Ball-OTOP?

A curated collection of **40+ AI skills** organized by workflow phase, so your team never has to memorize which command to use. Just describe the situation — `/ask-matt` routes you to the right tool automatically.

Example: `/ask-matt "found a strange bug, can't trace the cause"` → routes to `/debug-mantra` and kicks off the debugging workflow.

---

### 📦 Installation

**Step 1 — Clone & install skills:**
```powershell
git clone https://github.com/bornja55/Ball-OTOP.git
cd Ball-OTOP
powershell -ExecutionPolicy Bypass -File .\install.ps1
```
Copies all skills to `~\.claude\skills\`. Restart Claude Code / Cowork to load them.

**Step 2 — Install MCP Tools (one-time setup):**

| MCP | Purpose | Install |
|-----|---------|---------|
| 🗺️ **draw.io** | Generate architecture diagrams & flowcharts with auto company CI colors | `npx -y drawio-mcp-server --editor` |
| 📚 **NotebookLM** (GG-Research) | Zero-hallucination synthesis across PDFs, YouTube, Docs — cited to the source | `npx -y notebooklm-mcp-cli` |
| 🎨 **StitchMCP** | Auto-generate and apply UI screens & design systems | See [StitchMCP Docs](https://stitch.withgoogle.com/faq) |

---

### 🗂️ Skill Categories

All 40 skills live in `skills/`, organized by the [englishmania.co.th Toolbox](https://manual.englishmania.co.th/#tools).

| # | Category | Key Skills |
|---|----------|------------|
| 1 | Project Setup | `karpathy-guidelines`, `setup-matt-pocock-skills`, `git-guardrails-claude-code` |
| 2 | Planning & Alignment | `ask-matt` ⭐, `grill-with-docs`, `to-spec`, `to-tickets`, `wayfinder` |
| 3 | Building & Prototyping | `implement`, `tdd`, `resolving-merge-conflicts` |
| 4 | Quality Assurance | `code-review`, `scrutinize`, `codebase-design` |
| 5 | Incident Response | `debug-mantra`, `diagnosing-bugs`, `post-mortem` |
| 6 | Delegation & Ops | `management-talk`, `qwen-agent`, `triage`, `research` |
| 7 | Content & Communication | `englishmania-manual` ⭐, `edit-article`, `writing-*` |
| 8 | Team Upskilling | `teach`, `scaffold-exercises`, `wizard` |
| 9 | Handoff & Unblocking | `check-context` ⭐, `claude-handoff`, `loop-me`, `qwenchance` |

⭐ = Custom skills maintained in this repo

---

### Credits

| Repo | Author |
|------|--------|
| [mattpocock/skills](https://github.com/mattpocock/skills/) | @mattpocock |
| [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | @thananon (9arm) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | @multica-ai |
| [danuphon-san/notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) | @danuphon-san |
| [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) | @lgazo |

**Maintainer:** Ball
