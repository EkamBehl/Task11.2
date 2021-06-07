#import all the python libraries to run the project 
import RPi.GPIO as GPIO
from time import sleep #to turn off the LED,buzzer for some time
import requests   #to send the info to the IFTTT
from gpiozero import Buzzer
GPIO.setwarnings(False)
from gpiozero import MotionSensor

#Initialises the raspberry Pi mode
GPIO.setmode(GPIO.BCM)
buzzerIn =3    #sets the buzzer pin to GPIO 3
LED = 23       #sets the LED output pin to GPIO 23

pir =14     #Sets the pir sensor pin to 14
GPIO.setup(pir,GPIO.IN)        #sets the pir pin as input
GPIO.setup(LED, GPIO.OUT)      #sets the LED pin as output
GPIO.setup(buzzerIn,GPIO.OUT)          #sets the buzzerPin as output



#heps set time period for the buzzer to buzz
#Also works for using any Buzzer/LEDS which just have a positive and negative end
def buzzerbuzzing(times,pin):
    GPIO.output(pin,GPIO.HIGH)
    sleep(times)                #Keeps the output as High for times "seconds"
    GPIO.output(pin,GPIO.LOW)
    sleep(times)                #Keeps the output as LOW for times "seconds"

# inifinite loop to check the motion always
while True:
        
   
    if GPIO.input(pir)==1:    #returns 0 or 1 for motion not detected and detected respectively
        print("Motion detected")
        buzzerbuzzing(3,LED)                  #Turns LED on for 3 seconds
        buzzerbuzzing(3,buzzerIn)           # Turns Buzzer On for three seconds          ( needs to be set to 10000 for actual use)
           
        r = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/"ENTER YOUR KEY"', params={"value1":"none","value2":"none","value3":"none"})    #sends request to the IFTTT i.e. sends the event for further use 
		
        
    if not GPIO.input(pir):         #PRINTS MOTION NOT ON IF THE GPIO.input(pir ) doesn't return anything
        print("Motion not on")
        GPIO.output(buzzerIn, GPIO.LOW)
        sleep(1)
        
        
    
GPIO.cleanup()   #STOPS THE GPIO
