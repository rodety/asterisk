import lcddriver
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()


import time
 
 
# Create library object using our Bus I2C port
import os
import subprocess
import time
from time import sleep
#from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import PIPE, Popen
display = lcddriver.lcd()

display.lcd_clear()

# display text on LCD display \n = new line
try:
    display.lcd_display_string("Bienvenido",1)
    display.lcd_display_string("MAXTEL PERU",2)
    sleep(5)
    while True:
        display.lcd_clear()
        display.lcd_display_string("Asterisk PBX",1)
        display.lcd_display_string("maxtelperu.com",2)

        sleep(4)
        display.lcd_clear()

        CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2)) 
        #display.lcd_display_string results
        display.lcd_display_string("CPU Usage = " + CPU_Pct,1)
        
        sleep(4)
        display.lcd_clear()

        IP = str(os.popen('hostname -I').readline())
        display.lcd_display_string('Direccion IP es:',1)
        display.lcd_display_string(IP,2)

        sleep(4)
        display.lcd_clear()

        display.lcd_display_string('Estado conexion',1)
        sleep(1)
        display.lcd_clear()
        status = str(os.popen('tail -1 /var/log/asterisk/cdr-csv/Master.csv').readline())
        tam = len(status)

        display.lcd_display_string(status[tam-36:tam-20],1)
        display.lcd_display_string(status[tam-20:tam],2)

        sleep(4)
        encoder = '192.168.1.15'
        antenaRx = '192.168.1.21'
        antenaTx = '192.168.1.20'
        contador = 0
                



       
        for m in range(0,10):
            child = Popen(['ping', '192.168.1.15'], stdin = PIPE, stdout = PIPE, stderr = PIPE)
            time.sleep(1)
            child.terminate()
            x = child.stdout.read()
            display.lcd_clear()

            if(len(x) == 113 or len(x) == 0):
                display.lcd_display_string('ATA GrandStream',1)
                display.lcd_display_string('Desconectado',2)

            else:
                display.lcd_display_string('ATA Conectado',1)
                display.lcd_display_string(x[len(x)-15:len(x)],2)

                contador = contador +1
        sleep(2)
       # display.lcd_clear()
       # display.lcd_display_string x
except KeyboardInterrupt:
    display.lcd_display_string("Borrando",1)
    display.lcd_clear()
