# -*- coding: utf-8 -*-
from odoo import fields,models,api
import numpy as np
import logging
_logger = logging.getLogger(__name__)

class SdmStatistic(models.Model):
    _name = "sdm.statistic"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    type = fields.Selection([('all_time', 'all time'),('this_testing', 'this testing')],required="True",string='typ',readonly=True)
    testing_id = fields.Many2one(comodel_name="sdm.testing",string='testovanie',readonly=True)
    discipline_id = fields.Many2one(comodel_name="sdm.discipline", required="True",string='disciplína',readonly=True)
    age = fields.Char(string="Vek",readonly=True)

    minimum = fields.Float(string="minimum",readonly=True,group_operator="avg")
    lower_quartile = fields.Float(string="lower_quartile",readonly=True,group_operator="avg")
    median = fields.Float(string="median",readonly=True,group_operator="avg")
    upper_quartile = fields.Float(string="upper_quartile",readonly=True,group_operator="avg")
    maximum = fields.Float(string="maximum",readonly=True,group_operator="avg")
    count = fields.Integer(string="count",readonly=True,group_operator="sum")
    invalid_values = fields.Integer(string="invalid_values",readonly=True,group_operator="sum")
    all_values = fields.Char(string="all values",readonly=True,group_operator=False)

    def calculate_values(self,values):
        values.sort()
        checked_values = [num for num in values if num > 0]
        if checked_values:
            minimum = np.min(checked_values)
            lower_quartile = np.percentile(checked_values, 25)
            median = np.percentile(checked_values, 50)
            upper_quartile = np.percentile(checked_values, 75)
            maximum = np.max(checked_values)
            count = len(checked_values)
        else:
            minimum = 0
            lower_quartile = 0
            median = 0
            upper_quartile =0
            maximum = 0
            count = 0
        invalid_values = len(values) - len(checked_values)
        values_string = ["%.3f" % number for number in values]

        return {'minimum': minimum, 'lower_quartile': lower_quartile, 'median': median, 'upper_quartile': upper_quartile, 'maximum': maximum, 'count': count, 'invalid_values': invalid_values, 'all_values': values_string}

    def create_update_records(self,search_params,values):
        existing_record = self.search(search_params)
        if existing_record:
            existing_record.write(values)
        else:
            self.create(values)

    @api.model
    def create_record(self, age, testing_id, discipline_id):
        # this testing
        this_testing_records_search_params = [('age', '=', age),('testing_id', '=', testing_id),('discipline_id', '=', discipline_id)]
        this_testing_records = self.env['sdm.testingresult'].search(this_testing_records_search_params)
        this_testing_values = self.calculate_values([record.value for record in this_testing_records])

        self.create_update_records(
            [('type', '=', 'this_testing'),('age', '=', age), ('testing_id', '=', testing_id), ('discipline_id', '=', discipline_id)],
            {**this_testing_values,'type':'this_testing','age': age,'testing_id': testing_id,'discipline_id': discipline_id}
        )

        # all time
        all_time_records_search_params = [('age', '=', age),('discipline_id', '=', discipline_id)]
        all_time_records = self.env['sdm.testingresult'].search(all_time_records_search_params)
        all_time_values = self.calculate_values([record.value for record in all_time_records])

        self.create_update_records(
            [('type', '=', 'all_time'),('age', '=', age), ('discipline_id', '=', discipline_id)],
            {**all_time_values,'type':'all_time','age': age,'discipline_id': discipline_id}
        )
    
    def button_delete_create(self):
        self.unlink()
        results = self.env['sdm.testingresult'].search([])
        for result in results:
            self.create_record(result.age, result.testing_id.id, result.discipline_id.id)



    # _sql_constraints = [
    #     ('statistic_unique', 'UNIQUE (age,testing_id,discipline_id)',  'Kombinacia (vek,testovanie,disciplina) je uz vytvorena.')
    # ]