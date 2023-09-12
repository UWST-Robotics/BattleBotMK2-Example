from machine import Pin
import utime

class ErrorLED: #Works with Raspbery Pi Pico W, will need to change what pin in other pi's
    errorCode = 0
    led = Pin("LED", Pin.OUT)
    
    def __init__(self):
        self.led.value(0)
    
    def __str__(self):
        return self.errorCode
    
    def setError(self, error: int):
        self.errorCode = error
        
    def error(self): #this should be called every cycle
        if(self.errorCode == 0):
            self.led.value(1)
            return
        
        #Error Handling
        print("ErrorCode: ", self.errorCode)
        for x in range(self.errorCode):
            self.led.value(0)
            utime.sleep_ms(300)
            self.led.value(1)
            utime.sleep_ms(300)
        self.led.value(0)
        utime.sleep_ms(1000)
            
        
            
        
    
