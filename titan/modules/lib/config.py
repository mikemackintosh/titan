#!/usr/bin/env python
"""
This is the config for Titan
"""
from os.path import dirname, realpath


config = {}

current_dir = dirname(realpath(__file__))
if "/Users" in current_dir:
    config['database'] = 'titan_hids.sqlite'
else:
    config['database'] = '/tmp/titan_hids.sqlite'

config['plist_check_keys'] = [
    'RunAtLoad',
    'WatchPaths',
    'KeepAlive',
    'StartInterval',
    'StartOnMount',
    'OnDemand',
    'QueueDirectories',
    'StandardInPath',
    'StandardOutPath',
    'StandardErrorPath',
    'Debug',
    'LaunchOnlyOnce',
    'Sockets',
    'OSAXHandlers',
    'LSEnvironment',
    'CFBundleVersion',
]

config['plist_check_keys_hash'] = [
    'Program',
    'ProgramArguments'
]

config['firewall_keys'] = [
    'allowsignedenabled',
    'firewallunload',
    'globalstate',
    'loggingenabled',
    'previousonstate',
    'stealthenabled',
    'version',
]


# Maintain backwards compatibility
Config = config
