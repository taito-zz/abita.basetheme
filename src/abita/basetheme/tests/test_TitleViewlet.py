# -*- coding: utf-8 -*-
from abita.basetheme.tests.base import IntegrationTestCase
from abita.basetheme.browser.viewlet import TitleViewlet

import mock


class TitleViewletTestCase(IntegrationTestCase):
    """TestCase for TitleViewlet"""

    def test_subclass(self):
        from plone.app.layout.viewlets.common import TitleViewlet as BaseTitleViewlet
        self.assertTrue(issubclass(TitleViewlet, BaseTitleViewlet))

    @mock.patch('plone.app.layout.viewlets.common.getMultiAdapter')
    def test_update(self, getMultiAdapter):
        instance = self.create_viewlet(TitleViewlet)
        getMultiAdapter().navigation_root_title.return_value = 'navigation_root_title'
        getMultiAdapter().object_title.return_value = 'object_title'
        instance.update()
        self.assertEqual(instance.site_title, u'object_title &mdash; navigation_root_title')

        head = self.create_atcontent('Folder', id='head')
        instance.update()
        self.assertEqual(instance.site_title, u'object_title &mdash; navigation_root_title')

        head.title = 'Tıtle'
        head.reindexObject(idxs=['title'])
        instance.update()
        self.assertEqual(instance.site_title, 'Tıtle')

        doc = self.create_atcontent('Document', head, id='doc')
        instance.update()
        self.assertEqual(instance.site_title, 'Tıtle')

        doc.title = 'Döc'
        doc.reindexObject(idxs=['title'])
        instance.update()
        self.assertEqual(instance.site_title, 'Döc')
