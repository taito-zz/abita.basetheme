from abita.basetheme.tests.base import IntegrationTestCase
from abita.utils.utils import get_css_resource
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('abita.basetheme'))

    def test_browserlayer(self):
        from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
        from plone.browserlayer import utils
        self.assertIn(IAbitaBasethemeLayer, utils.registered_layers())

    def test_cssregistry__abita_theme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__abita_theme_main__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__abita_theme_main__compression(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__abita_theme_main__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__abita_theme_main__cookable(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__abita_theme_main__enabled(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__abita_theme_main__expression(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__abita_theme_main__media(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__abita_theme_main__rel(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__abita_theme_main__rendering(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__abita_theme_main__title(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__abita_theme_extra__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__abita_theme_extra__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__abita_theme_extra__compression(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__abita_theme_extra__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__abita_theme_extra__cookable(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__abita_theme_extra__enabled(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__abita_theme_extra__expression(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__abita_theme_extra__media(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__abita_theme_extra__rel(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__abita_theme_extra__rendering(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__abita_theme_extra__title(self):
        resource = get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css')
        self.assertIsNone(resource.getTitle())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-abita.basetheme:default'), u'0')

    def test_types__Plone_Site__immediate_view(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('immediate_view'), 'abita-view')

    def test_types__Plone_Site__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('default_view'), 'abita-view')

    def test_types__Plone_Site__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('view_methods'), ('abita-view',))

    def test_uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.basetheme'])
        self.assertFalse(installer.isProductInstalled('abita.basetheme'))

    def test_uninstall_browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.basetheme'])
        from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IAbitaBasethemeLayer, utils.registered_layers())

    def test_uninstall_cssregistry__abita_theme_main(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.basetheme'])
        self.assertIsNone(get_css_resource(self.portal, '++resource++abita.basetheme/css/main.css'))

    def test_uninstall_cssregistry__abita_theme_extra(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.basetheme'])
        self.assertIsNone(get_css_resource(self.portal, '++resource++abita.basetheme/css/extra.css'))
