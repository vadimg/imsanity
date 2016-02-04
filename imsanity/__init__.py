import os
import sys

script_dir = sys.path[0]

if not script_dir:
    # loaded interactively, assume cwd is the "script dir"
    script_dir = os.getcwd()

cur_dir = os.path.abspath(script_dir)

# loop until we get to filesystem root
while cur_dir != os.path.dirname(cur_dir):
    if os.path.isfile(os.path.join(cur_dir, '.imsanity')):
        sys.path.append(cur_dir)
        break
    cur_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))
