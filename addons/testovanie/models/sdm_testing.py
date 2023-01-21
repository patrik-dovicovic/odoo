# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmTesting(models.Model):
	_name = "sdm.testing"

	name = fields.Char(required="True",string='názov')
	date = fields.Date(required="True",string='dátum')
	season_id = fields.Many2one(comodel_name="sdm.season", required="True",string='sezóna')
