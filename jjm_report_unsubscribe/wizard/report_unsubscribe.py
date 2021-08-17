# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class ReportUnsubscribeReportView(models.AbstractModel):
    _name = 'report.jjm_report_unsubscribe.unsubscribe_report_template_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        supervisor = data['form']['supervisor']
        consultant = data['form']['consultant']
        campaign = data['form']['campaign']
        array = []
        encabezado = []
        args1 = []
        args = []

        if date_start <= date_end:
            args = [('jjm_date_unsubscribe',
                        '>=', date_start),
                    ('jjm_date_unsubscribe',
                        '<=', date_end),
                    ]
        else:
            raise ValidationError(
                "La fecha inicial debe ser menor o igual a la fecha final!")

        if supervisor:
            supervisor = self.env['res.partner'].browse(int(supervisor))
            args1.append(('jjm_manager', '=', int(supervisor)))
            if consultant:
                args1.append(('id', '=', int(consultant)))
                consultant = self.env['res.partner'].search(args1) or False
                args.append(('consultant_id', '=', consultant.id))

        else:
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

        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'fecha_inicio': date_start,
            'fecha_fin': date_end,
            'campaign': campaign_obj.name,
            'supervisor': supervisor and supervisor.name,
            'consultant': consultant and consultant.name or '',
            'current': current,
            'user': self.env.user.name,
        }
        args.append(('state', '=', 'cancel'))
        contract_obj = self.env['contract.contract'].search(args, order='partner_id desc') or False
        if contract_obj is False:
            raise ValidationError(
                "No se han encontrado contratos con los datos ingresados! ")

        for contract in contract_obj:
            lineas = {
                'cliente': contract.partner_id.name,
                'contrato': contract.name,
                'fecha_baja': contract.jjm_date_unsubscribe.strftime('%d-%m-%Y'),
                'motivo': contract.jjm_motivo_baja or False,
                'consultant': contract.consultant_id,
            }
            array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
        }
