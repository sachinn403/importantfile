import os
import subprocess
import tempfile
import git
import shutil

# Banner
print("""
______          _     _ _ _ 
|  _  |        | |   (_) | |
| | | |__ _ __ | |__  _| | |
| | | / _` | '_ \| '_ \| | | |
| |/ / (_| | |_) | |_) | | | |
\___/ \__,_|.__/|_.__/|_|_|
          | |              
          |_|              

** Automated Tool Installer **
** Version 1.0 **
""")

# Define the list of repositories to clone and install
repos = [
    {"url": "https://github.com/SecureAuthCorp/impacket.git", "install_cmd": "pip install.", "binary_name": "impacket.py"},
    {"url": "https://github.com/danielmiessler/SecLists.git", "install_cmd": "pip install.", "binary_name": "SecLists.py"},
    {"url": "https://github.com/carlospolop/PEASS-ng.git", "install_cmd": "pip install.", "binary_name": "peass-ng.py"},
    {"url": "https://github.com/danielbohannon/Invoke-Obfuscation.git", "install_cmd": "pip install.", "binary_name": "Invoke-Obfuscation.py"},
    {"url": "https://github.com/rebootuser/LinEnum.git", "install_cmd": "chmod +x LinEnum.sh", "binary_name": "LinEnum.sh"},
    {"url": "https://github.com/21y4d/nmapAutomator.git", "install_cmd": "pip install.", "binary_name": "nmapAutomator.py"},
    {"url": "https://github.com/RustScan/RustScan.git", "install_cmd": "cargo build --release", "binary_name": "RustScan"},
    {"url": "https://github.com/EmpireProject/Empire.git", "install_cmd": "pip install.", "binary_name": "Empire.py"},
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "install_cmd": "powershell -Command \"Import-Module.\\PowerSploit.ps1\"", "binary_name": "PowerSploit.ps1"},
    {"url": "https://github.com/ethicalhackingplayground/katana.git", "install_cmd": "pip install.", "binary_name": "katana"},
    {"url": "https://github.com/thewhiteh4t/FinalRecon.git", "install_cmd": "pip install.", "binary_name": "FinalRecon.py"},
    {"url": "https://github.com/bhavsec/reconspider.git", "install_cmd": "pip install.", "binary_name": "reconspider.py"},
    {"url": "https://github.com/411Hall/JAWS.git", "install_cmd": "pip install.", "binary_name": "JAWS.py"},
    {"url": "https://github.com/S3cur3Th1s/WinPwn.git", "install_cmd": "pip install.", "binary_name": "WinPwn.py"}
]

# Function to clone repositories
def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    temp_dir = tempfile.mkdtemp()
    dest_dir = os.path.join(temp_dir, repo_name)
    print(f"\n** Cloning {repo_name} **")
    print(f"Cloning into {dest_dir}...")
    git.Repo.clone_from(repo_url, dest_dir)
    return temp_dir, dest_dir

# Function to install software
def install_software(repo_path, install_cmd):
    print(f"\n** Installing {repo_path.split('/')[-1]} **")
    print(f"Running installation command: {install_cmd}")
    subprocess.run(install_cmd, shell=True, cwd=repo_path)

# Function to create symlinks
def create_symlink(binary_path, binary_name):
    print(f"\n** Creating symlink for {binary_name} **")
    print(f"Creating symlink at /usr/bin/{binary_name}")
    os.symlink(binary_path, f"/usr/bin/{binary_name}")

# Process each repository
for repo in repos:
    try:
        temp_dir, repo_path = clone_repo(repo["url"])
        install_software(repo_path, repo["install_cmd"])
        binary_path = os.path.join(repo_path, repo["binary_name"])
        create_symlink(binary_path, repo["binary_name"])
        print(f"\n** Deleting temporary files and directories for {repo_path.split('/')[-1]} **")
        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"\n** Error: Failed to process {repo['url']}. Error
