import os
from threading import Thread
import time
import subprocess

music_level = 30


class TTS():
	def __init__(self):
		self.t = Thread(target=self.speak_text_thread)
		self.t.start()

	def speak_text(self, text):
		s='(SayText "{0}")\n'.format(text)
		self.p.stdin.write(s)

	def speak_text_thread(self):
		self.p = subprocess.Popen('/usr/bin/festival --pipe'.split(),stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		while 1:
			time.sleep(1)
