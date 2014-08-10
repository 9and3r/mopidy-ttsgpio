import RPi.GPIO as GPIO
import logging

logger = logging.getLogger(__name__)


class GPIOManager():
    def __init__(self, pins):
        GPIO.setmode(GPIO.BCM)

        # Next Button
        GPIO.setup(pins['nex'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['next'], GPIO.BOTH, callback=left,
                              bouncetime=30)

        # Previous Button
        GPIO.setup(pins['previous'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['previous'], GPIO.BOTH, callback=right,
                              bouncetime=30)

        # Volume Up Button
        GPIO.setup(pins['up'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['up'], GPIO.BOTH, callback=up,
                              bouncetime=30)

        # Volume Down Button
        GPIO.setup(pins['down'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['down'], GPIO.BOTH, callback=right,
                              bouncetime=30)

        # Main Button
        GPIO.setup(pins['main'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pins['man'], GPIO.BOTH, callback=right,
                              bouncetime=30)


def right(channel):
    dict = {}
    if GPIO.input(channel) == 1:
        type = pygame.KEYUP
    else:
        type = pygame.KEYDOWN
    dict['key'] = pygame.K_RIGHT
    event = pygame.event.Event(type, dict)
    pygame.event.post(event)


def left(channel):
    dict = {}
    if GPIO.input(channel) == 1:
        type = pygame.KEYUP
    else:
        type = pygame.KEYDOWN
    dict['key'] = pygame.K_RIGHT
    event = pygame.event.Event(type, dict)
    pygame.event.post(event)


def down(channel):
    dict = {}
    if GPIO.input(channel) == 1:
        type = pygame.KEYUP
    else:
        type = pygame.KEYDOWN
    dict['key'] = pygame.K_DOWN
    event = pygame.event.Event(type, dict)
    pygame.event.post(event)


def up(channel):
    dict = {}
    if GPIO.input(channel) == 1:
        type = pygame.KEYUP
    else:
        type = pygame.KEYDOWN
    dict['key'] = pygame.K_UP
    event = pygame.event.Event(type, dict)
    pygame.event.post(event)


def enter(channel):
    dict = {}
    if GPIO.input(channel) == 1:
        type = pygame.KEYUP
    else:
        type = pygame.KEYDOWN
    dict['key'] = pygame.K_RETURN
    event = pygame.event.Event(type, dict)
    pygame.event.post(event)



