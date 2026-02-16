import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_neq_with_props(self):
        node1 = HTMLNode(props={"prop1": "hello"})
        node2 = HTMLNode(props={"prop1": "there"})
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_neq_with_children(self):
        node1 = HTMLNode(children=["child1"])
        node2 = HTMLNode(children=["child2"])
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1.__repr__(), node2.__repr__())
        self.assertEqual(node1.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode(props={
            "prop1": "apple",
            "prop2": "banana",
            "prop3": "www.orange.com"
        })

        expected_html = ' prop1="apple" prop2="banana" prop3="www.orange.com"'
        self.assertEqual(node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()