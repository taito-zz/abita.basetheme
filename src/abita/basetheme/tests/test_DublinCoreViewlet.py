# -*- coding: utf-8 -*-
from abita.basetheme.tests.base import IntegrationTestCase
from abita.basetheme.browser.viewlet import DublinCoreViewlet


class DublinCoreViewletTestCase(IntegrationTestCase):
    """TestCase for DublinCoreViewlet"""

    def test_subclass(self):
        from plone.app.layout.viewlets.common import DublinCoreViewlet as BaseDublinCoreViewlet
        self.assertTrue(issubclass(DublinCoreViewlet, BaseDublinCoreViewlet))

    def test_update(self):
        instance = self.create_viewlet(DublinCoreViewlet)
        instance.update()
        self.assertEqual(instance.metatags, [])

        head = self.create_atcontent('Folder', id='head')
        instance.update()
        self.assertEqual(instance.metatags, [])

        head.setDescription('Description of Heäd')
        head.reindexObject(idxs=['description'])
        instance.update()
        self.assertEqual(instance.metatags, [('description', 'Description of Heäd')])

        doc = self.create_atcontent('Document', head, id='doc')
        instance.update()
        self.assertEqual(instance.metatags, [('description', 'Description of Heäd')])

        doc.setDescription('Description of Döc')
        doc.reindexObject(idxs=['description'])
        instance.update()
        self.assertEqual(instance.metatags, [('description', 'Description of Döc')])
