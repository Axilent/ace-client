""" 
Plugins system.
"""
from ace import config
from ace.utils import get_module
import pkgutil

# ================================
# = Delegates to active plugins. =
# ================================
def seed_parser(parser):
    """ 
    Seeds the parser.
    """
    for plugin_name in config.get_installed_plugins():
        plugin_mod = get_module('ace.plugins.%s' % plugin_name)
        plugin_mod.seed_parser(parser)

def seed_commands(commands):
    """ 
    Seeds the commands.
    """
    for plugin_name in config.get_installed_plugins():
        plugin_mod = get_module('ace.plugins.%s' % plugin_name)
        plugin_mod.seed_commands(commands)

def help(command,subcommand):
    """ 
    Gets help for the specified command and subcommand.
    """
    pass # TODO

def get_available_plugins():
    """ 
    Returns the available, uninstalled plugins.
    """
    available_plugins = []
    for module_loader, name, ispkg in pkgutil.walk_packages(__path__):
        if not config.plugin_installed(name):
            available_plugins.append(name)
    return available_plugins

def available(args):
    """ 
    Lists the available, uninstalled plugins.
    """
    for name in get_available_plugins():
        mod = get_module('ace.plugins.%s' % name)
        help_text = mod.__help__
        print name,'\t\t\t',help_text
