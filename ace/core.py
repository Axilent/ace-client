""" 
Core module for ace-cli.
"""
from ace import config
from ace import project
from ace import graphstack
from ace import plugins
from inspect import getdoc

def seed_parser(parser):
    """ 
    Adds arguments to parser.
    """
    seed_parser_project(parser)
    seed_parser_graphstack(parser)
    seed_parser_plugins(parser)

def seed_commands(commands):
    """ 
    Adds commands.
    
    Core commands are:
    
        init
        project
            add
            remove
            set
            clear
            dump
            load
            ping
            apiversion
            current
            list
        graphstack
            add
            remove
            set
            clear
            current
            trigger
            apikey
            list
        plugins
            install
            uninstall
            list
            available
    """
    default_init = {'__default__':init_command}
    commands['init'] = default_init
    
    commands['project'] = project_commands()
    commands['graphstack'] = graphstack_commands()
    commands['plugins'] = plugins_commands()

def seed_help(help_messages):
    """ 
    Adds help messages to help block.
    """
    init_help = {'__default__':getdoc(init_command)}
    help_messages['init'] = init_help
    
    help_messages['project'] = project_help()
    help_messages['graphstack'] = graphstack_help()
    help_messages['plugins'] = plugins_help()

# ===============
# = Subcommands =
# ===============

def init_command(args):
    """ 
    Initializes ACE.
    """
    config.init_environment(args)
    
# =======================
# = Project Subcommands =
# =======================

def add_project_command(args):
    """ 
    Adds a project to main config.
    """
    config.add_project(args)

def remove_project_command(args):
    """ 
    Removes a project from main config.
    """
    config.remove_project(args)

def set_project_command(args):
    """ 
    Sets the local project.
    """
    config.set_project(args)

def clear_project_command(args):
    """ 
    Clears the local project.
    """
    config.clear_project(args)

def dump_project_command(args):
    """ 
    Dumps the local project to JSON.
    """
    project.dump_project(args)

def load_project_command(args):
    """ 
    Loads the project from JSON.
    """
    project.load_project(args)

def ping_library_command(args):
    """ 
    Pings the project library.
    """
    project.ping_library(args)

def api_version_command(args):
    """ 
    Gets the API vesion set for the current project.
    """
    return config.api_version(args)

def current_project_command(args):
    """ 
    Gets the current project.
    """
    return config.current_project(args)

def list_projects_command(args):
    """ 
    Lists the projects.
    """
    return config.list_projects(args)

# ==========================
# = GraphStack Subcommands =
# ==========================
def add_graphstack_command(args):
    """ 
    Adds a graphstack to the main config.
    """
    config.add_graphstack(args)

def remove_graphstack_command(args):
    """ 
    Removes a graphstack from the main config.
    """
    config.remove_graphstack(args)

def set_graphstack_command(args):
    """ 
    Sets the current graphstack.
    """
    config.set_graphstack(args)

def clear_graphstack_command(args):
    """ 
    Clears the current graphstack.
    """
    config.clear_graphstack(args)

def current_graphstack_command(args):
    """ 
    Gets the current graphstack.
    """
    return config.current_graphstack(args)

def trigger_graphstack_command(args):
    """ 
    Triggers the graphstack.
    """
    graphstack.trigger_graphstack(args)

def api_key_command(args):
    """ 
    Gets the API key for the current graphstack.
    """
    return config.api_key(args)

def list_graphstacks_command(args):
    """ 
    Lists the graphstacks for a project.
    """
    return config.list_graphstacks(args)


# =======================
# = Plugins Subcommands =
# =======================
def install_plugin_command(args):
    """ 
    Installs a plugin.
    """
    config.install_plugin(args)

def uninstall_plugin_command(args):
    """ 
    Uninstalls a plugin.
    """
    config.uninstall_plugin(args)

def list_installed_plugins_command(args):
    """ 
    Lists the installed plugins.
    """
    config.list_installed_plugins(args)

def available_plugins_command(args):
    """ 
    Lists the available, uninstalled plugins.
    """
    plugins.available(args)

# ====================
# = Command Builders =
# ====================
def project_commands():
    """ 
    Project actions.
    """
    pcom = {'add':add_project_command,
            'remove':remove_project_command,
            'set':set_project_command,
            'clear':clear_project_command,
            'dump':dump_project_command,
            'load':load_project_command,
            'ping':ping_library_command,
            'apiversion':api_version_command,
            'current':current_project_command,
            'list':list_projects_command}
    return pcom

def graphstack_commands():
    """ 
    GraphStack commands.
    """
    gscom = {'add':add_graphstack_command,
             'remove':remove_graphstack_command,
             'set':set_graphstack_command,
             'clear':clear_graphstack_command,
             'current':current_graphstack_command,
             'trigger':trigger_graphstack_command,
             'apikey':api_key_command,
             'list':list_graphstacks_command}
    
    return gscom

def plugins_commands():
    """ 
    Plugins commands.
    """
    picom = {'install':install_plugin_command,
             'uninstall':uninstall_plugin_command,
             'list':list_installed_plugins_command,
             'available':available_plugins_command}
    return picom

# ==================
# = Parser Seeders =
# ==================
def seed_parser_project(parser):
    """ 
    Seeds the parser for project related args.
    """
    parser.add_argument('--library-key',dest='library_key',default=None)
    parser.add_argument('--project',dest='project',default=None)
    parser.add_argument('--api-version',dest='api_version',default='astoria-preview')
    parser.add_argument('--data-file',dest='data_file',default=None)

def seed_parser_graphstack(parser):
    """ 
    Seeds the parser for graphstack related args.
    """
    parser.add_argument('--api-key',dest='api_key',default=None)
    parser.add_argument('--graphstack',dest='graphstack',default=None)
    parser.add_argument('--category',dest='category',default=None)
    parser.add_argument('--action',dest='action',default=None)
    parser.add_argument('--num-triggers',dest='num_triggers',default=1)
    parser.add_argument('--profile-distribution',dest='profile_distribution',default=1.0) # percent of triggers with unique profile ids
    parser.add_argument('--variables',dest='variables',default=None) # trigger variables with pattern var1:val1,var2:val2,var3:val3...
    parser.add_argument('--profile',dest='profile',default=None) # you can specify a particular profile

def seed_parser_plugins(parser):
    """ 
    Seeds the parser for plugins related args.
    """
    parser.add_argument('--plugin',dest='plugin',default=None)

# =================
# = Help Builders =
# =================
def project_help():
    """ 
    Help for project functions.
    """
    phelp = {'add':getdoc(add_project_command),
             'remove':getdoc(remove_project_command),
             'set':getdoc(set_project_command),
             'clear':getdoc(clear_project_command),
             'dump':getdoc(dump_project_command),
             'load': getdoc(load_project_command),
             'ping':getdoc(ping_library_command),
             'apiversion':getdoc(api_version_command),
             'current':getdoc(current_project_command),
             'list':getdoc(list_projects_command)}
    return phelp

def graphstack_help():
    """ 
    Help for graphstack functions.
    """
    gshelp = {'add':getdoc(add_graphstack_command),
              'remove':getdoc(remove_graphstack_command),
              'set':getdoc(set_graphstack_command),
              'clear':getdoc(clear_graphstack_command),
              'current':getdoc(current_graphstack_command),
              'trigger':getdoc(trigger_graphstack_command),
              'apikey':getdoc(api_key_command)}
    return gshelp

def plugins_help():
    """ 
    Help for plugins functions.
    """
    pihelp = {'install':getdoc(install_plugin_command),
              'uninstall':getdoc(uninstall_plugin_command),
              'list':getdoc(list_installed_plugins_command),
              'available':getdoc(available_plugins_command)}
    return pihelp
