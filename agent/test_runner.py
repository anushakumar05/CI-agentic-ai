# Forces Python to clone from the cloned repo, not locally
# Matches GitHub Actions behavior

import subprocess
import os

def run_tests(repo_root):
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.join(repo_root, "src")

    subprocess.run(
        ["pytest"],
        cwd=repo_root,
        check=True,
        env=env,
    )
