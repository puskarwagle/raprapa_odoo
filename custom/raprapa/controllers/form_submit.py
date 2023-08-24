from odoo import http
from odoo.http import request
import os

class MyFormController(http.Controller):
    @http.route('/submit_form', type='http', auth='public', website=True)
    def submit_form(self, **post):
        # Retrieve data from the submitted form
        name = post.get('name')
        phone = post.get('phone')

        birth_date = post.get('birth_date')
        citizenship_number = post.get('citizenship_number')
        voter_id = post.get('voter_id')
        email = post.get('email')
        membership_duration = post.get("membership_duration")
        membership_type = post.get("membership_type")

        # Create a new member record
        Member = request.env['raprapa.member']
        member_vals = {
            'name': name,
            'birth_date': birth_date,
            'citizenship_number': citizenship_number,
            'voter_id': voter_id,
            'phone': phone,
            'email': email,
            'membership_duration': membership_duration,
            'membership_type': membership_type,
        }
        new_member = Member.create(member_vals)

        # Store parameters in the session
        session = request.session
        session['name'] = name
        session['membership_duration'] = membership_duration
        session['membership_type'] = membership_type
        session['phone'] = phone
        session['email'] = email

        # Redirect to the payment page
        return request.redirect('/payment')


    @http.route('/payment', type='http', website=True, auth="public")
    def paymentpage(self):
        # Retrieve stored parameters from the session
        session = request.session
        name = session.get('name')
        membership_duration = session.get('membership_duration')
        membership_type = session.get('membership_type')
        email = session.get('email')
        phone = session.get('phone')

        return request.render('raprapa.payment', {
            'redirect_params': {
                'name': name,
                'membership_duration': membership_duration,
                'membership_type': membership_type,
                'email': email,
                'phone': phone,
            }
        })

