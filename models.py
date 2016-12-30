# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Homelibrary(models.Model):
    _name = 'homelibrary.homelibrary'
    owner = fields.Many2one('res.users', string='Propietario')
    name = fields.Char(required=True, string='Nombre')

class Book(models.Model):
    _name = 'homelibrary.book'
    name = fields.Char(required=True, string='Título')
    description = fields.Text(string='Descripción adicional')
    rack = fields.Integer(required=False, string='Estantería')
    author_id = fields.Many2one('homelibrary.author', string='Autor')

class Author(models.Model):
    _name = 'homelibrary.author'
    name = fields.Char(required=True, string='Nombre')
    book_ids = fields.One2many('homelibrary.book', 'author_id', string='Libros del autor')

class Video(models.Model):
    _name = 'homelibrary.video'
    name = fields.Char(required=True, string='Título')
    description = fields.Text(string='Descripción adicional')
    rack = fields.Integer(required=False, string='Estantería')

