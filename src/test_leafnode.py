import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "test link", props={"href": "https://test.com", "bold": "true"})
        expected_html = '<a href="https://test.com" bold="true">test link</a>'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()