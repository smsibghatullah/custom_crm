from odoo import api, models, _
from googletrans import Translator
import logging

_logger = logging.getLogger(__name__)

class Users(models.Model):
    _inherit = "res.users"


    @api.multi
    def write(self, vals):
        res = super(Users, self).write(vals)
        translator = Translator()
        print(vals,"ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        if 'lang' in vals:
            new_lang = vals['lang']
            stages = self.env['crm.stage'].search([]) 
            print(new_lang,stages,"ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
            for stage in stages:
                translated = translator.translate(stage.name, dest=new_lang)
                print(translated,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                stage.write({'name': translated.text,'display_name':translated.text})
        else :
            new_lang =self.lang
            stages = self.env['crm.stage'].search([]) 
            for stage in stages:
                translated = translator.translate(stage.name, dest=new_lang)
                print(translated,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                stage.write({'name': translated.text,'display_name':translated.text})
        return res
   
       
   