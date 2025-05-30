from htmlnode import HTMLNode
VALUE_ERROR_MESAGE = "A Leaf Node value must be provided"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError(VALUE_ERROR_MESAGE)
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError(VALUE_ERROR_MESAGE)
        if self.tag == None:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        