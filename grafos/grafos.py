from graphviz import Digraph

dot = Digraph(comment='Ejemplo de grafo')

dot.node('A', 'Nodo A')
dot.node('B', 'Nodo B')
dot.node('C', 'Nodo C')

dot.edges(['AB', 'AC', 'BC'])
dot.edge('C', 'A', constrint='false')

dot.save('ejemplo_grafo.dot')
dot.render('ejemplo_grafo', format='png', view=True)
