# Personalizar el modelo de usario de django

Django trae por defecto el modelo de usuario, pero este tiene muchas limitaciones entre ellas que no tiene un 
campo para el avatar y no permite loguearnos con el username.


En este tutorial enseñare como podremos personalizar para poder agragar mas campos y loguarnos usando el email
y que sea compatible con el admin de django

### Empezemos

para empezar debemos tener instalado django en su version mas reciente la version que se usa en este tutorial
se django 1.7

primero crearemos un projecto se llamara userprofile usando este comando en la terminal django-admin.py startproject userprofile

recomendacion al personalizar el modelo de usario este debe ser la primera migracion para no causar conflictos.

una ves creado el proyecto nos dirigimos dentro de el con cd userprofile y dentro del proyecto creamos ua app con python manage.py startapp users, una vez cread debemos tener un
