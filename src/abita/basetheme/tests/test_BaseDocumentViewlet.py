import unittest


class BaseDocumentViewletTestCase(unittest.TestCase):
    """TestCase for BaseDocumentViewlet"""

    def test_subclass(self):
        from plone.app.layout.viewlets.common import ViewletBase
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        self.assertTrue(issubclass(BaseDocumentViewlet, ViewletBase))
