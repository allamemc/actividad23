from bs4 import BeautifulSoup
with open('productos.xml','r') as f:
    data=f.read()

Bs_data=BeautifulSoup(data,'xml')
Descripcion=Bs_data.find_all('Descripcion')
print(Descripcion)

for tag in Bs_data.find_all('Producto', {'ID':"100001"}):
    tag['Precio'] = "9.95"
print(Bs_data.prettify())