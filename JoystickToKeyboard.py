import uinput
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#red=left, pin 11
LEFT_PIN = 11
#orange=right, pin 8
RIGHT_PIN = 8
#yellow=up, gpio pin 24
UP_PIN = 24
#green=down, pin 23
DOWN_PIN = 23
#black=gnd
FIRE_PIN = 7

GPIO.setup(FIRE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#while GPIO.input(7) == GPIO.HIGH:
#	time.sleep(.02)

events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0) )

device = uinput.Device(events)

fire = False
up = False
down = False
left = False
right = False

while True:
  if not fire and not GPIO.input(FIRE_PIN):
    fire = True
    device.emit(uinput.BTN_JOYSTICK, 1)
    print('firing')
  if fire and GPIO.input(FIRE_PIN):
    fire = False
    device.emit(uinput.BTN_JOYSTICK, 0)
    print('done firing')

  if not up and not GPIO.input(UP_PIN):
    up = True
    device.emit(uinput.ABS_Y,0)
    print('up')
  if up and GPIO.input(UP_PIN):
    up = False
    device.emit(uinput.ABS_Y,128)
    print('up done')

  if not down and not GPIO.input(DOWN_PIN):
    down = True
    device.emit(uinput.ABS_Y,255)
    print('down')
  if down and GPIO.input(DOWN_PIN):
    down = False
    device.emit(uinput.ABS_Y,128)
    print('down done')

  if not left and not GPIO.input(LEFT_PIN):
    left = True
    device.emit(uinput.ABS_X, 0)
    print('left')
  if left and GPIO.input(LEFT_PIN):
    left = False
    device.emit(uinput.ABS_X,128)
    print('left done')

  if not right and not GPIO.input(RIGHT_PIN):
    right = True
    device.emit(uinput.ABS_X, 255)
    print('right')
  if right and GPIO.input(RIGHT_PIN):
    right = False
    device.emit(uinput.ABS_X, 128)
    print('right done')

  time.sleep(.02)
