#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 2


params_values = {}


def get_param_value(name, default=None):
    return next((v for k, v in params_values.items() if k.endswith("." + name)), default)

def set_random_seed():
    random.seed(get_param_value("seed", 1234))

# A generic fake featurize script. Saves params amd "work" as json.
# Params might affect result in any way, work will improve metrics.
assert len(sys.argv) == 3, "Expected argv: featurize.py in out"

with open(sys.argv[2], "w") as feat:
    data_size = os.stat(sys.argv[1]).st_size
    json.dump({"params": params_values, "work": [math.log(data_size + 1), VERSION]}, feat)

# Comment to update: