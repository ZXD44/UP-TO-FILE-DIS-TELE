import os
import requests
import datetime
import getpass
import time
import json
import re
from dotenv import load_dotenv

# โหลด environment variables จากไฟล์ .env
load_dotenv()

# ========================================
# 🤖 BOT-ZX Simple Uploader v4.0
# ========================================

class SimpleUploader:
    def __init__(self):
        # ========= CONFIG จาก .env ========= #
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        self.bot_name = os.getenv("BOT_NAME", "BOT-ZX")
        self.bot_version = os.getenv("BOT_VERSION", "4.0")
        # ================================== #
        
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.user = getpass.getuser()
        
    def print_header(self):
        print("\n" + "=" * 50)
        print("🎮 BOT-ZX Simple Uploader v4.0")
        print("🚀 Minecraft Add-on Uploader")
        print("=" * 50)
    
    def show_progress(self, current, total):
        """แสดง progress bar"""
        progress = int((current / total) * 20)
        bar = "█" * progress + "░" * (20 - progress)
        percentage = int((current / total) * 100)
        print(f"📊 ความคืบหน้า: [{bar}] {percentage}%")
        
    def get_files(self):
        """ดึงรายการไฟล์เฉพาะ .mcaddon และ .zip จากโฟลเดอร์ upload_files"""
        files = []
        upload_dir = os.path.join(self.current_dir, 'upload_files')
        
        if os.path.exists(upload_dir):
            for f in os.listdir(upload_dir):
                if os.path.isfile(os.path.join(upload_dir, f)) and f.lower().endswith(('.mcaddon', '.zip')):
                    files.append(f)
        return files
    
    def format_file_size(self, bytes_size):
        """จัดรูปแบบขนาดไฟล์"""
        kb = bytes_size / 1024
        if kb >= 1024:
            mb = kb / 1024
            return f"{mb:.1f} MB"
        return f"{kb:.1f} KB"
    
    def show_files(self, files):
        """แสดงรายการไฟล์"""
        print(f"\n📁 ไฟล์ที่พบ ({len(files)} ไฟล์):")
        print("─" * 40)
        upload_dir = os.path.join(self.current_dir, 'upload_files')
        for i, file in enumerate(files, 1):
            file_path = os.path.join(upload_dir, file)
            size = os.path.getsize(file_path)
            formatted_size = self.format_file_size(size)
            print(f"  {i:2d}. 📦 {file}")
            print(f"      📊 ขนาด: {formatted_size}")
            print()
    
    def select_platform(self):
        """เลือกแพลตฟอร์ม"""
        print("\n🚀 เลือกแพลตฟอร์ม:")
        print("  ┌─ 1. 📱 Telegram")
        print("  ├─ 2. 📢 Discord") 
        print("  └─ 3. 🌐 ทั้งคู่")
        print("─" * 30)
        
        while True:
            choice = input("\n👉 เลือก (1/2/3): ").strip()
            if choice in ['1', '2', '3']:
                return choice
            print("❌ กรุณาเลือก 1, 2 หรือ 3")
    
    def select_files(self, files):
        """เลือกไฟล์"""
        print("\n📝 เลือกไฟล์:")
        print("  • ใส่หมายเลขไฟล์ (เช่น: 1,3,5)")
        print("  • ใส่ 'all' เพื่อเลือกทั้งหมด")
        print("─" * 30)
        choice = input("👉 ").strip().lower()
        
        if choice == 'all':
            return list(range(len(files)))
        
        try:
            if ',' in choice:
                indices = [int(x.strip())-1 for x in choice.split(',')]
            else:
                indices = [int(choice)-1]
            
            return [i for i in indices if 0 <= i < len(files)]
        except:
            print("❌ รูปแบบไม่ถูกต้อง")
            return []
    
    def get_addon_info(self, filename):
        """ดึงข้อมูล addon"""
        print(f"\n🔍 ตรวจสอบข้อมูล: {filename}")
        
        # ทำความสะอาดชื่อไฟล์ - ลบ (Add-on) และนามสกุลไฟล์
        clean_name = re.sub(r'\s*\(Add-on\)\s*', '', filename, flags=re.IGNORECASE)
        clean_name = re.sub(r'\.(mcpack|mcaddon|zip|rar|7z|txt|md)$', '', clean_name, flags=re.IGNORECASE)
        clean_name = re.sub(r'[_\-\.]', ' ', clean_name).strip()
        
        print(f"🔍 ชื่อไฟล์: {clean_name}")
        
        # ใช้ข้อมูลเริ่มต้น
        return {
            'name': clean_name,
            'title': clean_name,
            'description': f"""🌟 **สนับสนุนเซิร์ฟเวอร์**
└ ซื้อ VIP จากแอดมินเพื่อสิทธิพิเศษ! 🎯

🎮 **รับแมพและรีซอร์สแพ็กสุดพิเศษ**
└ แบบเอ็กซ์คลูซีฟ! 💎

💖 **ทดลองเล่นก่อนตัดสินใจซื้อ**
└ เพื่อช่วยเหลือผู้พัฒนา! 🙏

⚠️ **หมายเหตุสำคัญ**
└ ไฟล์ที่ดาวน์โหลดอาจมีข้อจำกัดด้านลิขสิทธิ์
└ ควรสนับสนุนผู้พัฒนาโดยการซื้อของแท้หากคุณชอบสิ่งนี้ 🛒""",
            'rating': "⭐ 4.5/5",
            'downloads': "📥 1.2K+"
        }
    
    def upload_to_telegram(self, file_path, addon_info):
        """อัปโหลดไป Telegram"""
        print(f"📱 กำลังส่งไป Telegram...")
        
        filename = os.path.basename(file_path)
        file_size_bytes = os.path.getsize(file_path)
        file_size = self.format_file_size(file_size_bytes)
        
        # 1. ส่งข้อความข้อมูล Addon ก่อน
        try:
            info_message = f"""🎮 **{addon_info['title']}**

{addon_info['description']}

{addon_info['rating']} | {addon_info['downloads']}

� **ไฟลโ์:** `{filename}`
📁 **ขนาด:** `{file_size}`
👤 **อัปโหลด:** `{self.user}`

🤖 {self.bot_name}"""
            
            message_data = {
                'chat_id': self.chat_id,
                'text': info_message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", data=message_data)
            if response.json().get('ok'):
                print("✅ ส่งข้อมูล Addon สำเร็จ")
            
        except Exception as e:
            print(f"⚠️ ไม่สามารถส่งข้อมูลได้: {e}")
        
        # 3. ส่งไฟล์
        try:
            with open(file_path, 'rb') as file:
                files = {'document': file}
                data = {
                    'chat_id': self.chat_id,
                    'caption': f"📥 ดาวน์โหลด {addon_info['name']}\n🤖 {self.bot_name}"
                }
                
                response = requests.post(f"https://api.telegram.org/bot{self.token}/sendDocument", files=files, data=data)
                
                if response.json().get('ok'):
                    print("✅ อัปโหลดไฟล์ Telegram สำเร็จ")
                    return True
                else:
                    print("❌ อัปโหลดไฟล์ Telegram ล้มเหลว")
                    return False
        except Exception as e:
            print(f"❌ ข้อผิดพลาด: {e}")
            return False
    
    def upload_to_discord(self, file_path, addon_info):
        """อัปโหลดไป Discord"""
        print(f"📢 กำลังส่งไป Discord...")
        
        filename = os.path.basename(file_path)
        file_size_bytes = os.path.getsize(file_path)
        file_size = self.format_file_size(file_size_bytes)
        
        try:
            # 1. ส่งข้อมูล Addon ก่อน (ไม่มีไฟล์)
            embed_info = {
                "title": f"🎮 {addon_info['title']}",
                "description": addon_info['description'],
                "color": 0x4CAF50,
                "fields": [
                    {"name": "📁 ไฟล์", "value": f"`{filename}`", "inline": True},
                    {"name": "📊 ขนาด", "value": f"`{file_size}`", "inline": True},
                    {"name": "👤 อัปโหลด", "value": f"`{self.user}`", "inline": True}
                ],
                "footer": {"text": f"🤖 {self.bot_name}"}
            }
            
            payload_info = {
                "embeds": [embed_info],
                "username": self.bot_name
            }
            
            # ส่งข้อมูลก่อน
            response_info = requests.post(self.discord_webhook, json=payload_info)
            if response_info.status_code == 204:
                print("✅ ส่งข้อมูล Discord สำเร็จ")
            else:
                print(f"⚠️ ส่งข้อมูล Discord ล้มเหลว: {response_info.status_code}")
            
            # 2. ส่งไฟล์แยก
            with open(file_path, 'rb') as file:
                files = {'file': (filename, file, 'application/octet-stream')}
                
                payload_file = {
                    "content": "",
                    "username": self.bot_name
                }
                
                data = {"payload_json": json.dumps(payload_file)}
                
                response_file = requests.post(self.discord_webhook, files=files, data=data)
                
                if response_file.status_code == 200:
                    print("✅ อัปโหลดไฟล์ Discord สำเร็จ")
                    return True
                else:
                    print("❌ อัปโหลดไฟล์ Discord ล้มเหลว")
                    return False
                    
        except Exception as e:
            print(f"❌ ข้อผิดพลาด: {e}")
            return False
    
    def run(self):
        """เรียกใช้โปรแกรมหลัก"""
        self.print_header()
        
        # ตรวจสอบ environment variables
        if not self.token or not self.chat_id or not self.discord_webhook:
            print("❌ ข้อผิดพลาด: ไม่พบ environment variables")
            print("กรุณาตรวจสอบไฟล์ .env")
            return
        
        # 1. ดึงรายการไฟล์
        files = self.get_files()
        if not files:
            print("❌ ไม่พบไฟล์ในโฟลเดอร์ upload_files")
            return
        
        # 2. แสดงและเลือกไฟล์
        self.show_files(files)
        selected_indices = self.select_files(files)
        
        if not selected_indices:
            print("❌ ไม่ได้เลือกไฟล์")
            return
        
        # 3. เลือกแพลตฟอร์ม
        platform = self.select_platform()
        
        # 4. อัปโหลดไฟล์
        success = 0
        total = len(selected_indices)
        
        print(f"\n🚀 เริ่มอัปโหลด {total} ไฟล์...")
        print("─" * 40)
        
        for idx, i in enumerate(selected_indices):
            filename = files[i]
            file_path = os.path.join(self.current_dir, 'upload_files', filename)
            
            # แสดง progress bar
            self.show_progress(idx, total)
            
            print(f"\n📤 กำลังประมวลผล ({idx+1}/{total}): {filename}")
            print("─" * 30)
            
            # ตรวจสอบข้อมูล
            addon_info = self.get_addon_info(filename)
            
            # อัปโหลด
            uploaded = False
            
            if platform in ['1', '3']:  # Telegram
                if self.upload_to_telegram(file_path, addon_info):
                    uploaded = True
            
            if platform in ['2', '3']:  # Discord
                if self.upload_to_discord(file_path, addon_info):
                    uploaded = True
            
            if uploaded:
                success += 1
                print("✅ สำเร็จ!")
            else:
                print("❌ ล้มเหลว!")
            
            time.sleep(1)  # พักเล็กน้อย
        
        # แสดง progress bar สุดท้าย (100%)
        self.show_progress(total, total)
        
        # สรุปผล
        print(f"\n🎉 เสร็จสิ้น!")
        print("=" * 40)
        print(f"✅ สำเร็จ: {success}/{total} ไฟล์")
        
        if success < total:
            print(f"❌ ล้มเหลว: {total - success} ไฟล์")
        
        print("=" * 40)

# เรียกใช้โปรแกรม
if __name__ == "__main__":
    uploader = SimpleUploader()
    uploader.run()