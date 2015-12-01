""" 
Client code for Dox.
"""
from dox.config import get_cfg
from dox.utils import slugify
from ace import client as ac
from ace import config as cfg

def ping_library(args):
    """
    Pings the library.
    """    
    lib = ac.get_client('axilent.library',cfg.get_library_key(args))
    env = cfg.get_env()
    lib.ping(content_type=env.get('Dox','content_type'))

def get_content_keys(args):
    """
    Gets the keys for the conten type.
    """
    api = ac.get_client('axilent.content',cfg.get_api_key(args))
    env = cfg.get_env()
    keys = api.getcontentkeys(content_type_slug=slugify(env.get('Dox','content_type')))
    return keys

def get_content_item(key,args):
    """
    Gets deployed content for the specified key.
    """
    env = cfg.get_env()
    resource = ac.get_resource('axilent.content','content',cfg.get_api_key(args),args)
    return resource.get(params={'content_type_slug':slugify(env.get('Dox','content_type')),'content_key':key})


