import RPi.GPIO as GPIO
import time
import sys
import datetime
import mailtext

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def IRread():
    
    GPIO.setup(40,GPIO.OUT)
    GPIO.output(40,0)
    
    GPIO.setup(8,GPIO.IN)
    
    if(GPIO.input(8) == True):
        print("...........IR reading...........")
        GPIO.output(40,1)
        mailtext.send_mail()
        time.sleep(4)
        GPIO.output(40,0)
        sys.exit()
    
def USonicRead():
    pin_trigger = 16
    pin_echo = 18

    GPIO.setup(pin_trigger,GPIO.OUT)
    GPIO.setup(pin_echo,GPIO.IN)

    GPIO.output(pin_trigger,1)  
    time.sleep(0.1)  # 1ms
    GPIO.output(pin_trigger,0)  

    start = time.time()
    stop = time.time()
    
    while GPIO.input(pin_echo) == 0:
        start = time.time()


    while GPIO.input(pin_echo) == 1:
        stop = time.time()

    timedifference = stop - start
    distance = ( timedifference * 34300 )/2  #distance = time*speed

    return distance

def main():
    try:
        while 1:
            dist = USonicRead()
            
            print("[+] Measured distance > % 1f cm\n" %dist, end='', file=open('/home/pi/IOT_py/output_file/file.txt','a'))
            #file = open('/home/pi/IOT_py/output_file/file.txt','a')
            #file.write("-----------" + str(datetime.time()) + "----------")
           
            #file.write("[+] Measured distance > % 1f cm \n" %dist)
            
            
            if dist <= 5.00 :
                    last_reading = dist
                    print("The Pit might be FULL\n")
                    print("[+] Last Value > % 1f cm" %last_reading)
                    
                    print("..Moving to IR sensor..")
                    time.sleep(1)
                    
                    IRread()
                    print("-------------------------------", end='', file=open('/home/pi/IOT_py/output_file/file.txt','a'))
            
                    
        file.close()
        return dist                   
                    
    except KeyboardInterrupt:
        print("[-] Measurement Stopped Forcefully")
        GPIO.cleanup()
    
if __name__ == '__main__':
    main()
    

