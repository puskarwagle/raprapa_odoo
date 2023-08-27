from odoo import http
from odoo.http import request
import os
import base64


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

        # Handle uploaded photo
        photo = post.get('photo')
        photo_filename = None
        if photo:
            photo_data = photo.read()  # Read the binary data from the FileStorage object

            # Get the file extension from the uploaded filename
            filename, extension = os.path.splitext(photo.filename)
            extension = extension.lower()  # Ensure lowercase

            # Construct the new filename
            new_filename = f"{name}_{phone[-5:]}{extension}"

            # Save the file to the desired directory
            photo_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static', 'user_images', new_filename
            )

            with open(photo_path, 'wb') as f:
                f.write(photo_data)

            # Store the photo filename for later use
            photo_filename = new_filename

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
            'photo_filename': photo_filename,
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

