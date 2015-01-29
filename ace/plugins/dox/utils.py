""" 
Utilities for Dox.
"""

from ace import config
import os.path
from os import getcwd, mkdir, remove, walk
import hashlib

def check_init():
    """ 
    Checks if Dox has been properly initialized.
    """
    env = config.get_env()
    if not env.has_option('Project','project'):
        raise ValueError('Project not set.  Set project with `ace project set` command.')
    
    if not env.has_section('Dox'):
        raise ValueError('Dox not initalized.  Initialze Dox with `ace dox init --content-type=<content-type> --body-field=<body-field> --key-field=<key-field>` command.')

def dox_dir():
    """
    Gets or creates the .dox directory.
    """
    dox_dirpath = os.path.join(getcwd(),'.dox')
    
    if not os.path.exists(dox_dirpath):
        mkdir(dox_dirpath)
    
    return dox_dirpath

def is_modified(markdown_file_path):
    """
    Tests if the markdown file has been modified.
    """
    with open(markdown_file_path,'r') as markdown_file:
        hashfile_path = '%s.hash' % os.path.join(dox_dir(),'hashes',os.path.split(markdown_file.name)[1])
        if os.path.exists(hashfile_path):
            d = hashlib.sha256()
            d.update(markdown_file.read())
            digest = d.hexdigest()
            with open(hashfile_path) as hashfile:
                stored_hash = hashfile.read()
                if stored_hash != digest:
                    return True # non-matching hashes - file is modified
                else:
                    return False # hashes match - file has not been modified
        else:
            return True # no stored hash - file is modified by definition

def write_hash(markdown_file_path):
    """
    Scans the file and records a hash digest of the contents.
    """
    with open(markdown_file_path) as markdown_file:
        d = hashlib.sha256()
        d.update(markdown_file.read())
        digest = d.hexdigest()
        hash_file_path = '%s.hash' % os.path.join(dox_dir(),'hashes',os.path.split(markdown_file.name)[1])
        with open(hash_file_path,'wb') as hash_file:
            hash_file.write(digest)

def clean_hashes():
    """
    Cleans the local file hash directory out.
    """
    hash_path = os.path.join(dox_dir(),'hashes')
    if os.path.exists(hash_path):
        for root, dirs, files in walk(hash_path):
            for name in files:
                if name.endswith('.hash'):
                    remove(os.path.join(root,name))
    else:
        mkdir(hash_path)

def get_keyfields():
    """
    Gets the keyfields data.
    """
    dirpath = dox_dir()
    keyfield_path = os.path.join(dirpath,'keyfields.json')
    if os.path.exists(keyfield_path):
        with open(keyfield_path,'r') as keyfield_file:
            keyfield_data = json.loads(keyfield_file.read())
            return keyfield_data
    else:
        return {}

def write_keyfields(data):
    """
    Writes the keyfield data file.
    """
    dirpath = dox_dir()
    keyfield_path = os.path.join(dirpath,'keyfields.json')
    with open(keyfield_path,'wb') as keyfield_file:
        keyfield_file.write(json.dumps(data))

def get_keymap():
    """
    Gets the keymap data.
    """
    dirpath = dox_dir()
    keymap_path = os.path.join(dirpath,'keymap.json')
    if os.path.exists(keymap_path):
        with open(keymap_path,'r') as keymap_file:
            keymap_data = json.loads(keymap_file.read())
            return keymap_data
    else:
        return {}

def write_keymap(data):
    """
    Saves the keymap data.
    """
    dirpath = dox_dir()
    keymap_path = os.path.join(dirpath,'keymap.json')
    with open(keymap_path,'wb') as keymap_file:
        keymap_file.write(json.dumps(data))
