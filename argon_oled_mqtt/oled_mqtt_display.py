import paho.mqtt.client as mqtt
import yaml
import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# Load config.yaml
with open("/config.yaml", "r") as file:
    config = yaml.safe_load(file)

MQTT_BROKER = config["mqtt"]["broker"]
MQTT_PORT = config["mqtt"].get("port", 1883)
MQTT_TOPIC = config["mqtt"]["topic"]
MQTT_USER = config["mqtt"].get("username")
MQTT_PASS = config["mqtt"].get("password")

# Setup OLED (SSD1306, 128x64 assumed)
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Optional: load custom font
font = ImageFont.load_default()

def display_text(message):
    with canvas(device) as draw:
        draw.text((0, 20), message, font=font, fill=255)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with code", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"Received: {payload}")
    display_text(payload[:20])  # Truncate if too long

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# Stay alive
while True:
    time.sleep(1)
