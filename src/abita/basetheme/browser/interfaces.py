from collective.base.interfaces import IBaseView
from collective.base.interfaces import IViewlet
from zope.interface import Attribute
from zope.interface import Interface


# Browser layer

class IAbitaBasethemeLayer(Interface):
    """Marker interface for browserlayer."""


# View

class INavigationRootView(IBaseView):
    """View interface for interface: plone.app.layout.navigation.interfaces.INavigationRoot"""


# Viewlet

class IBaseDocumentViewlet(IViewlet):
    """Viewlet interface to show description and text from content type: ATDocument"""

    name = Attribute('ID of document')

    def obj():
        """Return ATDocument object

        :rtype: obj
        """

    def description():
        """Return description

        :rtype: str
        """

    def text():
        """Return text

        :rtype: str
        """


class IAboutViewlet(IBaseDocumentViewlet):
    """Viewlet interface to show about"""
