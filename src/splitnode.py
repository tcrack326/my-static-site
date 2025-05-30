from textnode import TextNode, TextType
from extractmdimglink import IMAGE_REGEX,LINK_REGEX,extract_markdown_links, extract_markdown_images
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        split_text = text.split(delimiter)
        for idx, elem in enumerate(split_text):
            if idx % 2 == 0:
                new_nodes.append(TextNode(elem, node.text_type if node.text_type != None else TextType.TEXT, url=node.url))
            else:
                new_nodes.append(TextNode(elem, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(node.text)
        split_text = list(filter(lambda t: len(t) > 0, re.split(IMAGE_REGEX, text)))
        for idx, txt in enumerate(split_text):
            if idx % 3 == 0:
                new_nodes.append(TextNode(txt, node.text_type if node.text_type != None else TextType.TEXT, url=node.url))
            elif idx % 2 == 0:
                image_idx = 0 if idx == 2 else idx - 3
                image_text, src = images[image_idx]
                new_nodes.append(TextNode(image_text, TextType.IMAGE, url=src))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(node.text)
        split_text = list(filter(lambda t: len(t) > 0, re.split(LINK_REGEX, text)))
        for idx, txt in enumerate(split_text):
            if idx % 3 == 0:
                new_nodes.append(TextNode(txt, node.text_type if node.text_type != None else TextType.TEXT, url=node.url))
                if len(links) > 0 and (idx < len(split_text) - 1):
                    link_idx = int(idx/3)
                    link_text, url = links[link_idx]
                    new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
    return new_nodes