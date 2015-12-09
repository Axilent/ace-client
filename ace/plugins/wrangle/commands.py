""" 
Commands for Wrangle.
"""
from ace import client as ac
from ace.config import get_cfg, get_env, get_library_key


def _setup(args):
    client = ac.get_client('axilent.library',get_library_key(args),args)
    workflow_steps = []
    if args.workflow_steps:
        workflow_steps = args.workflow_steps.split(',')
    
    return (client,workflow_steps)

def deploy(args):
    """ 
    Deploys matching content.
    """
    client, workflow_steps = _setup(args)
    
    client.deployallcontent(deployment_target=args.deployment_target,
                            workflow_step_names=workflow_steps,
                            content_type=args.content_type)

def archive(args):
    """ 
    Archives matching content.
    """
    client, workflow_steps = _setup(args)
    
    client.archiveallcontent(content_type=args.content_type,
                             workflow_step_names=workflow_steps)

def advance(args):
    """ 
    Advances matching content in workflow.
    """
    client, workflow_steps = _setup(args)
    
    client.advanceallcontent(content_type=args.content_type,
                             workflow_step_names=workflow_steps)

def retreat(args):
    """ 
    Moves matching content back in workflow.
    """
    client, workflow_steps = _setup(args)
    
    client.retreatallcontent(content_type=args.content_type,
                             workflow_step_names=workflow_steps)

def reset(args):
    """ 
    Resets the workflow of matching content.
    """
    client, workflow_steps = _setup(args)
    
    client.resetallcontent(content_type=args.content_type,
                           workflow_step_names=workflow_steps)

def count(args):
    """ 
    Counts the matching content.
    """
    client, workflow_steps = _setup(args)
    
    print client.countcontent(content_type=args.content_type,
                              workflow_step_names=workflow_steps)
