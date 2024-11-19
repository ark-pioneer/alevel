from heading1 import Heading1
from image import Image
from paragraph import Paragraph

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

# The following will cause an error until you've 
# implemented the AnchorLink class, created new the method, and imported it properly
anchor_link = AnchorLink("Click here for German Shepherds!")
anchor_link.add_attribute("href", "https://www.instagram/nova.withers")
paragraph2 = Paragraph("German Shepherds are a well known breed of dog: fluffy, smart, and loyal!")
paragraph2.add_attribute("id", "para2")
elements.append(anchor_link)
elements.append(paragraph2)

build_html(elements)