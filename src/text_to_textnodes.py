from textnode import TextNode, TextType
from splitnode import split_nodes_link, split_nodes_delimiter, split_nodes_image
def text_to_textnodes(text):
    first_node = TextNode(text, text_type=TextType.TEXT)
    return split_nodes_image(split_nodes_link(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([first_node],'`', TextType.CODE),'_', TextType.ITALIC),'**', TextType.BOLD)))