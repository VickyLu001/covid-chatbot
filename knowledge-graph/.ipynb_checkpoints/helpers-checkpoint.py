# +
# %matplotlib inline
from nltk.stem import WordNetLemmatizer 
import matplotlib.pyplot as plt
import networkx as nx
import json


lemmatizer = WordNetLemmatizer() 
def reformat(text):
    """
    Performs and returns lemmatization on the input text (str).
    returns: lemmatized form of the input text
    """
    text = lemmatizer.lemmatize(text.lower())
    return text

def printGraph(graph):
    """
    Displays knowledge graph with node texts
    inputs:
        graph: networkX graph
    """
    pos = nx.spring_layout(graph)
    plt.figure()
    nx.draw(graph, pos, edge_color='black', width=1, linewidths=1,
            node_size=200, node_color='seagreen', alpha=0.9,
            labels={node: node for node in graph.nodes()})
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.axis('off')
    plt.savefig('kg_results/kg.png', dpi=500)
    plt.show()
    
def json_to_kg(filename):
    """
    Load a knowledge graph from a JSON file in the node-link format.
    inputs:
        filename: Name of saved JSON version of the graph
    returns: networkX form of the knowledge graph
    """
    with open(filename, 'r') as infile:
        data = json.load(infile)
        kg_json = nx.readwrite.json_graph.node_link_graph(data)
        return kg_json
    
def kg_to_json(kg, filename):
    """
    Save a given knowledge graph to a JSON file in the node-link format found here: 
    https://networkx.org/documentation/latest/reference/readwrite/json_graph.html
    inputs:
        kg: networkX graph
        filename: filename of JSON file to save the graph as
    """
    kg_json = nx.readwrite.json_graph.node_link_data(kg)
    with open(filename, 'w') as outfile:
        json.dump(kg_json, outfile)
