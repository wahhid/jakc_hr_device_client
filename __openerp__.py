# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2016-Jakc Labs. (<http://www.jakc-labs.com/>)
#
#################################################################################
{
    'name': 'HR Client Enhancement',
    'summary': 'Extend HR Client Enhancement',
    'version': '1.0',
    'category': 'HR',
    "sequence": 1,
    'description': """
HR Client Enhancement
=====================================
Features:
----------------
    * Add ability to integrate with HR Device.
    * For Odoo 8
""",
    "author": "Wahyu Hidayat - Jakc Labs.",
    'website': 'http://www.jakc-labs.com',
    'depends': [
        'hr',
        ],
    'data': [
        'views/jakc_hr_attendance_view.xml',
        'views/jakc_hr_employee_view.xml',
    ],    
    "installable": True,
    "application": True,
    "auto_install": False,        
}