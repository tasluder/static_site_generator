import re

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        ):
            return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # text_type must match one of the possible text_types
    # text_type_text = "text"
    # text_type_bold = "bold"
    # text_type_italic = "italic"
    # text_type_code = "code"
    # text_type_link = "link"
    # text_type_image = "image"

    new_nodes = []
    
    for node in old_nodes:
        if node.text_type == "text":
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Unmatched delimiter in text")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, "text"))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for match in matches:
                description, url = match
                parts = remaining_text.split(f"![{description}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], "text"))
                new_nodes.append(TextNode(description, "image", url))
                remaining_text = parts[1]
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, "text"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for match in matches:
                description, url = match
                parts = remaining_text.split(f"[{description}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], "text"))
                new_nodes.append(TextNode(description, "link", url))
                remaining_text = parts[1]
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, "text"))
    return new_nodes