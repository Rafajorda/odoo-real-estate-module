# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    
    # SQL constraints
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'A property type name must be unique.')
    ]

    name = fields.Char(required=True)
