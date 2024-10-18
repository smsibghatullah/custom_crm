from odoo import models,fields

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def search_all_companies(self):
        return self.sudo().search([])

    def search(self, args, offset=0, limit=None, order=None, count=False):
            context = self.env.context
            user = self.env.user
            allowed_company_ids = user.company_ids.ids
            selected_company_id = user.company_id.id
            if context.get('search_default_all_companies'):
                print (allowed_company_ids,' hhhhhhhhhhhhhhhhhhhhhhhhhh ')
                args += [('company_id', 'in', allowed_company_ids)]  # Ensure all company records are included
                return super(CRMLead, self.sudo()).search(args, offset, limit, order, count)
            print ('ssssssssssssssssssssssssssssssss')
            args += [('company_id', '=', selected_company_id)]  # Ensure all company records are included
            return super(CRMLead, self).search(args, offset, limit, order, count)


class CRMCreateWizard(models.TransientModel):
    _name = 'crm.create.wizard'
    _description = 'CRM Create Wizard'

    company_id = fields.Many2one('res.company', string='Company', required=True,default=lambda self: self.env.user.company_id.id)
    customer_price = fields.Float(string='Customer Price')
    name = fields.Char(string='Name', required=True)
    res_partner = fields.Many2one('res.partner', string='Customer', required=True)
    rating = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Rating')

    def create_crm_record(self):
        lead = self.env['crm.lead'].sudo().create({
        'company_id': self.company_id.id,
        'partner_id': self.res_partner.id,
        'planned_revenue': self.customer_price,
        'priority': self.rating,
        'name': self.name, 
        'stage_id':1 ,
        'Probability':10
        })
        return {
        'type': 'ir.actions.client',
        'tag': 'reload',
        }