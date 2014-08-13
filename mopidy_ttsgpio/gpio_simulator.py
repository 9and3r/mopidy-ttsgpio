from Tkinter import Button, Checkbutton, DISABLED, Tk
from threading import Thread


class GpioSimulator():
    def __init__(self, frontend):
        self.frontend = frontend
        self.playing_led = None
        thread = Thread(target=self.initial_simulator)
        thread.start()

    def initial_simulator(self):
        root = Tk()
        root.title("GPIO Simulator")
        previous = Button(root, text="Previous", command=self.previous)
        main = Button(root, text="Main button", command=self.main)
        next = Button(root, text="Next", command=self.next)
        vol_up = Button(root, text="Vol +", command=self.vol_up)
        vol_up_long = Button(root, text="Vol + long", command=self.vol_up_long)
        vol_down = Button(root, text="Vol -", command=self.vol_down)
        vol_down_long = Button(root, text="Vol - long",
                               command=self.vol_down_long)
        main_long = Button(root, text="Main long", command=self.main_long)
        self.playing_led = Checkbutton(text="playing_led", state=DISABLED)

        vol_up.grid(row=0, column=1)
        vol_up_long.grid(row=0, column=2)
        previous.grid(row=1, column=0)
        main.grid(row=1, column=1)
        main_long.grid(row=1, column=2)
        next.grid(row=1, column=3)
        vol_down.grid(row=2, column=1)
        vol_down_long.grid(row=2, column=2)
        self.playing_led.grid(row=3, column=1)

        root.mainloop()

    def previous(self):
        self.frontend.input({'key': 'previous', 'long': False})

    def main(self):
        self.frontend.input({'key': 'main', 'long': False})

    def main_long(self):
        self.frontend.input({'key': 'main', 'long': True})

    def next(self):
        self.frontend.input({'key': 'next', 'long': False})

    def vol_up(self):
        self.frontend.input({'key': 'volume_up', 'long': False})

    def vol_down(self):
        self.frontend.input({'key': 'volume_down', 'long': False})

    def vol_down_long(self):
        self.frontend.input({'key': 'volume_down', 'long': True})

    def vol_up_long(self):
        self.frontend.input({'key': 'volume_up', 'long': True})
