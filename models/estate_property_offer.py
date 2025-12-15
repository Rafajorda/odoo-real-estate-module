# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    
    # Action methods
    def action_accept(self):
        for record in self:
            # Check if another offer is already accepted for this property
            if record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted' and o.id != record.id):
                raise UserError("Another offer has already been accepted for this property.")
            
            record.status = 'accepted'
            # Set the selling price and buyer on the property
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
