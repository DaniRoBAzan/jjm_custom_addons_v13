# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date, datetime, timedelta

class ContractContract(models.Model):
    _inherit = 'contract.contract'

    def _set_contracts_states(self):
        # BUSCAMOS TODOS LOS CONTRATOS
        contract_obj = self.env['contract.contract'].search([('state', '=', 'confirm')])
        for contract in contract_obj:
            # POR CADA CONTRATO BUSCAMOS AL CLIENTE ASOCIADO
            partner_obj = self.env['res.partner'].search([('id', '=', contract.partner_id.id)])
            for partner in partner_obj:
                # POR CADA CLIENTE VEMOS SI TIENE FACTURAS IMPAGAS
                invoice_obj = self.env['account.move'].search([
                    ('partner_id', '=', partner.id),
                    ('invoice_origin', '=', contract.name),
                    ('amount_residual', '>', 0)
                ])
                # SI TIENE MAS DE 3 LE CAMBIO EL ESTADO AL CONTRATO!
                if len(invoice_obj) >= 3:
                    contract.state = "cancel"
                    contract.jjm_contract_state = "Baja"
                    contract.jjm_motivo_baja = "Baja dada por sistema, el cliente supera las 3 facturas vencidas."
