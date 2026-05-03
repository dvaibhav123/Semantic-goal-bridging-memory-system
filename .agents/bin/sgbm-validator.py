import os
import sys

def validate_goal(goal_dir):
    progress_path = os.path.join(goal_dir, "Progress.md")
    knowledge_path = os.path.join(goal_dir, "Knowledge.md")
    
    if not os.path.exists(progress_path) or not os.path.exists(knowledge_path):
        return True # Not a standard goal folder
    
    # Simple check: Does Knowledge.md contain SGBM headers?
    with open(knowledge_path, 'r') as f:
        content = f.read()
        if "## Goal Snapshot" not in content or "## Context Map" not in content:
            print(f"Error: {goal_dir} Knowledge.md is missing SGBM headers.")
            return False
            
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sgbm-validator.py <goal_directory>")
        sys.exit(1)
    
    if not validate_goal(sys.argv[1]):
        sys.exit(1)
