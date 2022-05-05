# -*- coding: utf-8 -*-
{
    'name': "Product price 2",

    'summary': """
        Agrega un nuevo campo para precio 2 en el from del producto
        """,

    'description': """
        Agrega un nuevo campo para precio 2 en el from del producto
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_view.xml"
    ],

}
