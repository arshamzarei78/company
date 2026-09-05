from odoo import models , fields , api

class CompanyTankhah(models.Model):
    _name = "company.tankhah"
    _description = "Company Tankhah"

    name = fields.Char(string="نام هزینه",required=True)
    price = fields.Float(string="هزینه",required=True)



