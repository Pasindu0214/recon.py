# Automated Recon Toolkit in Python

## Overview

This project is an Automated Recon Toolkit developed in Python. It performs various scanning and information-gathering tasks to assist in penetration testing and security assessments. The toolkit automates the installation and use of several essential tools, enhancing penetration testing efficiency by automating repetitive tasks for comprehensive information gathering.

## Features

- **Automated Installation**: Automatically installs required tools if they are not already installed.
- **Tools Used**:
  - `nmap`: Network exploration tool and security scanner.
  - `nslookup`: Network administration command-line tool for querying the Domain Name System (DNS).
  - `ping`: Utility to test the reachability of a host on an IP network.
  - `curl`: Command-line tool for transferring data with URLs.
  - `gobuster`: Tool to brute-force URIs (directories and files) in web sites and DNS subdomains (with wildcard support).
  - `nikto`: Web server scanner which performs comprehensive tests against web servers for multiple items.
  - `whatweb`: Next-generation web scanner that identifies what websites are running.

## Prerequisites

- Python 3.x installed on your Linux system.
- Sudo privileges for installing necessary tools.

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/<username>/automated-recon-toolkit.git
   cd automated-recon-toolkit
2. **Run the Script**:
   ```sh
   sudo python3 recon.py <TARGET_IP>
3. **Directory Structure**
   ```sh
   The script creates a directory named after the target IP to store the results.
   Results of each scan are stored in separate files within this directory.
