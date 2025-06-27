FROM ghcr.io/home-assistant/amd64-base-debian:bookworm

RUN apt-get update && \
    apt-get install -y python3 python3-pip i2c-tools && \
    pip3 install paho-mqtt adafruit-circuitpython-ssd1306

COPY run.sh /run.sh
COPY oled_display.py /oled_display.py

CMD [ "/run.sh" ]