# -*- coding: utf-8 -*-
from odoo import models, Command


class EstatePropertyAccount(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        # First call the original behavior
        res = super().action_sold()

        # Create invoices for sold properties when possible
        Journal = self.env['account.journal']
        Move = self.env['account.move']

        # Try to find a sale journal
        journal = Journal.search([('type', '=', 'sale')], limit=1)

        for record in self:
            partner = record.buyer_id
            if not partner:
                # No buyer, skip invoice creation
                continue

            # Choose a price to base fees on
            price = record.selling_price or record.best_price or record.expected_price or 0.0

            lines = [
                Command.create({
                    'name': f'Commission (6%) for {record.name}',
                    'quantity': 1.0,
                    'price_unit': price * 0.06,
                }),
                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1.0,
                    'price_unit': 100.0,
                }),
            ]

            move_vals = {
                'partner_id': partner.id,
                'move_type': 'out_invoice',
                'journal_id': journal.id if journal else False,
                'invoice_line_ids': lines,
            }

            Move.create(move_vals)

        return res
