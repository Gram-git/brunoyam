class StringVar:
    def __init__(self, value=""):
        self.value = value

    def set(self, new_value):
        self.value = new_value

    def get(self):
        return self.value


text = StringVar("I'm")

print(text.get())

text.set("back")

print(text.get())
