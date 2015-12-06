# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

from gluon import utils as gluon_utils
import json
import time

def index():
    pet_id = gluon_utils.web2py_uuid()
    return dict(pet_id=pet_id)

def get_pets():
    pet_dict = db.pets.select(
        db.pets.house_trained == request.vars.get(house_trained) &
        db.pets.kid_friendly == request.vars.get(kid_friendly) &
        db.pets.pet_friendly == request.vars.get(pet_friendly) &
        db.pets.outdoor_pet == request.vars.get(outdoor_pet) &
        db.pets.indoor_pet == request.vars.get(indoor_pet) &
        db.pets.frequent_exercise == request.vars.get(frequent_exercise) &
        db.pets.infrequent_exercise == request.vars.get(infrequent_exercise) &
        db.pets.young_pet == request.vars.get(young_pet) &
        db.pets.older_pet == request.vars.get(older_pet)
    )
    return dict(pet_dict=pet_dict)

def addpet():
    form = SQLFORM(db.pets)

    if form.process().accepted:
       response.flash = 'A new pet has been added.'
       redirect(URL('default', 'index'))
    elif form.errors:
       response.flash = 'Please fix up your form.'
    else:
       response.flash = 'Please fill out all that is necessary.'
    return dict(form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


