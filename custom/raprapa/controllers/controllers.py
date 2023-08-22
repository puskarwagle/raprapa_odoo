# -*- coding: utf-8 -*-
# from odoo import http


# class Raprapa(http.Controller):
#     @http.route('/raprapa/raprapa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/raprapa/raprapa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('raprapa.listing', {
#             'root': '/raprapa/raprapa',
#             'objects': http.request.env['raprapa.raprapa'].search([]),
#         })

#     @http.route('/raprapa/raprapa/objects/<model("raprapa.raprapa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('raprapa.object', {
#             'object': obj
#         })
