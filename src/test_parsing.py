import unittest

from textnode import TextNode, TextType 
from parsing import split_nodes_delimiter

class TestParsing(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN)
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_italic_split_with_delimiter_on_ends(self):
        node = TextNode("*I am italic.* No I'm not, but I am *again.*", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_nodes = [
            TextNode("I am italic.", TextType.ITALIC),
            TextNode(" No I'm not, but I am ", TextType.PLAIN),
            TextNode("again.", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_bold_split_with_multiple_input_nodes(self):
        nodes = [
            TextNode("This is **Node 1** out of **3 total nodes.**", TextType.PLAIN),
            TextNode("Here is **Node 2** out of **3 total nodes.", TextType.PLAIN),
            TextNode("Finally, the **last node** out of **3 total nodes.**", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("Node 1", TextType.BOLD),
            TextNode(" out of ", TextType.PLAIN),
            TextNode("3 total nodes.", TextType.BOLD),
            TextNode("Here is ", TextType.PLAIN),
            TextNode("Node 2", TextType.BOLD),
            TextNode(" out of ", TextType.PLAIN),
            TextNode("3 total nodes.", TextType.BOLD),
            TextNode("Finally, the ", TextType.PLAIN),
            TextNode("last node", TextType.BOLD),
            TextNode(" out of ", TextType.PLAIN),
            TextNode("3 total nodes.", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()