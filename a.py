import os
class Producto:
	def __init__(self,nombre,categoria,precio,codigo,cantidad,descripcion):
		self.nombre= nombre
		self.descripcion = descripcion
		self.precioendlrs = int(precio)
		self.precioenbs = int(precio)*int(PrecioDolar)
		self.codigo = codigo
		self.cantidad= int(cantidad)
		self.categoria = categoria
	def Mostrar(self):
		print('''Nombre: {}
Categoria: {}
Precio en dolares: {}$
Precio en bolivares: {}bs
Codigo: {}
Cantidad: {}
Descripcion: [{}]
'''.format(self.nombre,self.categoria,self.precioendlrs,self.precioenbs,self.codigo,self.cantidad,self.descripcion))
salida=False
Productos=list()
PrecioDolar= int()

def cls():
	os.system('cls')
try:
	datos = open("datos.txt","r")
	listadedatos= datos.read().splitlines()
	PrecioDolar = listadedatos[0]
	print(int((len(listadedatos))/6))
	for x in range(int((len(listadedatos))/6)):
		if x == 0:
			
			categoriatemp = listadedatos[1]
			nombretemp = listadedatos[2]
			cantidadtemp = int(listadedatos[3])
			codigotemp = listadedatos[4]
			preciotemp = int(listadedatos[5])
			descripciontemp= listadedatos[6]
			print(nombretemp)
		else:
			categoriatemp = listadedatos[x*6+1]
			nombretemp = listadedatos[x*6+2]
			cantidadtemp = int(listadedatos[x*6+3])
			codigotemp = listadedatos[x*6+4]
			preciotemp = int(listadedatos[x*6+5])
			descripciontemp= listadedatos[x*6+6]
			print(nombretemp)
		NuevoProducto = Producto(nombretemp,categoriatemp,preciotemp,codigotemp,cantidadtemp,descripciontemp)
		Productos.append(NuevoProducto)
	
	datos.close()
	
except:
	print("Bienvenido! es la primera vez que se inicia el programa")
	print("Ingresa el siguiente dato para continuar")
	PrecioDolar = int(input("Precio del dolar actual: "))
	datos = open("datos.txt","w")
	datos.write(str(PrecioDolar)+'\n')
	datos.close()
	cls()
	cls()
while salida==False:
	cls()
	print(''' 				TIENDA FLACCO Y ASOCIADOS
	
1-Agregar
2-Ver por categoria
3-Comprar
4-Mostrar todos los articulos
5-Actualizar precio del dolar
6-Ver ganancia total
7-Ver mercancia agotada
4-Salir
                                Precio actual del dolar: {}	bs
'''.format(PrecioDolar))
	opcion = input('Opcion: ')
	print('')
	if opcion == '1':
		while True:
			try:			
				nombre = input('Nombre: ')
				categoria = input('Categoria: ')
				precio = int(input('Precio: '))
				codigo = input('Codigo: ')
				cantidad = int(input('Cantidad: '))
				descripcion = input('Descripcion: ')
				NuevoProducto = Producto(nombre,categoria,precio,codigo,cantidad,descripcion)
				Productos.append(NuevoProducto)
				print('')
				cls()
				print('Producto agregado!')
				datos = open("datos.txt","a")
				datos.write(categoria+'\n')
				datos.write(nombre+'\n')
				datos.write(str(precio)+'\n')
				datos.write(codigo+'\n')
				datos.write(str(cantidad)+'\n')
				datos.write(descripcion+'\n')
				datos.close()
				break
			except:
				print('Ocurrio un error en los datos ingresados')
	elif opcion== '2':
		cls()
		if Productos == []:
			print('No hay articulos!')
			continue
		buscategoria = input('Ingrese la categoria que busca: ')
		cls()
		for contenido in Productos:
			if buscategoria.upper() == contenido.categoria.upper():
				contenido.Mostrar()
		input('Pulse enter para continuar')
		cls()
	elif opcion== '3':
		if Productos == []:
			cls()
			print('No hay productos disponibles!')
			continue
		comprar= input('Ingrese el codigo del producto: ')
		cls()
		for contenido in Productos:
			if comprar == contenido.codigo:
				contenido.Mostrar()
				contenido.cantidad -= 1
				
				try:
					datos2= open("datos2.txt","r")	
					reescribir= datos2.read().splitlines()
					datos2.close()	
					reescribir1 = int(reescribir[0])+ int(contenido.precioendlrs)
					reescribir2 = int(reescribir1)*int(PrecioDolar)
					
					datos2= open("datos2.txt","w")
					datos2.write(str(reescribir1)+'\n')
					
					datos2.write(str(reescribir2)+'\n')
					datos2.close()
					
				except:
					datos2= open("datos2.txt","a")
					datos2.write(str(contenido.precioendlrs)+'\n')
					datos2.write(str(contenido.precioenbs)+'\n')
					datos2.close()
				print('Articulo comprado!')
				if contenido.cantidad == 0:
					datos3= open("agotados.txt","a")
					datos3.write(contenido.nombre)
					datos3.close()
					Productos.remove(contenido)
					print('Se ha agotado este articulo!')
				datos = open("datos.txt","w")
				datos.write(str(PrecioDolar)+'\n')
				for contenido in Productos:
					datos.write(contenido.categoria+'\n')
					datos.write(contenido.nombre+'\n')
					datos.write(str(contenido.cantidad)+'\n')
					datos.write(contenido.codigo+'\n')
					datos.write(str(contenido.precioendlrs)+'\n')
					datos.write(contenido.descripcion+'\n')
				datos.close()
				input('Pulse enter para continuar')
				cls()
				break
			else:
				
				print('No hay articulos con ese codigo!')
				cls()
				continue
	elif opcion == '4':
		if Productos == []:
			cls()
			print('No hay productos disponibles')
			continue
		else:
			cls()
			for contenido in Productos:
				contenido.Mostrar()
			input('Pulse enter para continuar')
			cls()
	elif opcion == '5':
		cls()
		PrecioDolar = int(input('Ingrese el nuevo precio: '))
		datos = open("datos.txt","w")
		datos.write(str(PrecioDolar)+'\n')
		for contenido in Productos:
			contenido.precioenbs = int(contenido.precioendlrs)*int(PrecioDolar)	
			datos.write(contenido.categoria+'\n')
			datos.write(contenido.nombre+'\n')
			datos.write(str(contenido.cantidad)+'\n')
			datos.write(contenido.codigo+'\n')
			datos.write(str(contenido.precioendlrs)+'\n')
			datos.write(contenido.descripcion+'\n')
		datos.close()
		cls()
	elif opcion == '6':
		
		datos2= open("datos2.txt","r")
		ganancias= datos2.read().splitlines()
		print("Ganancias total en dolares:"+ganancias[0]+"$")
		print("Ganancias total en bolivares:"+ganancias[1]+"bs") 
		datos2.close()
		input('')
	elif opcion == '7':
		try:
			datos = open("agotados.txt","r")
			agotados = datos.read().splitlines()
			datos.close()
			for contenido in agotados:
				print(contenido)
			input('')
		except:
			print('Todavia no se ha agotado nada')
			input()
	elif opcion == '0':
		salida= True
	else:
		cls()
		print('Opcion invalida!')
				
