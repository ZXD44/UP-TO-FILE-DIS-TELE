# 📱 คู่มือการติดตั้ง Vesktop บน Ubuntu

> **Vesktop** เป็น Discord client ที่ปรับแต่งได้และมีฟีเจอร์เพิ่มเติมมากมาย คู่มือนี้จะแนะนำวิธีติดตั้งบน Ubuntu อย่างละเอียด

## 🎯 วิธีการติดตั้งที่แนะนำ: Flatpak

**เหตุผลที่แนะนำ Flatpak:**
- ✅ ติดตั้งง่าย ไม่ยุ่งยาก
- ✅ จัดการ dependencies อัตโนมัติ
- ✅ แยกจากระบบหลัก ไม่กระทบแพ็คเกจอื่น
- ✅ อัพเดทง่าย ปลอดภัย

---

## 📋 ขั้นตอนการติดตั้ง

### 1️⃣ ติดตั้ง Flatpak

เปิด Terminal (กด `Ctrl + Alt + T`) แล้วรันคำสั่ง:

```bash
sudo apt update
sudo apt install flatpak
```

**ตรวจสอบการติดตั้ง:**
```bash
flatpak --version
```
หากแสดงเวอร์ชันออกมา แสดงว่าติดตั้งสำเร็จ ✅

### 2️⃣ เพิ่ม Flathub Repository

Flathub เป็นแหล่งรวมแอปพลิเคชัน Flatpak ที่ใหญ่ที่สุด:

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

### 3️⃣ รีสตาร์ทระบบ ⚠️ **สำคัญมาก**

> **💡 หมายเหตุ:** ขั้นตอนนี้จำเป็นมาก เพื่อให้ระบบรู้จัก Flathub repository

```bash
sudo reboot
```

**หลังจากรีสตาร์ท:** เข้าสู่ระบบอีกครั้ง

### 4️⃣ ติดตั้ง Vesktop

เมื่อระบบพร้อมแล้ว รันคำสั่ง:

```bash
flatpak install flathub dev.vencord.Vesktop
```

ระบบจะถามให้ยืนยัน → กด `y` แล้ว `Enter`

### 5️⃣ เปิดใช้งาน Vesktop

**วิธีที่ 1:** เปิดจากเมนู Applications ของ Ubuntu

**วิธีที่ 2:** รันคำสั่งใน Terminal
```bash
flatpak run dev.vencord.Vesktop
```

---

## 🔧 การแก้ไขปัญหาที่พบบ่อย

### ❌ ปัญหา: `error: No remote refs found for 'flathub'`

**สาเหตุ:** ระบบไม่รู้จัก flathub repository

**วิธีแก้ไข:**

1. **เพิ่ม Flathub อีกครั้ง:**
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

2. **ตรวจสอบ remotes:**
   ```bash
   flatpak remotes
   ```
   ควรเห็น `flathub` ในรายการ

3. **รีสตาร์ทระบบ:**
   ```bash
   sudo reboot
   ```

### ❌ ปัญหา: `command not found` สำหรับ `flatpak`

**สาเหตุ:** Flatpak ยังไม่ได้ติดตั้ง

**วิธีแก้ไข:**
```bash
sudo apt update
sudo apt install flatpak
```

### ❌ ปัญหา: Vesktop ไม่เปิด

**วิธีแก้ไข:**

1. **ตรวจสอบ Error ใน Terminal:**
   ```bash
   flatpak run dev.vencord.Vesktop
   ```
   ดูข้อความ Error ที่แสดง

2. **ตรวจสอบพื้นที่ดิสก์:**
   ```bash
   df -h
   ```

3. **ตรวจสอบ RAM:**
   ```bash
   free -h
   ```

---

## 📞 ต้องการความช่วยเหลือเพิ่มเติม?

หากพบปัญหา ให้แจ้ง:
- 📝 ข้อความ Error ที่แม่นยำ
- 🔍 ขั้นตอนที่ติดขัด
- 💻 ข้อมูลระบบ (Ubuntu version, RAM, etc.)

---

## 🎉 เสร็จสิ้น!

ตอนนี้คุณสามารถใช้งาน Vesktop บน Ubuntu ได้แล้ว! 

**ข้อดีของ Vesktop:**
- 🎨 ปรับแต่งธีมได้
- 🔌 ปลั๊กอินมากมาย
- ⚡ ประสิทธิภาพดี
- 🛡️ ปลอดภัยกว่า Discord ธรรมดา

> **💡 เคล็ดลับ:** ลองสำรวจฟีเจอร์ต่างๆ ของ Vesktop ดูครับ มีอะไรน่าสนใจมากมาย!