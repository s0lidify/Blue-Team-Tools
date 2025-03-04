## Process Monitor
Tool designed to minitor active processes by comparing them against an integrated list of suspicious processes.
It has two modes `default` and `--alerts-only`. 
Default interval is `2` seconds, which can be modified with `--interval 3`
By default saves the log to `suspicious_processes.log` in the current directory, unless you specify a different log file `--log file.log`

## Usage
1. `python3 process_monitor.py --log process.log --alerts-only` 
2. `python3 process_monitor.py --log process.log --alerts-only --interval 3`
3. `python3 process_monitor.py --alerts-only` 
