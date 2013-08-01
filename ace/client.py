"""
Axilent Client functionality for Ace.
"""
from sharrock.client import HttpClient, ResourceClient, ServiceException
from ace.config import get_cfg, current_project, current_graphstack, api_version, get_api_key, get_library_key
from ace.utils import slugify
import json
import sys
from random import randint

def _get_resource(app,resource,key,args):
    """
    Gets a resource client.
    """
    cfg = get_cfg()
    return ResourceClient('%s/api/resource' % cfg.get('Connection','endpoint'),app,api_version(args),resource,auth_user=key)

def _get_client(app,key,args):
    """
    Gets a regular API client.
    """
    cfg = get_cfg()
    return HttpClient('%s/api' % cfg.get('Connection','endpoint'),app,api_version(args),auth_user=key)

def ping_library(args):
    """
    Pings the library - testing the connection.
    """
    c = _get_client('axilent.library',get_library_key(args),args)
    c.ping()

def dump_project_data(args):
    """
    Dumps the data from the project into JSON in stdout.
    """
    if not current_project(args):
        raise ValueError('Must specify project.')
    
    project_resource = _get_resource('axilent.library','project',get_library_key(args),args)
    #project_data = project_resource.get(params={'project':current_project(args)})
    project_data = project_resource.get()
    sys.stdout.write(json.dumps(project_data['project-data']))

def load_project_data(args):
    """
    Loads the data from the specified data file into project.
    """
    if not (current_project(args) and args.data_file):
        raise ValueError('Must specify both project and data file.')
    
    project_resource = _get_resource('axilent.library','project',get_library_key(args),args)
    data = None
    with open(args.data_file,'r') as data_file:
        data = data_file.read()
    
    #project_resource.put(data={'project':current_project(args),'project-data':data})
    project_resource.put(data={'project-data':data})
    print 'Project data loaded.'

def profile(args):
    """
    Gets a profile id.
    """
    c = _get_client('axilent.triggers',get_api_key(args),args)
    profile_data = c.profile()
    sys.stdout.write(profile_data['profile'])
    sys.stdout.write('\n')

def trigger(args):
    """
    Sends a one or more triggers.
    """
    if not args.category and args.action:
        raise ValueError('Must specify --category and --action.')
    
    num_triggers = int(args.num_triggers)
    distribution = float(args.profile_distribution)
    
    threshold = int(round(float(num_triggers) * distribution))
    
    c = _get_client('axilent.triggers',get_api_key(args),args)
    
    p = None
    if not args.profile:
        p = c.profile()['profile']
    else:
        p = args.profile
    
    # Variables
    var_dict = {}
    if args.variables:
        for var_pair in args.variables.split('&'):
            var_name, var_value = var_pair.split(':')
            var_dict[var_name] = var_value
    
    for i in xrange(num_triggers):
        if not args.profile:
            changer = randint(0,num_triggers)
            if changer > threshold:
                p = c.profile()['profile']
        
        c.trigger(data={'profile':p,
                        'category':args.category,
                        'action':args.action,
                        'variables':var_dict,
                        'environment':{}, # nothing for now
                        'identity':{}}) # nothing for now
        sys.stdout.write('.')
        sys.stdout.flush()
    
    sys.stdout.write('\n')

        
