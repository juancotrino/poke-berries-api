import os
import sys

# Add the root directory to the sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from docs import info

version = info.get('version')

if version:
    print(version)
else:
    raise ValueError("Version not found in info dictionary")
