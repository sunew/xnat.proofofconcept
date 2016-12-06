# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import xnat.proofofconcept


class XnatProofofconceptLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=xnat.proofofconcept)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'xnat.proofofconcept:default')


XNAT_PROOFOFCONCEPT_FIXTURE = XnatProofofconceptLayer()


XNAT_PROOFOFCONCEPT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(XNAT_PROOFOFCONCEPT_FIXTURE,),
    name='XnatProofofconceptLayer:IntegrationTesting'
)


XNAT_PROOFOFCONCEPT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(XNAT_PROOFOFCONCEPT_FIXTURE,),
    name='XnatProofofconceptLayer:FunctionalTesting'
)


XNAT_PROOFOFCONCEPT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        XNAT_PROOFOFCONCEPT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='XnatProofofconceptLayer:AcceptanceTesting'
)
