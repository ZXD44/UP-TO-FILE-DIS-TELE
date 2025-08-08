# 🤖 BOT-ZX Uploader

🎮 อัปโหลด Minecraft Add-on ไปยัง Telegram และ Discord

## 📁 ไฟล์สำคัญ

- **`web.html`** - เว็บแอปสำหรับอัปโหลด
- **`upload.py`** - โปรแกรม Console
- **`start.cmd`** - เปิดเว็บแอป (อัปเดต config อัตโนมัติ)
- **`config.js`** - การตั้งค่าสำหรับเว็บ (สร้างจาก .env)

## 🚀 วิธีใช้

1. **เว็บแอป (แนะนำ):** คลิก `start.cmd`
2. **Console:** รัน `python upload.py`

## ⚙️ การตั้งค่า

1. **คัดลอกไฟล์ตัวอย่าง:**
   ```bash
   copy .env.example .env
   ```

2. **แก้ไขไฟล์ `.env`** ใส่ข้อมูลจริง:
   ```
   TELEGRAM_TOKEN=your_actual_bot_token
   TELEGRAM_CHAT_ID=your_actual_chat_id
   DISCORD_WEBHOOK_URL=your_actual_webhook_url
   BOT_NAME=BOT-ZX
   ```

3. **สร้างโฟลเดอร์ไฟล์:**
   ```bash
   mkdir upload_files
   ```

4. **วางไฟล์ .mcaddon** ใน `upload_files/`

## 📊 ฟีเจอร์ใหม่

- ✅ **รองรับ KB และ MB** - แสดงขนาดไฟล์อัตโนมัติ
- ✅ **ดึงข้อมูลจาก .env** - ไม่ต้องใส่ API keys ในเว็บ
- ✅ **Progress Bar** - ติดตามความคืบหน้าแบบเรียลไทม์
- 🔒 **ปลอดภัย** - ไฟล์สำคัญถูกป้องกันด้วย .gitignore

## 🔒 ความปลอดภัย

ไฟล์เหล่านี้จะไม่ถูกอัปโหลดไป GitHub:
- `.env` - ข้อมูล API keys
- `config.js` - การตั้งค่าเว็บ
- `upload_files/` - ไฟล์ของผู้ใช้

---
**🎮 สนุกกับการใช้งาน!**