# -*- coding: utf-8 -*-
from odoo import fields,models,api


class SdmPlayer(models.Model):
	_name = "sdm.player"
	_inherits = {'res.partner': 'partner_id'}
	_inherit = ['mail.thread', 'mail.activity.mixin']
	
	partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade', auto_join=True,string='Related Partner',tracking=True)
	birth = fields.Date(required="False",string='dátum narodenia',tracking=True)
	school = fields.Char(string='Skola',required=False,tracking=True)
	parent1 = fields.Many2one('res.partner', string='Rodic 1',tracking=True)
	parent2 = fields.Many2one('res.partner', string='Rodic 2',tracking=True)
	current_team = fields.Many2one('sdm.team', string='Aktualny tim',required=True,tracking=True)


	@api.model
	def create(self, vals):
		res = super(SdmPlayer, self).create(vals)
		res.partner_id.is_player = True
		return res

	def name_get(self):
		result = []
		for rec in self:
			birth_year = rec.birth.strftime('%Y')
			result.append((rec.id, '%s (%s)' % (rec.name, birth_year)))
		return result




