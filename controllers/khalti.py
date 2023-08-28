import requests
from odoo import http
from odoo.http import request
from werkzeug.utils import redirect


class KhaltiController(http.Controller):
    @http.route('/initiate_khalti_payment/', type='http', auth='public', website=True, csrf=False)
    def initiate_khalti_payment(self, **post):
        url = "https://a.khalti.com/api/v2/epayment/initiate/"
        headers = {
            "Authorization": "Key 0ee3e3a99d294a01b700cb5c15323723",
            "Content-Type": "application/json"
        }

        # Get the form data from the POST request
        name = post.get("name")
        phone = post.get("phone")
        email = post.get("email")
        amount = post.get("amount")

        data = {
            "return_url": "http://localhost:8069/id_card/",  # Use a different URL for payment success
            "website_url": "http://localhost:8069/payment/",
            "amount": amount,
            "purchase_order_id": "12345",
            "purchase_order_name": "Raprapa id card",
            "customer_info": {
                "name": name,
                "email": email,
                "phone": phone
            }
        }

        response = requests.post(url, json=data, headers=headers)
        payment_data = response.json()
        payment_url = payment_data.get("payment_url")

        member = request.env['raprapa.member'].sudo().search([('phone', '=', phone)], limit=1)

        if member:
            member.write({'paid': True})

        # Redirect the user to the payment URL
        return redirect(payment_url, code=302)

    @http.route('/id_card/', type='http', auth='public', website=True, csrf=False)
    def payment_success(self):
        session = request.session
        name = session.get('name')
        return request.render('raprapa.id_card', {
            'redirect_params': {
                'name': name
            }
            })
