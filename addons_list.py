import os
import collections

directory = '/Users/pga/odoo/bk'

def get_modules():
    dirs = {}
    for d in os.scandir(directory):
        path = d.path
        if 'Chapter' in path:
            dirs[path] = []
            for sub_d in os.scandir(path):
                if sub_d.path.split('/')[-1].startswith('r'):
                    dirs[path].append(sub_d.path)
            dirs[path] = sorted(dirs[path])
    return collections.OrderedDict(sorted(dirs.items()))

