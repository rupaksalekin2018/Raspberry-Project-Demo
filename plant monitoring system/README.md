# Plant Monitoring System for Raspberry Pi 5

## Overview

The **Plant Monitoring System** is a comprehensive solution for tracking environmental conditions of plants using a Raspberry Pi 5. This system employs multiple sensors to measure temperature, humidity, soil moisture, and light intensity, ensuring optimal plant health. It also provides alert notifications and logs data for further analysis.

## Features

- **Environmental Monitoring**: Tracks temperature, humidity, soil moisture, and light levels.
- **Automated Alerts**: Triggers alerts when thresholds are exceeded.
- **Data Logging**: Stores sensor data in a CSV file for analysis.
- **Real-time Display**: Supports optional LCD display for instant readings.
- **Easy Setup**: Simple configuration and installation on Raspberry Pi 5.

## Hardware Requirements

To set up the Plant Monitoring System, the following components are required:

1. **Raspberry Pi 5**
2. **DHT22 Temperature & Humidity Sensor**
3. **Soil Moisture Sensor**
4. **LDR (Light Dependent Resistor) Sensor**
5. **16x2 LCD Display (Optional, I2C or GPIO)**
6. **Buzzer (Optional)**
7. **Jumper Wires and Resistors**

## Circuit Diagram

| Component          | GPIO Pin  |
|-------------------|-----------|
| DHT22 Sensor      | GPIO 4     |
| Soil Moisture     | GPIO 17    |
| LDR Sensor        | GPIO 27    |
| Buzzer            | GPIO 22    |
| LCD Display (SDA) | GPIO 2     |
| LCD Display (SCL) | GPIO 3     |

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/plant-monitoring-system.git
cd plant-monitoring-system
```

### Step 2: Install Dependencies
```bash
pip install Adafruit_DHT RPi.GPIO smbus
```

### Step 3: Run the Monitoring Script
```bash
python3 plant_monitoring_system.py
```

## Configuration

Adjust the threshold values in the script to customize alerts:

```python
TEMP_THRESHOLD = 30  # Celsius
HUM_THRESHOLD = 40   # Percent
SOIL_MOISTURE_THRESHOLD = 300  # ADC value
LIGHT_THRESHOLD = 500  # ADC value
```

## Data Logging

The system logs data to `plant_monitor_log.csv` in the following format:

```
Timestamp, Temperature, Humidity, Soil Moisture, Light Level
```

## How It Works

1. The system collects sensor readings every 10 seconds.
2. If any parameter exceeds the defined thresholds, an alert is triggered.
3. The data is stored for review and analysis.
4. Optionally, readings can be displayed on an LCD.

## Stopping the Program

To stop the monitoring system safely, press `CTRL+C`.

## Troubleshooting

- Ensure correct sensor wiring and connections.
- Verify that required dependencies are installed.
- Run the script with `sudo` if encountering permission issues.

## Future Enhancements

- Cloud integration for remote data access.
- Mobile app notifications.
- Additional sensor support (e.g., CO2, pH levels).


