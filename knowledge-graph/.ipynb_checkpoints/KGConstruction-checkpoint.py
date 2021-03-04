#!/usr/bin/env python
# coding: utf-8
# %%

# %%


get_ipython().run_line_magic('matplotlib', 'inline')

import scispacy
import spacy
from spacy.lang.en import English
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from spacy import displacy
from pprint import pprint
from nltk.stem import WordNetLemmatizer 
from pathlib import Path
import json
from helpers import printGraph, reformat, json_to_kg, kg_to_json


# %%


# %%


# %%


def getSentences(text):
    """
    Splits full text into individual sentences using spacy's sentencizer.
    inputs:
        text: document full text (str)
    return: list of sentences as strings
    """
    eng_model = English()
    eng_model.add_pipe(eng_model.create_pipe('sentencizer'))
    document = eng_model(text)
    return [sent.string.strip() for sent in document.sents]


# %%


def appendChunk(original, chunk):
    """
    Combine original and chunk strings to form chunks for subject/relation/object
    return: concatenation of both words into chunks
    """
    return original + ' ' + chunk


# %%


def process(abstract):
    """
    Updates knowledge graph given abstract input.
    inputs:
        abstract: document abstract (str)
    return: None
    """
    tokens = model(abstract)
    # visualizeTokens(tokens)
    
    # Create entities list from NER model
    entities_lst = [[entity.text, entity.label_] for entity in tokens.ents]
    i = 0
    # Create entities for negations as well
    for token in tokens:
        if token.dep_ == 'neg':
            if i + 1 < len(entities_lst):
                entities_lst[i+1][0] = appendChunk(token.lemma_ , entities_lst[i+1][0])    
                print (entities_lst[i+1][0])
        if entities_lst and i < len(entities_lst) and entities_lst[i][0] == token.lemma_:
            i += 1
    
    # Create nodes for the knowledge graph using entities.
    nodes_lst = []
    for text, label in entities_lst:
        text = reformat(text)
        knowledgeGraph.add_node(text)
        nodes_lst.append(text)
    
    # Create edges for the knowledge graph and update edge weights depending on number of cooccurences.
    for i in range(len(nodes_lst) - 1):
        for j in range(i + 1, len(nodes_lst)):
            node1 = nodes_lst[i]
            node2 = nodes_lst[j]
            if knowledgeGraph.has_edge(node1, node2):
                # print ("Refining edge " + str(node1) + ", " + str(node2))
                knowledgeGraph[node1][node2]['weight'] += 1
            else:
                # print ("Adding edge " + str(node1) + ", " + str(node2))
                knowledgeGraph.add_edge(node1, node2, weight = 1)

    


# %%


def kg_from_ner(filename):
    """
    Produce a knowledge graph from a completed NER text file. Format for these NER files is defined in the README.
    inputs:
        filename: name of saved NER file
    """
    kg = nx.Graph()
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.split("#")
            abstract_id = line[0]
            
            # Get all of the entities in this abstract
            entities = set()
            for i in range(1, len(line), 3):
                entities.add(line[i])
            entities = list(entities)
            # print ("Entities in " + str(abstract_id) + ": " + str(entities))
            
            # Add all of the entities as nodes in the knowledge graph
            nodes = []
            for entity in entities:
                text = reformat(entity)
                kg.add_node(text)
#                 if kg.has_node(text):
#                     kg.node[text]['ids'].add(abstract_id)
#                 else:
#                     kg.add_node(text, ids = set([abstract_id]))
                nodes.append(text)
            # print ("Nodes in " + str(abstract_id) + ": " + str(nodes))
            # Add all the co-occurrrences as edges 
            for i in range(len(nodes) - 1):
                for j in range(i + 1, len(nodes)):
                    node1 = nodes[i]
                    node2 = nodes[j]
                    if kg.has_edge(node1, node2):
                        # print ("Refining edge " + str(node1) + ", " + str(node2))
                        kg[node1][node2]['weight'] += 1
                    else:
                        # print ("Adding edge " + str(node1) + ", " + str(node2))
                        kg.add_edge(node1, node2, weight = 1)
    return kg


# %%


# %%


# %%


def combine_2_ner_files(file1, file2, combined_file):
    """
    This function will combine two completed NER files. The idea is to conduct NER 
    in two separate ways (such as med7 and scispacy) which produces two separate files.
    These files are in the same format (described in the README).
    
    inputs:
        file1, file2, combined_file: filenames of the NER files (str)
    """
    # map paper ID to its NER output
    pid_to_ner = {}
    
    # For each file, look through the NER for each abstract on each line
    for file in [file1, file2]:
        with open(file, 'r') as f:
            for line in f.read().splitlines():
                line = line.split("#")
                paper_id = line[0]
                
                # Use a set for entities (so that entities picked up by both file1 and file2 are not repeated)
                if paper_id not in pid_to_ner:
                    pid_to_ner[paper_id] = set()
                for i in range(1, len(line), 3):
                    pid_to_ner[paper_id].add((line[i], line[i+1], line[i+2]))
    
    # Deconstruct the mapping back to a single file
    with open(combined_file, 'w') as outfile:
        for pid, entities in pid_to_ner.items():
#             print("PID: " + pid)
#             print("RESULTS: " + str(entities))
#             print()
            # Construct a line for each abstract to put in the file
            string = ""
            
            # Start with the paper ID then add the entries for each entity
            string += pid
            for entity in entities:
                string += "#" + entity[0] + "#" + entity[1] + "#" + entity[2]
            
            outfile.write(string + "\n")
    
            
            


# %%

