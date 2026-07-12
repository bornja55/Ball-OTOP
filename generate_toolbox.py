import json

skills = [
    # Setup
    {"cmd": "/setup-matt-pocock-skills", "cat": "Project Setup", "desc": "ตั้งค่าโครงสร้างและหมวดหมู่ Issue/Label สำหรับโปรเจกต์ใหม่", "ex": "เมื่อเพิ่งสร้าง Repo ใหม่ และต้องการให้ AI วางโครงสร้าง Issue ให้พร้อมทำงานทันที"},
    {"cmd": "/git-guardrails-claude-code", "cat": "Project Setup", "desc": "ติดตั้งระบบป้องกันเพื่อไม่ให้ AI รันคำสั่ง Git ที่อันตราย", "ex": "ป้องกันความเสี่ยงที่ AI อาจเผลอลบ Branch หรือบังคับ Push ทับงานคนอื่นในทีม"},
    {"cmd": "/setup-pre-commit", "cat": "Project Setup", "desc": "ตั้งค่า Pre-commit Hooks ตรวจโค้ดอัตโนมัติก่อนที่จะ Commit", "ex": "อยากบังคับให้โค้ดของทุกคนในทีมถูกจัดฟอร์แมต (Format) และเช็ก Type ให้ผ่านก่อนส่งขึ้น Repo"},
    {"cmd": "/setup-ts-deep-modules", "cat": "Project Setup", "desc": "ตั้งค่าโครงสร้าง TypeScript ให้รองรับ Deep Modules", "ex": "เมื่อโปรเจกต์เริ่มใหญ่ และต้องการแยก Module ออกจากกันให้ชัดเจนเพื่อลดความซับซ้อน"},
    
    # Planning
    {"cmd": "/grill-with-docs", "cat": "Planning & Alignment", "desc": "ซักไซ้ไอเดียผู้ใช้จนกว่าภาพของระบบจะชัดเจนที่สุด", "ex": "หัวหน้าสั่งให้ทำ 'ระบบตะกร้าสินค้า' แต่ไม่ได้บอกสเปกอะไรมาเลย ให้ AI ช่วยถามกลับจนกว่าจะได้ภาพที่ชัดเจน"},
    {"cmd": "/to-spec", "cat": "Planning & Alignment", "desc": "แปลงสิ่งที่คุยมาทั้งหมดให้ออกมาเป็น Document สเปกระบบ", "ex": "หลังจากคุยไอเดียกับ AI จนจบแล้ว สั่งคำสั่งนี้เพื่อสรุปทั้งหมดเป็นไฟล์ Spec ให้ทุกคนอ่านตรงกัน"},
    {"cmd": "/to-tickets", "cat": "Planning & Alignment", "desc": "แตก Spec ออกเป็น Ticket งานเล็กๆ แจกให้ลูกทีมทำ", "ex": "เอาไฟล์ Spec มาย่อยเป็นงานยิบย่อย (เช่น งานฝั่ง Front-end, Back-end) เพื่อเอาไปแปะใน Jira"},
    {"cmd": "/wayfinder", "cat": "Planning & Alignment", "desc": "สำหรับโปรเจกต์สเกลใหญ่มาก ช่วยสร้างแผนที่นำทางแบบเห็นทีละก้าว", "ex": "เมื่อต้องไปแตะโค้ดระบบเก่า (Legacy) ที่พันกันมั่วไปหมด และไม่รู้จะเริ่มแก้ตรงไหนก่อนดี"},
    {"cmd": "/domain-modeling", "cat": "Planning & Alignment", "desc": "สร้างศัพท์กลางของทีม (Context) ป้องกันปัญหาต่างคนต่างเรียกชื่อระบบไม่ตรงกัน", "ex": "ทีมการตลาดเรียกว่า 'ผู้ใช้' ส่วนทีมไอทีเรียกว่า 'Account' คำสั่งนี้จะบังคับให้เราตกลงใช้คำเดียวกันทั้งบริษัท"},
    {"cmd": "/grill-me", "cat": "Planning & Alignment", "desc": "ซักถามสมมติฐานหรือไอเดียอย่างเข้มข้นก่อนเริ่มทำงานจริง", "ex": "ก่อนจะเริ่มเขียนโค้ด ให้ AI สวมบทบาทเป็นคนจับผิดว่าไอเดียของเรามีช่องโหว่ตรงไหนบ้าง"},
    {"cmd": "/grilling", "cat": "Planning & Alignment", "desc": "เหมือน /grill-me แต่เป็นชื่อสั้นๆ", "ex": "ใช้แทน /grill-me ได้เลย"},
    
    # Building
    {"cmd": "/implement", "cat": "Building & Prototyping", "desc": "ลุยเขียนโค้ดตามสเปกให้เป็นรูปร่าง", "ex": "หลังจากมีไฟล์ Spec แล้ว ก็สั่งให้ AI ลงมือเขียนโค้ดตามสเปกนั้นได้เลย"},
    {"cmd": "/tdd", "cat": "Building & Prototyping", "desc": "เขียน Test นำหน้าโค้ด เพื่อป้องกันระบบพังจากการแก้ไขในอนาคต", "ex": "อยากให้โค้ดใหม่เสถียรที่สุด ให้ AI เขียนระบบตรวจสอบ (Test) ขึ้นมาก่อน แล้วค่อยเขียนโค้ดให้ผ่านการตรวจสอบนั้น"},
    {"cmd": "/prototype", "cat": "Building & Prototyping", "desc": "สร้างโค้ดตัวต้นแบบแบบโยนทิ้งได้ เพื่อทดสอบว่าไอเดียเวิร์คไหม", "ex": "อยากรู้ว่าหน้าจอแบบใหม่จะใช้งานง่ายไหม สั่งให้ AI ปั่นโค้ดลวกๆ ขึ้นมาลองกดดูก่อน ค่อยไปเขียนจริงทีหลัง"},
    {"cmd": "/resolving-merge-conflicts", "cat": "Building & Prototyping", "desc": "ช่วยแก้ปัญหาไฟล์ชนกัน (Merge Conflict) จาก Git", "ex": "ตอนดึงงานของเพื่อนมาแล้วโค้ดตีกัน (Conflict) ให้ AI ช่วยวิเคราะห์ว่าควรเก็บโค้ดบรรทัดไหนไว้"},
    {"cmd": "/migrate-to-shoehorn", "cat": "Building & Prototyping", "desc": "แก้ปัญหา TypeScript ในไฟล์ Test ด้วย @total-typescript/shoehorn", "ex": "เมื่อมี Error ประเภท 'as' ในไฟล์ Test เยอะๆ ให้ AI ช่วยคลีนโค้ดให้สะอาดขึ้น"},
    
    # Review
    {"cmd": "/code-review", "cat": "Quality Assurance (QA)", "desc": "ช่วยตรวจ Code PR ของลูกทีมว่าตรงตามมาตรฐานโปรเจกต์หรือไม่", "ex": "ก่อนจะรับงานของลูกทีมเข้าโปรเจกต์หลัก ให้ AI ช่วยอ่านว่าเขาเขียนโค้ดได้ตามมาตรฐานที่ตกลงกันไว้ไหม"},
    {"cmd": "/scrutinize", "cat": "Quality Assurance (QA)", "desc": "การตรวจโค้ดแบบเข้มข้น ไล่ย้อนลอจิกจริงและตั้งคำถามอย่างตรงไปตรงมา", "ex": "เมื่อรู้สึกว่าโค้ดที่เพื่อนเขียนมามันทะแม่งๆ สั่ง AI ให้เจาะลึกแบบ Auditor ว่า 'มันมีวิธีที่ง่ายกว่านี้ไหม?'"},
    {"cmd": "/codebase-design", "cat": "Quality Assurance (QA)", "desc": "ช่วยออกแบบและวิเคราะห์โครงสร้าง Module เชิงลึก", "ex": "อยากรู้ว่าโครงสร้างไฟล์ที่เราวางไว้ มันแยกส่วนประกอบ (Decouple) กันดีพอหรือยัง"},
    {"cmd": "/improve-codebase-architecture", "cat": "Quality Assurance (QA)", "desc": "สแกนโค้ดทั้งระบบเพื่อหาจุดที่ออกแบบมาซับซ้อนเกินไป", "ex": "เมื่อโปรเจกต์เริ่มรกและเพิ่มฟีเจอร์ใหม่ยาก ให้ AI ช่วยชี้เป้าว่าต้องจัดระเบียบโครงสร้างตรงไหนบ้าง"},
    
    # Incident
    {"cmd": "/debug-mantra", "cat": "Incident Response", "desc": "ดึงสติ AI ให้เลิกเดา และใช้กระบวนการ 4 ขั้นตอนในการหาบั๊ก", "ex": "เมื่อระบบล่มบนโปรดักชัน แล้ว AI มัวแต่เดาทางแก้ สั่งคำสั่งนี้เพื่อให้มันกลับมาสืบสวนตามหลักวิทยาศาสตร์"},
    {"cmd": "/diagnosing-bugs", "cat": "Incident Response", "desc": "สืบสวนหาต้นตอของปัญหาแบบเจาะลึก", "ex": "มีผู้ใช้รายงานว่า 'บางครั้งกดปุ่มแล้วหน้าเว็บค้าง' ให้ AI ช่วยไล่โค้ดทีละบรรทัดเพื่อหาจุดเกิดเหตุ"},
    {"cmd": "/post-mortem", "cat": "Incident Response", "desc": "เขียนรายงานชันสูตร (RCA) หลังแก้ปัญหาเสร็จ", "ex": "หลังจากกู้ระบบล่มกลับมาได้แล้ว สั่งให้ AI เขียนสรุปว่าเกิดอะไรขึ้น แก้ยังไง เพื่อส่งให้ผู้บริหารอ่าน"},
    
    # Delegation
    {"cmd": "/management-talk", "cat": "Delegation & Ops", "desc": "แปลงโค้ดหรือศัพท์เทคนิคให้เป็นภาษาผู้บริหารหรือฝ่าย Business", "ex": "ต้องส่งอัปเดตงานให้ Project Manager ผ่าน Slack ให้ AI ช่วยลบศัพท์เทคนิคออกและเน้นผลกระทบทางธุรกิจ"},
    {"cmd": "/qwen-agent", "cat": "Delegation & Ops", "desc": "ส่งงานกรรมกรไปให้ AI โมเดลราคาถูกทำแทน", "ex": "งานเปลี่ยนชื่อไฟล์ทั้งโปรเจกต์ หรืองานจัดฟอร์แมต ให้ AI ตัวเล็กทำแทนเพื่อประหยัดโควต้า AI ตัวหลัก"},
    {"cmd": "/triage", "cat": "Delegation & Ops", "desc": "ปัดกวาดจัดลำดับความสำคัญของงานที่เข้ามาใหม่ใน Backlog", "ex": "หลังหยุดยาวแล้วมี Issue ค้างเยอะมาก ให้ AI ช่วยจัดกลุ่มว่าอันไหนคือบั๊กด่วน อันไหนคือฟีเจอร์รอได้"},
    {"cmd": "/research", "cat": "Delegation & Ops", "desc": "ให้ AI ไปอ่านคู่มือหรือหาข้อมูลแทนเรา", "ex": "อยากต่อ API ของธนาคารใหม่ แต่คู่มือยาว 100 หน้า ให้ AI ไปอ่านแล้วสรุปวิธีใช้งานมาให้ที"},
    {"cmd": "/obsidian-vault", "cat": "Delegation & Ops", "desc": "ดึงข้อมูลหรือจดโน้ตลงใน Obsidian Vault", "ex": "ให้ AI ช่วยค้นหาความรู้เก่าๆ ที่ทีมเคยจดไว้ใน Obsidian"},
    
    # Content & Comms
    {"cmd": "/edit-article", "cat": "Content & Communication", "desc": "ช่วยปรับปรุงบทความให้สละสลวยขึ้น", "ex": "เมื่อร่างประกาศถึงลูกค้าเสร็จแล้ว ให้ AI ช่วยเกลาภาษาให้เป็นทางการมากขึ้น"},
    {"cmd": "/writing-great-skills", "cat": "Content & Communication", "desc": "ช่วยเขียนและสร้าง Custom Skill ใหม่อย่างมีประสิทธิภาพ", "ex": "เมื่อคุณอยากสอน AI ให้ทำงานแบบใหม่ และต้องการให้มันช่วยเขียนสคริปต์ Skill.md ให้"},
    {"cmd": "/writing-beats", "cat": "Content & Communication", "desc": "จัดจังหวะการเล่าเรื่อง (Beats) ในงานเขียน", "ex": "ช่วยเรียบเรียงลำดับหัวข้อในสไลด์พรีเซนต์ให้ดึงดูดความสนใจคนฟังตั้งแต่ต้นจนจบ"},
    {"cmd": "/writing-fragments", "cat": "Content & Communication", "desc": "ปรับแต่งท่อนข้อความสั้นๆ ให้ทรงพลัง", "ex": "คิดประโยคเปิดอีเมลไม่ออก ให้ AI ช่วยแต่งมาให้เลือกหลายๆ แบบ"},
    {"cmd": "/writing-shape", "cat": "Content & Communication", "desc": "ปรับโครงสร้างภาพรวมของงานเขียน", "ex": "มีเอกสารยาวเหยียด ให้ AI ช่วยจัดย่อหน้าและใส่หัวข้อย่อยให้คนอ่านจับใจความง่ายขึ้น"},
    
    # Upskilling
    {"cmd": "/teach", "cat": "Team Upskilling", "desc": "ให้ AI รับบทเป็นติวเตอร์ส่วนตัว สอนเรื่องใหม่ๆ แบบ 1-on-1", "ex": "เมื่อต้องย้ายไปเขียนภาษา Rust แต่ไม่มีพื้นฐาน ให้ AI ค่อยๆ สอนปูพื้นฐานทีละสเต็ปจากโค้ดจริงในโปรเจกต์"},
    {"cmd": "/scaffold-exercises", "cat": "Team Upskilling", "desc": "สร้างโครงสร้างโฟลเดอร์สำหรับแบบฝึกหัด", "ex": "เมื่อต้องจัดเทรนนิ่งให้พนักงานใหม่ ให้ AI ช่วยจำลองโจทย์และเฉลยลงในโฟลเดอร์ให้พนักงานลองทำ"},
    {"cmd": "/wizard", "cat": "Team Upskilling", "desc": "ระบบนำทางสำหรับการตั้งค่าเครื่องมือต่างๆ", "ex": "มีเครื่องมือใหม่ที่ทีมยังไม่คุ้นเคย ให้ AI ค่อยๆ พาตั้งค่าไปทีละขั้นตอน"},
    
    # Handoff
    {"cmd": "/loop-me", "cat": "Handoff & Unblocking", "desc": "กระชากสติ AI เมื่อมันเริ่มทำงานวนลูป", "ex": "ถ้าเห็น AI สั่งแก้ไฟล์เดิมกลับไปกลับมาเกิน 3 รอบ สั่งคำสั่งนี้เพื่อให้มันถอยออกมาก้าวหนึ่งและคิดหาวิธีใหม่"},
    {"cmd": "/qwenchance", "cat": "Handoff & Unblocking", "desc": "ควบคุมไม่ให้ AI ตัวหลักคิดวนลูปจนหมดโควต้า", "ex": "เมื่อเจองานที่ซับซ้อนมากๆ และกลัวว่า AI จะออกทะเลจนเสียเวลาฟรี"},
    {"cmd": "/claude-handoff", "cat": "Handoff & Unblocking", "desc": "สรุปงานทั้งหมดที่ทำมา เพื่อนำไปคุยต่อในแชทใหม่", "ex": "เมื่อแชทยาวเกินไปจนเครื่องเริ่มค้าง สั่งให้ AI สรุปงานเป็นไฟล์เอกสาร เพื่อเอาไปแนบเปิดแชทอันใหม่แทน"},
    {"cmd": "/handoff", "cat": "Handoff & Unblocking", "desc": "คำสั่งทางเลือกสำหรับสรุปงานส่งต่อ", "ex": "ใช้เหมือนกับ /claude-handoff ได้เลย"}
]

import re

with open('manual.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Generate new toolbox HTML
toolbox_html = []
current_cat = ""
for skill in skills:
    if skill['cat'] != current_cat:
        if current_cat != "":
            toolbox_html.append("</div>") # close previous grid
        toolbox_html.append(f'<div class="sub">{skill["cat"]}</div>')
        toolbox_html.append('<div class="grid">')
        current_cat = skill['cat']
        
    toolbox_html.append(f'''  <div class="card">
    <div class="ct"><span class="cmd">{skill['cmd']}</span></div>
    <div class="desc">
      <strong>หน้าที่:</strong> {skill['desc']}<br>
      <div style="margin-top:6px;padding:8px;background:var(--bg3);border-radius:6px;border-left:2px solid var(--a9);">
        <span style="font-size:0.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.05em;display:block;margin-bottom:2px">💡 ตัวอย่างการใช้งาน</span>
        <span style="color:var(--text);font-size:0.82rem">{skill['ex']}</span>
      </div>
    </div>
  </div>''')
toolbox_html.append("</div>") # close last grid

toolbox_html_str = "\\n".join(toolbox_html)

start_marker = '<!-- ===== TOOLBOX ===== -->'
end_marker = '<!-- ===== INSTALL ===== -->'
if start_marker in html and end_marker in html:
    part1 = html.split(start_marker)[0]
    middle = html.split(start_marker)[1].split(end_marker)[0]
    part2 = html.split(end_marker)[1]
    
    header_end = middle.find('<p style="color:var(--muted)')
    header_end = middle.find('</p>', header_end) + 4
    
    toolbox_head = middle[:header_end]
    
    final_html = part1 + start_marker + toolbox_head + "\\n\\n" + toolbox_html_str + "\\n\\n" + end_marker + part2
    with open('manual.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced toolbox section.")
else:
    print("Could not find markers.")
