# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def ding(limit, offset):
 if limit==10
 frappe.msgprint(_("aaaaaaaa"))
 
 @frappe.whitelist()
def dong(limit, offset):
 	return frappe.db.sql(""" SELECT doctor_name as dname,reg_no,pin_code,
  per_mobile,per_phone,email FROM `tabDoctor Master` LIMIT {0}  OFFSET {1} """.format(limit,offset),as_dict=True)
