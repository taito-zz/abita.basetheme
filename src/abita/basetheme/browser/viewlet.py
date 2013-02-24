from Products.ATContentTypes.interfaces.document import IATDocument
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from abita.adapter.interfaces import IBaseAdapter
from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
from five import grok
from plone.app.viewletmanager.manager import OrderedViewletManager

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
    def folder(self):
        return self.context.get(self.name)

    @property
    def obj(self):
        adapter = IBaseAdapter(self.folder)
        return adapter.get_object(IATDocument, depth=1)

    @property
    def title(self):
        if self.obj:
            return self.obj.Title()
        return self.folder.Title()

    @property
    def description(self):
        if self.obj:
            return self.obj.Description()
        return self.folder.Description()

    @property
    def text(self):
        if self.obj:
            return self.obj.CookedBody()


class AboutViewlet(BaseDocumentViewlet):
    name = 'about'
    grok.name('abita.basetheme.about')
