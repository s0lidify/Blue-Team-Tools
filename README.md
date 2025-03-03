# Blue-Team-Tools
This repo is a stack of tools helpful for Blue Team operations.

## Make tools accessible anywhere
To make them accessible anywhere on the system do this:
1. `mkdir -p ~/blue_scripts`
2. `mv script.py ~/blue_scripts/`
3. Append to `~/.bashrc`
`echo 'export PATH="$HOME/blue_scripts:$PATH"' >> ~/.bashrc` 
4. Update `source ~/.bashrc`
5. `chmod +x ~/blue_scripts/your_script.py`
6. Run
`script.py`
