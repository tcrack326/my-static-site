import unittest
from leafnode import LeafNode

class Test_LeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "a link", {"href": "www.test.tst", "class": "link"})
        self.assertEqual(node.to_html(), '<a href="www.test.tst" class="link">a link</a>')

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "inner text")
        self.assertEqual(node.to_html(), "<div>inner text</div>")