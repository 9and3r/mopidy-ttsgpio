import logging
import traceback

from mopidy import core

import pykka

from .main_menu import MainMenu
from .tts import TTS

logger = logging.getLogger(__name__)


class TtsGpio(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super(TtsGpio, self).__init__()
        self.tts = TTS(self)
        self.menu = False
        self.backend = \
            pykka.ActorRegistry.get_by_class_name("TtsGpioBackend")[0]
        self.core = core
        self.main_menu = MainMenu(self)

        self.debug_gpio_simulate = config['ttsgpio']['debug_gpio_simulate']
        if self.debug_gpio_simulate:
            from .gpio_simulator import GpioSimulator
            self.simulator = GpioSimulator(self)
        else:
            from .gpio_input_manager import GPIOManager
            self.gpio_manager = GPIOManager(self, config['ttsgpio'])

    def track_playback_started(self, tl_track):
        self.speak_current_song(tl_track)

    def playback_state_changed(self, old_state, new_state):
        if self.debug_gpio_simulate:
            if new_state == core.PlaybackState.PLAYING:
                self.simulator.playing_led.select()
            else:
                self.simulator.playing_led.deselect()

    def input(self, input_event):
        try:
            if input_event['key'] == 'volume_up':
                if input_event['long']:
                    self.repeat()
                else:
                    current = self.core.playback.volume.get()
                    current += 10
                    self.backend.tell({'action': 'set_volume',
                                       'value': current})
            elif input_event['key'] == 'volume_down':
                if input_event['long']:
                    current = 0
                else:
                    current = self.core.playback.volume.get()
                    current -= 10
                self.backend.tell({'action': 'set_volume', 'value': current})
            elif input_event['key'] == 'main' and input_event['long'] \
                    and self.menu:
                self.exit_menu()
            else:
                if self.menu:
                    self.main_menu.input(input_event)
                else:
                    self.manage_input(input_event)

        except Exception:
            traceback.print_exc()

    def manage_input(self, input_event):
        if input_event['key'] == 'next':
            self.core.playback.next()
        elif input_event['key'] == 'previous':
            self.core.playback.previous()
        elif input_event['key'] == 'main':
            if input_event['long']:
                self.menu = True
                self.main_menu.reset()
            else:
                if self.core.playback.state.get() == \
                        core.PlaybackState.PLAYING:
                    self.core.playback.pause()
                else:
                    self.core.playback.play()

    def repeat(self):
        if self.menu:
            self.main_menu.repeat()
        else:
            self.speak_current_song(self.core.playback.current_tl_track.get())

    def speak_current_song(self, tl_track):
        if tl_track is not None:
            artists = ""
            for artist in tl_track.track.artists:
                artists += artist.name + ","
            self.tts.speak_text(tl_track.track.name + ' by ' + artists)

    def exit_menu(self):
        self.menu = False

    def playlists_loaded(self):
        self.main_menu.elements[0].reload_playlists()
        self.tts.speak_text("Playlists loaded")
