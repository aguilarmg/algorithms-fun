class Item():
    def __init__(self, value, size):
        self.value = value
        self.size = size

    def __str__(self):
        return f"Value: {self.value}, Size: {self.size}"
