## Guía de instalación de Nginx y Gunicorn

La librería de Python Django, utilizada para construir aplicativos webs de forma rápida y sencilla, cuenta con diversas características de forma nativa, pero, cuando se trata de aplicativos profesionales, el uso de Django por sí solo no suele ser recomendable, ya que especialmente, pueden existir vulnerabilidades de seguridad, por lo tanto, es común el uso de un WSGI (Web Server Gateway Interface). Esto sirve como una especie de intermediario entre una aplicación de Python (el cual en este caso será el aplicativo creado con Django) y un servidor web (el cual en este caso será Nginx), Gunicorn es el WSGI que se va a utilizar en esta guía.

Para levantar un proyecto de Django en Nginx lo primero que se debe hacer es instalar esta librería utilizando el siguiente comando:

    sudo apt install nginx

Una vez se ejecuta ese comando se descargarán e instalarán todos los componentes necesarios para el correcto uso de nginx. El siguiente paso es instalar el módulo de Python que nos permite crear y utilizar entornos virtuales, esto facilitará el uso de tanto Nginx como Django y Gunicorn, para esto se utiliza el comando:

    sudo apt install -y python3-venv

Una vez instalados estos dos componentes, el siguiente paso es crear el entorno virtual en donde se desarrollará el proyecto de Django, utilizando el siguiente comando se crea el entorno virtual:

    python3 -m venv nombre_venv

Ya que esta creado, ahora se debe activar el entorno virtual para empezar a trabajar dentro del mismo, se utiliza el comando:

    source nombre_env/bin/activate

Una vez dentro del entorno virtual, se instalan los componentes para la creación del proyecto, en primer lugar, se instala Django utilizando:

    pip install django

Y se instala Gunicorn:

    pip install gunicorn

En este punto ya se puede proceder con la creación del proyecto de Django. Se utiliza el siguiente comando:

    django-admin startproject nombre_proyecto

Con el comando anterior se crea de forma automática una carpeta en la cual se encuentra una base para la creación del proyecto, para evitar conflictos más adelante en este momento es recomendable declarar las IP de los hosts que se podrán utilizar para utilizar el aplicativo web, para realizar esta configuración se abre el archivo settings.py del proyecto de Django con el comando:

    nano nombre_proyecto/nombre_proyecto/settings.py

En ese momento se abrirá el archivo settings.py del proyecto, aquí se encuentra toda la configuración del proyecto de Django, aquí se pueden comprobar como está trabajando el proyecto y que características o rasgos del mismo están activados. Dentro de este archivo se debe buscar la sección de ALLOWED_HOSTS = [] y dentro de los corchetes agregar las IP de los hosts que tendrán permitido entrar en la aplicación, por ejemplo:

    ALLOWED_HOSTS = ["0.0.0.0","127.0.0.1","167.99.192.225", "190.96.96.140", "192.168.0.105"]

Ahora, se debe crear el archivo de configuración de Gunicorn, de la misma forma que con el archivo settings.py de Django este archivo de configuración servirá para activar o desactivar las principales características de Gunicorn y decirle como debe trabajar:

    mkdir conf
    nano conf/gunicorn_config.py

