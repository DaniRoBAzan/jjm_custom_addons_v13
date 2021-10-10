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
        vendor = data['form']['consultant']
        campaign = data['form']['campaign']
        current = ' '

        array = []
        arg_supervisor = []
        arg_vendor = []
        arg_campaign = []
        arg_contrato = []

        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'user': self.env.user.name,
        }

        #FILTROS:

        if supervisor:
            supervisor = self.env['res.partner'].browse(int(supervisor)) or False
            arg_vendor.append(('jjm_manager', '=', supervisor.id))
        else:
            supervisor = self.env['res.partner'].search(arg_supervisor) or False

        if vendor:
            vendor = self.env['res.partner'].browse(vendor) or False
            arg_contrato.append(('consultant_id', '=', vendor.id))
        else:
            vendor = self.env['res.partner'].search(arg_vendor) or False
            arg_contrato.append(('consultant_id', 'in', vendor.ids))


        if campaign:
            arg_campaign.append(('id', '=', campaign))
            campaign = self.env['contract.campaign'].search(arg_campaign) or False
            arg_contrato.append(('campaign_id', '=', campaign.id))
        else:
            campaign = self.env['contract.campaign'].search(arg_campaign) or False


        arg_contrato.append(('state', '=', 'confirm'))
        contract_obj = self.env['contract.contract'].search(arg_contrato, order='partner_id desc') or False

        if contract_obj is False:
            raise ValidationError(
                "Verifique los datos ingresados nuevamente, no se encontraron contratos asociados!")

        for contract in contract_obj:
            if contract.campaign_id.current:
                current = "Abierto"
            else:
                current = "Cerrado"
            lineas = {
                'cliente': contract.partner_id and contract.partner_id.name or False,
                'contrato': contract and contract.name or False,
                'forma_pago': contract.method_payment_id and contract.method_payment_id.name or False,
                'fecha_inicio': contract.date_accession and contract.date_accession.strftime('%d-%m-%Y') or ' ',
                'importe': sum(contract.mapped("contract_line_fixed_ids.price_subtotal")) or False,
                'consultant': contract.consultant_id or False,
                'currency_id': self.env.company.currency_id or False,
                'campaign': contract.campaign_id and contract.campaign_id.name or ' ',
                'supervis': contract.consultant_id.jjm_manager and contract.consultant_id.jjm_manager.name or 'Maurice',
                'current': current or False,
            }
            array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
            'currency_id': self.env.company.currency_id,
        }
