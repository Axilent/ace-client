"""
Utilities for Ace
"""
import unicodedata
import re

def slugify(value):
    """
    Makes slug-friendly string.
    """
    value = unicodedata.normalize('NFKD', unicode(value)).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

def get_module(module_name):
    """
    Imports and returns the named module.
    """
    module = __import__(module_name)
    components = module_name.split('.')
    for comp in components[1:]:
        module = getattr(module,comp)
    return module
