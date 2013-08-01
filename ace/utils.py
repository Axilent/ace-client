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
