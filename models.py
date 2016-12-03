# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Book(models.Model):
    _name = 'homelibrary.book'
    title = fields.Char(required=True, string='Título')
    rack = fields.Integer(required=True, string='Estantería')
    author_id = fields.Many2one('homelibrary.author', string='Autor')

class Author(models.Model):
    _name = 'homelibrary.author'
    name = fields.Char(required=True, string='Nombre')
    book_ids = fields.One2many('homelibrary.book', 'author_id', string='Libros del autor')
     
