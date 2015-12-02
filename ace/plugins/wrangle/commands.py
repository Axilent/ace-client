""" 
Commands for Wrangle.
"""
from ace import client as ac
from ace.config import get_cfg, get_env, get_library_key


def deploy(args):
    """ 
    Deploys matching content.
    """
    client = ac.get_client('axilent.library',get_library_key(args),args)
    
    workflow_steps = []
    if args.workflow_steps:
        workflow_steps = args.workflow_steps.split(',')
    
    client.deployallcontent(deployment_target=args.deployment_target,
                            workflow_step_names=workflow_steps,
                            content_type=args.content_type)

def archive(args):
    """ 
    Archives matching content.
    """
    client = ac.get_client('axilent.library',get_library_key(args),args)
    workflow_steps = []
    if args.workflow_steps:
        workflow_steps = args.workflow_steps.split(',')
    
    client.archiveallcontent(content_type=args.content_type,
                             workflow_step_names=workflow_steps)

def advance(args):
    """ 
    Advances matching content in workflow.
    """
    pass # TODO

def retreat(args):
    """ 
    Moves matching content back in workflow.
    """
    pass # TODO

