import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" target="_blank"', "props_to_html should generate correct HTML attributes")

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), '', "props_to_html should return an empty string for no attributes")

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello World", children=[], props={"class": "text-center"})
        expected_repr = ("HTMLNode(tag='p', value='Hello World', children=[], "
                         "props={'class': 'text-center'})")
        self.assertEqual(repr(node), expected_repr, "__repr__ should return a correct representation of the node")

    def test_repr_no_props(self):
        node = HTMLNode(tag="h1", value="Title")
        expected_repr = "HTMLNode(tag='h1', value='Title', children=[], props={})"
        self.assertEqual(repr(node), expected_repr, "__repr__ should handle missing props correctly")

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")

if __name__ == "__main__":
    unittest.main()

