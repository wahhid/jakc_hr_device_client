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
        