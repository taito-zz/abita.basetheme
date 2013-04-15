import unittest


class PloneSiteViewTestCase(unittest.TestCase):

    def test_subclass(self):
        from Products.Five import BrowserView
        from abita.basetheme.browser.template import PloneSiteView
        self.assertTrue(issubclass(PloneSiteView, BrowserView))
