import mock
import unittest


class UpgradesTestCase(unittest.TestCase):
    """TestCase for upgrade step"""

    def test_reimport_viewlets(self):
        from abita.basetheme.upgrades import reimport_viewlets
        step = mock.Mock()
        reimport_viewlets(step)
        step.runImportStepFromProfile.assert_called_with('profile-abita.basetheme:default', 'viewlets',
            run_dependencies=False, purge_old=False)
