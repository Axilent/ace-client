"""
Config for ACE.
"""
from ConfigParser import SafeConfigParser
import os.path
from os import getcwd, mkdir, remove, walk
import json
import hashlib

def init_environment(args):
    """
    Initializes the environment.
    """    
    dirpath = os.path.expanduser('~')
    
    cfg_path = os.path.join(dirpath,'.acerc')
    
    # Clean out previous config
    if os.path.exists(cfg_path):
        remove(cfg_path)
    
    # New Config File
    cfg = SafeConfigParser()
    cfg.add_section('Connection')
    cfg.set('Connection','endpoint',args.endpoint)
    
    with open(cfg_path,'wb') as cfg_file:
        cfg.write(cfg_file)

def _cfg_path():
    return os.path.join(os.path.expanduser('~'),'.acerc')

def add_project(args):
    """
    Adds a project definition to ace.
    """
    cfg = SafeConfigParser()
    cfg_path = _cfg_path()
    cfg.read(cfg_path)
    
    cfg.add_section('Project:%s' % args.project)
    cfg.set('Project:%s' % args.project,'library_key',args.library_key)
    cfg.set('Project:%s' % args.project,'api_version',args.api_version)
    
    with open(cfg_path,'wb') as cfg_file:
        cfg.write(cfg_file)

def get_cfg():
    """
    Gets the config file.
    """
    cfg = SafeConfigParser()
    cfg_path = _cfg_path()

    # Sanity check
    if not os.path.exists(cfg_path):
        raise ValueError('No config file found.  Use ace init.')

    cfg.read(cfg_path)
    
    return cfg

def _env_path():
    return os.path.join(getcwd(),'ace.txt')

def get_env():
    """
    Gets the local environment for ace.  Directory based.
    """
    cfg = SafeConfigParser()
    env_path = _env_path()
    if os.path.exists(env_path):
        cfg.read(env_path)
    return cfg

def current_project(args):
    """
    Gets the current project from a local ace.txt file, or from the arguments.
    """
    if args.project:
        return args.project
    
    env = get_env()
    return env.get('Project','project')

def set_project(args):
    """
    Sets the project in the local directory.
    """
    env = get_env()
    env.set('Project','project',args.project)
    
    with open(_env_path(),'wb') as env_file:
        env.write(env_file)
