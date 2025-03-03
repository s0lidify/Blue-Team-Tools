# Blue-Team-Tools
This repo is a stack of tools helpful for Blue Team operations.

## Make tools accessible anywhere
To make them accessible anywhere on the system do this:
1. `mkdir -p ~/blue_scripts`
2. `mv script.py ~/blue_scripts/`
3. Edit `~/.bashrc`
   `echo 'export PATH="$HOME/blue_scripts:$PATH"' >> ~/.bashrc` # Append
   `source ~/.bashrc`
4. `chmod +x ~/blue_scripts/your_script.py`
5. Run
   `script.py`
