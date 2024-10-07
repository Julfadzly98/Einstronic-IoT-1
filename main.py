#include <WiFi.h>
#include <HTTPClient.h>

// Replace with your network credentials
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// Replace with your Telegram Bot Token and Chat ID
String botToken = "your_BOT_TOKEN";
String chatID = "your_CHAT_ID";

// Rain sensor and other configurations
const int rainSensorPin = 34; // Analog pin for rain sensor

// URL for sending a Telegram message
String serverName = "https://api.telegram.org/bot" + botToken + "/sendMessage";

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Initialize Wi-Fi connection
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up rain sensor pin
  pinMode(rainSensorPin, INPUT);
}

void loop() {
  // Read rain sensor value
  int sensorValue = analogRead(rainSensorPin);
  Serial.println("Rain Sensor Value: " + String(sensorValue));

  // Check if it's raining (adjust threshold as needed)
  if (sensorValue < 500) {
    Serial.println("Rain detected!");

    // Send message to Telegram
    sendTelegramMessage("Rain detected! Sensor Value: " + String(sensorValue));
    
    // Wait before sending another alert
    delay(60000); // Send alert once per minute
  }

  // Wait a bit before the next reading
  delay(1000);
}

// Function to send message to Telegram
void sendTelegramMessage(String message) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    String serverPath = serverName + "?chat_id=" + chatID + "&text=" + message;
    
    http.begin(serverPath.c_str());
    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      Serial.println("Message sent successfully!");
    } else {
      Serial.println("Error sending message.");
    }
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }
}
