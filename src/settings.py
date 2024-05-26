#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 01 14:43:18 2021

@author: Hrishikesh Terdalkar
"""

import os
import glob

###############################################################################


class Configuration(dict):
    def __init__(self, *args, **kwargs):
        super(Configuration, self).__init__(*args, **kwargs)
        self.__dict__ = self


###############################################################################

CONFIG_PREFIX = 'NLTM_'
CONFIG = Configuration()

###############################################################################

CONFIG['SECRET_KEY'] = os.environ.get(
    f'{CONFIG_PREFIX}SECRET_KEY', 'nltm-interlingua'
)

CONFIG['SERVER_DIR'] = os.environ.get(
    f'{CONFIG_PREFIX}SERVER_DIR', os.path.dirname(os.path.realpath(__file__))
)

CONFIG['ABOUT_FILENAME'] = 'data/about.json'
CONFIG['TEAM_FILENAME'] = 'data/team.json'
CONFIG['DATASETS_FILENAME'] = 'data/datasets.json'
CONFIG['MODELS_FILENAME'] = 'data/models.json'

CONFIG['SAMANVAYA_URL'] = "https://sanskrit.iitk.ac.in/interlingua/samanvaya/"

###############################################################################
