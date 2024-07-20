from odoo import api, fields, models, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Doctor Records"
    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender", tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    active = fields.Boolean(default=True, tracking=True)


    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor')
        result = super(HospitalDoctor, self).create(vals)
        return result