# Inheritance: Homework 1

### Instructions
1. Extract shared behaviour to a parent class.
2. Extend program 
    - all elements should support a add_attribute() method
        - method has two parameters: attribute name, and value.
    - attributes should appear as pairs in the opening html tag like below:
    - eg: `paragraph.add_attribute("id", "main_paragraph")` should store these values on the instance using `self`
    - when `to_html()` is called, it would look like this: `<p id='main_paragraph'>some text</p>`

### Stretch
1. Add support for a <div> element.
2. Add support for nesting elements within elements.
eg: 
```html
<div id="main"><h1>My Great Homework!</h1></div>
```

