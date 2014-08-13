import logging

logger = logging.getLogger(__name__)


class PlaylistMenu():

    def __init__(self, frontend):
        self.frontend = frontend
        self.playlists = None
        self.selected = None
        self.reload_playlists()

    def __str__(self):
        return "playlists"

    def speak_current(self):
        if self.selected < len(self.playlists):
            self.frontend.tts.speak_text(self.playlists[self.selected].name)
        else:
            self.frontend.tts.speak_text("No playlists found")

    def reload_playlists(self):
        self.playlists = []
        for playlist in self.frontend.core.playlists.playlists.get():
            self.playlists.append(playlist)
        self.selected = 0

    def reset(self):
        self.selected = 0
        self.speak_current()

    def change_current(self, change):
        self.selected += change
        if self.selected < 0:
            self.selected = len(self.playlists) - 1
        if self.selected >= len(self.playlists):
            self.selected = 0
        self.speak_current()

    def input(self, input_event):
        if input_event['key'] == 'previous':
            self.change_current(1)
        elif input_event['key'] == 'next':
            self.change_current(-1)
        elif input_event['key'] == 'main':
            core = self.frontend.core
            core.tracklist.clear()
            core.tracklist.add(uri=self.playlists[self.selected].uri)
            core.playback.play()
            self.frontend.exit_menu()

    def repeat(self):
        self.speak_current()
