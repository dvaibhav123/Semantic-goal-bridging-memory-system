import os
import re
import json

def load_tags(goals_path):
    if not os.path.exists(goals_path):
        return {"error": "Goals file not found"}
    
    with open(goals_path, 'r') as f:
        content = f.read()
    
    # Extract tags using regex: [Tags: #tag1, #tag2]
    tag_pattern = re.compile(r'\[Tags: (.*?)\]')
    tags = tag_pattern.findall(content)
    
    # Flatten and clean tags
    all_tags = []
    for t_str in tags:
        all_tags.extend([t.strip() for t in t_str.split(',')])
    
    return list(set(all_tags))

if __name__ == "__main__":
    goals_file = "Goals/Goals.md"
    tags = load_tags(goals_file)
    print(json.dumps({"semantic_tags": tags}, indent=2))
