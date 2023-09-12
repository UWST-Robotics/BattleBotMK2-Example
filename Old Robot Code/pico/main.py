#Basic code for receiving serial connection

from machine import UART #importing PIN and PWM

#Defining UART channel and Baud Rate
uart= UART(0,9600)



#OUT1  and OUT2
mc1_in1=Pin(6,Pin.OUT)  #IN1`
mc1_in2=Pin(7,Pin.OUT)  #IN2
mc1_in3=Pin(4,Pin.OUT)  #IN3
mc1_in4=Pin(3,Pin.OUT)  #IN4


mc1_EN_A=PWM(Pin(8))
mc1_EN_B=PWM(Pin(2))
# Defining frequency for enable pins
mc1_EN_A.freq(1500)
mc1_EN_B.freq(1500)

# Setting maximum duty cycle for maximum speed (0 to 65025)
mc1_EN_A.duty_u16(65025)
mc1_EN_B.duty_u16(65025)

def abs(num: int):
    if num < 0:
        num = num * -1
    return num

def drivetrain(x: int, y: int):
    print(f"{x} | {y}")
    x_speed = float(abs(x))/100 * 65025
    y_speed = float(abs(y))/100 * 65025
    
    
    mc1_EN_A.duty_u16(int(x_speed)) #Setting Duty Cycle
    mc1_EN_B.duty_u16(int(x_speed)) #Setting Duty Cycle
    
    if x > 0:
        mc1_in1.high()
        mc1_in2.low()
        mc1_in3.high()
        mc1_in4.low()
        
    
    


while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        #print(data)

        # Decodes data and splits string into a list
        data = data.decode("ASCII").split(",")
        
        #Spliting array into variables and typecasting to an int
        x = int(data[0])
        y = int(data[1])
        a = int(data[2])
        b = int(data[3])
        rt = int(data[4])
        lt = int(data[5])
        
        #print(f" {x} | {y} | {a} | {b} | {rt} | {lt} | ")
        drivetrain(x, y)
      
        
        