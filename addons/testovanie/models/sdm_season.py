# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmSeason(models.Model):
	_name = "sdm.season"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	name = fields.Char(required="True",string='názov',tracking=True)
	date_start = fields.Date(required="True",string='začiatok sezóny',tracking=True)
	date_end = fields.Date(required="True",string='koniec sezóny',tracking=True)
	current_season = fields.Boolean(string="aktualna sezona",tracking=True)

	@api.constrains('current_season')
	def _change_current_season(self):
		if self.current_season:
			seasons = self.env['sdm.season'].search([('id', '!=', self.id)])
			for season in seasons:
				season.current_season = False
	
	_sql_constraints = [
		('sdm_season_unique', 'UNIQUE (name)',  'Sezona uz existuje.')
	]