#!/usr/bin/env python3
import sys, json
import random

VERSION = 4


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['train.weight_factor',
                  'model.num_est',
                  'train.min_features',
                  'preprocessing.drop',
                  'variables.weight_factor',
                  'model.sample',
                  'preprocessing.ngrams',
                  'variables.sample',
                  'tagging.drop',
                  'model.features',
                  'tagging.weight_factor',
                  'variables.max_features',
                  'preprocessing.folds',
                  'preprocessing.features',
                  'train.epochs',
                  'preprocessing.split',
                  'train.learning_rate',
                  'preprocessing.columns',
                  'tagging.features',
                  'preprocessing.min_split',
                  'variables.threads',
                  'model.folds',
                  'tagging.max_features',
                  'model.batch_size',
                  'variables.features']}]

params_values = {}
for rec in used_params:
    for fname, pnames in rec.items():
        with open(fname, 'r') as fd:
            params = yaml.safe_load(fd)

        for name in pnames:
            params_values[f"{fname}:{name}"] = get_in(params, name.split("."))


def get_param_value(name, default=None):
    return next((v for k, v in params_values.items() if k.endswith("." + name)), default)

def set_random_seed():
    random.seed(get_param_value("seed", 1234))

# A train generic fake script, simply add train params and "work" to the data
assert len(sys.argv) == 3, "Expected argv: train.py in model"

with open(sys.argv[1]) as fd, open(sys.argv[2], "w") as model:
    data = json.load(fd)
    data["params"].update(params_values)
    data["work"].append(VERSION)
    json.dump(data, model)

# Comment to update: