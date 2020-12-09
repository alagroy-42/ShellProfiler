#!/usr/bin/env python3

import os
import sys
import yaml
from src.profile import Profile
from src.executer import Executer

file = open(os.path.dirname(__file__) + '/profiles.yaml', 'r')
profilesInfos = yaml.safe_load(file)
profiles = list(profilesInfos)

if len(sys.argv) == 1:
    for i in range(len(profiles)):
        print(str(i) + ': ' + profiles[i])
    index = int(input('What profile would you like to load ? '))
    if index < 0 or index > len(profiles):
        print('This number doesn\'t correspond to any profile', file=sys.stderr)
        exit(1)
    index = profiles[index]
else:
    index = sys.argv[1]

profile = Profile(profilesInfos[index], index)
executer = Executer(profile.loadProfile(), profile.name, profile.shell)
executer.exec()

