class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""
        if self.props == None:
            return html_string
        for key,value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string

    def __repr__(self):
        return f"Node: {self.tag}, Value: {self.value}, Children: {', '.join([] if self.children == None else self.children)}, Props: {str(self.props)}"
