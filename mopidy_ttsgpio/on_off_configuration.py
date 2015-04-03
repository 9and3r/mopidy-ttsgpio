

class OnOffConfiguration():
    def __init__(self, name):
        self.name = name
        self.value = False

    def __str__(self):
        if self.value:
            return self.name + " on"
        else:
            return self.name + " off"

    def set_value(self, new_value):
        self.value = new_value
