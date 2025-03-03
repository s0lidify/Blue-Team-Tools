import os
import subprocess
import requests

# Replace with your actual AbuseIPDB API key
ABUSEIPDB_API_KEY = "YOUR_API_KEY" # <<< Enter Your API Here

def check_ip_abuse(ip):
    """
    Check an IP address using the AbuseIPDB API.
    Returns the abuse confidence score and the full API result.
    """
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        "ipAddress": ip,
        "maxAgeInDays": "90"  # Check reports in the last 90 days
    }
    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                result = data["data"]
                abuse_confidence = result.get("abuseConfidenceScore", 0)
                return abuse_confidence, result
            else:
                print(f"Unexpected API response for IP {ip}: {data}")
                return 0, None
        else:
            print(f"Error checking IP {ip}: HTTP {response.status_code}")
            return 0, None
    except requests.RequestException as e:
        print(f"Error checking IP {ip}: {e}")
        return 0, None

def get_active_connections():
    """
    Retrieves active network connections using netstat.
    Returns a list of tuples: (remote_ip, process_info)
    """
    connections = []
    
    # Run netstat command to get active TCP and UDP connections.
    result = subprocess.run(["netstat", "-tunp"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error running netstat.")
        return []
    
    lines = result.stdout.split("\n")
    for line in lines:
        parts = line.split()
        # Ensure the line is a connection record with enough fields and is TCP/UDP.
        if len(parts) < 7 or parts[0] not in ["tcp", "udp"]:
            continue
        
        # parts[3] is the local address; parts[4] is the remote address.
        remote_address = parts[4]
        process_info = parts[6] if "/" in parts[6] else "Unknown"
        
        # Remove the port number from the remote address.
        remote_ip = remote_address.rsplit(":", 1)[0]
        connections.append((remote_ip, process_info))
    
    return connections

def main():
    print("[*] Scanning active network connections...")
    connections = get_active_connections()
    
    if not connections:
        print("[-] No active connections found.")
        return

    flagged_connections = []
    for ip, process in connections:
        # Exclude local IP address 127.0.0.1 from queries.
        if ip == "127.0.0.1":
            continue
        print(f"Checking IP: {ip}")
        abuse_confidence, details = check_ip_abuse(ip)
        # Define a threshold: e.g., if abuse confidence score > 50, consider the IP suspicious.
        if abuse_confidence > 50:
            flagged_connections.append((ip, process, abuse_confidence, details))
    
    if flagged_connections:
        print("\n[!] Suspicious connections detected:")
        for ip, process, abuse_confidence, details in flagged_connections:
            print(f" - IP: {ip} | Process: {process} | Abuse Confidence Score: {abuse_confidence}")
    else:
        print("[+] No suspicious connections found.")

if __name__ == "__main__":
    main()
