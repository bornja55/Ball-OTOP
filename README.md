*Read in other languages: [🇹🇭 ภาษาไทย](#thai-version)*

# 🚀 Ball-OTOP AI Tooling

![NotebookLM](https://img.shields.io/badge/Powered_by-Google_NotebookLM-4285F4?style=for-the-badge&logo=google)
![Skills](https://img.shields.io/badge/Skills-30%2B_Premium_AI_Agents-6f42c1?style=for-the-badge&logo=openai)

A centralized repository for sharing **Skill.md** files and AI-connected tools. This repository is designed for personal reference, team members, and friends to easily access and utilize various AI capabilities and workflows.

## 🔥 The 30+ God-Tier AI Skills

- **`/ask-matt` (Master Router):** Don't know which skill to use? Just ask Matt! He acts as the central router to guide you through all 36+ skills and MCP tools in this repo.

Our AI operates on a meticulously crafted skill system organized into 4 core pillars:

### 🔍 1. Research & Data Synthesis
Focuses on gathering and making sense of data.
- **GG-Research (NotebookLM):** Zero-hallucination data synthesis across PDFs, YouTube, and Docs with 9-format Studio Artifact generation (Podcasts, Video, Slides).
- **Deep Research:** Digging deep into trusted original documents to find exact answers without guessing.

### ⚙️ 2. Engineering & Architecture
Focuses on writing robust code and designing scalable systems.
- **Codebase Design (Karpathy-style):** Designing clear, testable, and highly organized codebases.
- **TypeScript Wizardry (Matt Pocock-style):** Writing modern, error-free code that catches bugs before they happen.
- **Automated Diagramming (`/draw.io`):** Generate architectural diagrams and flowcharts on draw.io with the company's CI palette automatically applied.

### 🛡️ 3. Debugging & Code Review
Focuses on finding flaws and post-incident analysis.
- **Debug Mantra (9arm-style):** A strict 4-step debugging discipline (reproduce, trace, falsify, cross-reference) from the renowned 9arm.
- **Brutal Code Review (`/scrutinize`):** Outsider-perspective reviews for PRs and design docs to challenge intent and implementation.

### 👔 4. Delegation & Ops
Focuses on efficiency, teamwork, and leadership communication.
- **Qwen Delegation (9arm-skills):** Offloading repetitive, manual tasks (like renaming hundreds of files) to cost-effective sub-agents.
- **Executive Translation (`/management-talk`):** Translating deep engineering jargon into high-impact business updates for VPs/Directors via Slack or JIRA.

---

## 🤝 Acknowledgments & Credits
This powerhouse of a repository wouldn't be possible without the incredible open-source tools and skill definitions from the community. Massive thanks to:
- 📖 [notebooklm-py](https://github.com/danuphon-san/notebooklm-py) & [notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) by **@danuphon-san**
- 🧠 [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) by **@multica-ai**
- 🧙‍♂️ [mattpocock/skills](https://github.com/mattpocock/skills/) by **@mattpocock**
- 🦾 [9arm-skills](https://github.com/thananon/9arm-skills) by **@thananon**
- 🎨 [drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) by **@lgazo**

---

## 🛠️ Troubleshooting

### NotebookLM: `NotImplementedError` on Windows (`--master-token`)

- **Status:** Known upstream bug in `notebooklm-py` v0.8.0a3.
- **Impact:** Windows users attempting to use the headless Master Token login will experience a crash (`NotImplementedError`), completely blocking the login flow.
- **What broke:** The library forces an internal Windows setting (Event Loop Policy) that conflicts with the browser-launching engine (Playwright). The system refuses to launch the interactive login window.
- **Workaround 1 (Hot-patch):** Run this PowerShell command to automatically fix the bug in your local cache, then re-run the login command using `--python 3.12`:
```powershell
Get-ChildItem -Path "$env:LOCALAPPDATA\uv\cache" -Recurse -Filter "master_token.py" | ForEach-Object { (Get-Content $_.FullName) -replace 'with sync_playwright', "import asyncio; import sys; asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy()) if sys.platform == 'win32' else None`n    with sync_playwright" | Set-Content $_.FullName }
```
```bash
uvx --python 3.12 --from "notebooklm-py[headless,browser]>=0.8.0a3" notebooklm login --master-token --account YOUR_EMAIL
```
- **Workaround 2 (Alternative):** Bypass the master token feature entirely and extract cookies directly from your active Chrome session (no Playwright needed):
```bash
uvx --from "notebooklm-py[cookies]" notebooklm login --browser-cookies chrome
```

---

## 👨‍💻 Maintainer
- **Owner & Lead Maintainer:** Ball

---
<a id="thai-version"></a>
<br>

# 🇹🇭 ภาษาไทย (Thai Version)

# 🚀 คู่มือและเครื่องมือ AI (Ball-OTOP)

พื้นที่สำหรับแชร์ไฟล์ **Skill.md** และเครื่องมือต่างๆ ที่เชื่อมต่อกับ AI จัดทำขึ้นเพื่อใช้อ่านเอง แบ่งปันให้กับลูกน้องในทีม หรือเพื่อนๆ ที่มาขอคำแนะนำในการนำ AI ไปประยุกต์ใช้ในการทำงาน

## 🔥 ไฮไลท์สุดยอด AI Skills ทั้ง 4 หมวดหมู่

- **`/ask-matt` (Master Router):** ไม่รู้จะเริ่มตรงไหน หรือควรใช้คำสั่งไหนดี? ถาม Matt ได้เลย! นี่คือสมองกลที่จะช่วยวิเคราะห์สถานการณ์ และแนะนำวิธีดึงเครื่องมือทั้ง 36+ ตัวในคลังออกมาใช้ได้อย่างแม่นยำที่สุด

เราได้รวบรวมและจัดหมวดหมู่ AI Skills ระดับท็อปของวงการมาไว้ที่นี่ที่เดียว:

### 🔍 1. การวิจัยและสังเคราะห์ข้อมูล (Research & Data Synthesis)
- **GG-Research (NotebookLM):** ดึงข้อมูลข้ามแพลตฟอร์ม (เอกสาร, YouTube) มาวิเคราะห์หาจุดเชื่อมโยง ได้คำตอบอ้างอิงจากข้อมูลจริง 100% ไม่มีมโน พร้อมสั่งสร้างสื่อ 9 รูปแบบ เช่น สไลด์พรีเซนต์ และพอดแคสต์
- **Deep Research:** การสืบค้นข้อมูลเชิงลึกจากเอกสารต้นฉบับจริงที่เชื่อถือได้ เพื่อหาคำตอบที่ถูกต้องที่สุด

### ⚙️ 2. การออกแบบระบบและการเขียนโค้ด (Engineering & Architecture)
- **วิธีคิดระดับโลก (Karpathy & Pocock):** กระบวนการคิดและวางโครงสร้างโค้ดให้เป็นระเบียบสไตล์ Andrej Karpathy และเทคนิคการเขียนโค้ดที่ลดโอกาสเกิดบั๊กให้น้อยที่สุดสไตล์ Matt Pocock
- **ระบบวาดสถาปัตยกรรม (`/draw.io`):** สั่ง AI วาด Flowchart และแผนภาพระบบลง draw.io พร้อมคุมโทนสี Corporate Identity (CI) ขององค์กรอัตโนมัติ

### 🛡️ 3. การแก้ปัญหาและตรวจสอบคุณภาพ (Debugging & Code Review)
- **คาถาแก้บั๊ก (Debug Mantra):** กฎเหล็ก 4 ข้อในการหาต้นตอของปัญหาโค้ด สไตล์นายอาร์ม (9arm) ที่ฝังอยู่ในระบบคิดของ AI
- **ตรวจสอบโค้ดสุดโหด (`/scrutinize`):** รีวิวงานและโค้ดแบบคนนอกที่ไม่เกรงใจใคร เพื่อหาจุดอ่อนก่อนนำไปใช้งานจริง

### 👔 4. การจัดการและสื่อสาร (Delegation & Ops)
- **ระบบสั่งการลูกสมุน (9arm-skills):** โยนงานน่าเบื่อซ้ำซาก (เช่น แก้ชื่อไฟล์ทีละร้อยไฟล์) ไปให้ AI ระดับรองทำงานแทนด้วยราคาถูกแสนถูก เพื่อประหยัดสมอง AI ตัวท็อปไว้ใช้กับงานที่ต้องคิดวิเคราะห์
- **วุ้นแปลภาษาผู้บริหาร (`/management-talk`):** เปลี่ยนภาษาโค้ดที่ซับซ้อน ให้กลายเป็นรายงานสรุป (Executive Summary) ที่ผู้บริหารอ่านแล้วเข้าใจได้ทันทีว่าเกิดอะไรขึ้น และมีผลกระทบอย่างไร

---

## 🤝 ขอขอบคุณเครดิตต้นฉบับ (Credits)
คลังสมอง AI สุดเทพเหล่านี้จะเกิดขึ้นไม่ได้เลยหากขาดโปรเจกต์ Open-Source คุณภาพสูงจากนักพัฒนาเหล่านี้ ขอขอบคุณ:
- 📖 [notebooklm-py](https://github.com/danuphon-san/notebooklm-py) และ [notebooklm-mcp-cli](https://github.com/danuphon-san/notebooklm-mcp-cli) โดยคุณ **@danuphon-san**
- 🧠 [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) โดย **@multica-ai**
- 🧙‍♂️ [mattpocock/skills](https://github.com/mattpocock/skills/) โดย **@mattpocock**
- 🦾 [9arm-skills](https://github.com/thananon/9arm-skills) โดยคุณ **@thananon** (นายอาร์ม)
- 🎨 [drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) โดย **@lgazo**

---

## 🛠️ การแก้ไขปัญหาเบื้องต้น (Troubleshooting)

### NotebookLM: ขึ้น Error `NotImplementedError` บน Windows

- **สถานะ (Status):** บั๊กจากต้นทาง (Upstream) ใน `notebooklm-py` v0.8.0a3
- **ผลกระทบ (Impact):** ผู้ใช้ระบบ Windows ที่พยายาม Login แบบ Master Token จะเจอ Error ทันที ทำให้ไม่สามารถยืนยันตัวตนเพื่อใช้งาน NotebookLM ได้
- **สาเหตุ (What broke):** ตัวไลบรารีมีการบังคับใช้การตั้งค่าระบบพื้นฐานของ Windows (Event Loop Policy) ที่ขัดแย้งกับกลไกการเปิดหน้าเว็บ (Playwright) ระบบของ Windows จึงปฏิเสธคำสั่งเปิดหน้าต่าง Login
- **วิธีแก้ชั่วคราวที่ 1 (Hot-patch):** เปิด PowerShell แล้วรันคำสั่งด้านล่างเพื่อแก้โค้ดที่มีปัญหาในเครื่องคุณอัตโนมัติ จากนั้นให้ Login ใหม่อีกครั้งโดยบังคับใช้ `--python 3.12`:
```powershell
Get-ChildItem -Path "$env:LOCALAPPDATA\uv\cache" -Recurse -Filter "master_token.py" | ForEach-Object { (Get-Content $_.FullName) -replace 'with sync_playwright', "import asyncio; import sys; asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy()) if sys.platform == 'win32' else None`n    with sync_playwright" | Set-Content $_.FullName }
```
```bash
uvx --python 3.12 --from "notebooklm-py[headless,browser]>=0.8.0a3" notebooklm login --master-token --account อีเมลของคุณ
```
- **วิธีแก้ชั่วคราวที่ 2 (ทางเลือก):** เลี่ยงไปใช้ระบบดึง Cookie จากเบราว์เซอร์ Chrome ในเครื่องแทน (วิธีนี้ไม่ต้องเปิดหน้าต่าง Playwright ใหม่ จึงไม่รันไปชนกับบั๊กนี้):
```bash
uvx --from "notebooklm-py[cookies]" notebooklm login --browser-cookies chrome
```

---

## 👨‍💻 เครดิตและการดูแลระบบ
- **ผู้ดูแลระบบ:** Ball
