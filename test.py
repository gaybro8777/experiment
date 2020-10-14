#!/usr/bin/env python3

import os
import sys

cwd = os.getcwd()
path = os.path.join(cwd, 'federated')
sys.path.append(path)

from federated.utils import training_loop

print(dir(training_loop))
