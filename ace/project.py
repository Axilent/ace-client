""" 
Project functionality.
"""
from ace import config
from ace import client
import json
import sys

def dump_project(args):
    """ 
    Dumps the project to standard out.
    """
    if not config.get_active_project(args):
        raise ValueError('Must specify project.')
    
    project_resource = client.get_resource('axilent.library','project',config.get_library_key(args),args)
    project_data = project_resource.get()
    sys.stdout.write(json.dumps(project_data['project-data']))

def load_project(args):
    """ 
    Loads the project from the data file.
    """
    if not (config.get_active_project(args) and args.data_file):
        raise ValueError('Must specify both project and data file.')
    
    project_resource = client.get_resource('axilent.library','project',config.get_library_key(args),args)
    data = None
    with open(args.data_file,'r') as data_file:
        data = data_file.read()
    
    project_resource.put(data={'project-data':data})
    print 'Project data loaded.'

def ping_library(args):
    """ 
    Pings the project library.
    """
    c = client.get_client('axilent.library',config.get_library_key(args),args)
    c.ping()
    print 'pong'
