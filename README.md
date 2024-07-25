1) Es una web para cargar, mostrar y vender vehículos
2) Primero debemos agregar una marca de Vehículo: http://127.0.0.1:8000/add_brand/ o desde el navbar "Agregar Marca". Los campos que pide son el nombre de la marca y el país de procedencia
3) Luego debemos agregar los modelos de vehículos: http://127.0.0.1:8000/add_car/ o desde el navbar "Agregar Vehículo". Nos va a permitir seleccionar la marca ya guardada
y asociarla al vehículo. En modelo colocar la versión del vehículo, por ejemplo Corolla, luego año de fabricación y por último el precio.
4) El siguiente paso es la venta del vehículo: http://127.0.0.1:8000/add_owner/ o desde nabvar "Vender Vehículo" Donde pondremos el nombre del comprado y seleccionaremos que
vehículo queremos vender.
5) Podremos realizar una búsqueda desde http://127.0.0.1:8000/search/ opción "Buscar del navbar". En este caso buscaremos por nombre de vehículo, por ejemplo, corolla. Si ponemos
"cor" solamente, nos traerá todo lo que contiene cor.
6) Por último en index, agregue unas cards que muestran todos los vehículos cargados.
