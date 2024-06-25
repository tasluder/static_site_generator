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
        self.assertEqual(expected_test_result, tested_string)

    def test_regex_extraction(self):
        test_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        example_text = extract_markdown_images(test_text)
        expected_test_text = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(example_text, expected_test_text)
        test_link = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        example_link = extract_markdown_links(test_link)
        expected_test_link = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(example_link, expected_test_link)


if __name__ == "__main__":
    unittest.main()