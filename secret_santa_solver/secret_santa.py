import networkx as nx
import numpy as np
import random

MAX_RETRY = 10

def _edges_from_participants(participants):
    len_participants = len(participants)
    edges = []
    for i, participant in enumerate(participants):
        if participant['links'] is None:
            for j in range(len_participants):
                if i != j:
                    edges.append((i, j))
        else:
            links = []
            for j, potential_link in enumerate(participants):
                if potential_link['name'] in participant['links']:
                    edges.append((i, j))

    return edges


def _randomized_dfs_tour(graph, start):
    visited = set()
    path = []
    
    def _dfs(node):
        visited.add(node)
        path.append(node)
        
        # Get the directed neighbors (outgoing edges only) and shuffle them
        neighbors = list(graph.successors(node))
        random.shuffle(neighbors)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                _dfs(neighbor)
    
    _dfs(start)
    # Only return to start if a directed edge exists from the last node to the start
    if path and graph.has_edge(path[-1], start):
        path.append(start)  # Close the cycle if possible

    return path


def _path_to_solution(path, participants):
    assignments = {}
    for idx in range(len(path) - 1):
        assignments[participants[path[idx]]['name']] = participants[path[idx + 1]]['name']
    return assignments



def secret_santa(participants, retry=0):
    """
    This function takes a list of participants and assigns each participant a recipient they feel comfortable gifting to, if possible.    
    
    Parameters:
        participants (list): A list of dictionaries, each containing name, email, and links.
    Returns:
        dict: A dictionary with each participant's name as the key and their assigned recipient's name as the value. If None, that mean the solver haven't found a solution after trying MAX_RETRY times.
    """

    if retry == MAX_RETRY:
        return None
    G = nx.DiGraph()
    edges = _edges_from_participants(participants)
    G.add_edges_from(edges)

    path = _randomized_dfs_tour(G, start=0)

    if len(path) - 1 == len(participants):
        assignments = _path_to_solution(path, participants)
        return assignments
    else:
        return secret_santa(participants, retry + 1)

