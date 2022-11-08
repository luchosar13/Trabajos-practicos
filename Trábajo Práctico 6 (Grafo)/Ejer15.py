from grafo import Arista , Grafo
from cola import Cola

g = Grafo(dirigido=False)

# ! maravillas arquitectonicas
g.insertar_vertice('Palacio Legislativo', datos={'tipo': 'a', 'pais': 'Rumania'})
g.insertar_vertice('Gran Mezquita de Djenne', datos={'tipo': 'a', 'pais': 'Mali'})
g.insertar_vertice('Fuerte Derawar', datos={'tipo': 'a', 'pais': 'Pakistan'})
g.insertar_vertice('Chand Baori', datos={'tipo': 'a', 'pais': 'India'})
g.insertar_vertice('Puente de Mostar', datos={'tipo': 'a', 'pais': 'Bosnia Herzegovina'})
g.insertar_vertice('Gran Muralla', datos={'tipo': 'a', 'pais': 'India'})
g.insertar_vertice('Mezquita de Sheikh Lotfollauiteh', datos={'tipo': 'a', 'pais': 'Irán'})

#! maravillas naturales
g.insertar_vertice('Puerto Princesa', datos={'tipo': 'n', 'pais': 'Filipinas'})
g.insertar_vertice('Montaña de la Mesa', datos={'tipo': 'n', 'pais': 'Sudafrica'})
g.insertar_vertice('Cataratas del Iguazu', datos={'tipo': 'n', 'pais': 'Argentina'})
g.insertar_vertice('Amazonia', datos={'tipo': 'n', 'pais': ['Brasil','Bolivia','Colombia','Ecuador','Guayana Francesa','Guyana','Peru','Surinam','Venezuela']})
g.insertar_vertice('Bahia de Ha Long', datos={'tipo': 'n', 'pais': 'Vietnam'})
g.insertar_vertice('Isla Jeju', datos={'tipo': 'n', 'pais': 'Corea del Sur'})
g.insertar_vertice('Parque Nacional de Komodo', datos={'tipo': 'n', 'pais': 'Indonesia'})

#! maravillas arquitectonicas

g.insertar_arista('Palacio Legislativo', 'Gran Mezquita de Djenne', 6)
g.insertar_arista('Palacio Legislativo', 'Fuerte Derawar', 3)
g.insertar_arista('Palacio Legislativo', 'Chand Baori', 8)
g.insertar_arista('Palacio Legislativo', 'Puente de Mostar', 2)
g.insertar_arista('Palacio Legislativo', 'Gran Muralla', 2)
g.insertar_arista('Palacio Legislativo', 'Mezquita de Sheikh Lotfollauiteh', 9)
g.insertar_arista('Gran Mezquita de Djenne', 'Fuerte Derawar', 3)
g.insertar_arista('Gran Mezquita de Djenne', 'Chand Baori', 8)
g.insertar_arista('Gran Mezquita de Djenne', 'Puente de Mostar', 2)
g.insertar_arista('Gran Mezquita de Djenne', 'Gran Muralla', 2)
g.insertar_arista('Gran Mezquita de Djenne', 'Mezquita de Sheikh Lotfollauiteh', 9)
g.insertar_arista('Fuerte Derawar', 'Chand Baori', 8)
g.insertar_arista('Fuerte Derawar', 'Puente de Mostar', 2)
g.insertar_arista('Fuerte Derawar', 'Gran Muralla', 2)
g.insertar_arista('Fuerte Derawar', 'Mezquita de Sheikh Lotfollauiteh', 9)
g.insertar_arista('Chand Baori', 'Puente de Mostar', 2)
g.insertar_arista('Chand Baori', 'Gran Muralla', 2)
g.insertar_arista('Chand Baori', 'Mezquita de Sheikh Lotfollauiteh', 9)
g.insertar_arista('Puente de Mostar', 'Gran Muralla', 2)
g.insertar_arista('Puente de Mostar', 'Mezquita de Sheikh Lotfollauiteh', 9)
g.insertar_arista('Gran Muralla', 'Mezquita de Sheikh Lotfollauiteh', 2)

#! maravillas naturales

g.insertar_arista('Puerto Princesa', 'Montaña de la Mesa', 6)
g.insertar_arista('Puerto Princesa', 'Cataratas del Iguazu', 3)
g.insertar_arista('Puerto Princesa', 'Amazonia', 8)
g.insertar_arista('Puerto Princesa', 'Bahia Ha Long', 2)
g.insertar_arista('Puerto Princesa', 'Isla Jeju', 2)
g.insertar_arista('Puerto Princesa', 'Parque Nacional de Komodo', 9)
g.insertar_arista('Montaña de la Mesa', 'Cataratas del Iguazu', 3)
g.insertar_arista('Montaña de la Mesa', 'Amazonia', 8)
g.insertar_arista('Montaña de la Mesa', 'Bahia Ha Long', 2)
g.insertar_arista('Montaña de la Mesa', 'Isla Jeju', 2)
g.insertar_arista('Montaña de la Mesa', 'Parque Nacional de Komodo', 9)
g.insertar_arista('Cataratas del Iguazu', 'Parque Nacional de Komodo', 3)
g.insertar_arista('Cataratas del Iguazu', 'Amazonia', 8)
g.insertar_arista('Cataratas del Iguazu', 'Bahia Ha Long', 2)
g.insertar_arista('Cataratas del Iguazu', 'Isla Jeju', 2)
g.insertar_arista('Amazonia', 'Parque Nacional de Komodo', 9)
g.insertar_arista('Amazonia', 'Isla Jeju', 8)
g.insertar_arista('Amazonia', 'Bahia Ha Long', 2)
g.insertar_arista('Bahia Ha Long', 'Isla Jeju', 2)
g.insertar_arista('Bahia Ha Long', 'Parque Nacional de Komodo', 9)
g.insertar_arista('Isla Jeju', 'Parque Nacional de Komodo', 9)

arbol_min = g.kruskal()

arbol_min_a = arbol_min[1].split('-')
peso_total = 0
for nodo in arbol_min_a:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el arbol de expansión minimo de las maravillas arquitectonicas es de: {peso_total}")

print('')

arbol_min_n = arbol_min[2].split('-')
peso_total = 0
for nodo in arbol_min_n:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el arbol de expansión minimo de las maravillas naturales es de: {peso_total}")

g.contar_maravillas()




