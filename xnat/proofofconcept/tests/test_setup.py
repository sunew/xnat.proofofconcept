# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from xnat.proofofconcept.testing import XNAT_PROOFOFCONCEPT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that xnat.proofofconcept is properly installed."""

    layer = XNAT_PROOFOFCONCEPT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if xnat.proofofconcept is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'xnat.proofofconcept'))

    def test_browserlayer(self):
        """Test that IXnatProofofconceptLayer is registered."""
        from xnat.proofofconcept.interfaces import (
            IXnatProofofconceptLayer)
        from plone.browserlayer import utils
        self.assertIn(IXnatProofofconceptLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = XNAT_PROOFOFCONCEPT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['xnat.proofofconcept'])

    def test_product_uninstalled(self):
        """Test if xnat.proofofconcept is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'xnat.proofofconcept'))
