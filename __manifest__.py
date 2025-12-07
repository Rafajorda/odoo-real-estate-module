# -*- coding: utf-8 -*-
{
    'name': "Real Estate Management",

    'summary': """
    Real Estate Management Module""",

    'description': """
    Real Estate Management Module for managing properties, agents, and clients.
    """,
    'author': "Rafa Jorda",
    'website': "",
    #Indicamos que es una aplicación
    'application': True,

    # En la siguiente URL se indica que categorias pueden usarse
    # https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoria Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de modulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del modulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_tag_views.xml',
        'views/estate_menus.xml',
    ]
}
