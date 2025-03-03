# Blue-Team-Tools
This repo is a stack of tools helpful for Blue Team operations.

## Make tools accessible anywhere
To make them accessible anywhere on the system do this:
1. `mkdir -p ~/scripts`
2. `mv script.py ~/scripts/`
3. Edit `~/.bashrc`
   `echo 'export PATH="$HOME/scripts:$PATH"' >> ~/.bashrc` # Append
   `source ~/.bashrc`
4. `chmod +x ~/scripts/your_script.py`
5. Run
   `script.py`
