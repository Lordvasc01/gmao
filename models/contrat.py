from odoo import models, fields

class Contrat(models.Model):
    _name = 'contrat'

    code = fields.Char(string="Contrat",)
    desc = fields.Text(string="Description",)
    ss_traitant = fields.Char(string="Sous-Traitant",)
    etat = fields.Selection(selection=[('0','0.Ouvert'),('1','1.Annuel'),], string="Etat",)
    type_ct = fields.Selection(selection=[('0','0.Commande Ouverte'),('1','1.Annuel'),('2','2.Autres'),], string="Type",)
    entite = fields.Char(string="Entite",)
    valeur = fields.Float(string="Valeur",)
    date_deb = fields.Date(string="Date Déb.",)

    eqpts = fields.Many2many('topographie', 'contrats_equipements', 'contrat_id', 'equipement_id', string="Equipement",)