from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        if tag == None or children == None:
            raise ValueError("A Parent node must have both a tag and children values")
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("A Parent node must have a tag")
        if self.children == None:
            raise ValueError("A Parent node must have children")
        return f'<{self.tag}>{''.join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>'