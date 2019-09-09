import os
import yaml

path = os.path.dirname(os.path.abspath(__file__))
with open(path + "/configuration.yaml", 'r') as stream:
    CONFIG = yaml.safe_load(stream)
