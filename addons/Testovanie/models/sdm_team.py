# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmTeam(models.Model):
	_name = "sdm.team"

	name = fields.Char(required="True",string='názov')
	level = fields.Selection([('U6','U6'),('U7','U7'),('U8','U8'),('U9','U9'),('U10','U10'),('U11','U11'),('U12','U12'),('U13','U13'),('U14','U14'),('U15','U15'),('U16','U16'),('U17','U17'),('U18','U18'),('U19','U19')],required="True",string='ročník')