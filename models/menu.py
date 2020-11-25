# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(IMG(_src=URL('static', 'images/favicon.ico'), _href=URL('products', 'view')))

response.menu = [
    (T('Productos'), False, URL('products', 'view'), []),
    (T('Agregar producto'), False, URL('products', 'create'), [])
]
