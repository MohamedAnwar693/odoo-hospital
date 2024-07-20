# -*- coding: utf-8 -*-
{
    'name': "odoo16-hospital",
    'author': "Mohamed Anwar",
    'website': 'www.odoo16.com',
    'summary': 'Odoo 16 Development',
    'sequence': -96,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctors.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
