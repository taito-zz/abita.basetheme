import unittest


class BaseViewletManagerTestCase(unittest.TestCase):
    """TestCase for  BaseViewletManager"""

    def test_subclass(self):
        from abita.basetheme.browser.viewlet import BaseViewletManager
        from five.grok import ViewletManager
        from plone.app.viewletmanager.manager import OrderedViewletManager
        self.assertTrue(issubclass(BaseViewletManager, (OrderedViewletManager, ViewletManager)))

    def test_baseclass(self):
        from abita.basetheme.browser.viewlet import BaseViewletManager
        self.assertTrue(getattr(BaseViewletManager, 'martian.martiandirective.baseclass'))

    def test_layer(self):
        from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
        from abita.basetheme.browser.viewlet import BaseViewletManager
        self.assertEqual(getattr(BaseViewletManager, 'grokcore.view.directive.layer'), IAbitaBasethemeLayer)
