Steps:
- Wi-Fi Connection: Replace your_SSID and your_PASSWORD with your Wi-Fi credentials.
- Telegram Bot: Replace your_BOT_TOKEN with your Telegram bot token and your_CHAT_ID with your chat ID.
- Rain Detection: If the sensor value is below the threshold (500 in this example), a message is sent to the Telegram bot.


Libraries Installation:
- Go to Tools -> Manage Libraries in Arduino IDE.
- Search for and install:
- ArduinoHttpClient
- WiFi (already included with ESP32 boards)


This will send a Telegram message when rain is detected instead of activating the buzzer.
