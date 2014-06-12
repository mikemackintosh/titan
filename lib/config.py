#!/usr/bin/env python
"""
This is the config for Titan
"""
import ConfigParser
from os import path
from sys import argv,exit

def TiConfig( config_file):
    config = {}
    if path.isfile(config_file):
        cp = ConfigParser.ConfigParser()
        cp.read(config_file)
        for section in cp.sections():
            config[section] = {}
            for option in cp.options(section):
                config[section][option] = cp.get(section, option)
    else:
        exit('Failed to load configuration file, please check permissions')

    return config