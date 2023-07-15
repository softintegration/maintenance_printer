# -*- coding: utf-8 -*-

import ast

from datetime import date, datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    is_printer = fields.Boolean(string='Is printer',default=False)
    color_cpt = fields.Integer(string='Number of Colors')
    both_sides = fields.Boolean(string='Both sides', default=False)
    front_color_cpt = fields.Integer(string='Front number of Colors')
    back_color_cpt = fields.Integer(string='Back number of Colors')

