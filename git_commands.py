import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return result

# Define the repository path
repo_path = os.path.expanduser('~/Documents/git/Attention-Blitz')

# Create the directory if it does not exist
if not os.path.exists(repo_path):
    os.makedirs(repo_path)
    print(f"Created directory {repo_path}")

# Change to the repository directory
os.chdir(repo_path)

# Stage the changes
run_command('git add .')

# Commit the changes with a new commit message
commit_message = "Your new commit message"
run_command(f'git commit -m "{commit_message}"')

# Push the changes to the remote repository using PAT from environment variables
pat = os.getenv('GITHUB_PAT')
if pat:
    run_command(f'git push https://{pat}@github.com/sisi195/Attention-Blitz.git')
else:
    print("Personal Access Token (PAT) not found. Please set the GITHUB_PAT environment variable.")
