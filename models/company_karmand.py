from odoo import models, fields,


class CompanyKarmand(models.Model):
    _name = 'company.karmand'
    _description = "company karmand"

    name = fields.Char(required=True, string='نام و نام خانوادگی')
    description = fields.Char(required=True, string='توضیحات')
    code = fields.Char(required=True, string='کد کارمندی')
    gender = fields.Selection([('male','مرد') , ('female', 'زن')], string='جنسیت')
    birth_date = fields.Date(string = "تاریخ تولد",required=True, default=fields.Date.today())
    phone = fields.Char(required=True, string = "شماره تلفن")
    address = fields.Text(string = "آدرس")
    is_active = fields.Boolean(string = "فعال")





