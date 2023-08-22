from odoo import models, fields, api


class Member(models.Model):
    _name = 'raprapa.member'
    _description = 'Raprapa members'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Char(string='Date of birth', required=True)
    citizenship_number = fields.Char(string='Citizenship Number', required=True)
    voter_id = fields.Char(string='Voter ID')
    mobile_no = fields.Char(string="Mobile No")
    email = fields.Char(string='Email')
