import logging
import pykka
import traceback

from mopidy import core
from .tts import TTS

logger = logging.getLogger(__name__)


class TtsGpio(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(TtsGpio, self).__init__()
        self.tts = TTS()

    def track_playback_started(self, tl_track):
        try:
            self.tts.speak_text(tl_track.track.name + ' by ' + sorted(tl_track.track.artists)[0].name)
        except Exception:
            traceback.print_exc()