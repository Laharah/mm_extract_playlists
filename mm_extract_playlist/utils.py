from collections import defaultdict
import re

def groupby(iterable, key=lambda it: it):
    'Return a dic whose keys are key(it) and whose values are elements of iterable with that key.'
    dic = defaultdict(list)
    for it in iterable:
        dic[key(it)].append(it)
    return dic

CHAR_REPLACE = [
    (re.compile(r'[\\/]'), '_'),  # / and \ -- forbidden everywhere.
    (re.compile(r'^\.'), '_'),  # Leading dot (hidden files on Unix).
    (re.compile(r'[\x00-\x1f]'), ''),  # Control characters.
    (re.compile(r'[<>:"\?\*\|]'), '_'),  # Windows "reserved characters".
    (re.compile(r'\.$'), '_'),  # Trailing dots.
    (re.compile(r'\s+$'), ''),  # Trailing whitespace.
]


def sanitize(txt, replacements=None):
    'sanitize a path segment for filesystems'
    replacements = replacements or CHAR_REPLACE

    for regex, repl in replacements:
        txt = regex.sub(repl, txt)
    return txt
