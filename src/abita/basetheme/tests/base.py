from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import directlyProvides
from zope.publisher.browser import TestRequest

import mock
import unittest


class AbitaBasethemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import abita.basetheme
        self.loadZCML(package=abita.basetheme)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'abita.basetheme:default')

    def tearDownZope(self, app):
        """Tear down Zope."""


FIXTURE = AbitaBasethemeLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="AbitaBasethemeLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="AbitaBasethemeLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def create_atcontent(self, ctype, parent=None, **kwargs):
        """Create instance of AT content type"""
        if parent is None:
            parent = self.portal
        content = parent[parent.invokeFactory(ctype, **kwargs)]
        content.reindexObject()
        return content

    def create_viewlet(self, viewlet, context=None, view=None, manager=None):
        if context is None:
            context = self.portal
        request = TestRequest()
        directlyProvides(request, IAttributeAnnotatable)
        request.set = mock.Mock()
        return viewlet(context, request, view, manager)


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
