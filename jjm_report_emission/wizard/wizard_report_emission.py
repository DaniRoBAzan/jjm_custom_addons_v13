# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmissionReportWizard(models.TransientModel):
    _name = 'jjmemission.report.wizard'

    month = fields.Selection(
        [('1', '1- Enero'),
         ('2', '2- Febrero'),
         ('3', '3- Marzo'),
         ('4', '4- Abril'),
         ('5', '5- Mayo'),
         ('6', '6- Junio'),
         ('7', '7- Julio'),
         ('8', '8- Agosto'),
         ('9', '9- Septiembre'),
         ('10', '10- Octubre'),
         ('11', '11- Noviembre'),
         ('12', '12- Diciembre')],
        required=True,
        default='1',
        string="Mes"
    )
    collector = fields.Many2one('res.partner', "Cobrador", domain=[("is_collector", "=", True)])

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'month': self.month,
                'collector': self.collector.id,
            },
        }
        # ref(nombre_modulo.reporte_id)
        return self.env.ref('jjm_report_emission.jjm_emission_report').report_action(self, data=data)

