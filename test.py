import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Settings
button = 18 #GPIO Pin with button connected
lights = [24, 25] # GPIO Pins with LED's conneted


        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(lights, GPIO.OUT)
        GPIO.output(lights, GPIO.LOW)


while True:
  if (0 == GPIO.input(18)):
 #   print("Button Pressed")
 #   GPIO.output(lights, GPIO.LOW)
          for x in range(0, 3):
                   time.sleep(.2)
                   GPIO.output(25, GPIO.HIGH)
                   time.sleep(.2)
                   GPIO.output(lights, GPIO.LOW)

