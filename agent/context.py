import os

EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", ".github"}

def read_repo_context(root_dir):
    context = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith(".py") or file.endswith(".md"):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, root_dir)
                with open(path, "r") as f:
                    context.append(f"\n--- {rel_path} ---\n{f.read()}")
    return "\n".join(context)
