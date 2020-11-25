# -*- coding: utf-8 -*-

def index(): return dict(message="hello from products.py")

@auth.requires_login()
def view():
    products = db(db.products).select()
    return locals()

@auth.requires_login()
def create():
    form = SQLFORM(db.products)
    if form.process().accepted:
        session.flash = 'Producto aceptado'
        redirect(URL('view'))
    elif form.errors:
        response.flash = 'Complete bien los datos del producto'
    return locals()
