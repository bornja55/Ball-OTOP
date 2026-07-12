*Read in other languages: [🇹🇭 ภาษาไทย](#thai-version)*

# 🚀 English Mania Ops & AI Tooling (Ball-OTOP)

![Cloudflare Workers](https://img.shields.io/badge/Deployed_on-Cloudflare_Workers-F38020?style=for-the-badge&logo=cloudflare)
![NotebookLM](https://img.shields.io/badge/Powered_by-Google_NotebookLM-4285F4?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Status-Production_Ready-28A745?style=for-the-badge)

A premium, edge-deployed Operations Manual equipped with advanced AI workflow integrations. This repository centralizes organizational knowledge and provides the team with zero-hallucination, cross-platform data synthesis capabilities through our custom **GG-Research** engine.

## 🔥 Key Capabilities

### 🧠 1. Strategic Data Synthesis (GG-Research)
Instantly cross-reference massive datasets (PDFs, YouTube videos, internal docs, API specs) to find actionable insights. Powered by Google's NotebookLM, this engine guarantees zero-hallucination answers with precise source citations.

### 🎬 2. 9-Format Studio Generation
Transform raw requirements or meeting recordings into 9 different polished artifacts ready for executive review:
- **Slide Decks & Video Overviews** for rapid onboarding.
- **Audio Podcasts** featuring 2 AI hosts debating the topic.
- **Infographics, Flashcards, & Mind Maps** customized to your exact style preferences (e.g., Bento-grid, Professional).

### 👔 3. Automated Executive Translation (/management-talk)
Seamlessly translate deep engineering jargon into high-impact business updates. Automatically shapes the output for Jira, Slack, async standups, or email while retaining critical tracking metrics (Jira Keys, PR numbers).

---

## 👨‍💻 Credits & Maintenance
- **Owner & Lead Maintainer:** Ball (English Mania Engineering)
- **Deployment Structure:** Managed via Cloudflare Wrangler. The `manual.html` acts as the single source of truth, compiled seamlessly into a global edge-worker using `update_worker.py`.

---
<a id="thai-version"></a>
<br>

# 🇹🇭 ภาษาไทย (Thai Version)

# 🚀 คู่มือปฏิบัติงานอัจฉริยะ English Mania (Ball-OTOP)

แหล่งรวมคู่มือการทำงานของทีม ที่ยกระดับด้วยระบบ AI อัจฉริยะ เพื่อช่วยลดเวลาการทำงานซ้ำซ้อน และเพิ่มศักยภาพในการดึงข้อมูลเชิงกลยุทธ์ระดับองค์กรได้อย่างแม่นยำ

## 🔥 ไฮไลท์ฟีเจอร์เด่น

### 🧠 1. ระบบสังเคราะห์ข้อมูลเชิงกลยุทธ์ (GG-Research)
ดึงข้อมูลข้ามแพลตฟอร์ม (ไฟล์เอกสาร, คลิป YouTube, คู่มือ) มาวิเคราะห์หาจุดเชื่อมโยง (Connect the dots) ได้ในพริบตา ได้คำตอบที่อ้างอิงจากข้อมูลจริง 100% ไม่มีมโน (Zero Hallucination) พร้อมระบุแหล่งที่มาชัดเจน

### 🎬 2. แปลงข้อมูลเป็นสื่อ 9 รูปแบบ (Studio Artifacts)
เปลี่ยนข้อมูลดิบหรือคลิปประชุมยาวๆ ให้กลายเป็นสื่อพร้อมใช้งานระดับมืออาชีพ:
- **สไลด์พรีเซนต์ และ วิดีโอสรุป**
- **พอดแคสต์ (Audio Overview)** ให้ AI 2 คนมานั่งคุยและถกเถียงประเด็นให้ฟัง
- **Infographic, Mind Map, Flashcards** ที่สามารถเลือกสไตล์ได้ดั่งใจ (เช่น เรียบหรูแบบ Bento-grid)

### 👔 3. วุ้นแปลภาษาสำหรับผู้บริหาร (/management-talk)
เปลี่ยนภาษาโค้ดดิบๆ หรือศัพท์เทคนิคจ๋าๆ ให้กลายเป็นรายงานสถานะแบบมืออาชีพ (Executive Summary) ที่อ่านง่าย ตัดน้ำเน้นเนื้อ พร้อมปรับรูปแบบให้เหมาะกับช่องทางที่ส่ง (Slack, JIRA, Email) ทันที

---

## 👨‍💻 เครดิตและการดูแลระบบ
- **ผู้พัฒนาและดูแลระบบ:** Ball (English Mania Engineering)
- **สถาปัตยกรรม (Architecture):** ทำงานแบบ Serverless ผ่าน Cloudflare Workers รวดเร็วและไม่มีวันล่ม วิธีอัปเดตเพียงแค่แก้ไฟล์ `manual.html` รันสคริปต์ `update_worker.py` และ Deploy ด้วย `npx wrangler deploy`
