# -*- coding: utf-8 -*-

import ast

from datetime import date, datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    is_printer = fields.Boolean(string='Is printer',default=False)
    color_cpt = fields.Integer(string='Number of Colors')
    both_sides = fields.Boolean(string='Both sides', default=False)
    front_color_cpt = fields.Integer(string='Front number of Colors')
    back_color_cpt = fields.Integer(string='Back number of Colors')


    @api.constrains('both_sides','front_color_cpt','back_color_cpt')
    def _check_both_sides_color_cpt(self):
        for each in self:
            if each.both_sides and (not each.front_color_cpt or not each.back_color_cpt):
                raise ValidationError(_("Front number of Colors and Back number of Colors should be strictly positive in the case of both sides equipment"))


