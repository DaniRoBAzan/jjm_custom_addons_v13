# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class ReportProductionReportView(models.AbstractModel):
    _name = 'report.jjm_report_production.production_report_template_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        supervisor = data['form']['supervisor']
        consultant = data['form']['consultant']
        campaign = data['form']['campaign']
        array = []
        encabezado = []
        args1 = []
        args = []
        contador = 0
        importe = 0

        if supervisor:
            supervisor = self.env['res.partner'].browse(int(supervisor))
            args1.append(('jjm_manager', '=', int(supervisor)))
            if consultant:
                args1.append(('id', '=', int(consultant)))
                consultant = self.env['res.partner'].search(args1) or False
                args.append(('consultant_id', '=', consultant.id))

        else:
            consultant = self.env['res.partner'].browse(int(consultant))
            args.append(('consultant_id', '=', consultant.id))

        if campaign:
            campaign_obj = self.env['contract.campaign'].browse(int(campaign))
            args.append(('campaign_id', '=', campaign_obj.id))
            if campaign_obj.current:
                current = "Abierto"
            else:
                current = "Cerrado"

        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'campaign': campaign_obj.name,
            'supervisor': supervisor and supervisor.name,
            'consultant': consultant and consultant.name or '',
            'current': current,
            'user': self.env.user.name,
        }
        args.append(('state', '!=','cancel')) #traer contrato en estado confirmado
        contract_obj = self.env['contract.contract'].search(args, order='partner_id desc') or False
        if contract_obj is False:
            raise ValidationError(
                "Verifique los datos ingresados nuevamente, no se encontraron contratos asociados!")

        for contract in contract_obj:
            # contador += 1
            lineas = {
                # 'numero': contador,
                'cliente': contract.partner_id.name,
                'contrato': contract.name,
                'forma_pago': contract.method_payment_id.name,
                'fecha_inicio': contract.date_accession.strftime('%d-%m-%Y'),
                'importe': sum(contract.mapped("contract_line_fixed_ids.price_subtotal")) or False,
                'consultant': contract.consultant_id,
                'currency_id': self.env.company.currency_id,
            }
            array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
            'currency_id': self.env.company.currency_id,
        }
