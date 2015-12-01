""" 
Content Wrangling for ACE.
"""
__help__ = """ 
           The wrangle plugin provides bulk content wrangling services for ACE.
           
           Most wrangle comands take two additional arguments: --content-type and (optionally) --workflow-step.
           
           The wrangle commands will apply to ALL library content where the content type (and if specified, the workflow step) matches.
           The wrangle command will be applied to all matching content.
           
           The Wrangle plugin requires a valid current project with a library key.  Use 'ace project set' to set a project to the current
           working directory, or specify the project with the '--project' arg.
"""

def seed_parser(parser):
    """ 
    Seeds the arg parser.
    """
    parser.add_argument('--deployment-target',dest='deployment_target',default=None)
    parser.add_argument('--workflow-steps',dest='wokflow_steps',default=None)
    parser.add_argument('--content-type',dest='content_type',default=None)

def seed_commands(commands):
    """ 
    Addds wrangle commands.
    """
    from ace.plugins.wrangle import commands as cmd_functions
    
    wrangle_commands = {
        'deploy':cmd_functions.deploy,
        'archive':cmd_functions.archive,
        'advance':cmd_functions.advance,
        'retreat':cmd_functions.retreat,
    }
    
    commands['wrangle'] = wrangle_commands