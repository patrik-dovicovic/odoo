# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmPlayerseason(models.Model):
	_name = "sdm.playerseason"

	players_id = fields.Many2one(comodel_name="sdm.player", required="True",string='hráč')
	season_id = fields.Many2one(comodel_name="sdm.season", required="True",string='sezóna')
	team_id = fields.Many2one(comodel_name="sdm.team", required="True",string='tím')


	_sql_constraints = [
		('player_seasons_unique', 'UNIQUE (players_id,season_id)',  'Hrac je uz zaradeny v time v danej sezone.')
	]