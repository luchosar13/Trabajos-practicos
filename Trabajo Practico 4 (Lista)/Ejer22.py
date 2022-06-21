from listaParcial import Lista

class Jedi:
    nombre, maestro, colorS, especie = None, None, None, None

file = open('jedis.txt')
lineas = file.readlines()

lista1 = Lista()
lista2 = Lista()
vec1 = []
vec2 = []
vec3 = []
vec4 = []
vec5 = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    datos.pop(-1)
    #print(datos)
    #print(datos[4].split('/'))
    vec1.append(datos[0])
    vec2.append(datos[1])
    vec3.append(datos[2])
    vec4.append(datos[4])


for i in range (len(vec1)):
    dato = Jedi()
    dato.nombre = vec1[i]
    dato.maestro = vec2[i]
    dato.especie = vec3[i].split('/')
    dato.colorS = vec4[i].split('/')
    lista1.insertar(dato, campo= 'nombre')

for i in range (len(vec1)):
    dato = Jedi()
    dato.nombre = vec1[i]
    dato.maestro = vec2[i]
    dato.especie = vec3[i].split('/')
    dato.colorS = vec4[i].split('/')
    lista2.insertar(dato, campo= 'especie')

print('')
lista1.barrido()

print('-------------------------------------------------------------------')
#!B
print('--------La información de Ahosaka Tano y Kit Fisto--------')
lista1.barrido_a()
print('-------------------------------------------------------------------')
#!C
print('--------Los aprendices de padawan y jedi master--------')
lista1.barrido_b()
print('-------------------------------------------------------------------')
#!D
print('--------Los Jedis de especie humana--------')
lista1.barrido_c()
print('-------------------------------------------------------------------')
#!E
print('--------Los Jedis que comienzan con a--------')
lista1.barrido_d()
print('-------------------------------------------------------------------')
#!F
print('--------Los Jedis que usaron un sable de luz de mas de un color--------')
lista1.barrido_e()
print('-------------------------------------------------------------------')
#!G
print('--------Los Jedis que usaron un sable de luz amarillo o violeta--------')
lista1.barrido_f()
print('-------------------------------------------------------------------')
#!H
print('--------El nombre del padawan de Qui-gon Jin--------')
pos = lista1.busqueda('qui-gon jin', 'nombre')
print(pos.info.maestro)








