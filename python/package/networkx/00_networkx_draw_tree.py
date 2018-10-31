import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib
matplotlib.use('Agg')

# https://stackoverflow.com/questions/11479624/is-there-a-way-to-guarantee-hierarchical-output-from-networkx/11484144#11484144
# https://stackoverflow.com/questions/15661384/python-does-not-see-pygraphviz
# sudo apt-get install graphviz libgraphviz-dev pkg-config
# pip install pygraphviz
# https://stackoverflow.com/questions/4596962/display-graph-without-saving-using-pydot
# https://stackoverflow.com/questions/37604289/tkinter-tclerror-no-display-name-and-no-display-environment-variable
# import matplotlib; matplotlib.use('Agg')
# https://stackoverflow.com/questions/39411102/attributeerror-module-object-has-no-attribute-graphviz-layout-with-networkx/39603436

G = nx.DiGraph()
G.add_node("ROOT")

for i in range(5):
    G.add_node("Child_%i" % i)
    G.add_node("Grandchild_%i" % i)
    G.add_node("Greatgrandchild_%i" % i)

    G.add_edge("ROOT", "Child_%i" % i)
    G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
    G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
write_dot(G,'test.dot')

# same layout using matplotlib with no labels
plt.title('draw_networkx')
pos=graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=False, arrows=False)
plt.savefig('nx_test.png')



