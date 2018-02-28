# Visualizes with the dot language 
# a file of the format
# a     b
# a     c    etc...

import os, sys
from graphviz import Digraph

NodeDict={}
dot = Digraph(comment=sys.argv[2])

with open(sys.argv[1],'r') as infile:
    for line in infile:
        nodes =  line.split()
        try:
            NodeDict[nodes[0]].add(nodes[1]);
        except KeyError:
            NodeDict[nodes[0]]=set()
            NodeDict[nodes[0]].add(nodes[1])    

for key in NodeDict.keys():
#       print NodeDict[key]
        for target in NodeDict[key]:
                dot.edge(key, target )

dot.render(sys.argv[2]+'.gv', view=True)




