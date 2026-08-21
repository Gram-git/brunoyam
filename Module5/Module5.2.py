import json


class Model:
    def save(self, filename):
        data = {}

        for attribute_name in dir(self):
            if attribute_name.startswith("_"):
                continue

            attribute_value = getattr(self, attribute_name)

            if not callable(attribute_value):
                data[attribute_name] = attribute_value

        with open(filename, "w") as file:
            json.dump(data, file)


class Post(Model):
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author


post = Post('title', 'text', 'autor')
post.save("post.json")
