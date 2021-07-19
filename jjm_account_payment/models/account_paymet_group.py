
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"

    collector_id = fields.Many2one('res.partner', "Cobrador", store=True)
