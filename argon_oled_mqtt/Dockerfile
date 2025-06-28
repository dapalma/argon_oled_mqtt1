FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libopenjp2-7-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY oled_mqtt_display.py .
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
