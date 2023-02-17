import os

# Prompt the user for the Git URL
git_url = input("Enter the Git URL: ")

# Clone the repository
os.system(f"git clone {git_url}")

# Prompt the user for the branch to merge
branch_name = input("Enter the name of the branch to merge: ")

# Change to the repository directory
repo_name = git_url.split("/")[-1].replace(".git", "")
os.chdir(repo_name)

# Checkout the specified branch
os.system(f"git checkout {branch_name}")

# Merge the specified branch into the current branch
try:
    os.system(f"git merge {branch_name}")
except:
    # If there are conflicts, run the diff tool
    os.system("git mergetool")

    # Complete the merge once conflicts are resolved
    os.system("git merge --continue")

# Delete the specified branch
os.system(f"git branch -d {branch_name}")
