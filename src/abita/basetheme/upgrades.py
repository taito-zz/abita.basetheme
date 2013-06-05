PROFILE_ID = 'profile-abita.basetheme:default'


def reimport_viewlets(setup):
    """Reimport viewlets"""
    setup.runImportStepFromProfile(PROFILE_ID, 'viewlets', run_dependencies=False, purge_old=False)
