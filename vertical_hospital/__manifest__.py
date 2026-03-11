# -*- coding: utf-8 -*-
{
    'name': "vertical_hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Ambrocio De La Cruz",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '17.0.0.0',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/hospital_patients_views.xml',
        'views/hospital_treatments_views.xml',
        'report/paperformat.xml',
        'report/report_action.xml',
        'report/hospital_patient_report.xml',
    ],

    'web_icon': 'vertical_hospital,static/description/icon.png',

    'installable': True,
    'application': True,
}

