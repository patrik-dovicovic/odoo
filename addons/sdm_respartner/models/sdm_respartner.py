
# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class ResPartner(models.Model):
	_inherit = 'res.partner'

	
	is_player = fields.Boolean(required=False,string='je hrac')
	is_trainer = fields.Boolean(required=False,string='je trener')
	is_parent = fields.Boolean(required=False,string='je rodic')
	edupage_id = fields.Char(required=True,string='Edupage id')

