""" 
Graphstack functions.
"""
from ace import config
from ace import client

def trigger_graphstack(args):
    """ 
    Sends a trigger to the graphtack.
    """
    if not args.category and args.action:
        raise ValueError('Must specify --category and --action.')
    
    num_triggers = int(args.num_triggers)
    distribution = float(args.profile_distribution)
    
    threshold = int(round(float(num_triggers) * distribution))
    
    c = client.get_client('axilent.triggers',config.get_api_key(args),args)
    
    p = None
    if not args.profile:
        p = c.profile()['profile']
    else:
        p = args.profile
    
    # Variables
    var_dict = {}
    if args.variables:
        for var_pair in args.variables.split('&'):
            var_name, var_value = var_pair.split(':')
            var_dict[var_name] = var_value
    
    for i in xrange(num_triggers):
        if not args.profile:
            changer = randint(0,num_triggers)
            if changer > threshold:
                p = c.profile()['profile']
        
        c.trigger(data={'profile':p,
                        'category':args.category,
                        'action':args.action,
                        'variables':var_dict,
                        'environment':{}, # nothing for now
                        'identity':{}}) # nothing for now
        sys.stdout.write('.')
        sys.stdout.flush()
    
    sys.stdout.write('\n')
