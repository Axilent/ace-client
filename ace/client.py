"""
Axilent Client functionality for Ace.
"""
from sharrock.client import HttpClient, ResourceClient, ServiceException
from ace.config import get_cfg
from ace.utils import slugify
import json
import sys

def _get_resource(app,resource,key):
    """
    Gets a resource client.
    """
    cfg = get_cfg()
    return ResourceClient('%s/api/resource' % cfg.get('Connection','endpoint'),app,cfg.get('Connection','api_version'),resource,auth_user=key)

def _get_client(app,key):
    """
    Gets a regular API client.
    """
    cfg = get_cfg()
    return HttpClient('%s/api' % cfg.get('Connection','endpoint'),app,cfg.get('Connection','api_version'),auth_user=key)

def ping_library(key):
    """
    Pings the library - testing the connection.
    """
    c = _get_client('axilent.library',key)
    c.ping()

def dump_project_data(args):
    """
    Dumps the data from the project into JSON in stdout.
    """
    if not args.project:
        raise ValueError('Must specify project.')
    
    cfg = get_cfg()
    key = cfg.get(args.project,'library_key')
    project_resource = _get_resource('axilent.library','project',key)
    project_data = project_resource.get(params={'project':project})
    sys.stdout.write(json.dumps(project_data))
