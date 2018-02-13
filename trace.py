from datetime import datetime
import sys
from config import get_config

INFO = "INFO"
WARN = "WARN"
ERROR = "ERROR"
ALWAYS = "ALWAYS"

def trace(line, level):
    # Write a formatted trace line
    # INFO WARN ERROR
    # INFO: INFO WARN ERROR
    # WARN: WARN ERROR
    # ERROR: ERROR
    global config
    trace_level = get_config("trace_level")
    if trace_level == ERROR and level != ERROR:
        return
    elif trace_level == WARN and (level != ERROR and level != WARN):
        return
    print(level + " - "+datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str(line))
    sys.stdout.flush()