import re

IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text):
    img_matches = re.findall(IMAGE_REGEX, text)
    return img_matches

def extract_markdown_links(text):
    link_matches = re.findall(LINK_REGEX, text)
    return link_matches