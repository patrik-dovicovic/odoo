# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmDiscipline(models.Model):
	_name = "sdm.discipline"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	name = fields.Char(required="True",string='názov',tracking=True)
	aggregation = fields.Selection([('min','Min'),('max','Max')],required="True",default='min',string='agregácia',tracking=True)

	test_ids = fields.One2many(comodel_name="sdm.test", inverse_name="discipline_id",string='testy')

	_sql_constraints = [
			('sdm_discipline_unique', 'UNIQUE (name)',  'Nazov discipliny je uz pouzity.')
		]
