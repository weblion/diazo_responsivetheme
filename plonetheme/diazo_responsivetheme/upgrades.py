from Products.CMFCore.utils import getToolByName

def v1_to_v2(portal_setup):
    portal_quickinstaller = getToolByName(portal_setup, 'portal_quickinstaller')
    if not portal_quickinstaller.isProductInstalled('jarn.jsi18n'):
        return portal_setup.runAllImportStepsFromProfile('profile-jarn.jsi18n:default')


