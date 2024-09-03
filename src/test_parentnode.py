import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_children(self):
        node = ParentNode("p", [])  # Creating ParentNode with no children
        with self.assertRaises(TypeError) as context:
            node.to_html()  # Ensure to_html is called
        self.assertEqual(str(context.exception), "ParentNode must have at least one child")

    def test_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode(None, "Text")])
        self.assertEqual(str(context.exception), "A tag must be provided for ParentNode")

    def test_children_is_none(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", None)
        self.assertEqual(str(context.exception), "Children cannot be None for ParentNode")

    def test_children_is_not_list(self):
        with self.assertRaises(TypeError) as context:
            ParentNode("p", "invalid")
        self.assertEqual(str(context.exception), "Children must be provided as a list")

    def test_valid_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_parent_nodes(self):
        nested_node = ParentNode(
            "div",
            [
                ParentNode("span", [LeafNode(None, "Nested text")]),
                LeafNode("b", "Bold text"),
            ]
        )
        self.assertEqual(nested_node.to_html(), "<div><span>Nested text</span><b>Bold text</b></div>")

if __name__ == '__main__':
    unittest.main()

