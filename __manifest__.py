# -*- coding: utf-8 -*-
{
    'name': "Raprapa",

    'summary': """
        Final raprapa application""",

    'description': """
        Through this module u can create new members for rastriya prajatantra party
    """,

    'author': "Shangrila",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/index.xml',
        'views/payment.xml',
        'views/otp_verify.xml',
        'views/otp_unverified.xml',
        'views/id_card.xml',
    ],
    'installable': True,
    'auto_install': False,
}
