# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalTreatments(models.Model):
    """
        Modelo que representa los tratamientos realizados en el hospital
    """
    _name = 'hospital.treatments'
    _description = 'Hospital Treatments'

    name = fields.Char(string='Nombre del tratamiento', required=True)
    code = fields.Char(string='Código', required=True,)
    attending_physician = fields.Char(string='Medico tratante', required=True)


    @api.constrains('code')
    def _check_code(self):
        """
            Validar que el código no contenga '026'
        """
        for record in self:
            if '026' in (record.code or ''):
                raise ValidationError(_('El código no puede contener 026'))
