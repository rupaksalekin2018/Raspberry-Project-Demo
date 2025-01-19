import Adafruit_DHT
import RPi.GPIO as GPIO
import smbus
import time
import csv
import logging

# Sensor and pin configurations
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin for DHT sensor

SOIL_MOISTURE_PIN = 17  # GPIO pin for soil moisture sensor
LDR_PIN = 27  # GPIO pin for LDR sensor
BUZZER_PIN = 22  # GPIO pin for buzzer

# I2C LCD Address (if using LCD display)
I2C_ADDR = 0x27
bus = smbus.SMBus(1)

# Thresholds
TEMP_THRESHOLD = 30  # Celsius
HUM_THRESHOLD = 40   # Percent
SOIL_MOISTURE_THRESHOLD = 300  # ADC value
LIGHT_THRESHOLD = 500  # ADC value

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Setup logging
logging.basicConfig(filename="plant_monitor_log.csv", level=logging.INFO, format="%(asctime)s,%(message)s")

# Function to read temperature and humidity from DHT sensor
def read_dht():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 2), round(humidity, 2)
    else:
        return None, None

# Function to read soil moisture level
def read_soil_moisture():
    return GPIO.input(SOIL_MOISTURE_PIN)

# Function to read light intensity (simulated analog value using resistor divider)
def read_light_intensity():
    return GPIO.input(LDR_PIN)

# Function to trigger buzzer
def alert():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Function to log data
def log_data(temp, hum, soil, light):
    with open("plant_monitor_log.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temp, hum, soil, light])
    logging.info(f"{temp},{hum},{soil},{light}")

# Function to display data on I2C LCD (optional)
def lcd_display(text):
    bus.write_byte_data(I2C_ADDR, 0x80, 0x01)  # Clear display
    for char in text:
        bus.write_byte_data(I2C_ADDR, 0x40, ord(char))

# Main monitoring loop
def monitor():
    try:
        while True:
            temp, hum = read_dht()
            soil = read_soil_moisture()
            light = read_light_intensity()

            # Check thresholds and trigger alerts if needed
            if temp and (temp > TEMP_THRESHOLD or hum < HUM_THRESHOLD or soil == 0 or light == 0):
                print("Warning: Threshold Exceeded!")
                alert()

            # Log data
            print(f"Temp: {temp}C, Hum: {hum}%, Soil: {'Dry' if soil == 0 else 'Wet'}, Light: {'Low' if light == 0 else 'Good'}")
            log_data(temp, hum, soil, light)

            # Optional LCD Display
            lcd_display(f"T:{temp}C H:{hum}% S:{'Dry' if soil == 0 else 'Wet'} L:{'Low' if light == 0 else 'Good'}")

            time.sleep(10)  # Sleep for 10 seconds before next reading

    except KeyboardInterrupt:
        print("Monitoring Stopped")
        GPIO.cleanup()

# Run the monitoring system
if __name__ == "__main__":
    monitor()
