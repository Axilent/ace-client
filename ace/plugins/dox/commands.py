""" 
Commands for Dox.
"""
from ace.plugins.dox import utils
from ace import config
from os import walk, getcwd
import os.path
from ace.plugins.dox.uploader import upload_document, find_key, extract_keyfield
from ace.plugins.dox.client import ping_library, get_content_keys, get_content_item

def init(args):
    """ 
    Initializes Dox.
    """
    if not (args.content_type and args.body_field and args.key_field):
        raise ValueError('You must specify --content-type --body-field and --key-field')
    
    env = config.get_env()
    if not env.has_section('Dox'):
        env.add_section('Dox')
    
    env.set('Dox','content_type',args.content_type)
    env.set('Dox','body_field',args.body_field)
    env.set('Dox','key_field',args.key_field)
    config.write_env(env)
    
    print 'Dox environment initialized.'

def upload(args):
    """ 
    Upload command.
    """
    utils.check_init()
    print 'Uploading documents...'
    keymap = utils.get_keymap()
    keyfields = utils.get_keyfields()
    for root, dirs, fields in walk(getcwd()):
        # TODO - .doxignore
        
        for name in files:
            if name.endswith('.md'):
                path = os.path.join(root,name)
                if utils.is_modified(path):
                    key = find_key(path,keymap,keyfields)
                    key, created = upload_document(path,key=key)
                    utils.write_hash(path)
                    if created:
                        print 'Created new content item',key
                        keymap[path] = key
                        keyfield = extract_keyfield(path)
                        print 'assigning key',key,'to keyfields',keyfields,'under keyfield',keyfield
                        keyfields[keyfield] = key
                else:
                    print name, 'not modified. Skipping.'
    
    write_keyfields(keyfields)
    write_keymap(keymap)

def keyfields(args):
    """ 
    Keyfields command.
    """
    print 'Synchronizing keyfield cache.'
    keyfield_data = {}
    keys = get_content_keys()
    for key in keys:
        content_item = get_content_item(key)
        keyfield_data[content_item['data'][keyfield_name]] = key
        print 'Mapping',content_item['data'][keyfield_name],'to',key
    uitls.write_keyfields(keyfield_data)
    print 'Keyfield cache synchronized.'

def clean(args):
    """ 
    Clean command.
    """
    print 'Cleaning out local file records.  All local files eligible for upload.'
    utils.clean_hashes()

