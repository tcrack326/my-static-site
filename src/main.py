from textnode import TextNode, TextType
from copytopublic import copy_static_to_public
from generate_page import generate_pages_recursive

if __name__ == "__main__":
    copy_static_to_public()
    generate_pages_recursive('content', 'template.html', 'public')

