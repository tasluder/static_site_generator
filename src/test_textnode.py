import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "url1")
        node2 = TextNode("This is a text node", "bold", "url1")
        self.assertEqual(node, node2)
        node3 = TextNode("text node this is", "bold", "url2")
        node4 = TextNode("text node this is", "bold", "url2")
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", "bold", None)
        node6 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()