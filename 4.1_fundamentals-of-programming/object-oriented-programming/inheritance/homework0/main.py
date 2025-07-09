class Element():
    def __init__(self, data):
        self.data = data

    def add_attribute(self, name, value):
        self.name = name
        self.value = value

class Heading1(Element):
    def to_html(self):
        return "<h1>" + self.data + "</h1>"

class Image(Element):
    def to_html(self):
        return "<img src='" + self.data + "'/>"

class Paragraph(Element):
    def to_html(self):
        opening_tag = "<p " + self.name + "='" + self.value + "'" + ">"
        return opening_tag + self.data + "</p>"

class AnchorLink(Element):
    def to_html(self):
        opening_tag = "<a " + self.name + "='" + self.value + "'" + ">"
        return opening_tag + self.data + "</a>"
       
def build_html(elements):
    html = ""
    for element in elements:
        html += element.to_html()
    return html

elements = [
    Heading1("Canine Friends"),
    Image("https://images.squarespace-cdn.com/content/v1/5baffc59fb182025fee90fef/92442d27-b354-4240-b998-bcbe0f1cd91c/German-shepherd-training-main.jpg")
]

# The following line will cause an error until you've 
# implemented the AnchorLink class, created new the method, and imported it properly
anchor_link = AnchorLink("Click here for German Shepherds!")
# The following will cause an error until you've 
# implemented the AnchorLink class, created new the method, and imported it properly
anchor_link.add_attribute("href", "https://www.instagram/nova.withers")
paragraph2 = Paragraph("German Shepherds are a well known breed of dog: fluffy, smart, and loyal!")
paragraph2.add_attribute("class", "para2")
# The following will cause an error until you've 
# implemented the AnchorLink class, created new the method, and imported it properly
elements.append(anchor_link)
elements.append(paragraph2)

with open("nova.html", "w") as f:
    html = build_html(elements)  
    f.write(html)
    