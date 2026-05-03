import os
import json
import sys

LOG_FILE = ".agents/tmp/session_log.json"

def get_session_events():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def flush_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def sync_state(goal_dir):
    events = get_session_events()
    if not events:
        print(f"No session events detected for {goal_dir}. Checking for direct changes...")
        # Fallback to direct analysis if no tool logs exist
        return
    
    print(f"Detected {len(events)} events for synthesis in {goal_dir}.")
    # synthesis_input = json.dumps(events, indent=2)
    
    # SGBM Syncer: [STUB] synthesis logic would go here.
    # In practice, this output would be sent to an LLM to generate the Snapshot update.
    
    # flush_log() # Should be flushed after successful synthesis and write to Knowledge.md

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sgbm-syncer.py <goal_directory>")
        sys.exit(1)
    
    sync_state(sys.argv[1])
