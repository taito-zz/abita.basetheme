import unittest


class PloneSiteViewTestCase(unittest.TestCase):

    def test_subclass(self):
        from abita.basetheme.browser.template import BaseView
        from abita.basetheme.browser.template import PloneSiteView
        self.assertTrue(issubclass(PloneSiteView, BaseView))

    def test_context(self):
        from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
        from abita.basetheme.browser.template import PloneSiteView
        self.assertEqual(getattr(PloneSiteView, 'grokcore.component.directive.context'), IPloneSiteRoot)

    def test_name(self):
        from abita.basetheme.browser.template import PloneSiteView
        self.assertEqual(getattr(PloneSiteView, 'grokcore.component.directive.name'), 'abita-view')

    def test_template(self):
        from abita.basetheme.browser.template import PloneSiteView
        self.assertEqual(getattr(PloneSiteView, 'grokcore.view.directive.template'), 'plone-site')
