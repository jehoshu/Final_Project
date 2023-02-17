import os
import re

import git

# Get git URL from environment variable
url = os.environ.get('REPO_TO_CLONE')

# Check if the URL is from GitHub
if re.match(r"https://github.com/.*", url):
    # Check if the repository exists locally
    try:
        repo = git.Repo("./NewRepo")
    except git.exc.InvalidGitRepositoryError:
        # Clone the repository
        repo = git.Repo.clone_from(url, "./NewRepo")
    except Exception as e:
        print(e)
        raise SystemExit
      # Check if the branch exists, if not create it
    try:
        branch_name = os.environ.get('BRANCH_TO_MERGE')
        branch = repo.create_head(branch_name)
    except git.exc.GitCommandError:
        branch = repo.heads[branch_name]
    # Checkout the branch
    branch.checkout()
    # Attempt to merge the branch
    try:
        repo.git.merge("main")
    except git.exc.GitCommandError as e:
        if "CONFLICT" in e.stderr:
            # Handle merge conflicts
            print("Conflicts: ")
            print(e.stderr)
            resolve = input("Resolve conflicts and enter 'y' to continue: ")
            if resolve == "y":
                repo.git.add(A=True)
                repo.index.commit("Resolved conflicts")
    except Exception as e:
        print(e)
        raise SystemExit
else:
    print("you should use Github link only")