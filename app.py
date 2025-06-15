from flask import Flask, request
import requests
import json
import config

app = Flask(__name__)

@app.route(f"/{config.SECRET_PATH}", methods=["POST"])
def webhook():
    data = request.get_json()

    ip = request.remote_addr
    headers = dict(request.headers)
    text = json.dumps(data, indent=2)

    message = f"🚨 ВХОД НА БОЧКУМЕДА\nIP: {ip}\nHeaders: {headers.get('User-Agent')}\n\nPayload:\n{text[:1000]}"

    requests.get(f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage", params={
        "chat_id": config.YOUR_CHAT_ID,
        "text": message
    })

    return "OK", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)