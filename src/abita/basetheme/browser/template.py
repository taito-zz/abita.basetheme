from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PloneSiteView(BrowserView):
    """View for Plone Site"""

    __call__ = ViewPageTemplateFile('templates/plone-site.pt')
