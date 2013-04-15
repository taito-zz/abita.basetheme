from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class IAbitaBasethemeLayer(Interface):
    """Marker interface for browserlayer."""


class IPloneSiteViewletManager(IViewletManager):
    """Marker interface for abita.basetheme.viewletmanager.plone-site"""
