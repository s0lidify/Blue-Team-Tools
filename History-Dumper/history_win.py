import os
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Extract Windows command history for all users.")
    parser.add_argument("-o", "--output", required=True,
                        help="Output directory (use '.' for current working directory)")
    args = parser.parse_args()
    
    # Resolve and create output directory if needed
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Get user profiles from C:\Users
    users_dir = "C:\\Users"
    user_profiles = [d for d in os.listdir(users_dir) if os.path.isdir(os.path.join(users_dir, d))]
    
    for user in user_profiles:
        history_file = os.path.join(output_dir, f"{user}_history_{timestamp}.txt")
        with open(history_file, "w", encoding="utf-8") as out:
            out.write(f"Command History for {user}\n")
            out.write("=" * 40 + "\n\n")
            
            # Extract PowerShell history
            ps_history_path = os.path.join(users_dir, user, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadline", "ConsoleHost_history.txt")
            if os.path.exists(ps_history_path):
                out.write("[PowerShell History]\n")
                with open(ps_history_path, "r", encoding="utf-8", errors="ignore") as f:
                    out.writelines(f.readlines())
                out.write("\n")
            
            # Extract CMD history (Note: DOSKEY history is session-based and may not be stored persistently)
            # This is an example approach if a history file exists.
            cmd_history_path = os.path.join(users_dir, user, "AppData", "Roaming", "Microsoft", "Windows", "cmd.exe", "History")
            if os.path.exists(cmd_history_path):
                out.write("[CMD History]\n")
                with open(cmd_history_path, "r", encoding="utf-8", errors="ignore") as f:
                    out.writelines(f.readlines())
                out.write("\n")
    
    print(f"Command history saved to {output_dir}")

if __name__ == "__main__":
    main()
