from __future__ import unicode_literals
import frappe
from frappe import utils
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def get_count_of_objectives_of_bottom_emp(employee, designation):
 #frappe.msgprint(_(tree_user_bottom(employee, designation)))
 #return tree_user_bottom(employee, designation)
 email_list=""
 test=datetime.date.today()
 for email_emp in tree_user_bottom(employee, designation):
  email_list = email_list + "'"+email_emp.name + "',"
 
 email_list=email_list[:-1]
 
 #return email_list
 count_of_emp= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.tabObjective
where 1bd3e0294da19198.tabObjective.user in ({0})""".format(email_list), as_dict=1)
 
 #return (test,count_of_emp)


# this method is used for android heirachy user
 #it will featch all top and down users of selected user

def tree_user_bottom(employee, designation): 
 if designation == 'TBM':
   return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0}  or `tabUser`.`name` in(
 (select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )  """.format(employee), as_dict=1)
  
 elif designation == "ABM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0}  or `tabUser`.`name` in(
 (select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )  """.format(employee), as_dict=1)
 
 elif designation == "RBM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`rbm`={0}  or `tabUser`.`name` in(
 (select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee), as_dict=1)
 
 elif designation == "ZBM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`zbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ) """.format(employee), as_dict=1)
 
 elif designation == "SM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`sm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
)""".format(employee), as_dict=1)
 
 elif designation == "NBM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`nbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
)""".format(employee), as_dict=1)
 
 elif designation == "CRM":
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`crm`={0}
 """.format(employee), as_dict=1)
 
 elif (designation == "HR Manager" or designation == "Head of Marketing and Sales" or designation == "Admin"):
  return frappe.db.sql(""" select name from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`designation` in('TBM','ABM','RBM','ZBM','SM','NBM','CRM')
 """.format(employee), as_dict=1)
 
 else:
   return ""
