# -*- coding: utf-8 -*-
from odoo import http


class VerticalHospital(http.Controller):

    @http.route('/pacientes/consulta/<string:sequence>', type='http', auth='public', website=True)
    def consulta_paciente(self, sequence, **kw):
        """
            Controlador para consultar la información de un paciente por su número de secuencia
            y devolverla en formato JSON 
        """
        
        patient = http.request.env['hospital.patients'].sudo().search([('sequence', '=', sequence)], limit=1)

        if not patient:
            return http.request.make_json_response({
                'error': 'Paciente no encontrado'
            })

        return http.request.make_json_response({
            'seq': sequence,
            'name': patient.name,
            'rnc': patient.rnc,
            'state': patient.state
        })
