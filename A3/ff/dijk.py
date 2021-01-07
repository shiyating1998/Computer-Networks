import sys
import threading
from socket import *

import struct

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = float("inf")
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_unvisited(self):
        self.visited = False

    def __str__(self):
        return str(self.id)
        #return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __lt__(self, other): 
        if(self.get_distance()<other.get_distance()):
            return True
            #return "ob1 is lessthan ob2"
        else:
            return False
            #return "ob2 is less than ob1"

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start):
    for i in aGraph:
        i.set_unvisited()
        i.set_distance(float("inf"))
        i.set_previous(None)
    #print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for n in current.adjacent:
            # if visited, skip
            if n.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(n)
            
            if new_dist < n.get_distance():
                n.set_distance(new_dist)
                n.set_previous(current)
                print("updated: current = {} next = {} new_dist = {}".format(current.get_id(),n.get_id(),n.get_distance()))
            else:
                print ("not updated : current = {} next = {} new_dist = {}".format(current.get_id(), n.get_id(), n.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex(1)
 
   

    g.add_edge(1, 2, 5)            
    dijkstra(g, g.get_vertex(1))

    
    g.add_edge(2, 3, 6)
    dijkstra(g, g.get_vertex(1))
   
            
    g.add_edge(3, 1, 7)
    print ("Graph data:")
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ("( {} , {}, {})".format(vid, wid, v.get_weight(w)))
    dijkstra(g, g.get_vertex(1)) 
    for n in g:
        if (n.id!=g.get_vertex(1).id):
            target = g.get_vertex(n.id)
            path = [target.get_id()]
            shortest(target, path)
            print ("The shortest path : {}".format(path[::-1]))
            print ("Vertex: {}, distance: {}".format(n.id,g.get_vertex(n.id).get_distance()))

