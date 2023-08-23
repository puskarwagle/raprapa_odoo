from odoo import http
from odoo.http import request


class RaprapaController(http.Controller):
    @http.route('/', type='http', website=True, auth="public")
    def formpage(self):
        return request.render('raprapa.index_form')

    @http.route('/payment', type='http', website=True, auth="public")
    def paymentpage(self):
        return request.render('raprapa.payment')

