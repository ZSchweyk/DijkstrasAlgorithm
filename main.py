from NodeClass import Node
from GraphClass import Graph

harvard = Node("Harvard")
princeton = Node("Princeton")
yale = Node("Yale")
johns_hopkins = Node("Johns Hopkins")
cornell = Node("Cornell")
u_penn = Node("UPenn")
brown = Node("Brown")
university_of_rochester = Node("University of Rochester")

Node.bi_directional = True

harvard.cost_to(princeton, 4.567)
harvard.cost_to(yale, 2.233)
harvard.cost_to(johns_hopkins, 6.67)
harvard.cost_to(cornell, 5.67)
harvard.cost_to(u_penn, 5.383)
harvard.cost_to(brown, .9167)
harvard.cost_to(university_of_rochester, 6.2)

princeton.cost_to(yale, 2.4)
princeton.cost_to(johns_hopkins, 2.45)
princeton.cost_to(cornell, 4.15)
princeton.cost_to(u_penn, .783)
princeton.cost_to(brown, 4.05)
princeton.cost_to(university_of_rochester, 5.7667)

yale.cost_to(johns_hopkins, 4.45)
yale.cost_to(cornell, 4.85)
yale.cost_to(u_penn, 2.8833)
yale.cost_to(brown, 1.6833)

johns_hopkins.cost_to(cornell, 5.15)
johns_hopkins.cost_to(u_penn, 1.7)
johns_hopkins.cost_to(brown, 6.1)
johns_hopkins.cost_to(university_of_rochester, 5.71667)

cornell.cost_to(u_penn, 3.91667)
cornell.cost_to(brown, 5.5667)
cornell.cost_to(university_of_rochester, 1.8)

u_penn.cost_to(brown, 4.65)
u_penn.cost_to(university_of_rochester, 5.5667)
brown.cost_to(university_of_rochester, 6.2667)

graph = Graph([harvard, princeton, yale, johns_hopkins, cornell, u_penn, brown])
print(graph.shortest_path("University of Rochester", "University of Rochester"))

