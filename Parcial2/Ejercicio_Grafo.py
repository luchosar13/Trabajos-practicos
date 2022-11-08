from grafo import Arista , Grafo
from cola import Cola

g = Grafo(dirigido=False)

# Luke Skywalker, Darth Vader, Yoda, Boba Fett, C_3PO, Leia
g.insertar_vertice('Luke Skywalker')
g.insertar_vertice('Darth Vader')
g.insertar_vertice('Yoda')
g.insertar_vertice('Boba Fett')
g.insertar_vertice('C_3PO')
g.insertar_vertice('Leia')

g.insertar_arista('Luke Skywalker','Boba Fett',1)
g.insertar_arista('Luke Skywalker','Darth Vader',1)
g.insertar_arista('Luke Skywalker','Yoda',1)
g.insertar_arista('Luke Skywalker','Leia',1)
g.insertar_arista('Darth Vader','C_3PO',5)
g.insertar_arista('Leia','C_3PO',2)
g.insertar_arista('Leia','Luke Skywalker',2)
g.insertar_arista('Yoda','Boba Fett',4)
g.insertar_arista('Boba Fett','C_3PO',4)

arbol_min = g.kruskal()

arbol_min_jedis = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min_jedis:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
    
print('El arbol de expasion minimo tiene un costo de: ', peso_total)

print('')

print('Los Jedis que tienen mas de dos episodios compartidos son: ')

print(g.episodios_comp())