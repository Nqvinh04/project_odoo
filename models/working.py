from odoo import fields, models, api, _


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Name")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    origin = fields.Many2one(string="Source Document")

    parent_name = fields.Many2one(string="Name")
    parent_address = fields.Many2one(string="Address")
    phone = fields.Integer(string="Phone")
    assign_id = fields.Many2one(string="Assign")
    state_working = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting'),
        ('assigned', 'Ready'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status")
    # sale_id = fields.Many2one(related='group_id.sale.order')
    sale_id = fields.Many2one('sale.order')

    completed_work = fields.Selection([
        ('incomplete', 'Incomplete'),
        ('completed', 'Completed')
    ], string="Completed", default=False)

    def action_cancel(self):
        print("Cancel")

    def action_completed(self):
        print("Completed")


