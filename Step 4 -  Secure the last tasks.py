# -*- coding: utf-8 -*-



def create_graph(f):
    
    g = {}
    file = open(f,"r")
    if not file:
        print("ERROR : File {} not found.".format(f))
        return
    
    for line in file:
        t=line.split()
        edge0 = {}
        edge1 = {}        
        
        if t[0] not in g:
            g[t[0]]={}
        else:
            edge0=g[t[0]]
        if t[1] not in g:
            g[t[1]]={}
        else:
            edge1=g[t[1]]
        edge0[t[1]]=float(t[2])
        edge1[t[0]]=float(t[2])
        g[t[0]]=edge0
        g[t[1]]=edge1
        
    file.close()
    return g

        
def hamilton_path(graph, first):
  size = len(graph)
  nxt = [None, first]
  path = []
  while(nxt):
    v = nxt.pop()
    if v :
      path.append(v)
      if len(path) == size:
        break
      for el in set(graph[v])-set(path):
        nxt.append(None)
        nxt.append(el)
    else: 
      path.pop()
  return path


def step4(graph):
    vertex = [key for key in g.keys()]
    for el in vertex:
        path = hamilton_path(g,el)
        if len(path) > 0:
            print("Start : {} ",el)
            print(path)
        else:
            print("No unique path exist from the room : {}",el)
        print()
        
if __name__ == "__main__":
     g = create_graph("graph_step4.txt")
     step4(g)



