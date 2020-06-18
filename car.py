import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

def forward():
    init()
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, True) 
    GPIO.output(24, False)
    time.sleep(5)
    GPIO.cleanup()

def reverse():
    init()
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, False) 
    GPIO.output(24, True)
    time.sleep(5)
    GPIO.cleanup()
def right():
    init()
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, True) 
    GPIO.output(24, False)
    time.sleep(5)
    GPIO.cleanup()
def left():
    init()
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, False) 
    GPIO.output(24, True)
    time.sleep(5)
    GPIO.cleanup()
if __name__ == "__main__":
    while(True):
        print("Forward: 'F'\nReverse: 'B'\nRight:'r'\nLeft:'L'\nExit:'q'\n")
        secim = input("Enter:")
        if secim == 'F' or secim == 'f':
            forward()
        elif secim == 'B' or secim == 'b':
            reverse()
        elif secim == 'R' or secim == 'r':
            right()
        elif secim == 'L' or secim == 'l':
            left()
        elif secim == 'Q' or secim == 'q':
            break
    print("Exiting Program...")
