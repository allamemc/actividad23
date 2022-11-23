from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
print('Prueba en Python')

with open('Clientes.xml','r') as f:
    data = f.read()
#print(data)
with open('productos.xml','r') as f:
    datap = f.read()

BS_data=BeautifulSoup(data,'xml')
BS_datap=ET.parse('productos.xml')
root = BS_datap.getroot()
#root = ET.fromstring(BS_datap)
print(root.tag)
#print(BS_data)

telefonos  = BS_data.find_all('telefono')
#print(telefonos)

b_name = BS_data.find('cliente',{'ID':'C001'})
#print(b_name)

for tag in BS_data.find_all('cliente', {'ID':'C001'}):
    tag['ciudad'] = "Madrid"
#print(BS_data.prettify())

#descripcion  = BS_datap.find_all('Descripcion')
#print(descripcion)

#precios = '9950'
#for tag in BS_datap.find_all('Precio'):
    #tag['precio'] = precios
#print(BS_datap.prettify())

#cafe = BS_datap.find('Producto',{'ID':"100001"})
#print(cafe)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')