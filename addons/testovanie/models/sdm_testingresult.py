# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmTestingresult(models.Model):
	_name = "sdm.testingresult"

	players_id = fields.Many2one(comodel_name="sdm.player", required="True",string='hráč')
	testing_id = fields.Many2one(comodel_name="sdm.testing", required="True",string='testovanie')
	discipline_id = fields.Many2one(comodel_name="sdm.discipline", required="True",string='disciplína')
	value = fields.Float(required="True",string='hodnota')

	_sql_constraints = [
			('testing_results_unique', 'UNIQUE (players_id,testing_id,discipline_id)',  'Kombinacia (hrac,testovanie,disciplina) je uz vytvorena.')
		]

