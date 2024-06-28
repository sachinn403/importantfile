import os
import subprocess
import git

# List of GitHub repositories
repos = [
    "https://github.com/fortra/impacket",
    "https://github.com/danielmiessler/SecLists",
    "https://github.com/peass-ng/PEASS-ng",
    "https://github.com/danielbohannon/Invoke-Obfuscation",
    "https://github.com/rebootuser/LinEnum",
    "https://github.com/21y4d/nmapAutomator",
    "https://github.com/RustScan/RustScan",
    "https://github.com/EmpireProject/Empire",
    "https://github.com/PowerShellMafia/PowerSploit",
    "https://github.com/projectdiscovery/katana",
    "https://github.com/thewhiteh4t/FinalRecon",
    "https://github.com/bhavsec/reconspider",
    "https://github.com/411Hall/JAWS",
    "https://github.com/S3cur3Th1sSh1t/WinPwn"
]

# Path to the bin directory
bin_dir = "/usr/local/bin"

# Function to clone repositories
def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1]
    dest_dir = os.path.join(bin_dir, repo_name)
    if not os.path.exists(dest_dir):
        print(f"Cloning {repo_name}...")
        git.Repo.clone_from(repo_url, dest_dir)
    else:
        print(f"{repo_name} already exists. Skipping...")

# Ensure the bin directory exists
if not os.path.exists(bin_dir):
    os.makedirs(bin_dir)

# Clone each repository
for repo in repos:
    clone_repo(repo)

# Make scripts executable and create symlinks in the bin directory
for root, dirs, files in os.walk(bin_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith(".sh") or file.endswith(".py"):
            os.chmod(file_path, 0o755)
            symlink_path = os.path.join(bin_dir, os.path.basename(file_path))
            if not os.path.exists(symlink_path):
                os.symlink(file_path, symlink_path)
                print(f"Created symlink for {file_path} -> {symlink_path}")

print("All repositories have been cloned and symlinks created.")
