# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmTest(models.Model):
	_name = "sdm.test"


	discipline_id = fields.Many2one(comodel_name="sdm.discipline", required="True",string='disciplína')
	level = fields.Selection([('U6', 'U6'),('U7', 'U7'),('U8', 'U8'),('U9', 'U9'),('U10', 'U10'),('U11', 'U11'),('U12', 'U12'),('U13', 'U13'),('U14', 'U14'),('U15', 'U15'),('U16', 'U16'),('U17', 'U17'),('U18', 'U18'),('U19', 'U19')],required="True",string='ročník')