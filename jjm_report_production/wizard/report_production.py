# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
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

        if campaign:
            _logger.info('campaign %s' %(campaign))
            campaign_obj = self.env['contract.campaign'].browse(int(campaign))
            if campaign_obj.current:
                current = "Abierto"
            else:
                current = "Cerrado"

            if consultant:
                _logger.info('consultant %s' %(consultant))
                consultant_obj = self.env['res.partner'].browse(int(consultant))
                args.append(('campaign_id', '=', campaign_obj.id))
                args.append(('consultant_id', '=', consultant_obj.id))

                contract_obj = self.env['contract.contract'].search(args, order='partner_id desc') or False

                _logger.info('contract_obj %s' %(contract_obj))
                if contract_obj is False:
                    raise ValidationError(
                        "Verifique los datos ingresados nuevamente!")

                encabezado = {
                    'today': fields.Date.today(),
                    'campaign': campaign_obj.name,
                    'consultant': consultant_obj.name,
                    'current': current,
                }

                for contract in contract_obj:
                    contador += 1
                    lineas = {
                        'numero': contador,
                        'cliente': contract.partner_id.name,
                        'contrato': contract.name,
                        'fecha_inicio': contract.date_accession,
                        'importe': 1234,
                        # 'importe': sum(contract.contract_line_fixed_ids.price_subtotal),
                    }
                    array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
        }
