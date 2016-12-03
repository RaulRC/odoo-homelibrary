# -*- coding: utf-8 -*-
from openerp import http

# class Homelibrary(http.Controller):
#     @http.route('/homelibrary/homelibrary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/homelibrary/homelibrary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('homelibrary.listing', {
#             'root': '/homelibrary/homelibrary',
#             'objects': http.request.env['homelibrary.homelibrary'].search([]),
#         })

#     @http.route('/homelibrary/homelibrary/objects/<model("homelibrary.homelibrary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('homelibrary.object', {
#             'object': obj
#         })