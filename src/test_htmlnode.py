import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", value="some value", children=None, props=None)
        self.assertEqual(node.props_to_html(),"")

    def test_simple_html_node(self):
        node = HTMLNode("p", value="tHIS IS A P TAG", children=None, props={"class": "Test"})
        self.assertEqual(node.props_to_html(), ' class="Test"')
    
    def test_multipe_props(self):
        node = HTMLNode("a", value="somelink.com", children=None, props={"class": "Link", "href": "www.testing.tst"})
        self.assertEqual(node.props_to_html(), ' class="Link" href="www.testing.tst"')
