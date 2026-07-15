import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from gpiozero import Servo
from time import sleep
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BOT_TOKEN = "  "        
CHAT_ID = "  "

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        print("Telegram error")

reader = SimpleMFRC522()

AUTHORIZED_CARDS = {
    977741555344: "Kishore",
    220192189987: "Admin"
}

lcd = CharLCD('PCF8574',0x27)

BUZZER = 18
GPIO.setup(BUZZER,GPIO.OUT)

ROOM_LED = 21
GPIO.setup(ROOM_LED,GPIO.OUT)

IR_SENSOR = 16
GPIO.setup(IR_SENSOR,GPIO.IN)

servo_lock = Servo(17)
servo_door = Servo(27)

rows = [5,6,13,19]
cols = [12,20,26]

keys = [
['1','2','3'],
['4','5','6'],
['7','8','9'],
['*','0','#']
]

for r in rows:
    GPIO.setup(r,GPIO.OUT)
    GPIO.output(r,0)


for c in cols:
    GPIO.setup(c,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

PASSWORD = "1234"
entered = ""

def beep(times=1):

    for i in range(times):
        GPIO.output(BUZZER,1)
        sleep(0.2)
        GPIO.output(BUZZER,0)
        sleep(0.1)

def open_door():

    lcd.clear()
    lcd.write_string("Unlocking...")

    servo_lock.value = -1
    sleep(2)

    lcd.clear()
    lcd.write_string("Door Opening")

    servo_door.value = -1
    sleep(3)

    lcd.clear()
    lcd.write_string("Door Open")

    sleep(10)

    lcd.clear()
    lcd.write_string("Closing Door")

    servo_door.value = 1
    sleep(3)

    lcd.clear()
    lcd.write_string("Locking")

    servo_lock.value = 1
    sleep(2)

    send_telegram("Door opened and closed")

def read_keypad():

    for i in range(4):

        GPIO.output(rows[i],1)

        for j in range(3):

            if GPIO.input(cols[j]) == 1:

                key = keys[i][j]

                sleep(0.3)

                GPIO.output(rows[i],0)

                return key

        GPIO.output(rows[i],0)

    return None

lcd.clear()
lcd.write_string("SMART DOOR")
sleep(2)

lcd.clear()
lcd.write_string("Scan Card or")
lcd.cursor_pos=(1,0)
lcd.write_string("Enter Password")

print("System Ready")

try:

    while True:

        try:

            card_id = None

            try:
                card_id, text = reader.read_no_block()
            except:
                pass

            if card_id is not None:

                print("Card:", card_id)

                if card_id in AUTHORIZED_CARDS:

                    name = AUTHORIZED_CARDS[card_id]

                    lcd.clear()
                    lcd.write_string("Access Granted")
                    lcd.cursor_pos = (1,0)
                    lcd.write_string(name)

                    beep(2)

                    send_telegram(f"Access Granted\nUser: {name}")

                    open_door()

                else:

                    lcd.clear()
                    lcd.write_string("Access Denied")

                    beep(4)

                    send_telegram(f"Unauthorized card\nID:{card_id}")

                    sleep(2)

                lcd.clear()
                lcd.write_string("Scan Card or")
                lcd.cursor_pos = (1,0)
                lcd.write_string("Enter Password")

                sleep(1)

        except Exception as e:
            print("RFID error:", e)

        key = read_keypad()

        key = read_keypad()

        if key:

            print("Key:",key)

            if key == "#":

                if entered == PASSWORD:

                    lcd.clear()
                    lcd.write_string("Password OK")

                    beep(2)

                    send_telegram("Door opened using keypad")

                    open_door()

                else:

                    lcd.clear()
                    lcd.write_string("Wrong Password")

                    beep(4)

                    send_telegram("Wrong password attempt")

                    sleep(2)

                entered = ""

                lcd.clear()
                lcd.write_string("Scan Card or")
                lcd.cursor_pos=(1,0)
                lcd.write_string("Enter Password")

            elif key == "*":

                entered = ""

            else:

                entered += key

        if GPIO.input(IR_SENSOR) == 0:
            GPIO.output(ROOM_LED,1)
        else:
            GPIO.output(ROOM_LED,0)

        sleep(0.1)

except KeyboardInterrupt:

    print("System stopped")
    lcd.clear()
    GPIO.cleanup()
