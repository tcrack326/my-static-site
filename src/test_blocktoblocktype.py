import unittest
from blocktoblocktype import block_to_block_type, BlockType
class Test_BlockToBlockType(unittest.TestCase):
    def test_blocktoblocktype_paragraph(self):
        md = 'This is a paragraph'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_heading(self):
        md = '# This is a heading'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_code(self):
        md = '```This is some code```'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_quote(self):
        md = '>This is a quote'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_unordered_list(self):
        md = '- This is an unordered - list'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        md = '1. this is one 2. this is two'
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)