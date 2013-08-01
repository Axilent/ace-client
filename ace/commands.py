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
    if args.library_key:
        print 'Testing connection...'
        client.ping_library(args.library_key)
        print 'Connection OK'

def dumpproject(args):
    """
    Dumps a project to a JSON file.
    """
    client.dump_project_data(args)

def loadproject(args):
    """
    Loads a project from a JSON file.
    """
    client.load_project_data(args)

def addproject(args):
    """
    Adds a project definition locally.
    """
    config.add_project(args)

def setproject(args):
    """
    Sets the project in the local directory.
    """
    config.set_project(args)

def pinglibrary(args):
    """
    Pings the library.
    """
    cfg = config.get_cfg()
    key = cfg.get('Project:%s' % config.current_project(args),'library_key')
    client.ping_library(key,args)
    print 'pong'
