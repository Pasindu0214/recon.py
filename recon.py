import os
import subprocess
import shutil
import sys

def create_directory(target_ip):
    directory = f"{target_ip}_script"
    os.makedirs(directory, exist_ok=True)
    print(f"Creating directory {directory}.")
    return directory

def run_command(command, output_file):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    with open(output_file, 'w') as f:
        f.write(result.stdout)
    print(f"The results are stored in {output_file}.")

def check_and_install(tool_name, install_command):
    if shutil.which(tool_name) is None:
        print(f"{tool_name} is not installed. Installing {tool_name}...")
        result = subprocess.run(install_command, shell=True)
        if result.returncode != 0:
            print(f"Failed to install {tool_name}. Please install it manually.")
            return False
    return True

def nmap_scan(target_ip, directory):
    if check_and_install('nmap', 'sudo apt-get install -y nmap'):
        run_command(['nmap', target_ip], os.path.join(directory, 'nmap'))

def nslookup_scan(target_ip, directory):
    if check_and_install('nslookup', 'sudo apt-get install -y dnsutils'):
        run_command(['nslookup', target_ip], os.path.join(directory, 'nslookup'))

def ping_scan(target_ip, directory):
    if check_and_install('ping', 'sudo apt-get install -y iputils-ping'):
        run_command(['ping', '-c', '4', target_ip], os.path.join(directory, 'ping'))

def curl_scan(target_ip, directory):
    if check_and_install('curl', 'sudo apt-get install -y curl'):
        run_command(['curl', '-I', target_ip], os.path.join(directory, 'curl'))

def gobuster_scan(target_ip, directory):
    if check_and_install('gobuster', 'sudo apt-get install -y gobuster'):
        run_command(['gobuster', 'dir', '-u', f"http://{target_ip}", '-w', '/usr/share/wordlists/dirb/common.txt'], os.path.join(directory, 'gobuster_results.txt'))

def nikto_scan(target_ip, directory):
    if check_and_install('nikto', 'sudo apt-get install -y nikto'):
        run_command(['nikto', '-h', target_ip], os.path.join(directory, 'nikto'))

def whatweb_scan(target_ip, directory):
    if check_and_install('whatweb', 'sudo apt-get install -y whatweb'):
        run_command(['whatweb', target_ip], os.path.join(directory, 'whatweb'))

def main(target_ip):
    directory = create_directory(target_ip)
    nmap_scan(target_ip, directory)
    nslookup_scan(target_ip, directory)
    ping_scan(target_ip, directory)
    curl_scan(target_ip, directory)
    gobuster_scan(target_ip, directory)
    nikto_scan(target_ip, directory)
    whatweb_scan(target_ip, directory)
    # Add more tool integrations here

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <TARGET_IP>")
        sys.exit(1)
    target_ip = sys.argv[1]
    main(target_ip)
