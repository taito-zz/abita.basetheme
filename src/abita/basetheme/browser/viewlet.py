from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.base.interfaces import IAdapter
from plone.app.layout.viewlets.common import DublinCoreViewlet as BaseDublinCoreViewlet
from plone.app.layout.viewlets.common import TitleViewlet as BaseTitleViewlet
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.view import memoize


class BaseDocumentViewlet(ViewletBase):
    """Base document viewlet"""
    name = ''

    index = ViewPageTemplateFile('viewlets/document.pt')

    @memoize
    def folder(self):
        return self.context.get(self.name)

    @memoize
    def obj(self):
        folder = self.folder()
        adapter = IAdapter(folder)
        return adapter.get_object(IATDocument, depth=1) or folder

    @memoize
    def title(self):
        return self.obj().Title()

    @memoize
    def description(self):
        return self.obj().Description()

    @memoize
    def text(self):
        if hasattr(self.obj(), 'CookedBody'):
            return self.obj().CookedBody()


class AboutViewlet(BaseDocumentViewlet):
    """Viewlet: abita.basetheme.viewlet.about"""
    name = 'about'


class TitleViewlet(BaseTitleViewlet):
    """Viewlet to render title in head"""

    def update(self):
        super(TitleViewlet, self).update()
        if IPloneSiteRoot.providedBy(self.context):
            adapter = IAdapter(self.context)
            head = adapter.get_brain(IATFolder, id="head", depth=1)
            if head:
                doc = adapter.get_brain(IATDocument, path=head.getPath(), depth=1)
                if doc and doc.Title:
                    self.site_title = doc.Title
                elif head.Title:
                    self.site_title = head.Title


class DublinCoreViewlet(BaseDublinCoreViewlet):
    """Viewlet to render dublin core in head"""

    def update(self):
        super(DublinCoreViewlet, self).update()
        if IPloneSiteRoot.providedBy(self.context):
            adapter = IAdapter(self.context)
            head = adapter.get_brain(IATFolder, id="head", depth=1)
            if head:
                items = dict(self.metatags)
                doc = adapter.get_brain(IATDocument, path=head.getPath(), depth=1)
                if doc and doc.Description:
                    items['description'] = doc.Description
                elif head.Description:
                    items['description'] = head.Description

                self.metatags = items.items()
