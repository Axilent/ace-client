""" 
Placeholder plugin to test the plugin system.
"""
__help__ = 'Hello world.  A throwaway module.'

def seed_parser(parser):
    """ 
    Seed the parser.
    """
    parser.add_argument('--awesome',dest='awesome',default='completely')

def seed_commands(commands):
    """ 
    Seeds the commands.
    """
    def awesome(args):
        print 'I am',args.awesome,'awesome.'
        
    commands['yo'] = {'__default__':awesome}
