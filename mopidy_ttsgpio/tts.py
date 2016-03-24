import os
from threading import Thread

music_level = 30


class TTS():

    def __init__(self, frontend, config):
        self.frontend = frontend

    def speak_text(self, text):
        t = Thread(target=self.speak_text_thread, args=(text,))
        t.start()

    def speak_text_thread(self, text):
        os.system(' echo "' + text + '" | festival --tts')
