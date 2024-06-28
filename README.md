# Kali Linux Tools Downloader

This repository contains a Python script to download various security tools from GitHub and set them up in your Kali Linux environment. The script clones the specified repositories, makes the scripts executable, and creates symlinks in the `/usr/local/bin` directory, allowing you to run the tools directly from the command line.

## Tools Included

The script will download the following tools:

- [Impacket](https://github.com/fortra/impacket)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [winPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS)
- [linPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)
- [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [nmapAutomator](https://github.com/21y4d/nmapAutomator)
- [RustScan](https://github.com/RustScan/RustScan)
- [Empire](https://github.com/EmpireProject/Empire)
- [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)
- [Katana](https://github.com/projectdiscovery/katana)
- [FinalRecon](https://github.com/thewhiteh4t/FinalRecon)
- [ReconSpider](https://github.com/bhavsec/reconspider)
- [JAWS](https://github.com/411Hall/JAWS)
- [WinPwn](https://github.com/S3cur3Th1sSh1t/WinPwn)

## Requirements

Ensure you have the necessary Python packages installed:

```sh
pip install requests gitpython

## USAGE

1. Clone this repository to your local machine.

```sh
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository


2. Run the Python script with sufficient privileges to write to `/usr/local/bin`.

```sh
sudo python3 download_tools.py
```

The script will:

1. Clone each GitHub repository into the specified `bin_dir`.
2. Make all `.sh` and `.py` files within those repositories executable.
3. Create symlinks for those executable files in the `bin_dir`, allowing you to run them by their names.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the authors of the various tools included in this script.
- Inspired by the need to streamline the setup of essential security tools on Kali Linux.


