<!-- #region -->
The contents of this folder primarily handle the knowledge graph end, which includes-

- entityMapping.py:
    - saveEntityPaperMapping(filename, outfile): Method to save mapping of node entities to paper abstract IDs, to use as reference

- helpers.py: Contains helper methods to use for NER and Knowledge Graph construction
    - reformat(text): Performs and returns lemmatization on the input text
    - printGraph(graph): Displays knowledge graph with node texts
    - json_to_kg(filename): Load a knowledge graph from a JSON file in the node-link format.
    - kg_to_json(kg, filename): Save a given knowledge graph to a JSON file
    
- KGConstruction.py: Contains methods that constructs the knowledge graph from the combined NER results of sciSpacy and med7.

- PatientGraph.py: Contains methods that queries the existing pruned knowledge graph for surrounding nodes to create a chatbot response. Also creates and updates a patient trajectory mapping of their root symptom/drug nodes and predicted knowledege graph nodes, for each patient in the conversation database. Lastly, displays the color-coded trajectory for each patient.


Additionally, there are Python notebooks that utilize and experiment on these API methods in the `experiments` folder.

One notebook includes-
- trajectories workbook.ipynb: Contains code that attempts to compare the embeddings of two patient trajectories with their symptom/drug and predicted nodes over time, using pre-trained word embeddings from fastText.
<!-- #endregion -->
