import adafruit_character_lcd.character_lcd as charlcd
import digitalio
import board
from time import sleep
import frc_api as frc

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

challenge = 0

challenges = {
    1: 'GS',
    2: 'AN',
    3: 'HD',
    4: 'IA',
    5: 'PP',
}

while True:
    # Clear lcd before writing
    lcd.clear()

    line1 = frc.getRank() + ' | ' + frc.getTeamNumber() + ' | ' + frc.getOverall() + '\n'
    
    # increment the challenge variable, but keep it between 1 and 5
    challenge += 1
    if challenge > 5:
        challenge = 1

    functionName = 'get' + challenges[challenge]
    func = getattr(frc, functionName)
    line2 = challenges[challenge] + ': ' + func()

    lcd.message = line1 + line2

    sleep(2)