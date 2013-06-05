from abita.basetheme.tests.base import IntegrationTestCase
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

    def test_cssregistry__abita_theme_main(self):
        resource = getToolByName(self.portal, 'portal_css').getResource('++resource++abita.basetheme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__abita_theme_extra(self):
        resource = getToolByName(self.portal, 'portal_css').getResource('++resource++abita.basetheme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-abita.basetheme:default'), u'1')

    def test_types__Plone_Site__immediate_view(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('immediate_view'), 'abita-view')

    def test_types__Plone_Site__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('default_view'), 'abita-view')

    def test_types__Plone_Site__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        self.assertEqual(types.getTypeInfo('Plone Site').getProperty('view_methods'), ('abita-view',))

    def test_viewlets__hidden__plone_portalheader(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalheader"
        skinname = "*"
        for viewlet in (
            u'plone.app.i18n.locales.languageselector',
            u'plone.searchbox'):
            self.assertIn(viewlet, storage.getHidden(manager, skinname))

    def test_viewlets__hidden__plone_portalfooter(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"
        skinname = "*"
        for viewlet in (
            u'plone.colophon',
            u'plone.site_actions'):
            self.assertIn(viewlet, storage.getHidden(manager, skinname))

    def test_viewlets__order__collective_base_viewlet_manager_base(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "collective.base.viewlet-manager.base"
        skinname = "*"
        for viewlet in (
            u'abita.basetheme.viewlet.about',):
            self.assertIn(viewlet, storage.getOrder(manager, skinname))

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
        self.assertIsNone(getToolByName(self.portal, 'portal_css').getResource('++resource++abita.basetheme/css/main.css'))

    def test_uninstall_cssregistry__abita_theme_extra(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.basetheme'])
        self.assertIsNone(getToolByName(self.portal, 'portal_css').getResource('++resource++abita.basetheme/css/extra.css'))
