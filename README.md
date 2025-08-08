# 🤖 BOT-ZX Uploader

🎮 อัปโหลด Minecraft Add-on ไปยัง Telegram และ Discord อย่างง่ายดาย

## 📁 โครงสร้างโปรเจค

```
BOT-ZX-Uploader/
├── 📄 upload.py          # โปรแกรมหลัก (Console)
├── 🌐 web.html           # เว็บแอปพลิเคชัน
├── ⚙️ config.js          # การตั้งค่าเว็บ (สร้างอัตโนมัติ)
├── 🚀 start.cmd          # เปิดเว็บแอป
├── 🔒 .env               # การตั้งค่าส่วนตัว (ไม่อัปโหลด)
├── 🛡️ SECURITY.md        # คำแนะนำความปลอดภัย
└── 📁 upload_files/      # โฟลเดอร์ไฟล์ที่จะอัปโหลด
    └── *.mcaddon         # ไฟล์ Minecraft Add-on
```

## 🚀 วิธีใช้งาน

### 🌐 เว็บแอป (แนะนำ)
1. คลิกไฟล์ `start.cmd` 
2. เว็บเบราว์เซอร์จะเปิดขึ้นอัตโนมัติ
3. ลากไฟล์ .mcaddon มาวางหรือคลิกเลือกไฟล์
4. เลือกแพลตฟอร์ม (Telegram/Discord/ทั้งคู่)
5. คลิก "เริ่มอัปโหลด"

### 💻 Console
1. เปิด Command Prompt หรือ PowerShell
2. รันคำสั่ง: `python upload.py`
3. ทำตามขั้นตอนที่ปรากฏ

## ⚙️ การตั้งค่า

1. **สร้างไฟล์ `.env`** ในโฟลเดอร์หลัก:
   ```env
   # Telegram Configuration
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_telegram_chat_id_here
   
   # Discord Configuration  
   DISCORD_WEBHOOK_URL=your_discord_webhook_url_here
   
   # Bot Configuration
   BOT_NAME=BOT-ZX
   BOT_VERSION=4.0
   ```

2. **สร้างโฟลเดอร์ไฟล์:**
   ```bash
   mkdir upload_files
   ```

3. **วางไฟล์ .mcaddon** ใน `upload_files/`

### 🔑 วิธีหา API Keys

#### Telegram Bot Token:
1. ไปที่ [@BotFather](https://t.me/BotFather) บน Telegram
2. พิมพ์ `/newbot` และตั้งชื่อ Bot
3. คัดลอก Token ที่ได้

#### Telegram Chat ID:
1. เพิ่ม Bot เข้ากลุ่มหรือแชทส่วนตัว
2. ส่งข้อความใดๆ ให้ Bot
3. เปิด: `https://api.telegram.org/bot<TOKEN>/getUpdates`
4. หา `chat.id` ในผลลัพธ์

#### Discord Webhook:
1. เข้า Discord Server Settings
2. ไป Integrations → Webhooks
3. สร้าง New Webhook
4. คัดลอก Webhook URL

## ✨ ฟีเจอร์หลัก

- 🎯 **อัปโหลดหลายไฟล์** - รองรับ .mcaddon, .mcpack, .zip
- 📱 **รองรับหลายแพลตฟอร์ม** - Telegram และ Discord
- 🌐 **เว็บแอป** - ใช้งานง่ายผ่านเบราว์เซอร์
- 💻 **Console App** - สำหรับผู้ใช้ขั้นสูง
- 📊 **Progress Bar** - ติดตามความคืบหน้าแบบเรียลไทม์
- 📏 **แสดงขนาดไฟล์** - รองรับ KB และ MB
- 🔒 **ความปลอดภัย** - ป้องกันข้อมูลสำคัญด้วย .gitignore
- 🎨 **UI สวยงาม** - ออกแบบให้ใช้งานง่าย

## 📋 ความต้องการระบบ

- **Python 3.7+** พร้อม pip
- **Internet Connection**
- **Web Browser** (สำหรับเว็บแอป)

### 📦 Python Libraries ที่ต้องการ
- `requests` - สำหรับส่ง HTTP requests
- `python-dotenv` - สำหรับอ่านไฟล์ .env

## 📦 การติดตั้ง

1. **Clone หรือดาวน์โหลดโปรเจค**
   ```bash
   git clone <repository-url>
   cd BOT-ZX-Uploader
   ```

2. **ติดตั้ง Python libraries**
   ```bash
   pip install requests python-dotenv
   ```

3. **ตั้งค่าตามขั้นตอนด้านบน**

## 🔧 การแก้ไขปัญหา

### ❌ ไม่สามารถอัปโหลดได้
- ตรวจสอบ Token และ Chat ID ใน `.env`
- ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
- ตรวจสอบขนาดไฟล์ (Telegram: สูงสุด 50MB)

### ❌ เว็บแอปไม่เปิด
- ตรวจสอบว่าไฟล์ `config.js` ถูกสร้างแล้ว
- รัน `start.cmd` อีกครั้ง
- ตรวจสอบ port 8000 ว่าถูกใช้งานหรือไม่

### ❌ ไฟล์ไม่ปรากฏ
- ตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์ `upload_files/`
- รองรับเฉพาะไฟล์ `.mcaddon`, `.mcpack`, `.zip`

## 🔒 ความปลอดภัย

ไฟล์เหล่านี้จะไม่ถูกอัปโหลดไป GitHub:
- `.env` - ข้อมูล API keys
- `config.js` - การตั้งค่าเว็บ  
- `upload_files/` - ไฟล์ของผู้ใช้
- `*.mcaddon`, `*.mcpack` - ไฟล์ Minecraft

📖 **อ่านเพิ่มเติม:** [SECURITY.md](SECURITY.md)

---
**🎮 สนุกกับการใช้งาน BOT-ZX Uploader!**