import unittest
from extracttitle import extract_title

class Test_ExtractTitle(unittest.TestCase):
    def test_extract_title_from_markdown(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello") 
    
    def test_extract_title_w_multiple_headings(self):
        md = "# Main Heading \n ## Another Heading"
        title = extract_title(md)
        self.assertEqual(title, "Main Heading")