Este proyecto es una tienda virtual de juegos de video la cual se divide 4 diferentes
Aplicaciones:
Blog:  Mas que una aplicacion, es la base del proyecto la cual contiene el archivo urls.py y settings.py

Forms= Es la aplicación la cual se encarga de todo lo relacionado a los formularios de los juegos, ya sea el listar los juegos como actualizarlos, eliminarlos y crearlos,
además que es de contenido dinámico ya que dependiendo la información ingresada se irán creando las vistas del juego como los métodos del crud para la misma.
Ademas en esta en app en el archivo test.py se encuentrar las 3 pruebas unitarias

Login= Es la aplicación que se encarga de todo lo relacionado a los usuarios, aquí se encuentra la forma de crear un usuario, modificarlo, agregarle un avatar a elección, 
también es capaz de diferenciar si se inició sesión en la plataforma y también diferenciar si es un super usuario o un usuario sin permisos

Vistas= En esta app se mostrarán los datos de los juegos como si fuera una tienda de verdad,
es completamente dinámico ya que los registros se van mostrando de acuerdo con los que el super usuario vaya creando en la app forms y es capaz de separar los registros dependiendo a la plataforma que pertenezca cada uno 

!!!Nota IMPORTANTE= No se realizó un carrito para este proyecto ya que no era necesario según las consignas para el proyecto!!!

Las credenciales para ingresar como super usuario son:
Usuario: sadrac             		    (todo en minúscula)
Contraseña: Djangoform                  (la primera letra debe ser mayúscula)


Pruebas unitarias: python manage test forms


Url del video Explicativo: https://youtu.be/iAK-x_r6oIk


Autor: Sadrac Araneda Isla
Correo: saadrak.oai@gmail.com
