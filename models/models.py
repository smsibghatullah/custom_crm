from odoo import models

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