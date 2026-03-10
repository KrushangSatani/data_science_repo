import os
import json

def safe_write_json(data, filename, folder="outputdirectory"):
    if not os.path.exists(folder):
        os.makedirs(folder) # Tests directory creation on FUSE
    path = os.path.join(folder, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    return f"Successfully wrote to {path}"
