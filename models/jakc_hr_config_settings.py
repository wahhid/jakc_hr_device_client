from openerp.osv import fields, osv

class hr_config_settings(osv.osv_memory):
    _inherit = 'hr.config.settings'
    
    _columns = {
        'hrms_server': fields.char('HRMS Server', size=20, help='HRMS Server IP Address')
    }
    
    