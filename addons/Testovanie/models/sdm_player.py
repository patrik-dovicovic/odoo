# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmPlayer(models.Model):
	_name = "sdm.player"

	custom_id = fields.Char(required="True",string='id')
	firstname = fields.Char(required="True",string='meno')
	lastname = fields.Char(required="True",string='priezvisko')
	birth = fields.Date(required="True",string='dátum narodenia')

	def name_get(self):
		result = []
		for rec in self:
			birth_year = rec.birth.strftime('%Y')
			result.append((rec.id, '%s %s (%s)' % (rec.firstname, rec.lastname, birth_year)))
		return result

	_sql_constraints = [
		('player_custom_id_unique', 'UNIQUE (custom_id)',  'ID uz existuje.')
	]



