# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"
    
    # SQL constraints
    _check_price = models.Constraint(
        'CHECK(price > 0)',
        'The offer price must be strictly positive.'
    )

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
    property_type_id = fields.Many2one(related="property_id.property_type_id", string="Property Type", store=True)

    @api.model_create_multi
    def create(self, vals_list):
        # Normalize input: vals_list can contain dicts, (0,0,vals) tuples, or nested lists
        create_items = []
        if isinstance(vals_list, dict):
            create_items = [vals_list]
        else:
            for item in vals_list:
                if isinstance(item, dict):
                    create_items.append(item)
                elif isinstance(item, (list, tuple)):
                    # pattern (0, 0, vals)
                    if len(item) == 3 and isinstance(item[2], dict):
                        create_items.append(item[2])
                    else:
                        # item might be a list of dicts
                        for sub in item:
                            if isinstance(sub, dict):
                                create_items.append(sub)

        # Validate each offer and update property state
        for vals in create_items:
            price = vals.get('price')
            prop_id = vals.get('property_id')
            if prop_id and price is not None:
                prop = self.env['estate.property'].browse(int(prop_id))
                if prop.offer_ids:
                    max_price = max(prop.offer_ids.mapped('price'))
                    try:
                        price_val = float(price)
                    except Exception:
                        price_val = price
                    if price_val <= max_price:
                        raise UserError('New offer must be higher than existing offers.')
                prop.state = 'offer_received'

        return super(EstatePropertyOffer, self).create(create_items)
    
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
            # Mark the property as offer accepted
            record.property_id.state = 'offer_accepted'
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
