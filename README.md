# 🤖 BOT-ZX Simple Uploader v4.0

🎮 **Minecraft Add-on Uploader** - อัปโหลดไฟล์ .mcaddon และ .zip ไปยัง Telegram และ Discord

## 🚀 การติดตั้ง

### 1. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 2. สร้างไฟล์ .env
สร้างไฟล์ `.env` และเพิ่มข้อมูล:
```env
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
DISCORD_WEBHOOK_URL=your_discord_webhook_url
BOT_NAME=BOT-ZX
BOT_VERSION=4.0
```

### 3. เตรียมไฟล์
วางไฟล์ .mcaddon หรือ .zip ในโฟลเดอร์ `upload_files/`

## 🎯 การใช้งาน

```bash
python upload.py
```

### ขั้นตอน:
1. **เลือกไฟล์** - เลือกไฟล์ที่ต้องการอัปโหลด
2. **เลือกแพลตฟอร์ม** - Telegram, Discord หรือทั้งคู่
3. **รอการอัปโหลด** - ระบบจะอัปโหลดและแสดงผลลัพธ์

## 🎨 ตัวอย่างข้อความ

```
🎮 Chomp
🌟 สนับสนุนเซิร์ฟเวอร์
└ ซื้อ VIP จากแอดมินเพื่อสิทธิพิเศษ! 🎯

🎮 รับแมพและรีซอร์สแพ็กสุดพิเศษ
└ แบบเอ็กซ์คลูซีฟ! 💎

💖 ทดลองเล่นก่อนตัดสินใจซื้อ
└ เพื่อช่วยเหลือผู้พัฒนา! 🙏

⚠️ หมายเหตุสำคัญ
└ ไฟล์ที่ดาวน์โหลดอาจมีข้อจำกัดด้านลิขสิทธิ์
└ ควรสนับสนุนผู้พัฒนาโดยการซื้อของแท้หากคุณชอบสิ่งนี้ 🛒

📁 ไฟล์: Chomp (Add-on).mcaddon
📊 ขนาด: 913.8 KB
👤 อัปโหลด: ZirconX
🤖 BOT-ZX
```

## 📁 โครงสร้างไฟล์

```
upload/
├── upload.py          # ไฟล์หลัก
├── upload.cmd         # Batch file สำหรับ Windows
├── requirements.txt   # Dependencies
├── .env              # Environment variables
├── .gitignore        # Git ignore
├── README.md         # เอกสารนี้
└── upload_files/     # โฟลเดอร์สำหรับไฟล์ที่ต้องการอัปโหลด
```

## 🔧 การตั้งค่า

### Telegram Bot
1. สร้าง Bot ผ่าน @BotFather
2. รับ Token และใส่ใน `TELEGRAM_TOKEN`
3. รับ Chat ID และใส่ใน `TELEGRAM_CHAT_ID`

### Discord Webhook
1. สร้าง Webhook ใน Discord Server
2. คัดลอก Webhook URL และใส่ใน `DISCORD_WEBHOOK_URL`

## 📝 License

MIT License - ใช้งานได้อย่างอิสระ

---

**🎮 สนุกกับการเล่น Minecraft! 🚀**