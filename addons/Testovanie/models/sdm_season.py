# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmSeason(models.Model):
	_name = "sdm.season"

	name = fields.Char(required="True",string='názov')
	date_start = fields.Date(required="True",string='začiatok sezóny')
	date_end = fields.Date(required="True",string='koniec sezóny')