from openerp import http
from openerp.http import request
import json

class Device(http.Controller):
    
    @http.route('/att_device_client/status', type='http', auth='none', cors='*')
    def status_http(self):
        resp = """<html>
                    <head>
                        <title>Jakc Labs - Attendance Device Client API</title>
                    </head>
                    <body><center>Attendance Device Client API Ready</center></body>
                </html>"""
        return request.make_response(resp,{
            'Cache-Control': 'no-cache', 
            'Content-Type': 'text/html; charset=utf-8',
            'Access-Control-Allow-Origin':  '*',
            'Access-Control-Allow-Methods': 'GET',
        })
        
    @http.route('/att_device_client/employee/browse/<int:employeeid>', type='http', auth='none', cors='*')
    def employee_browse(self, employeeid):
        env_employee = http.request.env['hr.employee']
        employees = env_employee.sudo().browse([employeeid])
        if employees[0].name:
            name = employees[0].name
        else:
            name = ''
            
        if employees[0].otherid:
            otherid = employees[0].otherid
        else:
            otherid = ''            
            
        if employees[0].finger_client_01:
            finger01 = employees[0].finger_client_01
        else:
            finger01 = ''            
    
        if employees[0].finger_client_02:
            finger02 = employees[0].finger_client_02
        else:
            finger02 = ''            
            
        json_employee = '{"name":"' + name + '","otherid":"' + otherid +'","finger01":"' + finger01 + '","finger02":"' + finger02 +'"}'  
        
        return request.make_response(json_employee,{
            'Cache-Control': 'no-cache', 
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin':  '*',
            'Access-Control-Allow-Methods': 'GET',
        })
        