from odoo import models, fields, api


class Member(models.Model):
    _name = 'raprapa.member'
    _description = 'Raprapa members'

    photo_filename = fields.Char(string='Photo Filename')
    membership_type = fields.Char(string='Membership Type')
    membership_duration = fields.Char(string='Membership Duration')

    paid = fields.Boolean(string='Paid', default=False)
    membership_date = fields.Date(string='Membership Date')
    expiry_date = fields.Date(string='Expiry Date')

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Date of birth')
    citizenship_number = fields.Char(string='Citizenship Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    voter_id = fields.Char(string='Voter ID')
    phone = fields.Char(string="Mobile No")
    email = fields.Char(string='Email')
    family_count = fields.Integer(string='Family Count', default=0)

    perm_province = fields.Char(string='Permanent Province')
    perm_district = fields.Char(string='Permanent District')
    perm_parliamentary_constituency_no = fields.Integer(string='Permanent Parliamentary Constituency No.')
    perm_state_assembly_constituency_no = fields.Integer(string='Permanent State Assembly Constituency No.')
    perm_ward_no = fields.Integer(string='Permanent Ward No.')
    perm_municipality = fields.Char(string='Permanent Municipality')
    perm_voting_center = fields.Char(string='Permanent Voting Center')

    current_province = fields.Char(string='Temporary Province')
    current_district = fields.Char(string='Temporary District')
    current_parliamentary_constituency_no = fields.Integer(string='Temporary Parliamentary Constituency No.')
    current_state_assembly_constituency_no = fields.Integer(string='Temporary State Assembly Constituency No.')
    current_ward_no = fields.Integer(string='Current Ward No.')
    current_municipality = fields.Char(string='Temporary Municipality')
    current_voting_center = fields.Char(string='Temporary Voting Center')

    father_or_mother_name = fields.Char(string="Father's/Mother's name")
    husband_or_wife_name = fields.Char(string="Husband's/Wife's name")

    education = fields.Selection([
        ('ten plus two', 'Ten plus two'),
        ('graduation', 'Graduation'),
        ('masters', "Master's Degree"),
        ('phd', 'Ph.D.'),
        ('other', 'Other'),
    ], string='Education')

    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ], string='Marital Status')

    religion = fields.Char(string='Religion')

    caste = fields.Selection([
        ('aadivasi', 'Aadivasi/Tribe'),
        ('dalit', 'Dalit'),
        ('madhesi', 'Madhesi'),
        ('muslim', 'Muslim'),
        ('backward_region', 'Backward Region'),
        ('disabled', 'Disabled'),
        ('others', 'Others'),
    ], string='Caste')

    past_responsibility = fields.Char(string='Past Responsibility')
    approver_name = fields.Char(string='Approver Name')
    approver_position = fields.Char(string='Approver Position')


