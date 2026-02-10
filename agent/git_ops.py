from git import Repo
import os
import uuid
import shutil

def clone_repo(repo_url, workdir):
    if os.path.exists(workdir):
        shutil.rmtree(workdir)
    return Repo.clone_from(repo_url, workdir)

def create_feature_branch(repo):
    branch_name = f"ai-feature-{uuid.uuid4().hex[:8]}"
    repo.git.checkout("-b", branch_name)
    return branch_name

def commit_and_push(repo, message):
    repo.git.add(A=True)
    repo.index.commit(message)

    branch = repo.active_branch.name
    repo.remote().push(refspec=f"{branch}:{branch}", set_upstream=True)
