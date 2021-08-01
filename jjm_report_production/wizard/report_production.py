# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class ReportProductionReportView(models.AbstractModel):
    #report.nombre modulo.template_id
    _name = 'report.jjm_report_production.production_report_template_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        consultant = data['form']['consultant']
        campaign = data['form']['campaign']
        array = []
        encabezado = []
        args = []
        contador = 0
        importe = 0

        if consultant:
            consultant = self.env['res.partner'].browse(int(consultant))
            args.append(('consultant_id', '=', consultant.id))

        if campaign:
            campaign_obj = self.env['contract.campaign'].browse(int(campaign))
            args.append(('campaign_id', '=', campaign_obj.id))
            if campaign_obj.current:
                current = "Abierto"
            else:
                current = "Cerrado"

        today = fields.Date.today()
        encabezado = {
            'today': today,
            'campaign': campaign_obj.name,
            'consultant': consultant and consultant.name or '',
            'current': current,
            'user': self.env.user.name,
        }

        contract_obj = self.env['contract.contract'].search(args, order='partner_id desc') or False
        if contract_obj is False:
            raise ValidationError(
                "Verifique los datos ingresados nuevamente, no hay contratos asociados a esta campana, para este asesor!")

        for contract in contract_obj:
            contador += 1
            lineas = {
                'numero': contador,
                'cliente': contract.partner_id.name,
                'contrato': contract.name,
                'fecha_inicio': contract.date_accession,
                'importe': sum(contract.mapped("contract_line_fixed_ids.price_subtotal")) or False,
                'consultant': contract.consultant_id,
            }
            array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
        }
