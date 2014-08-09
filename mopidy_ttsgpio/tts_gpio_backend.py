import pykka
from mopidy import backend


class TtsGpioBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(TtsGpioBackend, self).__init__()
        self.audio = audio

    def on_receive(self, message):
        action = message['action']
        if action == 'set_volume':
            self.audio.set_volume(message['value'])
