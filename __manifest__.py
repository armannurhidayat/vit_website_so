# -*- coding: utf-8 -*-
{
    'name': "vit_website_so",

    'summary': """
        Sale Orders Website dengan Ajax
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Arman Nur Hidayat <vitraining.com>",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/web_asset.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}