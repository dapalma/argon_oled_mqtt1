# Base image
FROM python:3.11-alpine

# Set environment
ENV LANG C.UTF-8

# Set working directory
WORKDIR /app

# Copy local files into container
COPY run.sh /run.sh
COPY oled_display.py /oled_display.py
COPY oled_mqtt_display.py /oled_mqtt_display.py
COPY config.yaml /config.yml
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Install Python dependencies
# If you have a requirements.txt, uncomment this:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Make your script executable
RUN chmod +x /run.sh

# Run your startup script
CMD [ "/run.sh" ]
