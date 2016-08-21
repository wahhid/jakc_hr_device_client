from openerp import fields, models


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    finger_client_01 = fields.Binary("Finger Client #1")
    finger_client_02 = fields.Binary("Finger Client #2")
    