import requests
import time
import random

# Node-RED 的 HTTP Server URL
NODE_RED_URL = "http://192.168.76.131:1880/recieve_light_data"

def send_light_intensity(value):
    # 資料用 JSON 傳過去
    payload = {
        "light": value
    }
    response = requests.post(NODE_RED_URL, json=payload)
    print(f"Sent value: {value} lux, Response: {response.status_code}")

if __name__ == "__main__":
    while True:
        light_intensity = random.randint(0, 100)  # 隨機模擬 0~100 的光強度
        send_light_intensity(light_intensity)
        time.sleep(5)  # 每 5 秒送一筆