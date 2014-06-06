#!/usr/bin/env python
"""
This is the launcher for Titan
"""

import logging
from subprocess import Popen, PIPE
from os import listdir
from sys import argv
from os.path import dirname, realpath, isfile, join, splitext, basename
from collections import namedtuple
from itertools import chain
from socket import gethostname
from time import strftime, gmtime

# Types
TiLanguage = namedtuple("TiLanguage", "supported_extensions execution_string")

# Configurations
logging.basicConfig(format='%(message)s', level=logging.INFO)

# Contants
CURRENT_DIR = dirname(realpath(__file__))

PUBLIC_MODULES_DIR = join(CURRENT_DIR, "modules/public/")
PRIVATE_MODULES_DIR = join(CURRENT_DIR, "modules/private/")

# Log Directory
LOG_DIR = join(CURRENT_DIR, "log")

# Report Directory
REPORT_DIR = join(CURRENT_DIR, "reports")

# Get Hostname
HOSTNAME = gethostname()

# Get Runtime
DATE = strftime("%Y-%m-%dT%H:%M:%S%z", gmtime())

# Get modules
MODULES = [
    join(PUBLIC_MODULES_DIR, fname) for fname in listdir(PUBLIC_MODULES_DIR)\
    if isfile(join(PUBLIC_MODULES_DIR, fname))
]

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

SUPPORTED_LANGUAGES = [
    PYTHON_LANGUAGE,
    RUBY_LANGUAGE,
    BASH_LANGUAGE,
    PHP_LANGUAGE,
]

# Set Debugging
test = False

# Functions
def log_line(log_name, line):
    """log_line accepts a line a returns a properly formatted log line"""
    return "%s %s by[%s]: %s" % (
        DATE,
        HOSTNAME,
        log_name,
        line,
    )

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
            if test:
                print "Module: %s, Lang: %s, Name: %s" % (module, current_lang, mod_name)
            
            #spawn_module(module, current_lang, mod_name)

if __name__ == "__main__":
    if "--test" in argv[1:]:
        test = True

    launch_modules()
