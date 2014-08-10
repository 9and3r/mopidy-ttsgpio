from Tkinter import *
from threading import Thread

class GpioSimulator():

    def __init__(self, frontend):
        self.frontend = frontend
        thread = Thread(target = self.initial_simulator)
        thread.start()




    def initial_simulator(self):
        root = Tk()
        root.title("GPIO Simulator")
        button = Button(root, text="Up", command=self.up)
        button2 = Button(root, text="Main button", command=self.main)
        button3 = Button(root, text="Down", command=self.down)
        button4 = Button(root, text="Vol +", command=self.vol_up)
        button5 = Button(root, text="Vol -", command=self.vol_down)
        button6 = Button(root, text="Main long", command=self.main_long)
        button.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        root.mainloop()

    def up(self):
        self.frontend.input({'key':'up', 'long': False})
    def main(self):
        self.frontend.input({'key':'main', 'long': False})
    def main_long(self):
        self.frontend.input({'key':'main', 'long': True})
    def down(self):
        self.frontend.input({'key':'down', 'long': False})
    def vol_up(self):
        self.frontend.input({'key':'volume_up', 'long': False})
    def vol_down(self):
        self.frontend.input({'key':'volume_down', 'long': False})