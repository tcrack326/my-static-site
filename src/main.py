from textnode import TextNode, TextType
from copytopublic import copy_static_to_public
from generate_page import generate_pages_recursive
import sys

if __name__ == "__main__":
    print(f"{sys.argv}")
    basepath = '/' if len(sys.argv) > 1 else sys.argv[1]
    print(f"the basepath: {basepath}")
    copy_static_to_public()
    generate_pages_recursive('content', 'template.html', 'docs', basepath)

