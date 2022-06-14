from listaParcial import Lista
from jurasic import dinosaurs
from cola import Cola

file = open('jurasic2.txt')
lineas = file.readlines()

lista_alertas = Lista()
lista_dino = Lista()
lista_alertas2 = Lista()

cola_1 = Cola()
cola_2 = Cola()


vec1 = []
vec2 = []
vec3 = []
vec4 = []

lineas.pop(0)

for linea in lineas:
    datos = linea.split(';')
    #datos.pop(-1)
    #print(datos)
    #print(datos[4].split('/'))
    vec1.append(datos[0])
    vec2.append(datos[1])
    vec3.append(datos[2])
    vec4.append(datos[3])

vec5 = []
vec6 = []
vec7 = []
vec8 = []
vec9 = []

for dinosaurio in dinosaurs:
    vec5.append(dinosaurio['name'])
    vec6.append(dinosaurio['type'])
    vec7.append(dinosaurio['number'])
    vec8.append(dinosaurio['period'])
    vec9.append(dinosaurio['named_by'])

class Dinosaurio:
    name, type, number, period, named_by = None, None, None, None, None

class Alerta:
    time, zona_code, dino_number, alert_level, nombre_dino, tipo = None, None, None, None, None, None


for i in range(len(vec5)):
    dato = Dinosaurio()
    dato.name = vec5[i]
    dato.type = vec6[i]
    dato.number = vec7[i]
    dato.period = vec8[i]
    dato.named_by = vec9[i].split(',')
    #print(dato.name,'-',dato.type,'-',dato.number,'-',dato.period,'-',dato.named_by)
    lista_dino.insertar(dato, 'name')


for i in range (len(vec1)):
    dato = Alerta()
    dato.time = vec1[i]
    dato.zona_code = vec2[i]
    dato.dino_number = vec3[i]
    dato.alert_level = vec4[i]
    lista_alertas.insertar(dato, 'time')
    
for i in range(len(vec5)):
    dato = Alerta()
    dato.time = vec1[i]
    dato.zona_code = vec2[i]
    dato.dino_number = vec3[i]
    dato.alert_level = vec4[i].rstrip('\n')
    dato.nombre_dino = vec5[i]
    dato.tipo = vec6[i].strip()
    lista_alertas2.insertar(dato, 'nombre_dino')


print('-------------------------------')
lista_alertas2.barrido_alertas2()
    

lista_alertas.barrido_alertas()
print('------------------------Ultimo dinosaurio encontrado----------------------------')
pos = lista_alertas.mayor_de_lista_alertas('time')
print('El dinosaurio',pos.info.dino_number,'fue el ultimo encontrado en el horario: ',pos.info.time)
print('-----------------------Eliminacion de zonas-----------------------------')
pos1 = lista_alertas.busqueda('WYG075', campo = 'zona_code') 
pos2 = lista_alertas.busqueda('SXH966', campo = 'zona_code') 
pos3 = lista_alertas.busqueda('LYF010', campo = 'zona_code') 
if(pos1):
    print('La zona',pos1.info.zona_code,'fue eliminada')
    lista_alertas.eliminar('WYG075', 'zona_code')
if(pos2):
    print('La zona',pos2.info.zona_code,'fue eliminada')
    lista_alertas.eliminar_zone('SXH966', 'zona_code')
if(pos3):
    print('La zona',pos3.info.zona_code,'fue eliminada')
    lista_alertas.eliminar_zone('LYF010', 'zona_code')
poss = lista_alertas.busqueda('HYD195', campo = 'zona_code')
if(poss):
    poss.info.nombre_dino = 'Mosasaurus'
print('------------------------Listado de dinosaurios especificos----------------------------')
lista_alertas2.barrido_alertas3()
print('------------------------Colas----------------------------')
for i in range(lista_alertas2.tamanio()):
    dato = lista_alertas2.obtener_elemento(i)
    if((dato.tipo == 'carnívoro') and (dato.alert_level not in ['low','medium'])):
        cola_1.arribo(dato)
    elif((dato.tipo == 'herbívoro') and (dato.alert_level not in ['low','medium'])):
        cola_2.arribo(dato)

print(cola_1.tamanio())
print(cola_2.tamanio())

print('------------------------Zonas que necesitan apoyo---------------------------')
while(not cola_1.cola_vacia()):
    if(dato.zona_code != 'EPC944'):
        dato = cola_1.atencion()
    print('Las zonas que necesitan unidad de respaldo son: ', dato.zona_code)
print('------------------------Datos de Raptors, Carnosaurus y zonas donde hay Compsognathus---------------------------')
lista_alertas2.barrido_alertas4()
lista_alertas2.barrido_alertas5()


    

















