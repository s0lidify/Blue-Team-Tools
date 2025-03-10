import os
import argparse
from datetime import datetime
import pwd

def main():
    parser = argparse.ArgumentParser(description="Extract Linux shell history for all users, including root.")
    parser.add_argument("-o", "--output", required=True,
                        help="Output directory (use '.' for current working directory)")
    args = parser.parse_args()
    
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Iterate over all users, including root
    for user in pwd.getpwall():
        home_dir = user.pw_dir
        username = user.pw_name
        
        if not os.path.isdir(home_dir):
            continue  # Skip if the home directory does not exist
        
        output_file = os.path.join(output_dir, f"{username}_history_{timestamp}.txt")
        try:
            with open(output_file, "w", encoding="utf-8") as out:
                out.write(f"Command History for {username}\n")
                out.write("=" * 40 + "\n\n")
                
                for shell_history in [".bash_history", ".zsh_history", ".ash_history", ".sh_history"]:
                    history_path = os.path.join(home_dir, shell_history)
                    if os.path.exists(history_path):
                        out.write(f"[{shell_history}]\n")
                        try:
                            with open(history_path, "r", encoding="utf-8", errors="ignore") as f:
                                out.writelines(f.readlines())
                        except PermissionError:
                            out.write("Permission denied.\n")
                        out.write("\n")
        except PermissionError:
            print(f"Skipping {username} (Permission denied)")

    print(f"Command history saved to {output_dir}")

if __name__ == "__main__":
    main()
