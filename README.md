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

una ves creado el proyecto nos dirigimos dentro de el con cd userprofile y dentro del proyecto creamos ua app con python manage.py startapp users, una vez creado abrimos nuestro proyecto en el editor de tecto preferido.

abrimos el archivo models.py.

La forma más fácil de construir un modelo personalizado de usuario compatible es heredar de AbstractBaseUser.

Haci que lo importamos con otros clases mas asi:

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, PermissionsMixin
)


###### AbstractBaseUser => AbstractBaseUser proporciona la implementación del núcleo de un usuario modelo, incluyendo contraseñas hash y el restablecimiento de contraseñas

#### BaseUserManager => Nos sirvira como un admisitrado para crear superusuarios y usarios staff

### PermissionsMixin => Es un mixin con los permisos necesarios para el modelo de usario

class User(PermissionsMixin, AbstractBaseUser):
	email = models.EmailField(unique = True)
	avatar = models.ImageField(upload_to = "avatar")
	ciudad = models.CharField(max_length = 140)
	nombre = models.CharField(max_length = 140)
	edad = models.IntegerField(default = 0)
	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


