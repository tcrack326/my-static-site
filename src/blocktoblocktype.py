from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(md):
    if md[0] == '#':
        return BlockType.HEADING
    if md[0:3] == "```":
        return BlockType.CODE
    if md[0] == '>':
        return BlockType.QUOTE
    if len(re.findall("^\d\.\s", md)) > 0:
        return BlockType.ORDERED_LIST
    if md[0] == '-':
        return BlockType.UNORDERED_LIST
    
    return BlockType.PARAGRAPH