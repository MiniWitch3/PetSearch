# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

from gluon import utils as gluon_utils
import json
import time

def index():
    pet_id = gluon_utils.web2py_uuid()
    return dict(pet_id=pet_id)

def get_pets():
    condition_list = []
    qset = db()
    user_selection = request.vars.get('user_selection[]') or request.vars.get('user_selection') or []
    if isinstance(user_selection, (str, unicode)):
        user_selection = [user_selection]


    for j in user_selection[0:]:
        if j == "house_trained": qset=qset(db.pets.id > 0)
    pet_dict = qset.select()

    #pet_dict = db((db.pets.house_trained == request.vars.house_trained) &
    #             (db.pets.kid_friendly == request.vars.kid_friendly) &
    ###          (db.pets.indoor_pet == request.vars.indoor_pet) &
    #         (db.pets.frequent_exercise == request.vars.frequent_exercise) &
    #        (db.pets.infrequent_exercise == request.vars.infrequent_exercise) &
    #       (db.pets.young_pet == request.vars.young_pet) &
    #      (db.pets.older_pet == request.vars.older_pet)).select()
    return dict(pet_dict=pet_dict)

def addpet():
    form = SQLFORM(db.pets)
    if form.process().accepted:
       session.flash = T('A new pet has been added.')
       redirect(URL('index'))
    else:
       session.flash = T('Please fill out all that is necessary.')
    return dict(form=form)

@auth.requires_signature
def edit():
    pets = db.pets(request.args(0))
    if pets is None:
        session.flash = T('This pet is unavailable.')
        redirect(URL('index'))
    if form.process().accepted:
        session.flash = T('The pet profile has been updated.')
        redirect(URL('pets', args=[pets.id]))
    return dict(form=form)

@auth.requires_signature
def delete():
    deleted = db.pets(request.args(0))
    if deleted is None:
        session.flash = T('This pet is unavailable.')
        redirect(URL('index'))
    db(db.pets.id == deleted.id).delete()
    session.flash = T('The pet profile has been removed.')
    redirect(URL('index'))

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

