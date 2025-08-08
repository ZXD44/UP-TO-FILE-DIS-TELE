# 🔒 ความปลอดภัย

## ⚠️ ข้อมูลสำคัญ

**อย่าแชร์ข้อมูลเหล่านี้:**
- 🔑 Telegram Bot Token
- 💬 Telegram Chat ID  
- 🔗 Discord Webhook URL
- 📁 ไฟล์ในโฟลเดอร์ `upload_files/`

## 🛡️ ไฟล์ที่ถูกป้องกัน

ไฟล์เหล่านี้จะไม่ถูกอัปโหลดไป GitHub:

### 📋 ไฟล์การตั้งค่า
- `.env` - ข้อมูล API keys หลัก
- `config.js` - การตั้งค่าสำหรับเว็บ
- `.env.local`, `.env.production` - การตั้งค่าสภาพแวดล้อม

### 📁 ไฟล์ผู้ใช้
- `upload_files/` - โฟลเดอร์ไฟล์ที่อัปโหลด
- `*.mcaddon`, `*.zip` - ไฟล์ Minecraft Add-on

### 🔐 ไฟล์ความปลอดภัย
- `*.key`, `*.pem` - ไฟล์ private key
- `secrets.txt`, `passwords.txt` - ไฟล์รหัสผ่าน

## ✅ การตั้งค่าที่ปลอดภัย

1. **สร้างไฟล์ .env:**
   ```bash
   # สร้างไฟล์ .env ใหม่
   notepad .env
   ```

2. **ใส่ข้อมูลจริงเฉพาะใน .env:**
   - ไม่แชร์ไฟล์ `.env` กับใคร
   - ไฟล์ `config.js` จะถูกสร้างอัตโนมัติจาก `.env`

3. **ตรวจสอบก่อน commit:**
   ```bash
   git status
   ```
   ต้องไม่เห็นไฟล์ `.env` หรือ `config.js`

## 🚨 หากข้อมูลรั่วไหล

1. **เปลี่ยน Token ทันที:**
   - Telegram: สร้าง Bot ใหม่ผ่าน @BotFather
   - Discord: สร้าง Webhook ใหม่

2. **ลบ commit ที่มีข้อมูลสำคัญ:**
   ```bash
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch .env' \
   --prune-empty --tag-name-filter cat -- --all
   ```

3. **Force push:**
   ```bash
   git push origin --force --all
   ```

---
**🔒 ความปลอดภัยเป็นสิ่งสำคัญ!**