# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

@frappe.whitelist(allow_guest=True)
def ping():
    return 'pong'

