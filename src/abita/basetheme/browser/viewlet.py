from Products.ATContentTypes.interfaces.document import IATDocument
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from abita.basetheme.browser.interfaces import IAboutViewlet
from abita.basetheme.browser.interfaces import IBaseDocumentViewlet
from collective.base.interfaces import IAdapter
from collective.base.viewlet import Viewlet
from plone.memoize.view import memoize
from zope.interface import implements


class BaseDocumentViewlet(Viewlet):
    """Base document viewlet"""
    implements(IBaseDocumentViewlet)
    index = ViewPageTemplateFile('viewlets/document.pt')
    name = None

    @memoize
    def available(self):
        """Return True or False

        :rtype: bool
        """
        if self.obj():
            return True
        else:
            return False

    @memoize
    def obj(self):
        """Return ATDocument object

        :rtype: obj
        """
        adapter = IAdapter(self.context)
        if self.name:
            return adapter.get_object(IATDocument, depth=1, id=self.name)
        else:
            return adapter.get_object(IATDocument, depth=1)

    @memoize
    def description(self):
        """Return description

        :rtype: str
        """
        return self.obj().Description()

    @memoize
    def text(self):
        """Return text

        :rtype: str
        """
        return self.obj().CookedBody()


class AboutViewlet(BaseDocumentViewlet):
    """Viewlet: abita.basetheme.viewlet.about"""
    implements(IAboutViewlet)
    name = 'about'
