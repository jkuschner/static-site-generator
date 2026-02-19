from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            blocks = node.text.split(delimiter)
            tmp_new_nodes = []
            useType = False
            for block in blocks:
                if block == "":
                    useType = not useType
                    continue
                if useType:
                    tmp_new_nodes.append(TextNode(block, text_type))
                else:
                    tmp_new_nodes.append(TextNode(block, TextType.PLAIN))
                useType = not useType
            new_nodes.extend(tmp_new_nodes)
    return new_nodes