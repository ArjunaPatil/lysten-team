from __future__ import unicode_literals
import frappe
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def lock_master_forms(employee):
    
    lock_pro=0
    lock_pat=0
    lock_doc=0
    lock_che=0
    
    t_obj1=0
    t_obj2=0
    t_obj=0
    
    t_drc1=0
    t_drc2=0
    t_drc=0
    
    t_chc1=0
    t_chc2=0
    t_chc=0
    
    t_cmc1=0
    t_cmc2=0
    t_cmc=0
    
    today_date = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
    current_time = local_time()
    
    
    lock_pro = frappe.db.sql("""select m_pro from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    lock_pat = frappe.db.sql(""" select m_pat from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    lock_doc = frappe.db.sql(""" select m_doc from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    lock_che = frappe.db.sql(""" select m_che from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    
    t_obj1,t_obj2,t_obj = frappe.db.sql(""" select ifnull(t_obj1,'')as obj_frm_date,ifnull(t_obj2,'')as obj_to_date,ifnull(t_obj_time,'')as obj_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    
    t_drc1,t_drc2,t_drc = frappe.db.sql(""" select ifnull(t_drc1,'')as doc_frm_date,ifnull(t_drc2,'')as doc_to_date,ifnull(t_drc_time,'')as doc_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    
    t_chc1,t_chc2,t_chc = frappe.db.sql(""" select ifnull(t_chc1,'')as che_frm_date,ifnull(t_chc2,'')as che_to_date,ifnull(t_chc_time,'')as che_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    
    t_cmc1,t_cmc2,t_cmc = frappe.db.sql(""" select ifnull(t_cmc1,'')as cam_frm_date,ifnull(t_cmc2,'')as cam_to_date,ifnull(t_cmc_time,'')as cam_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
    
    dict = {'lock_pro': '',
            'lock_pat': '',
            'lock_doc':'',
            'lock_che': '',            
            'today_date': '',
            'current_time': '',            
            'lock_T_Obj1': '',
            'lock_T_Obj2': '',
            'lock_T_Obj': '',
            'lock_T_DrC1': '',
            'lock_T_DrC2': '',
            'lock_T_DrC': '',
            'lock_T_ChC1': '',
            'lock_T_ChC2': '',
            'lock_T_ChC': '',
            'lock_T_CmC1': '',
            'lock_T_CmC2': '',
            'lock_T_CmC': ''
           }
    
    dict['lock_pro'] = lock_pro[0].m_pro;
    dict['lock_pat'] = lock_pat[0].m_pat;
    dict['lock_doc'] = lock_doc[0].m_doc;
    dict['lock_che'] = lock_che[0].m_che;
    
    dict['today_date'] = today_date;
    dict['current_time'] = current_time;
    
    dict['lock_T_Obj1'] = t_obj1[0].obj_frm_date;
    dict['lock_T_Obj2'] = t_obj2[0].obj_to_date;
    dict['lock_T_Obj'] = t_obj[0].obj_time;
    
    dict['lock_T_DrC1'] = t_drc1[0].doc_frm_date;    
    dict['lock_T_DrC2'] = t_drc2[0].doc_to_date;
    dict['lock_T_DrC'] = t_drc[0].doc_time;
    
    dict['lock_T_ChC1'] = t_chc1[0].che_frm_date;
    dict['lock_T_ChC2'] = t_chc2[0].che_to_date;    
    dict['lock_T_ChC'] = t_chc[0].che_time;
    
    dict['lock_T_CmC1'] = t_cmc1[0].cam_frm_date;
    dict['lock_T_CmC2'] = t_cmc2[0].cam_to_date;
    dict['lock_T_CmC'] = t_cmc[0].cam_time;
    
    return dict
         

#Europe/Berlin
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')


    #import datetime
    #print(datetime.datetime.now().time())
    ###from datetime import datetime
    ###from pytz import timezone

    #Europe/Berlin
    ###def local_time(zone='Asia/Kolkata'):
    ###  other_zone = timezone(zone)
    ###  other_zone_time = datetime.now(other_zone)
    ###  return other_zone_time.strftime('%T')


    ###print(local_time())
