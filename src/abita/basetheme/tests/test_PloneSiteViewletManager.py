import unittest


class PloneSiteViewletManagerTestCase(unittest.TestCase):
    """TestCase for  PloneSiteViewletManager"""

    def test_subclass(self):
        from abita.basetheme.browser.viewlet import PloneSiteViewletManager
        from abita.basetheme.browser.viewlet import BaseViewletManager
        self.assertTrue(issubclass(PloneSiteViewletManager, BaseViewletManager))

    def test_context(self):
        from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
        from abita.basetheme.browser.viewlet import PloneSiteViewletManager
        self.assertEqual(getattr(PloneSiteViewletManager, 'grokcore.component.directive.context'), IPloneSiteRoot)

    def test_name(self):
        from abita.basetheme.browser.viewlet import PloneSiteViewletManager
        self.assertEqual(getattr(PloneSiteViewletManager, 'grokcore.component.directive.name'),
            'abita.basetheme.plonesite.manager')
