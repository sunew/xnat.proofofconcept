# -*- coding: utf-8 -*-
import logging

from plone.protect import CheckAuthenticator
from Products.CMFPlone.utils import log
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


class XnatView(BrowserView):

    template = ViewPageTemplateFile('templates/xnatview.pt')

    def __call__(self):
        self.status = None
        if self.request.form.has_key('submitted'):
            CheckAuthenticator(self.request)
            if self.request.form.has_key('uploadxnat'):
                self.status = 'XNAT window opened.'
                self.grant_access_redirect()

        return self.template()

    @property
    def xnat_base_url(self):
        return 'http://10.0.1.144:8080/xnat/app/template/Login.vm'

