@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo 🔄 Updating config from .env...

rem Default values
set "TELEGRAM_TOKEN="
set "TELEGRAM_CHAT_ID="
set "DISCORD_WEBHOOK_URL="
set "BOT_NAME=BOT-ZX"
set "BOT_VERSION=4.0"

if exist ".env" (
  for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    set "k=%%A"
    set "v=%%B"
    if defined k if not "!k:~0,1!"=="#" if not "!k!"=="" (
      set "!k!=!v!"
    )
  )
)

> "config.js" (
  echo // การตั้งค่าจาก .env
  echo const CONFIG = {
  echo     TELEGRAM_TOKEN: '!TELEGRAM_TOKEN!',
  echo     TELEGRAM_CHAT_ID: '!TELEGRAM_CHAT_ID!',
  echo     DISCORD_WEBHOOK_URL: '!DISCORD_WEBHOOK_URL!',
  echo     BOT_NAME: '!BOT_NAME!',
  echo     BOT_VERSION: '!BOT_VERSION!'
  echo };
)

echo ✅ อัปเดต config.js สำเร็จ!
if defined TELEGRAM_TOKEN (echo 📱 Telegram: ✅ พร้อมใช้งาน) else (echo 📱 Telegram: ❌ ไม่พบ Token)
if defined DISCORD_WEBHOOK_URL (echo 📢 Discord: ✅ พร้อมใช้งาน) else (echo 📢 Discord: ❌ ไม่พบ Webhook)
echo 🤖 Bot Name: !BOT_NAME!

echo.
echo 🚀 Starting Web Uploader...
start "" "%~dp0web.html"
echo ✅ Opened in browser!
pause