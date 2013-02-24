import unittest


class BaseViewletTestCase(unittest.TestCase):

    def test_templatedir(self):
        from abita.basetheme.browser import viewlet
        self.assertEqual(getattr(viewlet, 'grokcore.view.directive.templatedir'), 'viewlets')

    def test_subclass(self):
        from five.grok import Viewlet
        from abita.basetheme.browser.viewlet import BaseViewlet
        self.assertTrue(issubclass(BaseViewlet, Viewlet))

    def test_baseclass(self):
        from abita.basetheme.browser.viewlet import BaseViewlet
        self.assertTrue(getattr(BaseViewlet, 'martian.martiandirective.baseclass'))

    def test_layer(self):
        from abita.basetheme.browser.viewlet import BaseViewlet
        from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
        self.assertEqual(getattr(BaseViewlet, 'grokcore.view.directive.layer'), IAbitaBasethemeLayer)

    def test_require(self):
        from abita.basetheme.browser.viewlet import BaseViewlet
        self.assertEqual(getattr(BaseViewlet, 'grokcore.security.directive.require'), ['zope2.View'])
