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
    
delimiters = {
    '**' : 'bold',
    '*' : 'italic',
    '`' : 'code',
    '![' : 'image',
    '[' : 'link'
}

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

def text_to_textnodes(text):
    new_nodes = []
    while text:
        next_delimiter = None
        next_index = len(text)
        for delim in delimiters:
            index = text.find(delim)
            if 0 <= index < next_index:
                next_delimiter = delim
                next_index = index
        if next_delimiter is None:
            new_nodes.append(TextNode(text, "text"))
            break
        if next_index > 0:
            new_nodes.append(TextNode(text[:next_index], "text"))
        if next_delimiter in delimiters:
            text = text[next_index + len(next_delimiter):]
            end_index = text.find(next_delimiter)
            if end_index != -1:
                content = text[:end_index]
                text = text[end_index + len(next_delimiter):]
                if next_delimiter == '**':
                    new_nodes.append(TextNode(content, delimiters["**"]))
                elif next_delimiter == '*':
                    new_nodes.append(TextNode(content, delimiters["*"]))
                elif next_delimiter == '`':
                    new_nodes.append(TextNode(content, delimiters["`"]))
                elif next_delimiter == '![':
                    end_image_index = text.find(')')
                    url = text[:end_image_index]
                    text = text[end_image_index + 1:]
                    new_nodes.append(TextNode(content, delimiters["!["], url))
                elif next_delimiter == '[':
                    end_link_index = text.find(')')
                    url = text[:end_link_index]
                    text = text[end_link_index + 1:]
                    new_nodes.append(TextNode(content, delimiters["["], url))
        if next_delimiter is None:
            break
    return new_nodes