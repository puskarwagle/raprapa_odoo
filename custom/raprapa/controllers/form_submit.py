from odoo import http
from odoo.http import request


class MyFormController(http.Controller):
    @http.route('/submit_form', type='http', auth='public', website=True)
    def submit_form(self, **post):
        # Retrieve data from the submitted form
        name = post.get('name')
        birth_date = post.get('birth_date')
        citizenship_number = post.get('citizenship_number')
        voter_id = post.get('voter_id')
        mobile_no = post.get('mobile_no')
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
            'mobile_no': mobile_no,
            'email': email,
            'membership_duration': membership_duration,
            'membership_type': membership_type

        }
        new_member = Member.create(member_vals)

        # Redirect to a thank you page or any other page after form submission
        return request.redirect('/payment?name=%s&membership_duration=%s&membership_type=%s' % (name, membership_duration, membership_type))
        # return request.redirect('/payment')
