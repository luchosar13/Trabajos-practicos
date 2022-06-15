from listaParcial import Lista
from jurasic import dinosaurs
from cola import Cola

file = open('jurasic2.txt')
lineas = file.readlines()

lista_alertas = Lista()
lista_alertas2 = Lista()

cola_1 = Cola()
cola_2 = Cola()


vec1 = []
vec2 = []
vec3 = []
vec4 = []

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name'], dino['type']

lineas.pop(0)

for linea in lineas:
    datos = linea.split(';')
    #datos.pop(-1)
    #print(datos)
    #print(datos[4].split('/'))
    vec1.append(datos[0])
    vec2.append(datos[1])
    vec3.append(datos[2])
    vec4.append(datos[3][:-1])

class Alerta:
    time, zona_code, dino_number, alert_level, nombre_dino, tipo = None, None, None, None, None, None


for i in range (len(vec1)):
    dato = Alerta()
    dato.time = vec1[i]
    dato.zona_code = vec2[i]
    dato.dino_number = vec3[i]
    dato.alert_level = vec4[i]
    lista_alertas.insertar(dato, 'time')
    
for i in range(len(vec1)):
    dato = Alerta()
    dato.time = vec1[i]
    dato.zona_code = vec2[i]
    dato.dino_number = vec3[i]
    dato.alert_level = vec4[i]
    #for linea in lineas:
    #    datoo = linea.split(';')
    #datoo[3] = datoo[3][:-1]
    dato.nombre_dino, dato.tipo = busqueda(dato.dino_number)
    #datoo.append(name)
    #dato.nombre_dino = (str(datoo[4]))
    #dato.tipo = vec6[i].strip()
    lista_alertas2.insertar(dato, 'nombre_dino')


print('-------------------------------')
lista_alertas2.barrido_alertas2()
    

#lista_alertas.barrido_alertas()
print('------------------------Ultimo dinosaurio encontrado----------------------------')
pos = lista_alertas.mayor_de_lista_alertas('time')
print('El dinosaurio',pos.info.dino_number,'fue el ultimo encontrado en el horario: ',pos.info.time)
print('-----------------------Eliminacion de zonas-----------------------------')
pos1 = lista_alertas.busqueda('WYG075', campo = 'zona_code')
pos2 = lista_alertas.busqueda('SXH966', campo = 'zona_code') 
pos3 = lista_alertas.busqueda('LYF010', campo = 'zona_code') 
if(pos1):
    print('La zona',pos1.info.zona_code,'fue eliminada')
    lista_alertas2.eliminar('WYG075', 'zona_code')
    lista_alertas.eliminar('WYG075', 'zona_code')
if(pos2):
    print('La zona',pos2.info.zona_code,'fue eliminada')
    lista_alertas.eliminar('SXH966', 'zona_code')
    lista_alertas2.eliminar('SXH966', 'zona_code')
if(pos3):
    print('La zona',pos3.info.zona_code,'fue eliminada')
    lista_alertas.eliminar('LYF010', 'zona_code')
    lista_alertas2.eliminar('LYF010', 'zona_code')
poss = lista_alertas.busqueda('HYD195', campo = 'zona_code')
if(poss):
    poss.info.nombre_dino = 'Mosasaurus'
print('------------------------Listado de dinosaurios especificos----------------------------')
lista_alertas2.barrido_alertas3()
print('------------------------Colas----------------------------')
for i in range(lista_alertas2.tamanio()):
    dato = lista_alertas2.obtener_elemento(i)
    if((dato.tipo == 'herbívoro') and (dato.alert_level not in ['low','medium'])):
        cola_1.arribo(str(dato.zona_code))
    elif((dato.tipo == 'carnívoro') and (dato.alert_level not in ['low','medium'])):
        cola_2.arribo(str(dato.zona_code))

print('La cantidad de dinosaurios Herbívoros son: ',cola_1.tamanio())
print('La cantidad de dinosaurios Carnívoros son: ',cola_2.tamanio())

print('------------------------Zonas que necesitan apoyo---------------------------')
print('Las zonas que necesitan unidad de respaldo son: ')
while(not cola_2.cola_vacia()):
    dato = cola_2.atencion()
    if(dato != 'EPC944'):
        print(dato)
print('------------------------Datos de Raptors, Carnosaurus y zonas donde hay Compsognathus---------------------------')
lista_alertas2.barrido_alertas4()
lista_alertas2.barrido_alertas5()


    

















