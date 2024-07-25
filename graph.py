class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj.keys():
            self.adj[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj.keys() and v2 in self.adj.keys():
            self.adj[v1].append(v2)
            self.adj[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj.keys() and v2 in self.adj.keys():
            try:
                self.adj[v1].remove(v2)
                self.adj[v2].remove(v1)
                return True
            except ValueError:
                pass
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            try:
                for el in self.adj_list[vertex]:
                    self.adj_list[el].remove(vertex)
                del self.adj_list[vertex]
                return True
            except ValueError:
                pass
        return False
            
    
    def print_graph(self):
        for vertex in self.adj:
            print(vertex, ':', self.adj[vertex])


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.print_graph()

# print(graph.remove_edge('A', 'D'))
# graph.print_graph()

print(graph.remove_vertex('D'))
graph.print_graph()