from textnode import TextNode
from htmlnode import *

def main():
    children_list = [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
    node = ParentNode("p", children_list)
    test_string = node.to_html()
    print(test_string)

main()