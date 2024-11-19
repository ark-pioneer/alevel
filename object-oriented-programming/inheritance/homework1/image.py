class Image():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<img src='" + self.data + "'/>"