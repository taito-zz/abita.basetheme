from abita.basetheme.browser.interfaces import IAboutViewlet
from abita.basetheme.browser.viewlet import AboutViewlet
from abita.basetheme.tests.base import IntegrationTestCase


class AboutViewletTestCase(IntegrationTestCase):
    """TestCase for AboutViewlet"""

    def test_subclass(self):
        from abita.basetheme.browser.viewlet import BaseDocumentViewlet as Base
        self.assertTrue(issubclass(AboutViewlet, Base))
        from abita.basetheme.browser.interfaces import IBaseDocumentViewlet as Base
        self.assertTrue(issubclass(IAboutViewlet, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_viewlet(AboutViewlet)
        self.assertTrue(verifyObject(IAboutViewlet, instance))
