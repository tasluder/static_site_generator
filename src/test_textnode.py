import unittest

from textnode import *


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
    
    def test_delimiter(self):
        test_node = TextNode("This is text with a **bolded** word", "text")
        expected_test_result = [TextNode("This is text with a ", "text"), TextNode("bolded", "bold"), TextNode(" word", "text")]
        tested_string = split_nodes_delimiter([test_node], "**", text_type = "bold")
        print(tested_string)
        self.assertEqual(expected_test_result, tested_string)

if __name__ == "__main__":
    unittest.main()