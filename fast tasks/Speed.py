import networkx as nx

minForAnswer = 10000000
maxForAnswer = -10000000

weights = [1, 7, 6, 12, 3, 9]

G = nx.Graph()
G.add_edge(1,3,weight=2)
G.add_edge(4,2,weight=8)
G.add_edge(1,2,weight=11)
G.add_edge(1,4,weight=3)
G.add_edge(1,3,weight=6)
G.add_edge(5,3,weight=5)
G.add_edge(3,6,weight=9)
G.add_edge(7,6,weight=6)
G.add_edge(5,6,weight=3)
G.add_edge(2,5,weight=7)

maxweight = -1000000
minweight = 1000000
difference = 1000000
currentMax = -100000000
currentMin = 100000000

nodes = [1,2,3,4,5,6,7]
nodeshelper = nodes[:]
iteration = 0

for x in weights:
    for y in weights:
        print "iteration: {}".format(iteration)
        print "({} {})".format(x,y)
        if x<y:
            minweight = x
            maxweight = y
        else:
            minweight = y
            maxweight = x
        H = nx.Graph([(u,v,d) for (u,v,d) in  G.edges(data=True) if d['weight']>=minweight and d['weight']<=maxweight])

        print "edges in H: {}".format(H.edges())
        for h in H.edges():
            try:
                nodeshelper.remove(h[0]) 
            except:
                pass
            try:
                nodeshelper.remove(h[1])
            except:
                pass
        print "nodeshelper: {}".format(nodeshelper)

        try:
            if nx.edge_connectivity(H) and len(nodeshelper) == 0:
                print "CONNECTED WITH ALL NODES!!!"
                print len(H.edges())
                for slavi in H.edges():
                    
                    weight = G[slavi[0]][slavi[1]]['weight']
                    print "weight: {}".format(weight)
                    if weight > currentMax:
                        currentMax = weight
                    if weight < currentMin:
                        currentMin = weight
                if difference > currentMax - currentMin:
                    difference = currentMax - currentMin
                    print "NEW DIFFERENCE: {} ; currentMax: {} ; currentMin: {}".format(difference, currentMax, currentMin)
                    maxForAnswer = currentMax
                    minForAnswer = currentMin      
        except:
            print "in except!"
            pass
        currentMin = 1000000
        currentMax = -1000000
        nodeshelper = nodes[:]
        iteration += 1
        print "\n"


print "Minspeed: {} ; Maxspeed: {} ;".format(minForAnswer, maxForAnswer)


