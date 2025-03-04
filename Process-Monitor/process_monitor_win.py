import psutil
import time
import argparse

SUSPICIOUS_PROCESSES = {
    "mimikatz.exe", "nc.exe", "netcat.exe", "powershell.exe", "cmd.exe",
    "taskmgr.exe", "regedit.exe", "wscript.exe", "cscript.exe", "schtasks.exe",
    "rundll32.exe", "svchost.exe", "mshta.exe", "certutil.exe", "wmic.exe",
    "explorer.exe", "procdump.exe", "winrar.exe", "winzip.exe",
    "unrar.exe", "putty.exe", "plink.exe", "psftp.exe", "ftp.exe",
    "telnet.exe", "sqlcmd.exe", "sc.exe", "net.exe", "nslookup.exe",
    "whoami.exe", "arp.exe", "route.exe", "ipconfig.exe", "netsh.exe",
    "curl.exe", "wget.exe", "bitsadmin.exe", "adb.exe",
}

def log_detection(log_file, message):
    """Writes detections to a log file."""
    with open(log_file, "a") as log:
        log.write(message + "\n")

def get_processes():
    """Returns a set of currently running process names."""
    return {proc.name().lower() for proc in psutil.process_iter(attrs=["name"])}

def monitor_processes(log_file, interval, alerts_only):
    """Continuously monitors for new and suspicious processes."""
    print(f"[*] Starting Windows process monitoring (Logging to: {log_file})...")
    seen_processes = get_processes()

    while True:
        time.sleep(interval)
        current_processes = get_processes()
        new_processes = current_processes - seen_processes

        for process in new_processes:
            if process in SUSPICIOUS_PROCESSES:
                alert = f"[!] ALERT: Suspicious process detected -> {process.upper()}"
                print(alert)
                log_detection(log_file, alert)
            elif not alerts_only:
                message = f"[+] New process detected: {process}"
                print(message)
                log_detection(log_file, message)

        seen_processes = current_processes  # Update process list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Windows Live Process Monitor")
    parser.add_argument("--log", default="suspicious_processes.log", help="Path to the log file")
    parser.add_argument("--interval", type=int, default=2, help="Time interval between checks (in seconds)")
    parser.add_argument("--alerts-only", action="store_true", help="Only log alerts (skip normal new process detections)")

    args = parser.parse_args()
    monitor_processes(args.log, args.interval, args.alerts_only)
