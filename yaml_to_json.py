import yaml
import json
from yaml.loader import SafeLoader

# Open the file and load the file
with open('gripper.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)

with open('gripper.json', 'w') as f:
    json.dump(data, f, sort_keys=False)