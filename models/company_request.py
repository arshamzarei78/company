from importlib.metadata import requires

from odoo import models,fields,api

class ResturantRequest(models.Model):
    _name = "company.Request"
    _description = "درخواست ها"

    karmand_id      = fields.Many2one("company.karmand", string="کارمند")
    Request_line_ids   = fields.One2many('company.Request.line','Request_id',string='درخواست')
    description      = fields.Text(string="توضیحات تکمیلی")
    date = fields.Date(string='تاریخ تنظیم', default=fields.Date.today())

    status = fields.Selection([('pending', 'تایید نشده'),('confirmed', 'تایید شده'),], string='وضعیت', default='pending')

    total_amount = fields.Float(string='مجموع کل سفارشات', compute='_compute_total_amount')

    @api.depends('Request_line_ids.total')
    def _compute_total_amount(self):
        for records in self:
            records.total_amount = sum(records.Request_line_ids.mapped('total'))
















