#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import networkx as nx
import json
from helpers import reformat, printGraph
import heapq
import pandas as pd
import ast
import matplotlib.pyplot as plt


# %%
patient_id_trajectory = {}
def get_trajectory():
    """
    Simple getter for the 'globally' stored trajectory.
    """
    return patient_id_trajectory


# %%
def query_kg(kg, patient_id, symptomsList, drugsList, numSlots):
    """
    Query the knowledge graph using the potential entities from the symptoms and drugs list of the patient database.
    Updates patient trajectory with the given patient ID.
    inputs:
        patient_id: ID of the current database patient
        symptomsList: list of symptoms from the patient over time
        drugsList: list of drug names from the patient over time
        numSlots: number of heavily weighted neighbor nodes to query from the knowledge graph
    returns:
        'numSlots': number of neighbor nodes in the knowledge graph to use for chatbot response        
    """
    weighted_nodes = []
    combined = []
    # Combine symptoms and drugs list
    if symptomsList:
        symptomsList = ast.literal_eval(symptomsList)
        combined.extend(symptomsList)
    if drugsList:
        drugsList = ast.literal_eval(drugsList)
        combined.extend(drugsList)
        
    combined = [reformat(node) for node in combined]
    for node in combined:
        if kg.has_node(node):
            edges = kg.edges(node)
            # Find neighbor nodes with highest weight (maintain in min heap)
            for node1, node2 in edges:
                heapq.heappush(weighted_nodes, (kg[node1][node2]['weight'], node1, node2))
                if len(weighted_nodes) > numSlots:
                    heapq.heappop(weighted_nodes)
                    
    # Update patient trajectory mapping
    if patient_id in patient_id_trajectory:
        patient_id_trajectory[patient_id].append(weighted_nodes)
    else:
        patient_id_trajectory[patient_id] = [weighted_nodes]
        
    # Find some way to figure uot similar patients (the embeddings go)
    # helper method ()
    nbrs = [val[2] for val in weighted_nodes]
    return nbrs

    

