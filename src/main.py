from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello, World!", TextType.PLAIN)
    node2 = TextNode("This is italic text.", TextType.ITALIC)
    node3 = TextNode("This is bold text.", TextType.BOLD)
    node4 = TextNode("This is code.", TextType.CODE)
    node5 = TextNode("This is a link.", TextType.LINK, url="https://example.com")
    node6 = TextNode("This is an image.", TextType.IMAGE, url="https://example.com/image.png")

    print(node1)
    print(node2)
    print(node3)
    print(node4)
    print(node5)
    print(node6)

main()