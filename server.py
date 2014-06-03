#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""server.py: TODO"""

import bottle as app

import controllers

@app.get('/')
def index():
    return app.template('index', data='Hello World!')

@app.route('/<controller>/<action>', method=['GET', 'POST'])
def serve(controller, action):
    template_path = '{0}/{1}.tpl'.format(controller, action)
    class_object = getattr(controllers, controller.title())
    class_method = getattr(class_object(), action)()
    return app.template(template_path, data=class_method)

app.run()
