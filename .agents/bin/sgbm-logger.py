import os
import json
import sys
import datetime

LOG_FILE = ".agents/tmp/session_log.json"

def log_event(tool_name, intent, result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    event = {
        "timestamp": datetime.datetime.now().isoformat(),
        "tool": tool_name,
        "intent": intent,
        "result": result
    }
    
    events = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as f:
                events = json.load(f)
        except json.JSONDecodeError:
            pass
            
    events.append(event)
    
    with open(LOG_FILE, 'w') as f:
        json.dump(events, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        # If not enough args, assume it's being called with raw data
        print("Usage: python sgbm-logger.py <tool_name> <intent> <result>")
        sys.exit(1)
    
    log_event(sys.argv[1], sys.argv[2], sys.argv[3])
