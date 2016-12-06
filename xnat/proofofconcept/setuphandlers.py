# -*- coding: utf-8 -*-
from logging import getLogger

log = getLogger('xnat.proofofconcept:install')

def post_install(context):
    """Post install script"""
    if context.readDataFile('xnatproofofconcept_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()
    log.info("Running install: setuphandlers.")


def post_install_initialsetup(context):
    """Post install script for initialsetup profile - only to be run once"""
    if context.readDataFile('xnatproofofconcept_initialsetup_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()
