import time

longpress_time = 0.3
try:
    import RPi.GPIO as GPIO
except ImportError:
    print "Could not import GPIO"


class GPIOManager():

    def __init__(self):

        # Set the pins you are using
        pins = {}
        pins['pin_button_next'] = 22
        pins['pin_button_previous'] = 23
        pins['pin_button_vol_up'] = 24
        pins['pin_button_vol_down'] = 25
        pins['pin_button_main'] = 17

        # Variables to control if it is a longpress
        self.down_time_previous = 0
        self.down_time_next = 0
        self.down_time_main = 0
        self.down_time_vol_up = 0
        self.down_time_vol_down = 0

        try:
            # GPIO Mode
            GPIO.setmode(GPIO.BCM)

            # Next Button
            GPIO.setup(pins['pin_button_next'], GPIO.IN,
                       pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['pin_button_next'],
                                  GPIO.BOTH, callback=self.next, bouncetime=30)

            # Previous Button
            GPIO.setup(pins['pin_button_previous'], GPIO.IN,
                       pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['pin_button_previous'], GPIO.BOTH,
                                  callback=self.previous, bouncetime=30)

            # Volume Up Button
            GPIO.setup(pins['pin_button_vol_up'], GPIO.IN,
                       pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['pin_button_vol_up'], GPIO.BOTH,
                                  callback=self.vol_up, bouncetime=30)

            # Volume Down Button
            GPIO.setup(pins['pin_button_vol_down'], GPIO.IN,
                       pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['pin_button_vol_down'],
                                  GPIO.BOTH, callback=self.vol_down,
                                  bouncetime=30)

            # Main Button
            GPIO.setup(pins['pin_button_main'], GPIO.IN,
                       pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['pin_button_main'],
                                  GPIO.BOTH, callback=self.main, bouncetime=30)

            self.correctlyLoaded = True

        except RuntimeError:
            print "TTSGPIO: Not enough permission "

    def previous(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_previous + longpress_time > time.time():
                print "Previous button released: Short press"
            else:
                print "Previous button released: Long press"
        else:
            print "Previous button pressed"

    def next(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_next + longpress_time > time.time():
                print "Next button released: Short press"
            else:
                print "Next button released: Long press"
        else:
            print "Next button pressed"

    def main(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_main + longpress_time > time.time():
                print "Main button released: Short press"
            else:
                print "Main button released: Long press"
        else:
            print "Main button pressed"

    def vol_up(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_vol_up + longpress_time > time.time():
                print "Vol+ button released: Short press"
            else:
                print "Vol+ button released: Long press"
        else:
            print "Vol+ button pressed"

    def vol_down(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_vol_down + longpress_time > time.time():
                print "Vol- button released: Short press"
            else:
                print "Vol+ button pressed"
        else:
            self.down_time_vol_down = time.time()

GPIOManager()
