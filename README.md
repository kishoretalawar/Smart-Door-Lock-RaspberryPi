# IoT-Enabled RFID-Based Smart Door Lock System Using Raspberry Pi Zero 2W

## Project Overview

This project is an IoT-based smart door security system developed using the Raspberry Pi Zero 2W. The system authenticates users through RFID cards, controls a servo motor to lock or unlock the door, displays system status on a 16×2 I2C LCD, provides buzzer feedback, and sends Telegram notifications for authorized and unauthorized access attempts.

The project demonstrates the integration of embedded systems, IoT, hardware interfacing, and real-time security monitoring.

## Key Features

- RFID authentication
- Automatic door locking and unlocking
- Servo motor-based door mechanism
- Real-time Telegram notifications
- 16×2 LCD status display
- Buzzer indication
- Unauthorized access detection
- Raspberry Pi GPIO control
- Modular Python implementation

## Hardware Components

- Raspberry Pi Zero 2W
- MFRC522 RFID Reader
- SG90 Servo Motor
- 16×2 I2C LCD Display
- Active Buzzer
- Breadboard
- Jumper Wires
- 5V Power Supply

## Software Used

- Raspberry Pi OS
- Python
- Visual Studio Code
- GitHub

## Working Principle

1. System starts on Raspberry Pi.
2. LCD displays the welcome message.
3. RFID reader waits for a card.
4. Card ID is compared with authorized IDs.
5. If authorized:
   - Servo unlocks the door.
   - LCD displays "Access Granted".
   - Telegram notification is sent.
   - Door locks automatically after a delay.
6. If unauthorized:
   - LCD displays "Access Denied".
   - Buzzer sounds.
   - Telegram notification is sent.

## Applications

- Smart Homes
- Office Security
- Laboratory Access
- Hostel Rooms
- College Laboratories
- Industrial Access Control

## Future Improvements

- Face Recognition
- Fingerprint Authentication
- Mobile App Control
- Cloud Database
- Visitor Logging
- AI-based Intrusion Detection

## Author

Kishore Talawar

Electronics & Communication Engineering Student

Aspiring Embedded Systems & Semiconductor Engineer
