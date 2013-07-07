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
    dirpath = getcwd()
    
    cfg_path = os.path.join(dirpath,'.acerc')
    
    # Clean out previous config
    if os.path.exists(cfg_path):
        remove(cfg_path)
    
    # New Config File
    cfg = SafeConfigParser()
    cfg.add_section('Connection')
    cfg.set('Connection','endpoint',args.endpoint)
    cfg.set('Connection','api_version',args.api_version)
    
    with open(cfg_path,'wb') as cfg_file:
        cfg.write(cfg_file)

def add_project(args):
    """
    Adds a project definition to ace.
    """
    cfg = SafeConfigParser()
    cfg_path = os.path.join(getcwd(),'.acerc')
    cfg.read(cfg_path)
    
    cfg.add_section('Project:%s' % args.project)
    cfg.set('Project:%s' % args.project,'library_key',args.library_key)
    
    with open(cfg_path,'wb') as cfg_file:
        cfg.write(cfg_file)

def get_cfg():
    """
    Gets the config file.
    """
    cfg = SafeConfigParser()
    cfg_path = os.path.join(getcwd(),'.acerc')

    # Sanity check
    if not os.path.exists(cfg_path):
        raise ValueError('No config file found.  Directory has not been initialized for ace.  Use ace init.')

    cfg.read(cfg_path)
    
    return cfg

