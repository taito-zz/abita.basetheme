from abita.basetheme.browser.view import NavigationRootView
from abita.basetheme.tests.base import IntegrationTestCase
from abita.basetheme.browser.interfaces import INavigationRootView


class NavigationRootViewTestCase(IntegrationTestCase):
    """TestCase for NavigationRootView"""

    def test_subclass(self):
        from collective.base.view import BaseView as Base
        self.assertTrue(issubclass(NavigationRootView, Base))
        from collective.base.interfaces import IBaseView as Base
        self.assertTrue(issubclass(INavigationRootView, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_view(NavigationRootView)
        self.assertTrue(verifyObject(INavigationRootView, instance))

    def test___call__(self):
        instance = self.create_view(NavigationRootView)
        self.assertTrue(instance().startswith(u'\n<!DOCTYPE html>'))
