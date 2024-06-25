class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        opening_tag = f"{self.tag}{self.props_to_html()}"
        children_html = "".join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return opening_tag + children_html + closing_tag


#text node to html node function to implement for all classes
def text_node_to_html_node(text_node):
    text_type_to_html = {
        "text": lambda node: LeafNode("", node['value']),
        "bold": lambda node: LeafNode("b", node['value']),
        "italic": lambda node: LeafNode("i", node['value']),
        "code": lambda node: LeafNode("code", node['value']),
        "link": lambda node: LeafNode("a", node['anchor'], props={'href':node['href']}),
        "image": lambda node: LeafNode("img", "", props = {'src': node['src'], 'alt': node['alt']}),
    }

    text_type = text_node['type']
    
    if text_type in text_type_to_html:
        return text_type_to_html[text_type](text_node)
    
    raise Exception("Unsupported TextNode type: " + text_type)
