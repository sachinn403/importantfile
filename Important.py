import os
import subprocess
import tempfile
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
bin_dir = "/usr/bin"

# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr.decode())
        raise Exception(f"Command failed: {command}")
    return result.stdout.decode()

# Function to clone repositories
def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1]
    temp_dir = tempfile.mkdtemp()
    dest_dir = os.path.join(temp_dir, repo_name)
    print(f"Cloning {repo_name} into {dest_dir}...")
    git.Repo.clone_from(repo_url, dest_dir)
    return dest_dir

# Function to install software
def install_software(repo_path):
    print(f"Installing software from {repo_path}...")
    run_command(f"cd {repo_path} && make install")  # Adjust the installation command as needed

# Function to create symlinks
def create_symlink(binary_path, binary_name):
    symlink_path = os.path.join(bin_dir, binary_name)
    if not os.path.exists(symlink_path):
        os.symlink(binary_path, symlink_path)
        print(f"Created symlink for {binary_path} -> {symlink_path}")
    else:
        print(f"Symlink for {binary_name} already exists. Skipping...")

# Process each repository
for repo in repos:
    try:
        repo_path = clone_repo(repo)
        install_software(repo_path)
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".sh") or file.endswith(".py"):
                    binary_path = os.path.join(root, file)
                    os.chmod(binary_path, 0o755)
                    create_symlink(binary_path, file)
    except Exception as e:
        print(f"Failed to process {repo}: {e}")

print("All repositories have been cloned, installed, and symlinks created.")
