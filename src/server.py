#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 02:52:57 2021

@author: Hrishikesh Terdalkar
"""

###############################################################################

import re
import os
import json
import datetime

from flask import Flask, render_template, url_for, redirect
# from natsort import natsorted

from settings import CONFIG as cfg

###############################################################################


def parse_json(filename):
    with open(filename, encoding='utf-8', mode='r') as f:
        data = json.load(f)
    return data

###############################################################################

OBJECTIVES = parse_json(cfg.OBJECTIVES_FILENAME)
MODELS = parse_json(cfg.MODELS_FILENAME)
DATASETS = parse_json(cfg.DATASETS_FILENAME)

###############################################################################

webapp = Flask(__name__)
webapp.config['SECRET_KEY'] = cfg.SECRET_KEY
webapp.url_map.strict_slashes = False

###############################################################################

def zfill(int_or_str, length):
    return str(int_or_str).zfill(length)

###############################################################################


@webapp.context_processor
def inject_globals():
    """Available in each path"""
    return {
        'title': 'NLTM Interlingua',
        'header': 'NLTM Interlingua',
        'navigation': {
            'about': (show_about.__qualname__, 'About'),
            'samanvaya': (cfg.SAMANVAYA_URL, 'Samanvaya', True),
            'datasets': (show_datasets.__qualname__, 'Datasets'),
            'models': (show_models.__qualname__, 'Models'),
        },
        'now': datetime.datetime.utcnow(),
    }
    

###############################################################################
# Views


@webapp.route("/")
def show_about():
    data = {'title': 'About'}
    data['objectives'] = parse_json(cfg.OBJECTIVES_FILENAME)
    return render_template("about.html", data=data)


@webapp.route("/team/")
def show_team():
    data = {'title': 'Team'}
    data['team'] = parse_json(cfg.TEAM_FILENAME)
    return render_template('team.html', data=data)


@webapp.route("/datasets/")
def show_datasets():
    data = {'title': 'Datasets'}
    data['datasets'] = parse_json(cfg.DATASETS_FILENAME)
    return render_template("datasets.html", data=data)


@webapp.route("/models/")
def show_models():
    data = {'title': 'Models'}
    data['models'] = parse_json(cfg.MODELS_FILENAME)
    return render_template("models.html", data=data)


###############################################################################


if __name__ == '__main__':
    import socket

    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = '2605'

    webapp.run(host=host, port=port, debug=True)
