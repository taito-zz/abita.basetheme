from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from abita.basetheme.browser.interfaces import IAbitaBasethemeLayer
from five import grok

grok.templatedir('templates')


class BaseView(grok.View):
    """Base view"""
    grok.baseclass()
    grok.layer(IAbitaBasethemeLayer)
    grok.require('zope2.View')


class PloneSiteView(BaseView):
    """View for Plone Site"""
    grok.context(IPloneSiteRoot)
    grok.name('abita-view')
    grok.template('plone-site')
