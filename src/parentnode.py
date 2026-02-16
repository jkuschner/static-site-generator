from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError(f"Missing tag from ParentNode: {self}")
        if not self.children:
            raise ValueError(f"Missing children from ParentNode: {self}")

        html = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
            html += node.to_html()

        html += f"</{self.tag}>"
        return html
        