from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
from collective.base.interfaces import IAdapter
from five import grok
from plone.app.layout.viewlets.common import DublinCoreViewlet as BaseDublinCoreViewlet
from plone.app.layout.viewlets.common import TitleViewlet as BaseTitleViewlet
from plone.app.viewletmanager.manager import OrderedViewletManager
from plone.memoize.view import memoize


grok.templatedir('viewlets')


class BaseViewletManager(OrderedViewletManager, grok.ViewletManager):
    """Base viewlet manager"""
    grok.baseclass()
    grok.layer(IAbitaBasethemeLayer)


class PloneSiteViewletManager(BaseViewletManager):
    """Viewlet manager for Plone Site"""
    grok.context(IPloneSiteRoot)
    grok.name('abita.basetheme.plonesite.manager')


class BaseViewlet(grok.Viewlet):
    """Base viewlet"""
    grok.baseclass()
    grok.layer(IAbitaBasethemeLayer)
    grok.require('zope2.View')


class BaseDocumentViewlet(BaseViewlet):
    """Base document viewlet"""
    name = ''
    grok.baseclass()
    grok.context(IPloneSiteRoot)
    grok.template('document')
    grok.viewletmanager(PloneSiteViewletManager)

    @property
    @memoize
    def folder(self):
        return self.context.get(self.name)

    @property
    @memoize
    def obj(self):
        adapter = IAdapter(self.folder)
        return adapter.get_object(IATDocument, depth=1)

    @property
    @memoize
    def title(self):
        if self.obj:
            return self.obj.Title()
        if self.folder:
            return self.folder.Title()

    @property
    @memoize
    def description(self):
        if self.obj:
            return self.obj.Description()
        return self.folder.Description()

    @property
    @memoize
    def text(self):
        if self.obj:
            return self.obj.CookedBody()


class AboutViewlet(BaseDocumentViewlet):
    name = 'about'
    grok.name('abita.basetheme.about')


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
