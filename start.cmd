@echo off
echo 🔄 Updating config from .env...

REM อ่านไฟล์ .env และสร้าง config.js
python -c "
import os
env_data = {}
if os.path.exists('.env'):
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_data[key.strip()] = value.strip()

config_content = f'''// การตั้งค่าจาก .env
const CONFIG = {{
    TELEGRAM_TOKEN: \'{env_data.get(\"TELEGRAM_TOKEN\", \"\")}\',
    TELEGRAM_CHAT_ID: \'{env_data.get(\"TELEGRAM_CHAT_ID\", \"\")}\',
    DISCORD_WEBHOOK_URL: \'{env_data.get(\"DISCORD_WEBHOOK_URL\", \"\")}\',
    BOT_NAME: \'{env_data.get(\"BOT_NAME\", \"BOT-ZX\")}\',
    BOT_VERSION: \'{env_data.get(\"BOT_VERSION\", \"4.0\")}\'
}};'''

with open('config.js', 'w', encoding='utf-8') as f:
    f.write(config_content)

print('✅ อัปเดต config.js สำเร็จ!')
print(f'📱 Telegram: {\"✅ พร้อมใช้งาน\" if env_data.get(\"TELEGRAM_TOKEN\") else \"❌ ไม่พบ Token\"}')
print(f'📢 Discord: {\"✅ พร้อมใช้งาน\" if env_data.get(\"DISCORD_WEBHOOK_URL\") else \"❌ ไม่พบ Webhook\"}')
print(f'🤖 Bot Name: {env_data.get(\"BOT_NAME\", \"BOT-ZX\")}')
"

echo.
echo 🚀 Starting Web Uploader...
start "" "web.html"
echo ✅ Opened in browser!
pause