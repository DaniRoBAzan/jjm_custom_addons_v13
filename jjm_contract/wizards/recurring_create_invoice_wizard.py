# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RecurringCreateInvoiceWizard(models.TransientModel):
    _name = 'recurring.create.invoice.wizard'

    def recurring_create_invoice(self):
        print ('active_id', self._context['active_id'])
        print ('active_ids', self._context['active_ids'])
        invoices = self.env['contract.contract'].browse(self._context['active_ids'])
        for invoice in invoices:
            print ('creando invoice %s'%(invoice))
            invoice.recurring_create_invoice()