1) Es una web para cargar, mostrar y vender vehiculos
2) Primero debemos agregar una marca de Vehiculo: http://127.0.0.1:8000/add_brand/ o desde el navbar "Agregar Marca". Los campos que pide son el nombre de la marca y el pais de procedencia
3) Luego devemos agregar los modelos de vehiculos: http://127.0.0.1:8000/add_car/ o desde el navbar "Agregar Vehiculo". Nos va a permitir seleccionar la marca ya guardada
y asociarla al vehiculo. En modelo colocar la version del vehiculo, por ejemplo Corolla, luego año de fabricacion y por ultimo el precio.
4) El siguiente paso es la venta del vehiculo: http://127.0.0.1:8000/add_owner/ o desde nabvar "Vender Vehiculo" Donde pondremos el nombre del comprado y seleccionaremos que
vehiculo queremos vender.
5) Podremos realizar una busqueda desde http://127.0.0.1:8000/search/ opcion "Buscar del navbar". En este caso buscaremos por nombre de vehiculo, por ejemplo corolla. Si ponemos
"cor" solamente, nos traera todo lo que contiene cor.
6) Por ultimo en index, agregue unas cards que muestran todos los vehiculos cargados. 
