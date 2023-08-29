from odoo import http
from odoo.http import request
import os
import smtplib
import random
from datetime import datetime, timedelta
import base64


class MyFormController(http.Controller):
    def send_verification_code(self, recipient_email):
        subject = 'Your Verification Code'
        verification_code = str(random.randint(100000, 999999))
        message = f'Your verification code is: {verification_code}'

        sender_email = 'utshabbardewa2055@gmail.com'  # Replace with your sender email
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # Replace with the appropriate port
        smtp_username = "utshabbardewa2055@gmail.com"
        smtp_password = "xwhydejfrkvbmqms"  # Replace with your SMTP password
        http.request.session['verification_code'] = verification_code
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            msg = f'Subject: {subject}\n\n{message}'
            server.sendmail(sender_email, recipient_email, msg)
            server.quit()
            print("Verification code sent successfully.")
        except Exception as e:
            print(f"Error sending verification code: {e}")
    @http.route('/submit_form', type='http', auth='public', website=True)
    def submit_form(self, **post):
        # Retrieve data from the submitted form
        print("Received POST data:", post)

        csrf_token = http.request.csrf_token()
        submitted_token = post.get('csrf_token')
        print("Generated CSRF Token:", csrf_token)
        print("Submitted CSRF Token:", submitted_token)

        # if csrf_token != submitted_token:
        #     return http.Response('Invalid CSRF token', status=403)

        name = post.get('name')
        phone = post.get('phone')
        birth_date = post.get('birth_date')
        citizenship_number = post.get('citizenship_number')
        voter_id = post.get('voter_id')
        email = post.get('email')
        if email:
            self.send_verification_code(email)
        membership_duration = post.get("membership_duration")
        membership_type = post.get("membership_type")

        current_date = datetime.now().date()
        expiry_date = current_date
        if membership_duration == 'is_fouryears':
            expiry_date += timedelta(days=365 * 4)  # Adding 4 years' worth of days
        elif membership_duration == 'is_oneyear':
            expiry_date += timedelta(days=365)
        print(expiry_date)

        current_datetime = datetime.now()
        id_no = str(int(current_datetime.timestamp() * 1000))[-6:]
        print(id_no)

        gender = post.get("gender")
        family_count = post.get("family_count")
        perm_province = post.get("perm_province")
        perm_district = post.get("perm_district")
        perm_parliamentary_constituency_no = post.get("perm_parliamentary_constituency_no")
        perm_state_assembly_constituency_no = post.get("perm_state_assembly_constituency_no")
        perm_ward_no = post.get("perm_ward_no")
        perm_municipality = post.get("perm_municipality")
        perm_voting_center = post.get("perm_voting_center")

        current_province = post.get("current_province")
        current_district = post.get("current_district")
        current_parliamentary_constituency_no = post.get("current_parliamentary_constituency_no")
        current_state_assembly_constituency_no = post.get("current_state_assembly_constituency_no")
        current_ward_no = post.get("current_ward_no")
        current_municipality = post.get("current_municipality")
        current_voting_center = post.get("current_voting_center")

        membership_date = post.get("membership_date")

        father_or_mother_name = post.get("father_or_mother_name")
        husband_or_wife_name = post.get("husband_or_wife_name")

        education = post.get("education")
        marital_status = post.get("marital_status")
        religion = post.get("religion")
        caste = post.get("caste")
        past_responsibility = post.get("past_responsibility")
        name_of_approver = post.get("name_of_approver")
        position_of_approver = post.get("position_of_approver")

        # Handle uploaded photo
        photo = post.get('photo')
        photo_filename = None
        if photo:
            photo_data = photo.read()  # Read the binary data from the FileStorage object

            # Get the file extension from the uploaded filename
            filename, extension = os.path.splitext(photo.filename)
            extension = extension.lower()  # Ensure lowercase

            # Construct the new filename
            new_filename = f"{name.replace(' ', '_')}_{phone[-5:]}{extension}"

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
            'citizenship_number': citizenship_number,
            'voter_id': voter_id,
            'phone': phone,
            'email': email,
            'id_no': id_no,
            'membership_duration': membership_duration,
            'membership_type': membership_type,
            'expiry_date': expiry_date,
            'photo_filename': photo_filename,
            'birth_date': birth_date,
            'gender': gender,
            'family_count': family_count,
            'perm_district': perm_district,
            'perm_province': perm_province,
            'perm_parliamentary_constituency_no': perm_parliamentary_constituency_no,
            'perm_state_assembly_constituency_no': perm_state_assembly_constituency_no,
            'perm_ward_no': perm_ward_no,
            'perm_municipality': perm_municipality,
            'perm_voting_center': perm_voting_center,
            'current_province': current_province,
            'current_district': current_district,
            'current_parliamentary_constituency_no': current_parliamentary_constituency_no,
            'current_state_assembly_constituency_no': current_state_assembly_constituency_no,
            'current_ward_no': current_ward_no,
            'current_municipality': current_municipality,
            'current_voting_center': current_voting_center,
            'membership_date': membership_date,
            'father_or_mother_name': father_or_mother_name,
            'husband_or_wife_name': husband_or_wife_name,
            'education': education,
            'marital_status': marital_status,
            'religion': religion,
            'caste': caste,
            'past_responsibility': past_responsibility,
            'name_of_approver': name_of_approver,
            'position_of_approver': position_of_approver,
        }
        new_member = Member.create(member_vals)

        # Store parameters in the session
        session = request.session
        session['name'] = name
        session['id_no'] = id_no
        session['membership_duration'] = membership_duration
        session['membership_type'] = membership_type
        session['phone'] = phone
        session['email'] = email
        session['voter_id'] = voter_id
        session['citizenship_number'] = citizenship_number
        session['gender'] = gender
        session['photo_filename'] = photo_filename
        print(photo_filename)
        session['expiry_date'] = expiry_date

        # Redirect to the payment page
        return request.render('raprapa.otp_verify')

    @http.route('/verify_otp', type='http', auth='public', website=True)
    def verify_otp(self, **post):
        # Get the entered verification code
        entered_code = post.get('verification_code')

        # Retrieve the stored verification code
        stored_code = http.request.session.get('verification_code')

        # Check if the entered code matches the stored code
        if entered_code == stored_code:
            # If the verification code is correct, redirect to the payment page
            return http.request.redirect('/payment')
        else:
            # If the code is incorrect, you can display an error message or redirect as needed
            return request.render('raprapa.otp_unverified')

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

