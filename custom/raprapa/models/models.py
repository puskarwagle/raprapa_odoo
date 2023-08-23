from odoo import models, fields, api


class Member(models.Model):
    _name = 'raprapa.member'
    _description = 'Raprapa members'

    membership_type = fields.Char(string='Membership Type')
    membership_duration = fields.Char(string='Membership Duration')
    expiry_date = fields.Date(string='Expiry Date')

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Char(string='Date of birth')
    citizenship_number = fields.Char(string='Citizenship Number')
    voter_id = fields.Char(string='Voter ID')
    mobile_no = fields.Char(string="Mobile No")
    email = fields.Char(string='Email')