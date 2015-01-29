""" 
Dox Markdown publishing for ACE.
"""
__help__ = """
           Dox is a markdown oriented command line publishing tool for ACE.
           
           After installation, dox requires the following initialization:
           
           ace dox init --content-type=<content-type> --body-field=<body-field> --key-field=<key-field>
           
           This will write the environment in local directory. The content type is the ACE content type
           to use for uploaded documents.  The body field specifies which field of the content type
           should be used for the contents of the body of the documents, and the key field specifies
           the unique field by which existing content items can be identified.
           
           Dox also requires a valid project set with the 'ace project set' command, or with the '--project'
           flag.
           """

def seed_parser(parser):
    """ 
    Seeds the arg parser.
    """
    parser.add_argument('--content-type',dest='content_type',default=None)
    parser.add_argument('--body-field',dest='body_field',default=None)
    parser.add_argument('--key-field',dest='key_field',default=None)

def seed_commands(commands):
    """ 
    Seeds the commands.
    """
    from ace.plugins.dox import commands as cmd_functions
    
    dox_commands = {
        'init':cmd_functions.init,
        'up':cmd_functions.upload,
        'upload':cmd_functions.upload,
        'keyfields':cmd_functions.keyfields,
        'clean':cmd_functions.clean
    }
    
    commands['dox'] = dox_commands
