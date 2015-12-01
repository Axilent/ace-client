""" 
Commands for Wrangle.
"""
from ace import client as ac
from ace.config import get_cfg, get_env


def deploy(args):
    """ 
    Deploys matching content.
    """
    cfg = get_cfg()
    client = ac.get_client('axilent.library',cfg.get_library_key(args))
    
    client.deployallcontent(deployment_target=args.deployment_target,
                            workflow_step_names=args.workflow_steps,
                            content_type=args.content_type)

def archive(args):
    """ 
    Archives matching content.
    """
    pass # TODO

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

