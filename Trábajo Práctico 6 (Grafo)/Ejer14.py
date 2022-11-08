from grafo import Arista , Grafo
from cola import Cola

g = Grafo(dirigido=False)

#cocina, comedor, cochera, quincho,
#baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

g.insertar_vertice('cocina')
g.insertar_vertice('comedor')
g.insertar_vertice('cochera')
g.insertar_vertice('quincho')
g.insertar_vertice('baño 1')
g.insertar_vertice('baño 2')
g.insertar_vertice('habitacion 1')
g.insertar_vertice('habitacion 2')
g.insertar_vertice('sala de estar')
g.insertar_vertice('terraza')
g.insertar_vertice('patio')

g.insertar_arista('cocina','cochera',10)
g.insertar_arista('cocina','terraza',5)
g.insertar_arista('cocina','baño 1',4)
g.insertar_arista('comedor','quincho',5)
g.insertar_arista('comedor','baño',7)
g.insertar_arista('comedor','habitacion 2',1)
g.insertar_arista('cochera','terraza',4)
g.insertar_arista('chochera','habitacion 1',14)
g.insertar_arista('cochera','patio',13)
g.insertar_arista('quincho','sala de estar',9)
g.insertar_arista('quincho','cochera',17)
g.insertar_arista('quincho','baño 2',5)
g.insertar_arista('baño 1','cocina',8)
g.insertar_arista('baño 1','comedor',3)
g.insertar_arista('baño 1','cochera',5)
g.insertar_arista('baño 2','patio',13)
g.insertar_arista('baño 2','terraza',4)
g.insertar_arista('baño 2','sala de estar',3)
g.insertar_arista('habitacion 1','baño 1',9)
g.insertar_arista('habitacion 1','comedor',2)
g.insertar_arista('habitacion 1','cocina',14)
g.insertar_arista('habitacion 2','patio',1)
g.insertar_arista('habitacion 2','cocina',2)
g.insertar_arista('habitacion 2','comedor',5)
g.insertar_arista('sala de estar','patio',9)
g.insertar_arista('sala de estar','baño 1',3)
g.insertar_arista('sala de estar','baño 2',13)
g.insertar_arista('terraza','patio',11)
g.insertar_arista('terraza','baño 2',2)
g.insertar_arista('terraza','cocina',7)
g.insertar_arista('terraza','comedor',2)
g.insertar_arista('terraza','sala de estar',7)
g.insertar_arista('patio','cocina',1)
g.insertar_arista('patio','baño 1',6)
g.insertar_arista('patio','terraza',12)
g.insertar_arista('patio','baño 2',6)
g.insertar_arista('patio','comedor',12)

#g.barrido_amplitud('patio')

arbol_min = g.kruskal()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
    
print(f"Se necesitan {peso_total} metros de cable para conectar todos los ambientes")

print()

if g.existe_paso('habitacion 1', 'sala de estar'):
    resultados1 = g.dijkstra('habitacion 1')
    camino = g.camino(resultados1, 'habitacion 1', 'sala de estar')
    print('El camino de la habitacion 1 a la sala de estar es: ', camino['camino'])
    print('Y el costo en metros de cableado para conectar los dos ambientes es de: ', camino['costo'])
else:
    print('no se puede llega de habitacion 1 a sala de estar')


