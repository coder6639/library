import json


class Library:
    def __init__(self):
        try:
            with open("booklibrary.json", "r") as f:
                self.allitems = json.load(f)
        except FileNotFoundError:
            self.allitems = []

    def all(self):
        return self.allitems

    def get(self, id):
        return self.allitems[id - 1]

    def create(self, data):
        data.pop("csrf_token")
        self.allitems.append(data)

    def save_all(self):
        with open("booklibrary.json", "w") as f:
            json.dump(self.allitems, f)

    def update(self, id, data):
        data.pop("csrf_token")
        self.allitems[id - 1] = data
        self.save_all()


bookstore = Library()
