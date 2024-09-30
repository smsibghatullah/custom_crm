# -*- coding: utf-8 -*-
from odoo import http

# class CustomCrmDsm(http.Controller):
#     @http.route('/custom_crm_dsm/custom_crm_dsm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm_dsm/custom_crm_dsm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm_dsm.listing', {
#             'root': '/custom_crm_dsm/custom_crm_dsm',
#             'objects': http.request.env['custom_crm_dsm.custom_crm_dsm'].search([]),
#         })

#     @http.route('/custom_crm_dsm/custom_crm_dsm/objects/<model("custom_crm_dsm.custom_crm_dsm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm_dsm.object', {
#             'object': obj
#         })