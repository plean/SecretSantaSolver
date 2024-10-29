import networkx as nx
import numpy as np
import random


def edges_from_participants(particpants):
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


def randomized_dfs_tour(graph, start):
    visited = set()
    path = []
    
    def dfs(node):
        visited.add(node)
        path.append(node)
        
        # Get the directed neighbors (outgoing edges only) and shuffle them
        neighbors = list(graph.successors(node))
        random.shuffle(neighbors)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start)
    # Only return to start if a directed edge exists from the last node to the start
    if path and graph.has_edge(path[-1], start):
        path.append(start)  # Close the cycle if possible

    return path


def path_to_solution(path):
    solution = {}
    for idx in range(len(path) - 1):
        solution[participants[path[idx]]['name']] = participants[path[idx + 1]]['name']
    return solution



def secret_santa(participants, retry=0):
    if retry == MAX_RETRY:
        return None
    G = nx.DiGraph()
    edges = edges_from_participants(participants)
    G.add_edges_from(edges)

    path = randomized_dfs_tour(G, start=0)

    if len(path) - 1 == len(participants):
        assignments = path_to_solution(path)
        return assignments
    else:
        return secret_santa(participants, retry + 1)


def main():
    from participants import participants
    assignments = secret_santa(participants)
    for giver, recipient in assignments.items():
        print(f"{giver} will gift to {recipient}")
    pass


if __name__ == '__main__':
    main()
    pass
