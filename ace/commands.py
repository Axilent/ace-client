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
