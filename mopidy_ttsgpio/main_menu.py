import os
import socket

import mopidy

from .playlist_menu import PlaylistMenu


class MainMenu():
    def __init__(self, frontend):
        self.current = 0
        self.fronted = frontend
        self.main_menu = False
        self.elements = [PlaylistMenu(frontend), 'exit mopidy']
        self.elements.append('shutdown')
        self.elements.append('reboot')
        self.elements.append('check ip')

    def reset(self):
        self.current = 0
        self.say_current_element()
        self.main_menu = True

    def input(self, input_event):
        if self.main_menu:
            if input_event['key'] == 'next':
                self.change_current(1)
            elif input_event['key'] == 'previous':
                self.change_current(-1)
            elif input_event['key'] == 'main':
                if isinstance(self.elements[self.current], str):
                    self.item_selected(self.elements[self.current])
                else:
                    self.main_menu = False
                    self.elements[self.current].reset()
        else:
            self.elements[self.current].input(input_event)

    def item_selected(self, item):
        if item == 'exit mopidy':
            mopidy.utils.process.exit_process()
        elif item == 'shutdown':
            os.system("shutdown now -h")
        elif item == 'reboot':
            os.system("shutdown -r now")
        elif item == 'check ip':
            self.check_ip()

    def change_current(self, move):
        self.current += move
        if self.current < 0:
            self.current = len(self.elements) - 1
        elif self.current >= len(self.elements):
            self.current = 0
        self.say_current_element()

    def say_current_element(self):
        self.fronted.tts.speak_text(str(self.elements[self.current]))

    def repeat(self):
        if self.main_menu:
            self.say_current_element()
        else:
            self.elements[self.current].repeat()

    def check_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            self.fronted.tts.speak_text("Your IP is: " + ip)
        except socket.error:
            s.close()
            self.fronted.tts.speak_text("No internet connection found")
