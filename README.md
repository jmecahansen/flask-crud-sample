# flask-crud-sample
Pequeña aplicación de prueba con Flask para realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar)

## Instalación
Esta aplicación depende de **Python 3.x** con los paquetes **pip** y **venv** instalados. Este sería un ejemplo de instalación con Debian:

```
sudo apt install python3{,-{pip,venv}}
```

Clonamos este repositorio:

```
git clone https://github.com/jmecahansen/flask-crud-sample.git
```

A continuación, creamos (y activamos) un entorno virtual para nuestra aplicación

```
python3 -m venv flask-crud-sample/venv
cd flask-crud-sample
source venv/bin/activate
```

Una vez dentro del entorno virtual, instalamos las dependencias de esta aplicación (**Flask**):

```
pip3 install -r requirements.txt
```

Una vez instaladas las dependencias, configuramos los parámetros de Flask para esta aplicación y la ejecutamos:

```
export FLASK_APP="main.py"
flask run
```
