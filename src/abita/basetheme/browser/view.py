from abita.basetheme.browser.interfaces import INavigationRootView
from collective.base.view import BaseView
from zope.interface import implements


class NavigationRootView(BaseView):
    """View for interface: plone.app.layout.navigation.interfaces.INavigationRoot"""
    implements(INavigationRootView)

    def __call__(self):
        return self.template()
