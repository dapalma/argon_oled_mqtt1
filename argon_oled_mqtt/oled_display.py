import time
import os
import board
import busio
import paho.mqtt.client as mqtt
from adafruit_ssd1306 import SSD1306_I2C

broker = os.environ.get("MQTT_BROKER", "localhost")
topic = os.environ.get("MQTT_TOPIC", "ha/pi/cpu_temp")

# Setup OLED display
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

value = "…waiting…"

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, msg):
    global value
    value = msg.payload.decode()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()

while True:
    oled.fill(0)
    oled.text("Home Assistant", 0, 0, 1)
    oled.text(f"Value: {value}", 0, 16, 1)
    oled.text(time.strftime("%H:%M:%S"), 0, 32, 1)
    oled.show()
    time.sleep(5)