from odoo import api, fields, models



_STATES = [
    ('draft', 'Draft'),
    ('to_approve', 'To Approve'),
    ('approval1','Approve'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('done', 'Done')
]

        
    
class SaleOrder(models.Model):
    _inherit = "sale.order"   
    
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('approval1','Approve'),
        ('approval','Final Approval'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
    
    def button_app(self):
        self.write({'state':'approval'})

    
    @api.multi
    def approved1(self):
        self.action_confirm()    


    
