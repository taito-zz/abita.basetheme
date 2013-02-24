import unittest


class BaseDocumentViewletTestCase(unittest.TestCase):
    """TestCase for BaseDocumentViewlet"""

    def test_subclass(self):
        from abita.basetheme.browser.viewlet import BaseViewlet
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        self.assertTrue(issubclass(BaseDocumentViewlet, BaseViewlet))

    def test_context(self):
        from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        self.assertEqual(getattr(BaseDocumentViewlet, 'grokcore.component.directive.context'), IPloneSiteRoot)

    def test_template(self):
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        self.assertEqual(getattr(BaseDocumentViewlet, 'grokcore.view.directive.template'), 'document')

    def test_name(self):
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        from abita.basetheme.browser.viewlet import PloneSiteViewletManager
        self.assertEqual(getattr(BaseDocumentViewlet, 'grokcore.viewlet.directive.viewletmanager'), PloneSiteViewletManager)

    def test_viewlet_name(self):
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet
        self.assertEqual(BaseDocumentViewlet.name, '')
