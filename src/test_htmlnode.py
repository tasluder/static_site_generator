import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_text(self):
        text_node = {'type': 'text', 'value': 'Hello'}
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.tag, '')
        self.assertEqual(result.value, 'Hello')
    
    def test_bold(self):
        bold_node = {'type': 'bold', 'value': 'bold hello'}
        result = text_node_to_html_node(bold_node)
        self.assertEqual(result.tag, 'b')
        self.assertEqual(result.value, 'bold hello')
    
    def test_italic(self):
        italic_node = {'type': 'italic', 'value': 'italic hello'}
        result = text_node_to_html_node(italic_node)
        self.assertEqual(result.tag, 'i')
        self.assertEqual(result.value, 'italic hello')
    
    def test_code(self):
        code_node = {'type': 'code', 'value': 'code hello'}
        result = text_node_to_html_node(code_node)
        self.assertEqual(result.tag, 'code')
        self.assertEqual(result.value, 'code hello')

    def test_link(self):
        link_node = {'type': 'link', 'anchor': 'click hello', 'href': 'http://test.com'}
        result = text_node_to_html_node(link_node)
        self.assertEqual(result.tag, 'a')
        self.assertEqual(result.value, 'click hello')
        self.assertEqual(result.props['href'], "http://test.com")
    
    def test_image(self):
        image_node = {'type': 'image', 'src': 'http://image.com/i.png', 'alt': 'example img'}
        result = text_node_to_html_node(image_node)
        self.assertEqual(result.tag, 'img')
        self.assertEqual(result.props['src'], 'http://image.com/i.png')
        self.assertEqual(result.props['alt'], 'example img')

if __name__ == "__main__":
    unittest.main()