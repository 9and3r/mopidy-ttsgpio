import urllib

import gst

music_level = 30


class TTS():

    def __init__(self, frontend):
        self.frontend = frontend
        self.player = gst.element_factory_make("playbin", "player")
        self.last_volume = 0
        self.volume_restored = True

    def set_low_volume(self):
        if self.volume_restored:
            self.volume_restored = False
            self.last_volume = self.frontend.core.playback.volume.get()
            if self.last_volume > music_level:
                self.frontend.backend.tell({'action': 'set_volume',
                                            'value': music_level})

    def set_last_volume(self):
        self.frontend.backend.tell({'action': 'set_volume',
                                    'value': self.last_volume})
        self.volume_restored = True

    def speak_text(self, text):
        self.player.set_state(gst.STATE_NULL)
        self.set_low_volume()
        params = {}
        params['tl'] = 'en'
        params['q'] = text.encode('ascii', 'ignore')
        music_stream_uri = 'http://translate.google.com/translate_tts?' \
                           + urllib.urlencode(params)
        self.player.set_property('uri', music_stream_uri)
        self.player.set_property('volume', 3)
        self.player.set_state(gst.STATE_PLAYING)

        bus = self.player.get_bus()
        bus.enable_sync_message_emission()
        bus.add_signal_watch()
        bus.connect('message::eos', self.end_of_stream)

    def end_of_stream(self, a, b):
        self.set_last_volume()
