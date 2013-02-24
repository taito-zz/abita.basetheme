import unittest


class BaseViewTestCase(unittest.TestCase):

    def test_templatedir(self):
        from abita.basetheme.browser import template
        self.assertEqual(getattr(template, 'grokcore.view.directive.templatedir'), 'templates')

    def test_subclass(self):
        from five.grok import View
        from abita.basetheme.browser.template import BaseView
        self.assertTrue(issubclass(BaseView, View))

    def test_baseclass(self):
        from abita.basetheme.browser.template import BaseView
        self.assertTrue(getattr(BaseView, 'martian.martiandirective.baseclass'))

    def test_layer(self):
        from abita.basetheme.browser.template import BaseView
        from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
        self.assertEqual(getattr(BaseView, 'grokcore.view.directive.layer'), IAbitaBasethemeLayer)

    def test_require(self):
        from abita.basetheme.browser.template import BaseView
        self.assertEqual(getattr(BaseView, 'grokcore.security.directive.require'), ['zope2.View'])
