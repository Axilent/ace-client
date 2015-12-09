"""
Config for ACE.
"""
from ConfigParser import SafeConfigParser, NoOptionError
import os.path
from os import getcwd, mkdir, remove, walk
import json
import hashlib
from ace.utils import slugify

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
    
    write_cfg(cfg)

def _cfg_path():
    return os.path.join(os.path.expanduser('~'),'.acerc')

def add_project(args):
    """
    Adds a project definition to ace.
    """
    cfg = get_cfg()
    
    cfg.add_section('Project:%s' % args.project)
    cfg.set('Project:%s' % args.project,'library_key',args.library_key)
    if args.api_version:
        cfg.set('Project:%s' % args.project,'api_version',args.api_version)
    else:
        cfg.set('Project:%s' % args.project,'api_version','astoria') # Default API version
    
    write_cfg(cfg)

def remove_project(args):
    """ 
    Removes the project.
    """
    cfg = get_cfg()
    
    section_name = 'Project:%s' % args.project
    cfg.remove_section(section_name)
    
    write_cfg(cfg)

def list_projects(args):
    """ 
    Lists the projects.
    """
    cfg = get_cfg()
    
    for section in cfg.sections():
        if section.startswith('Project:'):
            prefix, project_name = section.split(':')
            print project_name

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

def write_cfg(cfg):
    """
    Writes the config to file.
    """
    with open(_cfg_path(),'wb') as cfg_file:
        cfg.write(cfg_file)

def get_env():
    """
    Gets the local environment for ace.  Directory based.
    """
    cfg = SafeConfigParser()
    env_path = _env_path()
    if os.path.exists(env_path):
        cfg.read(env_path)
    return cfg

def write_env(env):
    """
    Writes the environment to file.
    """
    with open(_env_path(),'wb') as env_file:
        env.write(env_file)

def get_active_project(args):
    """
    Gets the current project from a local ace.txt file, or from the arguments.
    """
    if args.project:
        return args.project
    
    env = get_env()
    return env.get('Project','project')

def library_key(args):
    """ 
    Gets the current project's library key.
    """
    cfg = get_cfg()
    project = get_active_project(args)
    if not cfg.has_section('Project:%s' % project):
        raise ValueError('Project %s has not been defined. Run `ace project add` first.' % project)
    
    print cfg.get('Project:%s' % project,'library_key')

def set_project(args):
    """
    Sets the project in the local directory.
    """
    env = get_env()
    if not env.has_section('Project'):
        env.add_section('Project')
    
    env.set('Project','project',args.project)
    write_env(env)

def clear_project(args):
    """ 
    Clears the project from the local directory.
    """
    env = get_env()
    if env.has_section('Project'):
        env.remove_option('Project','project')
    write_env(env)

def current_project(args):
    """ 
    Returns the local directory current project.
    """
    env = get_env()
    if env.has_section('Project'):
        if env.has_option('Project','project'):
            print env.get('Project','project')
        else:
            print 'Project is not set for this directory'
    else:
        print 'No project info defined for this directory'

def add_graphstack(args):
    """
    Adds a graphstack to the current project.
    """
    project = get_active_project(args)
    cfg = get_cfg()
    if not cfg.has_section('Project:%s' % project):
        raise ValueError('Project %s has not been defined. Run `ace project add` first.' % project)
    
    if not args.graphstack and args.api_key:
        raise ValueError('You must specify the graphstack to add with the --graphstack option, and it\'s API key with the --api-key option.')
    
    cfg.set('Project:%s' % project,'graphstack-%s' % slugify(args.graphstack),args.api_key)
    write_cfg(cfg)

def remove_graphstack(args):
    """ 
    Removes the graphstack from the project def.
    """
    project = get_active_project(args)
    cfg = get_cfg()
    if not cfg.has_section('Project:%s' % project):
        raise ValueError('Project %s has not been defined.  Run ace addproject first.' % project)
    
    if not args.graphstack:
        raise ValueError('You must specify the graphstack to remove with the --graphstack option.')
    
    if cfg.has_option('Project:%s' % project,'graphstack-%s' % slugify(args.graphstack)):
        cfg.remove_option('Project:%s' % project,'graphstack-%s' % slugify(args.graphstack))
    
    write_cfg(cfg)

def list_graphstacks(args):
    """ 
    Lists graphstacks for a project.
    """
    project = get_active_project(args)
    cfg = get_cfg()
    if not cfg.has_section('Project:%s' % project):
        raise ValueError('Project %s has not been defined.  Run ace addproject first.' % project)
    
    for option in cfg.options('Project:%s' % project):
        if option.startswith('graphstack-'):
            prefix, gs_name = option.split('-',1)
            print gs_name

def set_graphstack(args):
    """
    Sets the local graphstack.
    """
    env = get_env()
    env.set('Project','graphstack',slugify(args.graphstack))
    
    write_env(env)

def clear_graphstack(args):
    """ 
    Clears the local graphstack.
    """
    env = get_env()
    if env.has_option('Project','graphstack'):
        env.remove_option('Project','graphstack')
    write_env(env)

def get_active_graphstack(args):
    """
    Gets the current graphstack.
    """
    if args.graphstack:
        return slugify(args.graphstack)
    
    env = get_env()
    return env.get('Project','graphstack')

def current_graphstack(args):
    """ 
    Print the current graphstack.
    """
    try:
        gs = get_active_graphstack(args)
        print gs
    except NoOptionError:
        print 'Current graphstack is not set'

def get_active_api_version(args):
    """
    Gets the active api version to use.
    """
    if args.api_version:
        return args.api_version
    
    cfg = get_cfg()
    project = get_active_project(args)
    return cfg.get('Project:%s' % project,'api_version')

def api_version(args):
    """ 
    Gets the api version of the active project.
    """
    av = get_active_api_version(args)
    print av

def get_api_key(args):
    """
    Gets the API key for the appropriate graphstack.
    """
    if args.api_key:
        return args.api_key
    
    cfg = get_cfg()
    gs = get_active_graphstack(args)
    project = get_active_project(args)
    return cfg.get('Project:%s' % project,'graphstack-%s' % gs)

def api_key(args):
    """ 
    Prints the api key.
    """
    ak = get_api_key(args)
    print ak

def get_library_key(args):
    """
    Gets the library key for the current project.
    """
    if args.library_key:
        return args.library_key
    
    cfg = get_cfg()
    project = get_active_project(args)
    return cfg.get('Project:%s' % project,'library_key')

def plugin_installed(plugin_name):
    """ 
    Tests if the specified plugin is installed.
    """
    cfg = get_cfg()
    return cfg.has_section('Plugin:%s' % plugin_name)

def get_installed_plugins():
    """ 
    Gets a list of the installed plugins.
    """
    try:
        cfg = get_cfg()
        installed_plugins = []
        for section in cfg.sections():
            if section.startswith('Plugin:'):
                prefix, plugin_name = section.split(':')
                installed_plugins.append(plugin_name)
        return installed_plugins
    except ValueError:
        # this will be the case in an uninitialized environment
        return []

def list_installed_plugins(args):
    """ 
    Lists the installed plugins.
    """
    cfg = get_cfg()
    for section in cfg.sections():
        if section.startswith('Plugin:'):
            prefix, plugin_name = section.split(':')
            print plugin_name

def install_plugin(args):
    """ 
    Adds the plugin to the config.
    """
    if not args.plugin:
        raise ValueError('You must specify the plugin to install with the --plugin option.')
    cfg = get_cfg()
    section_name = 'Plugin:%s' % args.plugin
    if not cfg.has_section(section_name):
        cfg.add_section(section_name)
        write_cfg(cfg)
    else:
        print args.plugin,'is already installed.'

def uninstall_plugin(args):
    """ 
    Uninstalls the plugin.
    """
    if not args.plugin:
        raise ValueError('You must specifiy the plugin to uninstall.')
    cfg = get_cfg()
    section_name = 'Plugin:%s' % args.plugin
    if cfg.has_section(section_name):
        cfg.remove_section(section_name)
        write_cfg(cfg)
    else:
        print args.plugin,'is not installed.'


