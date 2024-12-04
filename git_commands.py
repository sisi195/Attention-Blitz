import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return result

# Define the repository path
repo_path = '/Users/sierragordon/Documents/git/Attention-Blitz'

# Create the directory if it does not exist
if not os.path.exists(repo_path):
    os.makedirs(repo_path)
    print(f"Created directory {repo_path}")

# Change to the repository directory
os.chdir(repo_path)

# Stage the changes
run_command('git add .')

# Commit the changes with your new commit message
run_command('git commit -m "Your new commit message"')

# Push the changes to the remote repository using PAT
run_command('git push https://<your_personal_access_token>@github.com/sisi195/Attention-Blitz.git')
    
