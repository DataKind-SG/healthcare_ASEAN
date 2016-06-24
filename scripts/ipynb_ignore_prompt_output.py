#!/usr/bin/env python

import sys
import json

nb = sys.stdin.read() # Read the notebook from stdin.

# First, check the metadata for the following JSON block:
# "git" : {
#     "suppress_outputs" : true
# }
json_in = json.loads(nb)
nb_metadata = json_in["metadata"]
suppress_output = False
if "git" in nb_metadata:
    if "suppress_outputs" in nb_metadata["git"] and nb_metadata["git"]["suppress_outputs"]:
        suppress_output = True

if not suppress_output:
    # Metadata tells us not to suppress output:
    # simply send notebook, as is, to stdout.
    sys.stdout.write(nb)
    exit() 
 
# Get the IPython version used to write the notebook.
ipy_version = int(json_in["nbformat"])-1 # nbformat is 1 more than actual version.
 
def strip_output_from_cell(cell):
    """
    Takes a notebook cell and removes the "prompt_number" field 
    and the "outputs" field.
    """
    if "outputs" in cell:
        cell["outputs"] = []
    if "prompt_number" in cell:
        del cell["prompt_number"]
 
# Process the notebook
if ipy_version == 2:
    for sheet in json_in["worksheets"]:
        for cell in sheet["cells"]:
            strip_output_from_cell(cell)
else:
    for cell in json_in["cells"]:
        strip_output_from_cell(cell)

# Dump the processed notebook to stdout.
json.dump(json_in, sys.stdout, sort_keys=True, indent=1, separators=(",",": "))