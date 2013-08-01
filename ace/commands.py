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
    client.ping_library(args)
    print 'pong'

def addgraphstack(args):
    """
    Adds a graphstack.
    """
    config.add_graphstack(args)

def setgraphstack(args):
    """
    Sets the default graphstack.
    """
    config.set_graphstack(args)

def profile(args):
    """
    Gets a profile ID.
    """
    client.profile(args)

def trigger(args):
    """
    Sends a trigger.
    """
    client.trigger(args)
