class Paragraph():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<p>" + self.data + "</p>"
        
class Heading1():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<h1>" + self.data + "</h1>"

class Image():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<img src='" + self.data + "'/>"

def build_html(elements):
    html = ""

    for element in elements:
        html += element.to_html()
    
    print(html)

elements = [
    Heading1("Canine Friends"),
    Paragraph("Dogs are the best! They are lovely animals that some people treat as an additional family member"),
    Image("https://images.squarespace-cdn.com/content/v1/5baffc59fb182025fee90fef/92442d27-b354-4240-b998-bcbe0f1cd91c/German-shepherd-training-main.jpg")
]

build_html(elements)