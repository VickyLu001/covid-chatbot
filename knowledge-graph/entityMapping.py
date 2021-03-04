#!/usr/bin/env python
# coding: utf-8
# %%

# %%


from helpers import reformat
import json

def saveEntityPaperIDMapping(filename, outfile):
    """
    Saves a mapping, to the outfile, of each entity in the NER file to its paper abstract ID.
    inputs:
        filename: name of NER file
        outfile: name of file to save entity mapping
    """
    mapping = {}
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.split("#")
            abstract_id = line[0]

            # Get all of the entities in this abstract
            entities = set()
            for i in range(1, len(line), 3):
                entities.add(line[i])
            entities = list(entities)
            # update mapping with entities to paper ID
            for entity in entities:
                if entity in mapping:
                    mapping[entity].add(abstract_id)
                else:
                    mapping[entity] = set([abstract_id])

    # Convert values to list
    for entity in mapping.keys():
        mapping[entity] = list(mapping[entity])
        
    # Save mapping to outfile
    with open(outfile, 'w') as f:
        json.dump(mapping, f)
    return mapping


# %%

