import graph import Node


def dfs(node):
    # First create new node.
    temp_node = Node()
    temp_node.val = node.val
    reversed_graph[node.val] = temp_node
    n = len(node.neighbours)
    # Visit all the neighbours.
    for i in range(0, n):
        # If node is not visited then first visit it.
        if not node.neighbours[i].val in reversed_graph:
            dfs(node.neighbours[i])
        # Add the reverse edge.
        reversed_graph[node.neighbours[i].val].neighbours.append(reversed_graph[node.val])

def build_other_graph(node):
    # Build the graph.
    dfs(node)
    # Return any node of the new graph.
    return reversed_graph[1]
