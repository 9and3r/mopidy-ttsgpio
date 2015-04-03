import urllib

import gst

music_level = 30


class TTS():

    def __init__(self, frontend, config):
        self.frontend = frontend
        self.player = gst.element_factory_make("playbin", "tts")
        output = gst.parse_bin_from_description(config['audio']['output'],
                                                                     ghost_unconnected_pads=True)
        self.player.set_property('audio-sink', output)

    def speak_text(self, text):
        self.player.set_state(gst.STATE_NULL)
        self.player.set_property('volume', 2)
        params = {}
        params['tl'] = 'en'
        params['q'] = text.encode('ascii', 'ignore')
        music_stream_uri = 'http://translate.google.com/translate_tts?' \
                           + urllib.urlencode(params)
        self.player.set_property('uri', music_stream_uri)
        self.player.set_state(gst.STATE_PLAYING)

        bus = self.player.get_bus()
        bus.enable_sync_message_emission()
        bus.add_signal_watch()
        # bus.connect('message::eos', self.end_of_stream)


