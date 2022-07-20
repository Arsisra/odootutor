from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseRequisitionReceived(models.Model):
    _inherit = 'purchase.requisition.line'


    qty_received = fields.Float(compute='_compute_received_qty', string='Received Quantities')
    
    

    @api.depends('requisition_id.purchase_ids.state')
    def _compute_received_qty(self):
        line_found = set()
        for line in self:
            total = 0.0
            for po in line.requisition_id.purchase_ids.filtered(lambda purchase_order: purchase_order.state in ['purchase', 'done']):
                for po_line in po.order_line.filtered(lambda order_line: order_line.product_id == line.product_id):
                    if po_line.product_uom != line.product_uom_id:
                        total += po_line.product_uom._compute_quantity(po_line.qty_received, line.product_uom_id)
                    else:
                        total += po_line.qty_received
            if line.product_id not in line_found :
                line.qty_received = total
                line_found.add(line.product_id)
            else:
                line.qty_received = 0


class PurchaseRequisitionTotal(models.Model):
    _inherit = 'purchase.requisition'

    ordered_total = fields.Float(compute='_compute_total_order', string="Order Total" )
    received_total = fields.Float(compute='_compute_total_order', string="Receive Total" )

    @api.depends('line_ids.qty_ordered','line_ids.qty_received')
    def _compute_total_order(self):
        for request in self:
            ordered_total = received_total = 0.0
            for line in request.line_ids.filtered(lambda lines: lines.requisition_id.id == request.id):
                ordered_total += line.qty_ordered
                received_total += line.qty_received
            request.update({
                'ordered_total': ordered_total,
                'received_total': received_total,
            })


    
