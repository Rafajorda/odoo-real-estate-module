# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    
    # SQL constraints
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'A tag name must be unique.')
    ]

    name = fields.Char(required=True)
