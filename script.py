import heapq
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_node, to_node, weight):
        self.graph[from_node].append((to_node, weight))

    def load_graph(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                node, edges = line.strip().split(':', 1)
                for edge in edges.split(','):
                    to_node, weight = edge.split(':')
                    self.add_edge(node, to_node, int(weight))

def dfs(graph, start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    order_of_exploration = []

    while stack:
        node, path, cost = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order_of_exploration.append(node)
        if node == goal:
            return {
                'path': ''.join(path),
                'order_of_exploration': ''.join(order_of_exploration),
                'depth': len(path) - 1,
                'cost': cost
            }
        for neighbor, weight in sorted(graph[node], reverse=True):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor], cost + weight))
    return None

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = set([start])
    order_of_exploration = [start]

    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            return {
                'path': ''.join(path),
                'order_of_exploration': ''.join(order_of_exploration),
                'depth': len(path) - 1,
                'cost': cost
            }
        for neighbor, weight in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                order_of_exploration.append(neighbor)
                queue.append((neighbor, path + [neighbor], cost + weight))
    return None

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()
    order_of_exploration = []

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        order_of_exploration.append(node)
        if node == goal:
            return {
                'path': ''.join(path),
                'order_of_exploration': ''.join(order_of_exploration),
                'depth': len(path) - 1,
                'cost': cost
            }
        for neighbor, weight in sorted(graph[node]):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python search_algorithms.py <graph_file> <start_node> <goal_node>")
        sys.exit(1)

    graph_file = sys.argv[1]
    start_node = sys.argv[2]
    goal_node = sys.argv[3]

    graph = Graph()
    graph.load_graph(graph_file)

    bfs_result = bfs(graph.graph, start_node, goal_node)


    if bfs_result:
        print("BFS Path:", bfs_result['path'])
        print("BFS Order of Exploration:", bfs_result['order_of_exploration'])
        print("BFS Depth:", bfs_result['depth'])
        print("BFS Cost:", bfs_result['cost'])

