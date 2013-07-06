"""
Axilent Client functionality for Ace.
"""
from sharrock.client import HttpClient, ResourceClient, ServiceException
from ace.config import get_cfg
from ace.utils import slugify
import json
import sys

def _get_resource(app,resource,library=True):
    """
    Gets a resource client.
    """
    cfg = get_cfg()
    apikey_setting = 'library_key' if library else 'api_key'
    return ResourceClient('%s/api/resource' % cfg.get('Connection','endpoint'),app,cfg.get('Connection','api_version'),resource,auth_user=cfg.get('Connection',apikey_setting))

def _get_client(app,library=True):
    """
    Gets a regular API client.
    """
    cfg = get_cfg()
    apikey_setting = 'library_key' if library else 'api_key'
    return HttpClient('%s/api' % cfg.get('Connection','endpoint'),app,cfg.get('Connection','api_version'),auth_user=cfg.get('Connection',apikey_setting))

def get_library_client():
    """
    Gets the library API client.
    """
    return _get_client('axilent.library')

def ping_library():
    """
    Pings the library - testing the connection.
    """
    c = _get_client('axilent.library')
    c.ping()

def dump_project_data():
    """
    Dumps the data from the project into JSON in stdout.
    """
    cfg = get_cfg()
    project_resource = _get_resource('axilent.library','Project')
    project_data = project_resource.get(params={'project':cfg.get('Connection','project')})
    sys.stdout.write(json.dumps(project_data))
