from openerp import fields, models
import urllib2
import json

class hr_attendance(models.Model):
    _inherit = 'hr.attendance'
    iface_sync = fields.Boolean('Sync Status', default=False, readonly=True)
    
    
    