from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Working ID", copy=False, index=True, default=lambda self: _('New'))
    start_time = fields.Datetime(string="Start Time", default=fields.Datetime.now)
    end_time = fields.Datetime(string="End Time")
    origin = fields.Char(string="Source Document", index=True)
    sale_order_line_id = fields.One2many('sale.order.line', 'working_id', string="Sale Order Line")
    product_id = fields.Many2one('product.product', string='Product', related='sale_order_line_id.product_id',
                                 domain="[('type', 'in', ['service'])]")
    partner_id = fields.Many2one('res.partner', string="Name")
    partner_address = fields.Text(string="Address", track_visibility='always')
    partner_phone = fields.Char(string="Phone", related='partner_id.phone')
    assign = fields.Many2one('hr.employee', string="Assign")
    company_id = fields.Many2one('res.company', string='Company')
    user_id = fields.Many2one('res.users', string='User', track_visibility='onchange', readonly=True,
                              state_working={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    state_working = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirm'),
        # ('completed', 'Completed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", readonly=True, default='draft')


    sale_id = fields.Many2one('sale.order', string="Sales Order")

    show_get_job = fields.Boolean(compute='_compute_show_get_job')
    show_completed = fields.Boolean(default=True)

    def action_confirm(self):
        print("action")
        print(self.show_get_job)
        for rec in self:
            rec.state_working = 'confirmed'
            print(rec.show_get_job)
        print(self._compute_show_get_job())
    print(show_get_job)

    def action_completed(self):
        print("Completed")
        print(self.show_completed)
        for rec in self:
            rec.state_working = 'done'
            # rec.write_working()
        print(self._compute_show_completed())


    def action_done(self):
        print("Done")
        for rec in self:
            rec.state_working = 'done'

    def action_cancel(self):
        print("Cancel")
        for rec in self:
            rec.state_working = 'cancel'

    @api.depends('state_working', 'sale_order_line_id')
    def _compute_show_completed(self):
        print("show_completed")
        for working in self:
            if working.state_working != 'done':
                working.show_completed = False
            else:
                working.show_completed = True
            print(self.show_completed)



    @api.depends('state_working', 'sale_order_line_id')
    def _compute_show_get_job(self):
        print("Hoạt động")
        for working in self:
            if working.state_working != 'draft':
                working.show_get_job = False
            else:
                working.show_get_job = True
        print(self.show_get_job)

    def _set_start_time(self):
        for working in self:
            if working.state_working in ('done', 'cancel'):
                raise UserError(_("You cannot change the Scheduled Date on a done or cancelled transfer."))
            # working.move_lines.write({'date': working.start_time})

    @api.model
    def create(self, vals):
        if vals.get('name') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('working.sequence') or _('New')
        result = super(Working, self).create(vals)
        result.env['mail.activity'].create({
                'res_model': 'working',
                'res_id': result.id,
                'res_model_id': result.env['ir.model']._get('working').id,
                'user_id': result.assign and result.assign.user_id and result.assign.user_id.id or None,
        })
        return result



