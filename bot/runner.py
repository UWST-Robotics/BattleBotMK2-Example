#Imports for Classes
import imports.secrets as secrets
import imports.ErrorLED as ErrorLED
import imports.Servo as Servo
from imports.funct import abs

from machine import Pin, PWM
import network
import socket
#import utime
#Network Stuff
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)





#ErrorLED Initialization
errorLED = ErrorLED.ErrorLED()
#Servo Initialization
servo = Servo.Servo(pin_id=16)


#Init Error Codes
if(not wlan.isconnected()):     errorLED.setError(1)



#Socket Initialization, for udp communication
UDP_IP = "10.10.20.200" #ip address
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
try:
    sock.bind((UDP_IP, UDP_PORT))
except OSError:
    errorLED.setError(2)



#Binds pins for motor control
mc1_in1=Pin(21, Pin.OUT)  #IN1
mc1_in2=Pin(22, Pin.OUT)  #IN2
mc1_in3=Pin(26, Pin.OUT)  #IN3
mc1_in4=Pin(27,Pin.OUT)  #IN4
mc1_EN_A=PWM(Pin(20))    #ENA
mc1_EN_B=PWM(Pin(28))    #ENB


if(errorLED.errorCode > 0): # Will Go into Fatal Error Mode and only run error handling code
    while True:
        errorLED.error()



def drivetrain(x :int, y : int):
    pass



print("No Errors")
while True: # If no init errors, then run main loop
    errorLED.error()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode("ASCII").split(",")

    x = int(data[0])
    y = int(data[1])
    rt = int(data[2])
    lt = int(data[3])
    print(
f"""received message: [
x {x}
y {y}
rt {rt}
lt {lt}
]"""
)
    
    #Servo Logic
    if(lt > 5): servo.write(135); #utime.sleep_ms(200) #Lower Ramp
    if(rt > 5): servo.write(100);   #utime.sleep_ms(200) #Raise Ramp

    drivetrain(x, y) #Runs drive train depending on x and y value



"""
for position in reversed(range(0, 180)):  # Step the position reverse from 180deg to 0deg
        print(position)  # Show the current position in the Shell/Plotter
        servo.write(position)  # Set the Servo to the current position
"""
