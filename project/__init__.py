# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
toolbar = DebugToolbarExtension(app)
from project.controllers import *




# # Database ====================================================================
from project.models.entity.employee import db, InfoModel
CONF_POSTGRES = {
    'user': 'admin',
    'pw': 'poon795193',
    'db': 'postgres',
    'host': '35.198.210.172',
    'port': '49157',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % CONF_POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# # =============================================================================