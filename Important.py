import os
import subprocess
import tempfile
import git
import shutil
import sys

# Banner
print("""
______       _   _ _ _
| _ |    | |  (_) | |
| | | |__ _ __ | |__ _| | |
| | | / _` | '_ \\| '_ \\| | | |
| |/ / (_| | |_) | |_) | | | |
\\___/ \\__,_|.__/|_.__/|_|_| 
         | |         
         |_|         

** Automated Tool Installer **
** Version 1.2 **
""")

# Define the list of repositories to clone and install
repos = [
    {"url": "https://github.com/SecureAuthCorp/impacket.git", "install_cmd": "pip install .", "binary_name": "impacket-findDelegation"},
    {"url": "https://github.com/danielmiessler/SecLists.git", "install_cmd": "None", "binary_name": "SecLists"},
    {"url": "https://github.com/carlospolop/PEASS-ng.git", "install_cmd": "pip install .", "binary_name": "linpeas.sh"},
    {"url": "https://github.com/danielbohannon/Invoke-Obfuscation.git", "install_cmd": "pip install .", "binary_name": "Invoke-Obfuscation"},
    {"url": "https://github.com/rebootuser/LinEnum.git", "install_cmd": "chmod +x LinEnum.sh", "binary_name": "LinEnum.sh"},
    {"url": "https://github.com/21y4d/nmapAutomator.git", "install_cmd": "pip install .", "binary_name": "nmapAutomator"},
    {"url": "https://github.com/RustScan/RustScan.git", "install_cmd": "cargo build --release", "binary_name": "target/release/rustscan"},
    {"url": "https://github.com/EmpireProject/Empire.git", "install_cmd": "./setup/install.sh", "binary_name": "Empire"},
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "install_cmd": "powershell -Command \"Import-Module .\\PowerSploit.ps1\"", "binary_name": "PowerSploit.ps1"},
    {"url": "https://github.com/ethicalhackingplayground/katana.git", "install_cmd": "pip install .", "binary_name": "katana"},
    {"url": "https://github.com/thewhiteh4t/FinalRecon.git", "install_cmd": "pip install .", "binary_name": "FinalRecon"},
    {"url": "https://github.com/bhavsec/reconspider.git", "install_cmd": "pip install .", "binary_name": "reconspider"},
    {"url": "https://github.com/411Hall/JAWS.git", "install_cmd": "pip install .", "binary_name": "JAWS"},
    {"url": "https://github.com/S3cur3Th1s/WinPwn.git", "install_cmd": "pip install .", "binary_name": "WinPwn"}
]

# Function to check if a tool is installed
def is_tool_installed(binary_name):
    return shutil.which(binary_name) is not None

# Function to clone repositories
def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    temp_dir = tempfile.mkdtemp()
    dest_dir = os.path.join(temp_dir, repo_name)
    print(f"\n** Cloning {repo_name} **")
    print(f"Cloning into {dest_dir}...")
    try:
        git.Repo.clone_from(repo_url, dest_dir)
    except git.exc.GitCommandError as e:
        print(f"Error cloning {repo_url}: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred while cloning {repo_url}: {e}")
        return None, None
    return temp_dir, dest_dir

# Function to install software
def install_software(repo_path, install_cmd):
    if install_cmd == "None":
        return
    print(f"\n** Installing {repo_path.split('/')[-1]} **")
    print(f"Running installation command: {install_cmd}")

    # Ensure correct execution permissions before running scripts
    if install_cmd.startswith("./") or "install.sh" in install_cmd:
        subprocess.run(f"chmod +x {install_cmd.split()[0]}", shell=True, cwd=repo_path, check=True)

    try:
        subprocess.run(install_cmd, shell=True, cwd=repo_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {install_cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Stderr: {e.stderr.decode()}")
        return

# Function to create symlinks
def create_symlink(binary_path, binary_name):
    print(f"\n** Creating symlink for {binary_name} **")
    install_dir = os.environ.get("TOOLS_PATH", "/usr/local/bin")
    symlink_path = os.path.join(install_dir, binary_name)

    if not os.path.exists(binary_path):
        print(f"** Warning: Binary {binary_path} not found. Skipping symlink creation. **")
        return

    if os.path.exists(symlink_path):
        os.remove(symlink_path)

    print(f"Creating symlink at {symlink_path}")
    os.symlink(binary_path, symlink_path)

# Function to check and install dependencies
def check_and_install_dependencies(dependencies):
    try:
        subprocess.run(["which", "apt"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for dep in dependencies:
            try:
                subprocess.run(["apt", "install", "-y", dep], check=True)
                print(f"Installed dependency: {dep}")
            except subprocess.CalledProcessError:
                print(f"Failed
