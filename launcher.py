#!/usr/bin/env python
"""
This is the launcher for Titan
"""

import logging
import ConfigParser
from subprocess import Popen, PIPE
from os import listdir,walk,path,environ
from sys import argv,exit
from os.path import dirname, realpath, isfile, join, splitext, basename
from collections import namedtuple
from itertools import chain
from socket import gethostname
from time import strftime, gmtime

# Into message
print "Titan - The Golden Apple For Mac Security"
print ""

# Get Titan Env and Config
TITAN_PATH = (environ.get('TITAN_PATH') or '/usr/local/titan/')
TITAN_CONFIG = join(TITAN_PATH, 'titan.conf')

# Config
Config = ConfigParser.SafeConfigParser()
if path.isfile(TITAN_CONFIG):
  Config.read(TITAN_CONFIG)
else:
  print "[!] Please create titan.conf"
  exit()

# Types
TiLanguage = namedtuple("TiLanguage", "supported_extensions execution_string")

# Configurations
logging.basicConfig(format='%(message)s', level=logging.INFO)

# Constants
CURRENT_DIR = dirname(realpath(__file__))

# Base Modules Dir
MODULES_DIR = join(CURRENT_DIR, "modules/")

# Log Directory
LOG_DIR = join(CURRENT_DIR, "logs")

# Report Directory
REPORT_DIR = join(CURRENT_DIR, "reports")

# Get Hostname
HOSTNAME = gethostname()

# Get Runtime
DATE = strftime("%Y-%m-%dT%H:%M:%S%z", gmtime())

# Define Module Packs
MODULE_PACKS = [
    join(MODULES_DIR, mod_pack) for mod_pack in listdir(MODULES_DIR) if mod_pack not in ["lib"]
]

# Define all of our modules
MODULES = []
for path in MODULE_PACKS:
    for root,dirs,files in walk(path):
        for f in (f for f in files if f not in [".gitkeep", "README"]):
            MODULES.append( join(root,f) )


PYTHON_LANGUAGE = TiLanguage(
    supported_extensions = [".py", ".pyc"],
    execution_string = "python",
)

RUBY_LANGUAGE = TiLanguage(
    supported_extensions = [".rb"],
    execution_string = "ruby"
)

BASH_LANGUAGE = TiLanguage(
    supported_extensions = [".bash", ".sh"],
    execution_string = "/bin/bash"
)

PHP_LANGUAGE = TiLanguage(
    supported_extensions = [".php"],
    execution_string = "php"
)

PHP_LANGUAGE = TiLanguage(
    supported_extensions = [".pl"],
    execution_string = "perl"
)

SUPPORTED_LANGUAGES = [
    PYTHON_LANGUAGE,
    RUBY_LANGUAGE,
    BASH_LANGUAGE,
    PHP_LANGUAGE,
    PERL_LANGUAGE,
]

# Set Debugging
testing_enabled = False

# Functions
def log_line(log_name, line):
    """log_line accepts a line a returns a properly formatted log line"""
    return "%s %s by[%s]: %s" % (
        DATE,
        HOSTNAME,
        log_name,
        line,
    )

# Spawn module, capture output
def spawn_module(module, current_lang, mod_name):
    """spawn_module executes an individual Titan module"""
    log_file = join(LOG_DIR, mod_name + ".log")

    command = list(chain(
        current_lang.execution_string.split(" "),
        [module],
    ))

    execution = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout = execution.stdout.readlines()
    stderr = execution.stderr.readlines()

    file_handler = open(log_file, "a")

    for stdout_line in stdout:
        file_handler.write(log_line(mod_name, stdout_line))

    for stderr_line in stderr:
        file_handler.write(log_line(mod_name, stderr_line))

# Detect Modules
def launch_modules():
    """launch_modules launches Titan's executable modules"""
    for module in MODULES:
        current_lang = None
        mod_name, ext = splitext(basename(module))

        for language in SUPPORTED_LANGUAGES:
            if ext in language.supported_extensions:
                current_lang = language
                break

        if current_lang is not None and isinstance(current_lang, TiLanguage):
            if testing_enabled:
                print "[D] Module: %s, Lang: %s, Name: %s" % (module, current_lang.execution_string, mod_name)
            
            spawn_module(module, current_lang, mod_name)

# Main Python Instructions
if __name__ == "__main__":
    if "--test" in argv[1:]:
        testing_enabled = True

    launch_modules()
