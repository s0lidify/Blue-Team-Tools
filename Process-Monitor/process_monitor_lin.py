import psutil
import time
import argparse

SUSPICIOUS_PROCESSES = {
    "nc", "netcat", "bash", "sh", "dash", "zsh", "fish", "python",
    "perl", "ruby", "php", "nmap", "hydra", "john", "sqlmap", "msfconsole",
    "weevely", "hashcat", "tcpdump", "tshark", "wireshark", "socat",
    "scp", "wget", "curl", "ssh", "telnet", "ftp", "rsync",
    "gcc", "make", "objdump", "strace", "ltrace", "gdb",
    "chkrootkit", "rkhunter", "lynis", "netstat", "arp", "route",
    "ip", "iptables", "firewalld", "systemctl", "journalctl", "cron",
    "at", "htop", "top", "ps", "kill", "pkill", "pkexec", "sudo",
}

def log_detection(log_file, message):
    """Writes detections to a log file."""
    with open(log_file, "a") as log:
        log.write(message + "\n")

def get_processes():
    """Returns a set of currently running process names."""
    return {proc.name().lower() for proc in psutil.process_iter(attrs=["name"])}

def monitor_processes(log_file, interval, log_alerts_only):
    """Continuously monitors for new and suspicious processes."""
    print(f"[*] Starting Linux process monitoring (Logging to: {log_file})...")
    seen_processes = get_processes()

    while True:
        time.sleep(interval)
        current_processes = get_processes()
        new_processes = current_processes - seen_processes

        for process in new_processes:
            message = f"[+] New process detected: {process}"
            
            if not log_alerts_only:
                print(message)
                log_detection(log_file, message)

            if process in SUSPICIOUS_PROCESSES:
                alert = f"[!] ALERT: Suspicious process detected -> {process.upper()}"
                print(alert)
                log_detection(log_file, alert)

        seen_processes = current_processes  # Update process list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux Live Process Monitor")
    parser.add_argument("--log", default="suspicious_processes.log", help="Path to the log file")
    parser.add_argument("--interval", type=int, default=2, help="Time interval between checks (in seconds)")
    parser.add_argument("--alerts-only", action="store_true", help="Only log alerts (skip normal new process detections)")

    args = parser.parse_args()
    monitor_processes(args.log, args.interval, args.log_alerts)
