import os
import requests

UNLOCK_DATA = "3A65636829900601#5A593232465235474A48006D6F746F726F6C0000#74778B86398747D368C1BC33C6162A2CDBDB1924C6A70C54E10B7AE28A2A9236#FCC157AC000000000000000000000000"
TELEGRAM_TOKEN = "8991871207:AAE0vrd6Qzjhe1yc8Z0eWYytG27WJ1j0YFA"
TELEGRAM_CHAT_ID = "48270932"

URL = "https://en-us.support.motorola.com/app/standalone/bootloader/unlock-your-device-b"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print(f"[!] Telegram send error: {e}")

def check_portal():
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if "Technical Difficulties" in response.text or "ORACLE" in response.text:
            print("[~] Portal is STILL DOWN (Oracle/Technical Error).")
        else:
            print("[!] SUCCESS: Motorola Portal is BACK ONLINE!")
            payload = {"unlock_data": UNLOCK_DATA}
            submit_res = requests.post(URL, data=payload, headers=headers)
            
            msg = f"🎉 **خبر خوش! پورتال موتورولا باز شد!**\n\nدرخواست آنلاک با موفقیت ارسال شد.\n\nپاسخ سرور:\n`{submit_res.text[:300]}`"
            send_telegram(msg)
            print("[+] Data Submitted & Telegram Notification Sent!")
    except Exception as e:
        print(f"[!] Network error: {e}")

if __name__ == "__main__":
    check_portal()
