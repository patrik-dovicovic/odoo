# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class SdmDiscipline(models.Model):
	_name = "sdm.discipline"

	name = fields.Char(required="True",string='názov')
	aggregation = fields.Selection([('min','Min'),('max','Max')],required="True",default='min',string='agregácia')