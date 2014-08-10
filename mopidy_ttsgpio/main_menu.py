

class MainMenu():
    def __init__(self, frontend):
        self.current = 0
        self.fronted = frontend
        self.elements = ['playlists', 'exit mopidy', 'shutdown', 'reset']

    def reset(self):
        self.current = 0
        self.say_current_element()

    def input(self, input_event):
        if input_event['key'] == 'down':
            self.change_current(1)
        elif input_event['key'] == 'up':
            self.change_current(-1)
        elif input_event['key'] == 'main':
            if input_event['long']:
                self.fronted.menu_back()

    def change_current(self, move):
        self.current += move
        if self.current < 0:
            self.current = len(self.elements) -1
        elif self.current >= len(self.elements):
            self.current = 0
        self.say_current_element()

    def say_current_element(self):
        self.fronted.tts.speak_text(self.elements[self.current])

