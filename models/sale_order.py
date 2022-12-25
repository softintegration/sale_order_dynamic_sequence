# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        """ Inherit this method to add the dynamic prefix in the call of the sequence so that any dynamic sequence configuration can be detected"""
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].with_context(dynamic_prefix_fields=vals).next_by_code('sale.order', sequence_date=seq_date) or _('New')
        return super(SaleOrder, self).create(vals)

