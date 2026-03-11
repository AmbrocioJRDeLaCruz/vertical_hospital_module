# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HospitalPatients(models.Model):
    """
        Modelo para gestionar los pacientes del hospital
    """
    _name = 'hospital.patients'
    _order = 'sequence desc'
    _description = 'Hospital Patients'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre y Apellido', required=True, tracking=True)
    sequence = fields.Char(readonly=True, index=True, tracking=True, copy=False, default=lambda self: _('New'),)
    treatments = fields.Many2one('hospital.treatments', string='Tratamiento',)
    code = fields.Char(string='Código', related='treatments.code')
    name_treatments = fields.Char(string='Nombre del tratamiento', related='treatments.name')
    rnc = fields.Char(string='RNC', tracking=True)
    per_treatments = fields.Char(string='Tratamientos realizados')
    date_registration = fields.Date(string='Fecha de registro', required=True)
    date_update = fields.Date(string='Fecha de actualizacion')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Alta'),
        ('cancelled', 'Baja'),
    ], string='Estado', default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        """
            Sobrescribe el método create para asignar un número de secuencia único a cada paciente creado
        """
        for vals in vals_list:
            if vals.get('sequence', _('New')) == _('New'):
                vals['sequence'] = self.env['ir.sequence'].next_by_code('hospital.patients')
        return super().create(vals_list)

    def action_print_report(self):
        """
        Acción para imprimir el reporte de consulta del paciente
        """
        self.ensure_one()
        return self.env.ref('vertical_hospital.action_report_consulta_paciente').report_action(self)

