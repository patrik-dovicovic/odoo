# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmTesting(models.Model):
	_name = "sdm.testing"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	name = fields.Char(required="True",string='názov',tracking=True)
	date = fields.Date(required="True",string='dátum',tracking=True)
	season_id = fields.Many2one(comodel_name="sdm.season", required="True",string='sezóna',tracking=True)
	current_testing = fields.Boolean(string="aktualne testovanie",tracking=True)

	@api.constrains('current_testing')
	def _change_current_testing(self):
		if self.current_testing:
			testings = self.env['sdm.testing'].search([('id', '!=', self.id)])
			for testing in testings:
				testing.current_testing = False
	
	_sql_constraints = [
		('sdm_testing_unique', 'UNIQUE (name)',  'Nazov uz existuje.')
	]
