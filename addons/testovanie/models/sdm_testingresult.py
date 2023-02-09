# -*- coding: utf-8 -*-
from odoo import fields,api,models,exceptions
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)

class SdmTestingresult(models.Model):
	_name = "sdm.testingresult"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	def _default_testing(self):
		testing = self.env['sdm.testing'].search([('current_testing', '=', True)])
		return testing


	player_id = fields.Many2one(comodel_name="sdm.player", required="True",string='hráč',tracking=True)
	testing_id = fields.Many2one(comodel_name="sdm.testing", required="True",string='testovanie',default=_default_testing,tracking=True)
	season_id = fields.Many2one(comodel_name='sdm.season', related='testing_id.season_id',store=True, string='Sezona',tracking=True)
	discipline_id = fields.Many2one(comodel_name="sdm.discipline", required="True",string='disciplína',tracking=True)
	value = fields.Float(required="True",string='hodnota', group_operator=False,digits = (42,3),tracking=True)
	age = fields.Char(readonly='True',default='0',compute='calculate_age',store='True',string='Vek pocas merania',tracking=True)
	team_id = fields.Many2one(comodel_name='sdm.team', string='Tim pocas merania',store='True',tracking=True)
	team_level = fields.Selection(related='team_id.level',string='Rocnik',store=True,tracking=True)
	correct_value = fields.Boolean(readonly=True,string="correct_value",store='True',compute="check_value",tracking=True)
	correct_value_string = fields.Char(readonly=True,string="Spravna hodnota",store='True',compute="compute_correct_value_string",tracking=True)

	@api.depends('player_id.birth', 'testing_id')
	def calculate_age(self):
		for rec in self:
			age = relativedelta(rec.testing_id.date, rec.player_id.birth).years
			if(age > 100):
				rec.age = 'undefined'
			else:
				rec.age = relativedelta(rec.testing_id.date, rec.player_id.birth).years


	@api.onchange('player_id')
	def onchange_player_id(self):
		for rec in self:
			rec.team_id = rec.player_id.current_team


	@api.depends('value')
	def check_value(self):
		for rec in self:
			if (rec.value > 0):
				rec.correct_value = True
			else:
				rec.correct_value = False

	@api.depends('correct_value')
	def compute_correct_value_string(self):
		for rec in self:
			if rec.correct_value:
				rec.correct_value_string = 'Spravna hodnota' 
			else:
				rec.correct_value_string = 'Nespravna hodnota' 

	@api.model
	def create(self, vals):
		record = super(SdmTestingresult, self).create(vals)
		self.env['sdm.statistic'].create_record(record.age, record.testing_id.id, record.discipline_id.id)
		current_testing = self.env['sdm.testing'].search([('current_testing', '=', True)])
		for rec in record:
			if not rec.team_id:
				if rec.testing_id.season_id.name == current_testing.season_id.name:
					rec.team_id = rec.player_id.current_team
			# check if discipline is valid
			if rec.team_id and rec.discipline_id:
				valid_discipline = self.env['sdm.test'].search([('level','=',rec.team_level),('discipline_id.name','=',rec.discipline_id.name)])
				if not valid_discipline:
					disciplines = []
					for discipline in self.env['sdm.test'].search([('level','=',rec.team_level)]):
						disciplines.append(discipline.discipline_id.name)
					raise exceptions.ValidationError("Disciplina %s nie je urcena pre tim %s (%s) u hraca %s. Povolene discipliny %s" % (rec.discipline_id.name,rec.team_id.name,rec.team_level,rec.player_id.name,disciplines))
		return record

	def write(self, vals):
		result = super(SdmTestingresult, self).write(vals)
		for record in self:
			self.env['sdm.statistic'].create_record(record.age, record.testing_id.id, record.discipline_id.id)
		return result
	

	_sql_constraints = [
			('sdm_testing_results_unique', 'UNIQUE (player_id,testing_id,discipline_id)',  'Kombinacia (hrac,testovanie,disciplina) je uz vytvorena.')
		]

