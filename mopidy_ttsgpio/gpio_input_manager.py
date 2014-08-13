import logging
import time

import RPi.GPIO as GPIO

logger = logging.getLogger(__name__)
longpress_time = 0.3


class GPIOManager():

    def __init__(self, frontend, pins):

        self.frontend = frontend

        # Variables to control if it is a longpress
        self.down_time_previous = 0
        self.down_time_next = 0
        self.down_time_main = 0
        self.down_time_vol_up = 0
        self.down_time_vol_down = 0

        # GPIO Mode
        GPIO.setmode(GPIO.BCM)

        # Next Button
        GPIO.setup(pins['pin_button_next'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
        GPIO.add_event_detect(pins['pin_button_vol_down'], GPIO.BOTH,
                              callback=self.vol_down, bouncetime=30)

        # Main Button
        GPIO.setup(pins['pin_button_main'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['pin_button_main'], GPIO.BOTH,
                              callback=self.main, bouncetime=30)

    def previous(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_previous + longpress_time > time.time():
                self.frontend.input({'key': 'previous', 'long': False})
            else:
                self.frontend.input({'key': 'previous', 'long': True})
        else:
            self.down_time_previous = time.time()

    def next(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_next + longpress_time > time.time():
                self.frontend.input({'key': 'next', 'long': False})
            else:
                self.frontend.input({'key': 'next', 'long': True})
        else:
            self.down_time_next = time.time()

    def main(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_main + longpress_time > time.time():
                self.frontend.input({'key': 'main', 'long': False})
            else:
                self.frontend.input({'key': 'main', 'long': True})
        else:
            self.down_time_main = time.time()

    def vol_up(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_vol_up + longpress_time > time.time():
                self.frontend.input({'key': 'volume_up', 'long': False})
            else:
                self.frontend.input({'key': 'volume_up', 'long': True})
        else:
            self.down_time_vol_up = time.time()

    def vol_down(self, channel):
        if GPIO.input(channel) == 1:
            if self.down_time_vol_down + longpress_time > time.time():
                self.frontend.input({'key': 'volume_down', 'long': False})
            else:
                self.frontend.input({'key': 'volume_down', 'long': True})
        else:
            self.down_time_vol_down = time.time()
