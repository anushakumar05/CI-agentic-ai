# agent/apply_file_changes.py
import os

def apply_changes(repo_root, files):
    for f in files:
        full_path = os.path.join(repo_root, f["path"])
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as fh:
            fh.write(f["content"])
