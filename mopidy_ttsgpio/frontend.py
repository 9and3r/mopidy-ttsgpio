import logging
import pykka
import traceback
from mopidy import core
import mopidy
from .tts import TTS
from .main_menu import MainMenu


logger = logging.getLogger(__name__)


class TtsGpio(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(TtsGpio, self).__init__()
        self.tts = TTS()
        self.menu = False
        self.backend = \
            pykka.ActorRegistry.get_by_class_name("TtsGpioBackend")[0]
        self.core = core
        self.main_menu = MainMenu(self)
        from .gpio_simulator import GpioSimulator
        GpioSimulator(self)

    def track_playback_started(self, tl_track):
        try:
            self.tts.speak_text(tl_track.track.name + ' by ' + sorted(tl_track.track.artists)[0].name)
        except Exception:
            traceback.print_exc()

    def input(self, input_event):
        if input_event['key'] == 'volume_up':
            current = self.core.playback.volume.get()
            current += 10
            self.backend.tell({'action':'set_volume', 'value':current})
        elif input_event['key'] == 'volume_down':
            current = self.core.playback.volume.get()
            current -= 10
            self.backend.tell({'action':'set_volume', 'value':current})
        elif self.menu:
            self.main_menu.input(input_event)
        else:
            if input_event['long'] and input_event['key'] == 'main':
                self.menu = True
                self.main_menu.reset()
            else:
                if input_event['key'] == 'down':
                    self.core.playback.next()
                elif input_event['key'] == 'up':
                    self.core.playback.previous()
                elif input_event['key'] == 'main':
                    if self.core.playback.state.get() == mopidy.core.PlaybackState.PLAYING:
                        self.core.playback.pause()
                    else:
                        self.core.playback.play()

    def menu_back(self):
        self.menu = False


