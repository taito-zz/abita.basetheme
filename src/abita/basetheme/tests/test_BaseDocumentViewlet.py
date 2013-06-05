# -*- coding: utf-8 -*-
from abita.basetheme.browser.viewlet import BaseDocumentViewlet
from abita.basetheme.browser.interfaces import IBaseDocumentViewlet
from abita.basetheme.tests.base import IntegrationTestCase

import mock


class BaseDocumentViewletTestCase(IntegrationTestCase):
    """TestCase for BaseDocumentViewlet"""

    def test_subclass(self):
        from collective.base.viewlet import Viewlet as Base
        self.assertTrue(issubclass(BaseDocumentViewlet, Base))
        from collective.base.interfaces import IViewlet as Base
        self.assertTrue(issubclass(IBaseDocumentViewlet, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_viewlet(BaseDocumentViewlet)
        self.assertTrue(verifyObject(IBaseDocumentViewlet, instance))

    def test_obj__0(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        self.assertIsNone(instance.obj())

    def test_obj__1(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        doc1 = self.create_atcontent('Document', id='doc1')
        self.assertEqual(instance.obj(), doc1)

    def test_obj__2(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        self.create_atcontent('Document', id='doc1')
        instance.name = 'doc2'
        self.assertIsNone(instance.obj())

    def test_obj__3(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        self.create_atcontent('Document', id='doc1')
        instance.name = 'doc2'
        doc2 = self.create_atcontent('Document', id='doc2')
        self.assertEqual(instance.obj(), doc2)

    def test_available__0(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        self.assertFalse(instance.available())

    def test_available__1(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        instance.obj = mock.Mock()
        self.assertTrue(instance.available())

    def test_description(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        obj = mock.Mock()
        obj.Description.return_value = 'DESCRIPTION'
        instance.obj = mock.Mock(return_value=obj)
        self.assertEqual(instance.description(), 'DESCRIPTION')

    def test_text(self):
        instance = self.create_viewlet(BaseDocumentViewlet)
        obj = mock.Mock()
        obj.CookedBody.return_value = 'TEXT'
        instance.obj = mock.Mock(return_value=obj)
        self.assertEqual(instance.text(), 'TEXT')
