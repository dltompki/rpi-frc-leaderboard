import adafruit_character_lcd.character_lcd as charlcd
import digitalio
import board
from time import sleep

# LCD Config
lcd_columns = 16
lcd_rows = 2

# Pin setup
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

# Init lcd
lcd = charlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Clear lcd before writing
lcd.clear()

message = ''
while True:
    if len(message) > 33 :
        message = ''
        lcd.clear()
        continue

    if len(message) == 16 :
        message += '\n'

    message += '|'

    lcd.message = message

    sleep(0.5)