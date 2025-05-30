from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type, BlockType
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text2html import text_node_to_html_node
from textnode import TextNode, TextType
import re

def get_html_tag_from_block_type(blocktype,  heading_count):
    if blocktype == BlockType.PARAGRAPH:
        return 'p'
    if blocktype == BlockType.CODE:
        return 'pre'
    if blocktype == BlockType.HEADING:
        return f"h{heading_count}"
    if blocktype == BlockType.ORDERED_LIST:
        return 'ol'
    if blocktype == BlockType.UNORDERED_LIST:
        return 'ul'
    if blocktype == BlockType.QUOTE:
        return 'blockquote'

def get_heading_count(md):
    return len(md.split('#'))-1

def strip_space(text):
    return " ".join(text.split()).strip()

def text_to_children(text):
    stripped_text = strip_space(text)
    text_nodes = text_to_textnodes(stripped_text)
    html_nodes = list(map(lambda t: text_node_to_html_node(t), text_nodes))
    return html_nodes

def code_block_to_children(block):
    stripped_text = ''.join(block.split("```")[1]).lstrip().replace('  ', '')
    text_node = TextNode(stripped_text, TextType.CODE)
    return text_node_to_html_node(text_node)

def unordered_list_block_to_html(block):
    #print(f"DEBUG LISTS: {block}")
    lines = list(map(lambda l: f"{l.replace('- ', '<li>')}</li>", block.split('\n')))
    block = ''.join(lines)
    #print(f"DEBUG LIST BLOCK {block}")
    return block

def ordered_list_block_to_html(block):
    #print(f"DEBUG LISTS: {block}")
    block = re.sub(r"\d+\.\s", '<li>', block)
    #print(f"DEBUG OL LiST: {block}")
    lines = list(map(lambda l: f"{l}</li>", block.split('\n')))
    block = ''.join(lines)
    #print(f"DEBUG LIST BLOCK {block}")
    return block

def map_block_to_html_nodes(block):
    block_type = block_to_block_type(block)
    tag = get_html_tag_from_block_type(block_type, get_heading_count(block))
    # if heading remove hashtags
    if block_type == BlockType.HEADING:
       block = block.replace('#', '')
    if block_type == BlockType.UNORDERED_LIST:
       block = unordered_list_block_to_html(block)
    if block_type == BlockType.ORDERED_LIST:
        block = ordered_list_block_to_html(block)
    if block_type == BlockType.QUOTE:
        block = block.replace('> ', '')
    children = text_to_children(block) if block_type != BlockType.CODE else [code_block_to_children(block)]
    parentNode = ParentNode(tag, children=children)
    return parentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    return ParentNode("div", children=list(map(lambda b: map_block_to_html_nodes(b), blocks)))