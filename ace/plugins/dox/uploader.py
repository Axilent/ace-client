"""
Uploads documents to Axilent.
"""
import markdown
from ace.config import get_cfg, get_env
from ace.plugins.dox.utils import get_keymap, get_keyfields
from ace import client as ac

from dox.client import get_content_library_resource, get_library_client

def _tagging(md,content_key,content_type,args):
    """
    Apply tagging
    """
    cfg = get_cfg()
    client = ac.get_client('axilent.library',cfg.get_library_key(args))
    
    # tagging
    tags = md.Meta['tags']
    for tag in tags:
        if tag:
            client.tagcontent(content_type=content_type,
                              content_key=content_key,
                              tag=tag,
                              search_index=args.search_index)

def upload_document(path,args,key=None):
    """
    Uploads the specified document, returns the key of the uploaded document.
    """
    # 1. Prepare data for upload
    cfg = get_cfg()
    env = get_env()
    body_field_name = cfg.get('Connection','body_field')
    data = {}
    md = markdown.Markdown(extensions=['meta','tables','attr_list'])
    with open(path) as docfile:
        body = md.convert(docfile.read())
        
        for field_name, field_value in md.Meta.items():
            data[field_name] = field_value[0]
        
        data[body_field_name] = body
    
    
    # Upload Content
    return_key = None
    resource = ac.get_resource('axilent.library','content',cfg.get_api_key(args))
    if key:
        resource.put(data={'content':data,
                           'content_type':env.get('Dox','content_type'),
                           'key':key,
                           'search_index':args.search_index,
                           'reset_workflow':args.reset_workflow})
        _tagging(md,key,env.get('Dox','content_type'),args)
        
        return (key,False) # no new document created
    else:
        response = resource.post(data={'content':data,
                                       'content_type':env.get('Dox','content_type'),
                                       'search_index':args.search_index})
        
        created_content_type, created_key = response['created_content'].split(':')
        
        _tagging(md,created_key,cfg.get('Dox','content_type'),args)
        
        return (created_key,True) # new document created
    
def find_key(path,keymap,keyfields):
    """
    Finds a key for the specified document if it exists.
    """
    # First try to pull key from the keymap
    try:
        return keymap[path]
    except KeyError:
        pass
    
    # Try to find it from a keyfield
    try:
        env = get_env()
        keyfield_name = cfg.get('Dox','key_field')
        md = markdown.Markdown(extensions=['meta','tables','attr_list'])
        with open(path) as docfile:
            md.convert(docfile.read())
            keyfield = md.Meta[keyfield_name][0]
            return keyfields[keyfield]
    except KeyError:
        pass
    
    # Give up
    return None

def extract_keyfield(path):
    """
    Extracts the keyfield value from the document.
    """
    cfg = get_cfg()
    keyfield_name = cfg.get('Connection','key_field')
    md = markdown.Markdown(extensions=['meta','tables','attr_list'])
    with open(path) as docfile:
        md.convert(docfile.read())
        try:
            keyfield = md.Meta[keyfield_name][0]
            return keyfield
        except KeyError:
            return None
