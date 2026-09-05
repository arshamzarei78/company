from odoo import models, fields, api


class CompanyRequestLine(models.Model):
    _name = 'company.request.line'
    _description = 'Company Order Line'

    request_id = fields.Many2one('company.request',string='درخواست',required=True)

    tankhah_id = fields.Many2one('company.request',string='غذا',required=True)

    quantity = fields.Integer(string='تعداد',required=True,default=1)

    total = fields.Float(string='مجموع',compute='_compute_total')


    @api.depends('tankhah_id.price', 'quantity')
    def _compute_total(self):
        for records in self:
           records.total = records.tankhah_id.price * records.quantity













