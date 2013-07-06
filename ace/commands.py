"""
Commands for ACE client.
"""
from ace import config
from ace import client

def init(args):
    """
    Initializes the directory.
    """
    print 'Initializing environment.'
    config.init_environment(args)
    print 'Environment initialized'
    if not args.no_ping:
        print 'Testing connection...'
        client.ping_library()
        print 'Connection settings OK'

def dumpproject(args):
    """
    Dumps a project to a JSON file.
    """
    pass #TODO

def loadproject(args):
    """
    Loads a project from a JSON file.
    """
    pass # TODO
