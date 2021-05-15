# -*- coding: utf-8 -*-

from odoo import models, fields, api

class achat(models.Model):
    _name = 'achat.achat'

    article = fields.Char(string = "Article")
    unite = fields.Char(string = "Unité")
    quantite = fields.Char(string = "Quantité")
    valeur = fields.Char(string = "Valeur")

