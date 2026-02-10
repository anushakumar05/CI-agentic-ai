from agent.git_ops import clone_repo, create_feature_branch, commit_and_push
from agent.context import read_repo_context
from agent.llm import generate_code
from agent.apply_file_changes import apply_changes
from agent.test_runner import run_tests
from agent.config import STRATO_REPO_URL, WORKDIR


def run(user_request):

    if not STRATO_REPO_URL:
        raise RuntimeError("STRATO_REPO_URL is not set")

    if not WORKDIR:
        raise RuntimeError("WORKDIR is not set")
    
    repo = clone_repo(STRATO_REPO_URL, WORKDIR)
    branch = create_feature_branch(repo)

    context = read_repo_context(WORKDIR)
    plan = generate_code(context, user_request)

    apply_changes(WORKDIR, plan["files"])
    run_tests(WORKDIR)

    commit_and_push(repo, plan["summary"])
    print(f"✅ Pushed branch {branch}")
